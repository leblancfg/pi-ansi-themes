# pi-ansi-themes

ANSI-native dark and light themes for the [pi coding agent](https://github.com/badlogic/pi-mono).

Uses only ANSI palette indices 0--15 and `""` (terminal default), so pi inherits
whatever color scheme your terminal already has.

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
| `ansi-dark` | Bright ANSI (8--15) | Terminal default |
| `ansi-light` | Standard ANSI (0--7) | Terminal default |

No hex, no 256-color, no grayscale ramp. The `export` section keeps hex for
HTML output since ANSI indices don't apply there.

## Contributing

PRs welcome. One rule: colors must stay within ANSI 0--15 and `""`. CI enforces
this via `scripts/validate-ansi-only.py`.

## License

MIT
