# hermes-no-tui-bloat

Strip decorative faces, verbs, emoji, and pet from the Hermes TUI.

The terminal is for work. This plugin removes:

- Busy-face kaomoji (`( . .) musing...`) → plain `...` faces, `working` verbs
- Tool emoji (`���� preparing`, `���� $`) → `get_tool_emoji` returns `""`
- The pet in the terminal (via `NO_TUI_PET` env + cli.py gate)
- The busy spinner in the TUI frontend (via `NO_TUI_BLOAT` env)

**Mechanism:** Sets `NO_TUI_PET=1` and `NO_TUI_BLOAT=1` at load, and patches `agent/display.py` in memory to neutralize the kaomoji/emoji sources. Desktop (Electron) never sets these envs, so the pet and faces stay there.

## Installation

```bash
# Copy to your Hermes plugins directory
mkdir -p ~/.hermes/plugins/no-tui-bloat
cp __init__.py ~/.hermes/plugins/no-tui-bloat/
cp plugin.yaml ~/.hermes/plugins/no-tui-bloat/

# Enable in ~/.hermes/config.yaml:
plugins:
  enabled:
    - no-tui-bloat
```

Then restart Hermes (`launchctl bootout gui/$(id -u)/com.hermes.gateway && launchctl bootstrap gui/$(id -u)/com.hermes.gateway`).

## Environment

- `NO_TUI_PET=1` — disables pet rendering in terminal (read by TUI frontend `ui-tui`)
- `NO_TUI_BLOAT=1` — disables kaomoji/spinner in terminal (read by `agent/display.py`)

These are set automatically by the plugin; no manual export needed unless running without the plugin.
