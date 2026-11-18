# Color Picker documentation

Complete reference for the Color Picker add-on for Blender. For a quick overview, see the [README](README.md). For common questions and troubleshooting, see the [FAQ](FAQ.md).

**Contents**

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Quick start](#quick-start)
4. [Opening and closing the picker](#opening-and-closing-the-picker)
5. [The picker at a glance](#the-picker-at-a-glance)
6. [Layouts](#layouts)
7. [Weight Paint](#weight-paint)
8. [Recent colors](#recent-colors)
9. [Hex code](#hex-code)
10. [Which color gets changed](#which-color-gets-changed)
11. [Settings](#settings)
12. [Hotkeys](#hotkeys)
13. [Updating and uninstalling](#updating-and-uninstalling)
14. [Building from source](#building-from-source)
15. [Getting help](#getting-help)

---

## Requirements

| Requirement | Supported |
| --- | --- |
| Blender | 5.0 or newer (tested in 5.3) |
| Editor | 3D Viewport |
| Modes | Texture Paint, Vertex Paint, Weight Paint |
| License | GPL-3.0 |

Builds for Blender 2.93, 3.x and 4.x are in the [`releases`](releases) folder. They don't receive updates.

## Installation

1. Download the zip from the [latest release](https://github.com/jfranmatheu/Blender-Color-Picker/releases/latest), or from your [Superhive](https://superhivemarket.com/products/color-picker) purchase. It's the same add-on everywhere.
2. In Blender, go to *Edit > Preferences > Get Extensions*.
3. Open the menu in the top-right corner, choose *Install from Disk…* and select the zip. You can also drag and drop the zip into Blender.

Don't unzip the file first. Blender installs the zip directly and enables the add-on.

## Quick start

1. Select a mesh and switch to **Texture Paint**, **Vertex Paint** or **Weight Paint**.
2. Hover over the 3D Viewport and **hold `Space`**.
3. Click or drag on the picker. The brush updates immediately.
4. **Release `Space`**. The picker closes and you can keep painting.

![Made for painting fast](docs/images/features.png)

## Opening and closing the picker

The picker opens centered on your mouse. Near the edges of the 3D Viewport it shifts so it always stays fully visible. It only opens when the current paint mode has an active brush.

How it closes depends on the *Close on Hot-key Release* setting:

| Close on Hot-key Release | How to close the picker |
| --- | --- |
| **On** (default) | Release the hotkey, or press `Esc`. |
| **Off** | Press the hotkey again, click outside the picker, or press `Esc`. |

With the setting **on**, the picker works like a quick "hold to pick" overlay. With it **off**, it works like a toggle that stays open while you try colors.

While the picker is open, the brush outline is hidden so it doesn't get in the way. It comes back when the picker closes.

## Keyboard shortcuts while the picker is open

These work in Texture Paint and Vertex Paint while you hold `Space` (or while the picker is open, if *Close on Hot-key Release* is off):

| Shortcut | What it does |
| --- | --- |
| `Tab` / `Shift+Tab` | Switch to the next / previous picker layout (SV Square → SV+H Square & Ring → HS Circle). The choice is saved as your *Color Picker Type*. |
| Hold `H` + move the mouse left/right | Change the **hue**. It wraps around. |
| Hold `S` + move the mouse left/right | Change the **saturation**. |
| Hold `V` + move the mouse left/right | Change the **value** (brightness). |
| Add `Shift` while moving | Fine adjustment (10× slower). |

Moving the mouse across the picker's width covers the full 0 to 1 range. When you release `H`, `S` or `V`, the new color is added to the recent colors, like after dragging a slider.

## The picker at a glance

![SV Square](docs/images/sv_square.png)

In Texture Paint and Vertex Paint, the picker has two parts.

**Left:** the main color area. Its shape depends on the [layout](#layouts) you choose.

**Right:** the same panel in every layout:

| Part | What it does |
| --- | --- |
| Color swatch (top left) | Split in two: the top half shows the color before your last change, the bottom half shows the current color. |
| Recent colors (top) | The colors you picked recently. Click one to use it again. See [Recent colors](#recent-colors). |
| **H**, **S**, **V** sliders | Hue, saturation and value (brightness). |
| **R**, **G**, **B** sliders | Red, green and blue channels. |

Every slider shows a live gradient of the colors you'd get by moving it, so you can see the result before you drag. All the controls stay in sync: changing one updates the others right away.

## Layouts

![Three picker layouts](docs/images/layouts.png)

Choose a layout with *Color Picker Type* in the [settings](#settings).

### SV Square (default)

A square where the horizontal axis is **saturation** and the vertical axis is **value**. Change the hue with the **H** slider. It's the most familiar layout and the quickest for picking shades of one hue.

### SV+H Square & Ring

The saturation/value square inside a **hue ring**. Drag around the ring to change the hue and inside the square to set saturation and value. You can pick any color without touching the sliders.

### HS Circle

A color wheel. The angle sets the **hue** and the distance from the center sets the **saturation**. Change the brightness with the **V** slider. This is the layout closest to a traditional painter's wheel.

## Weight Paint

![Weight Paint bar](docs/images/weight_paint.png)

In Weight Paint, the picker is a single **weight bar**: a blue-to-green-to-red gradient from 0.0 to 1.0, matching Blender's weight colors. The current value is shown in the middle. Click or drag along the bar to set the brush weight.

## Recent colors

Each time you finish changing a color, it's added to the recent colors strip next to the swatch. Click a recent color to make it the brush color again.

Recent colors are shared between Texture Paint and Vertex Paint and kept while Blender is open. They're cleared when you restart Blender.

## Hex code

![SV Square with hex code](docs/images/sv_square_hex.png)

Turn on *Show Hex* to show the current color as a hexadecimal code, for example `#d85914`, under the sliders. On Windows and macOS, click the code to copy it to the clipboard.

## Which color gets changed

The picker changes the same color Blender's own color field would:

- If **Unified Color** is on for that paint mode, it changes the shared color used by all brushes.
- If it's off, it changes the active brush's own color.

Weight Paint works the same way with **Unified Weight**.

## Settings

There are two places to change settings:

- **Sidebar panel:** in the 3D Viewport, press `N` and open *Paint > Color Picker*. It only shows while you're in a paint mode, and only shows the hotkey for the current mode.
- **Add-on preferences:** *Edit > Preferences > Add-ons > ColorPicker*. Shows every setting, the hotkeys for all three paint modes, and a link to support development.

<img src="docs/images/sidebar_panel.png" width="252" alt="Color Picker sidebar panel">

| Setting | Default | What it does |
| --- | --- | --- |
| Color Picker Type | SV Square | The layout: SV Square, SV+H Square & Ring, or HS Circle. Not used in Weight Paint. |
| Close on Hot-key Release | On | Closes the picker when you release the hotkey. See [Opening and closing the picker](#opening-and-closing-the-picker). |
| Screen DPI | 72 | Scales the picker's size and text. Raise it on high-resolution screens. Range 72–300. |
| Scale Factor | 1.0 | Extra size multiplier on top of Screen DPI. Range 0.5–2. Preferences only. |
| Show Hex | Off | Shows the color's hex code in the picker. |

The picker's size is 400 × 200 pixels (360 × 72 in Weight Paint), multiplied by *Screen DPI / 72* and by *Scale Factor*.

## Hotkeys

The default hotkey is `Space` in all three paint modes. In those modes it opens the picker instead of playing the animation.

Each paint mode has its own hotkey, so you can use different keys per mode. To change one:

- In the sidebar panel, change the key shown under *Keymap*. This changes the hotkey for the current paint mode.
- In the add-on preferences, each paint mode (*Image Paint*, *Vertex Paint*, *Weight Paint*) has its own row.

You can also change the input type (keyboard, mouse and so on) next to the key.

## Updating and uninstalling

**Update:** install the new zip the same way as the first time. Blender replaces the old version.

**Uninstall:** go to *Edit > Preferences > Add-ons*, find *ColorPicker*, open its menu and choose *Uninstall*.

## Building from source

The add-on source is in the [`color_picker`](color_picker) folder, with its extension manifest in `color_picker/blender_manifest.toml`. To build an installable zip with Blender's command-line tool:

```bash
blender --command extension build --source-dir color_picker --output-dir dist
```

The zip is written to the `dist` folder.

## Getting help

- **Questions and troubleshooting:** see the [FAQ](FAQ.md).
- **Bugs:** open an issue on [GitHub](https://github.com/jfranmatheu/Blender-Color-Picker/issues). Include your Blender version, your operating system, the paint mode, and any error from Blender's system console.
- **Support development:** Color Picker is free and open source. If it saves you time, you can support it on [Superhive](https://superhivemarket.com/products/color-picker). Thank you! ♥
