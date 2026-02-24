# pi-ansi-themes

ANSI-native dark and light themes for the [pi coding agent](https://github.com/badlogic/pi-mono).

The built-in `dark` and `light` themes ship hardcoded hex colors. These themes
use standard ANSI palette indices (0--15) instead, so pi inherits whatever color
scheme your terminal is already configured with -- Solarized, Catppuccin,
Dracula, Gruvbox, Nord, Tokyo Night, you name it.

## Install

```bash
pi install git:github.com/leblancfg/pi-ansi-themes
```

Then select a theme via `/settings` or in your `settings.json`:

```json
{
  "theme": "ansi-dark"
}
```

## Themes

| Theme | Description |
|-------|-------------|
| `ansi-dark` | Bright ANSI colors (indices 9--14) on a dark grayscale background |
| `ansi-light` | Standard ANSI colors (indices 1--6) on a light grayscale background |

Both themes use:
- ANSI palette indices 0--15 for all foreground/accent colors, deferring to the terminal
- The 232--255 grayscale ramp for subtle background shading
- Empty strings (`""`) for default text, so it matches your terminal's foreground

## How it works

The 256-color palette breaks down as:

- **0--15** -- the 16 standard ANSI colors, defined by your terminal theme
- **16--231** -- a fixed 6x6x6 RGB cube
- **232--255** -- a 24-step grayscale ramp

By targeting only the first group for semantic colors, these themes become a thin
pass-through to whatever palette your terminal already defines.

## License

MIT
