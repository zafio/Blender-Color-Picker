# Color Picker

> Fork by Zafio of [jfranmatheu/Blender-Color-Picker](https://github.com/jfranmatheu/Blender-Color-Picker), made to run on **Blender 4.5 LTS** (it keeps working on 5.x), with extra keyboard shortcuts.

<div align="center">

**[⬇️ Download](https://github.com/zafio/Blender-Color-Picker/archive/refs/heads/main.zip)** · **[⌨️ Shortcuts](#keyboard-shortcuts-while-the-picker-is-open)** · **[❓ FAQ](FAQ.md)** · **[❤️ Support the original developer](#️-support-the-original-developer)**

</div>

A quick color picker for Blender's paint modes. Press a hotkey in the 3D Viewport and a compact picker opens under your mouse, so you can change the brush color or weight without going to the tool header or the sidebar.

It works in **Texture Paint**, **Vertex Paint** and **Weight Paint**, and it is **free and open source** (GPL-3.0).

## Installation

Version 1.6.0, for **Blender 4.5 and newer**.

1. Download the repository as a zip: **[main.zip](https://github.com/zafio/Blender-Color-Picker/archive/refs/heads/main.zip)** (or *Code > Download ZIP* on GitHub).
2. In Blender, go to *Edit > Preferences > Get Extensions*, open the menu in the top-right corner and choose *Install from Disk…*, then select the zip. You can also drag and drop the zip into Blender.

Don't unzip it first: Blender installs the zip directly. To update, install the new zip the same way.

Builds for older Blender versions (2.93 to 4.1) are in the [original repository's `releases` folder](https://github.com/jfranmatheu/Blender-Color-Picker/tree/main/releases).

## Usage

1. Enter Texture Paint, Vertex Paint or Weight Paint mode.
2. Hover over the 3D Viewport and **hold `Space`**. The picker opens under your mouse.
3. Click or drag on the picker to choose a color. The brush updates right away.
4. **Release `Space`** to close the picker.

While it's open you can also switch layouts and change hue, saturation or value from the keyboard (see [Keyboard shortcuts](#keyboard-shortcuts-while-the-picker-is-open)).

You can also close it with `Esc`. If you turn off *Close on Hot-key Release*, the picker stays open after you release the key. Then press `Space` again or click outside the picker to close it.

The picker opens centered on your mouse; near the edges of the 3D Viewport it shifts so it stays fully visible. It only opens when the current paint mode has an active brush, and the brush outline is hidden while it's open.

The picker edits the same color Blender's brush uses. If *Unified Color* is on, it changes the shared color; otherwise it changes the active brush's own color.

## Keyboard shortcuts while the picker is open

These work in Texture Paint and Vertex Paint while you hold `Space` (or while the picker is open, if *Close on Hot-key Release* is off):

| Shortcut | What it does |
| --- | --- |
| `Tab` / `Shift+Tab` | Switch to the next / previous picker layout (SV Square → SV+H Square & Ring → HS Circle). The choice is saved as your *Color Picker Type*. |
| Hold `H` + move the mouse left/right | Change the **hue**. It wraps around. |
| Hold `S` + move the mouse left/right | Change the **saturation**. |
| Hold `V` + move the mouse left/right | Change the **value** (brightness). |
| Hold `R`, `G` or `B` + move the mouse left/right | Change the **red**, **green** or **blue** channel. |
| Add `Shift` while moving | Fine adjustment (10× slower). |
| Mouse wheel | **SV Square** and **SV+H Square & Ring**: change the **hue**. **HS Circle**: change the **value**. Hold `Shift` for smaller steps. |

Moving the mouse across the picker's width covers the full 0 to 1 range. When you release `H`, `S`, `V`, `R`, `G` or `B`, the new color is added to the recent colors, like after dragging a slider. After scrolling, the color is added once when you press another key, click, or close the picker.

## Picker layouts

Choose a layout under *Color Picker Type* in the settings (see [Settings](#settings)), or press `Tab` while the picker is open. Every layout has the same panel on the right:

- **Color preview** at the top.
- **H / S / V sliders** for hue, saturation and value.
- **R / G / B sliders** for the red, green and blue channels.

Every slider shows a live gradient of the colors you would get by moving it, so you can see the result before you drag.

| Layout | How it works |
| --- | --- |
| **SV Square** (default) | A square where the horizontal axis is **saturation** and the vertical axis is **value** (brightness). Use the H slider or the mouse wheel to change the hue. |
| **SV+H Square & Ring** | The same saturation/value square, inside a **hue ring**. Drag around the ring to change the hue and inside the square to set saturation and value, without using the sliders. The mouse wheel also changes the hue. |
| **HS Circle** | A color wheel: the angle sets the **hue** and the distance from the center sets the **saturation**. Use the V slider or the mouse wheel to change the brightness. |
| **Hex code** | Turn on *Show Hex* to show the current color as a hexadecimal code (for example `#d85914`) under the sliders. Works with any layout. |
| **Weight Paint** | In Weight Paint mode the picker is a single **weight bar**: a blue-to-red gradient from 0.0 to 1.0, with the current value in the middle. Click or drag along it to set the brush weight. |

## Settings

The settings are in the 3D Viewport sidebar (`N`), under *Paint > Color Picker*, while you are in a paint mode. The same options are also in the add-on's preferences.

| Setting | What it does |
| --- | --- |
| Color Picker Type | Picks the layout: SV Square, SV+H Square & Ring, or HS Circle. |
| Keymap | The key that opens the picker (`Space` by default). You can set it separately for each paint mode. |
| Close on Hot-key Release | When on, the picker closes as soon as you release the key. When off, it stays open until you press the key again, click outside it, or press `Esc`. |
| Screen DPI | Scales the picker's text and widgets. Raise it on high-resolution screens. |
| Scale Factor | Extra size multiplier for the picker (0.5–2), applied on top of Screen DPI. Only in the add-on's preferences. |
| Show Hex | Shows the color's hex code in the picker. |

## ❤️ Support the original developer

Color Picker was created by [J. Fran Matheu](https://github.com/jfranmatheu). This fork only adds Blender 4.5 support and the keyboard shortcuts above.

<div align="center">

### If it saves you time, please consider getting it on Superhive: purchases fund the original add-on's development.

<a href="https://superhivemarket.com/products/color-picker"><img src="https://img.shields.io/badge/Get%20it%20on-Superhive-ff6a00?style=for-the-badge&logo=blender&logoColor=white" alt="Get Color Picker on Superhive" width="360"></a>

</div>

## FAQ

Questions about installing, hotkeys, compatibility or why it's sold on Superhive? See the [FAQ](FAQ.md).

## License

GPL-3.0. See [LICENSE](LICENSE).
