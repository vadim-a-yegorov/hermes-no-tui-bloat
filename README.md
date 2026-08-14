# hermes-no-tui-bloat

The terminal is for work. This plugin removes:

- The busy spinner kaomoji (`( . .) musing...`) and working is now "Working..." (`NO_TUI_BLOAT`)
- Keeps your desktop pet, but disables pet in the terminal (`NO_TUI_PET`)

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

## Environment

```bash
export NO_TUI_BLOAT=1
export NO_TUI_PET=1
```
