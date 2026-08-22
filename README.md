# hermes-tui-distraction-free

The terminal is for work. This plugin removes:

- The busy spinner kaomoji (`( . .) musing...`) and working is now "Working..." (`NO_TUI_BLOAT`)
- Keeps your desktop pet, but disables pet in the terminal (`NO_TUI_PET`)

## Install

```bash
cd ~/.hermes/plugins/ && git clone https://github.com/vadim-a-yegorov/hermes-tui-distraction-free/
```

## Enable

```
# Enable in ~/.hermes/config.yaml:
plugins:
  enabled:
    - tui-distraction-free
```

## Environment

```bash
export NO_TUI_BLOAT=1
export NO_TUI_PET=1
```
