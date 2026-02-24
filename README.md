# pi-ansi-themes

Dark and light themes for the [pi coding agent](https://github.com/badlogic/pi-mono)
that match your terminal's color scheme instead of overriding it.

Pi's built-in themes use hardcoded hex colors, so they clash with terminal
themes like Tokyo Night, Catppuccin, Dracula, Nord, Gruvbox, Solarized, and
others. These themes fix that by using only the 16 standard ANSI color indices,
letting your terminal -- WezTerm, Kitty, iTerm2, Alacritty, Ghostty, Windows
Terminal, or anything else -- provide the actual colors.

## Install

```bash
pi install git:github.com/leblancfg/pi-ansi-themes
```

Then in `settings.json`:

```json
{ "theme": "ansi-dark" }
```

Or `ansi-light` for light terminals.

## Themes

| Theme | Foreground palette | Background |
|-------|-------------------|------------|
| `ansi-dark` | Bright ANSI (8--15) | ANSI black |
| `ansi-light` | Standard ANSI (0--7) | Terminal default |

No hex, no 256-color, no grayscale ramp. Colors come from your terminal and
nowhere else.

## Contributing

PRs welcome. One rule: colors must stay within ANSI 0--15 and `""`. CI enforces
this via `scripts/validate-ansi-only.py`.

## License

MIT
