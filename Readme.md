## What it does

It iterate on every leaf layer (layer without children), take their boundary, and calculate the minimum size of
the document (also named image/canvas) for them to fit into.

It only take visible layers. It does not crop anything (nothing ever get deleted). Meaning, running this script after re-enabling a layer, that has something drawn
outside the canvas, will enlarge the canvas.

**It is basically a "trim to all visible layers" instead of "trim to current layer".**

## Use case

It is useful when you make a sprite, and want to remove the unused space before exporting.

## Install


`resize_to_visible.desktop` and `resize_to_visible` folder are to be put in `pykrita` folder
in [Resources folder](https://docs.krita.org/en/reference_manual/resource_management.html#resource-management).

Example: `%APPDATA%\krita\pykrita` for Window.


`resize_to_visible.action` file go [there](https://docs.krita.org/en/user_manual/python_scripting/krita_python_plugin_howto.html#creating-configurable-keyboard-shortcuts)
`<your_installation_path>\share\krita\actions`.


Restart Krita.

## Usage

In the menu bar, `Tools -> Scripts -> Resize to Visible`

To setup a shortcut, go into `Configure Krita -> Keyboard Shortcuts -> Scripts -> My Scripts -> Resize to visible`


