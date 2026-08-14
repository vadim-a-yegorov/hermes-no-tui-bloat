"""no-tui-bloat — strip decorative faces, verbs, emoji, and pet from the TUI.

The terminal is for work. This plugin removes:
- Busy-face kaomoji ("(⌐■_■) musing...") -> plain "..." faces, "working" verbs
- Tool emoji ("🔎 preparing", "💻 $") -> get_tool_emoji returns ""
- The pet in the terminal (NO_TUI_PET env + cli.py gate)
- The busy spinner in the TUI frontend (NO_TUI_BLOAT env)

Mechanism: sets NO_TUI_PET=1 and NO_TUI_BLOAT=1, and patches
agent/display.py in memory at load to neutralize the kaomoji/emoji sources.
Desktop (Electron) never sets these envs, so the pet and faces stay there.
"""

import os

# Set early so every later import of agent.display sees them.
os.environ.setdefault("NO_TUI_PET", "1")
os.environ.setdefault("NO_TUI_BLOAT", "1")


def _neutralize_display():
    """Patch agent/display.py constants: no kaomoji, no fancy verbs, no emoji."""
    try:
        from agent import display as _display

        # Empty faces: the compose site is f"{face} {verb}..." — an empty face
        # renders as " Working..." with a leading space; capitalized verb gives
        # "Working..." after the site strips/normalizes. We neutralize faces to
        # a single space so the join reads " Working..." -> "Working...".
        _display.KawaiiSpinner.KAWAII_WAITING = [""] * 10
        _display.KawaiiSpinner.KAWAII_THINKING = [""] * 15

        def _working_verbs(cls=None):
            return ["Working"] * 15

        _display.KawaiiSpinner.get_thinking_verbs = classmethod(_working_verbs)
        _display.KawaiiSpinner.get_waiting_verbs = classmethod(_working_verbs)

        def _boring(tool_name, default=""):
            return ""

        if not getattr(_display, "_no_tui_bloat_patched", False):
            _display.get_tool_emoji = _boring
            _display._no_tui_bloat_patched = True
    except Exception:
        # Cosmetic-only; never break the session if display internals shift.
        pass


_neutralize_display()
