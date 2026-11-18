# Color Picker

> Fork by Zafio of [jfranmatheu/Blender-Color-Picker](https://github.com/jfranmatheu/Blender-Color-Picker), lowered to run on **Blender 4.5 LTS** (the 1.3.x code also keeps working on 5.x).

![Color Picker for Blender](docs/images/cover.png)

<div align="center">

**[⬇️ Download the latest release](https://github.com/jfranmatheu/Blender-Color-Picker/releases/latest)** · **[🌐 Website & live demo](https://jfranmatheu.github.io/Blender-Color-Picker/)** · **[📖 Docs](DOCS.md)** · **[❓ FAQ](FAQ.md)** · **[❤️ Support the developer](#️-support-the-developer)**

</div>

A quick color picker for Blender's paint modes. Press a hotkey in the 3D Viewport and a compact picker opens under your mouse, so you can change the brush color or weight without going to the tool header or the sidebar.

It works in **Texture Paint**, **Vertex Paint** and **Weight Paint**, and it is **free and open source** (GPL-3.0).

## Installation

**Blender 4.5 and newer** (5.x tested upstream in 5.3):

1. Download the zip: for **Blender 4.5** use [`releases/ColorPicker_v1.4.0_(Blender_4.5).zip`](releases); for 5.x the same build works, or use the **[latest upstream release](https://github.com/jfranmatheu/Blender-Color-Picker/releases/latest)**.
2. In Blender, go to *Edit > Preferences > Get Extensions*, open the menu in the top-right corner and choose *Install from Disk…*, then select the zip. You can also drag and drop the zip into Blender.

Older builds for Blender 2.93, 3.x and 4.0/4.1 are in the [`releases`](releases) folder.

## Usage

![Made for painting fast](docs/images/features.png)

1. Enter Texture Paint, Vertex Paint or Weight Paint mode.
2. Hover over the 3D Viewport and **hold `Space`**. The picker opens under your mouse.
3. Click or drag on the picker to choose a color. The brush updates right away.
4. **Release `Space`** to close the picker.

While it's open you can also:

- Press **`Tab`** (or `Shift+Tab`) to switch between picker layouts.
- Hold **`H`**, **`S`** or **`V`** and move the mouse left/right to change hue, saturation or value. Add `Shift` for fine control.

You can also close it with `Esc`. If you turn off *Close on Hot-key Release*, the picker stays open after you release the key. Then press `Space` again or click outside the picker to close it.

The picker edits the same color Blender's brush uses. If *Unified Color* is on, it changes the shared color; otherwise it changes the active brush's own color.

## Picker layouts

![Three picker layouts](docs/images/layouts.png)

Choose a layout under *Color Picker Type* in the settings (see [Settings](#settings)). Every layout has the same panel on the right:

- **Color preview** at the top.
- **H / S / V sliders** for hue, saturation and value.
- **R / G / B sliders** for the red, green and blue channels.

Every slider shows a live gradient of the colors you would get by moving it, so you can see the result before you drag.

| Layout | How it works | |
| --- | --- | --- |
| **SV Square** (default) | A square where the horizontal axis is **saturation** and the vertical axis is **value** (brightness). Use the H slider to change the hue. | <img src="docs/images/sv_square.png" width="320" alt="SV Square"> |
| **SV+H Square & Ring** | The same saturation/value square, inside a **hue ring**. Drag around the ring to change the hue and inside the square to set saturation and value, without using the sliders. | <img src="docs/images/sv_square_hue_ring.png" width="320" alt="SV+H Square and Ring"> |
| **HS Circle** | A color wheel: the angle sets the **hue** and the distance from the center sets the **saturation**. Use the V slider to change the brightness. | <img src="docs/images/hs_circle.png" width="320" alt="HS Circle"> |
| **Hex code** | Turn on *Show Hex* to show the current color as a hexadecimal code (for example `#d85914`) under the sliders. Works with any layout. | <img src="docs/images/sv_square_hex.png" width="320" alt="SV Square with hex code"> |
| **Weight Paint** | In Weight Paint mode the picker is a single **weight bar**: a blue-to-red gradient from 0.0 to 1.0, with the current value in the middle. Click or drag along it to set the brush weight. | <img src="docs/images/weight_paint.png" width="320" alt="Weight Paint bar"> |

## Settings

The settings are in the 3D Viewport sidebar (`N`), under *Paint > Color Picker*, while you are in a paint mode. The same options are also in the add-on's preferences.

<img src="docs/images/sidebar_panel.png" width="252" alt="Color Picker sidebar panel">

| Setting | What it does |
| --- | --- |
| Color Picker Type | Picks the layout: SV Square, SV+H Square & Ring, or HS Circle. |
| Keymap | The key that opens the picker (`Space` by default). You can set it separately for each paint mode. |
| Close on Hot-key Release | When on, the picker closes as soon as you release the key. When off, it stays open until you press the key again, click outside it, or press `Esc`. |
| Screen DPI | Scales the picker's text and widgets. Raise it on high-resolution screens. |
| Scale Factor | Extra size multiplier for the picker (0.5–2), applied on top of Screen DPI. Only in the add-on's preferences. |
| Show Hex | Shows the color's hex code in the picker. |

## ❤️ Support the developer

[![Support the developer](docs/images/support.png)](https://superhivemarket.com/products/color-picker)

<div align="center">

### Thanks to your support, Color Picker stays **open, free and public**.<br>If it saves you time, please consider getting it on Superhive: every purchase directly funds its development and future Blender updates.

<a href="https://superhivemarket.com/products/color-picker"><img src="https://img.shields.io/badge/Get%20it%20on-Superhive-ff6a00?style=for-the-badge&logo=blender&logoColor=white" alt="Get Color Picker on Superhive" width="360"></a>

</div>

## Documentation and FAQ

The complete reference, including recent colors, hotkeys and how the picker is sized, is in the [documentation](DOCS.md).

Questions about installing, hotkeys, compatibility or why it's sold on Superhive? See the [FAQ](FAQ.md).

## License

GPL-3.0. See [LICENSE](LICENSE).
