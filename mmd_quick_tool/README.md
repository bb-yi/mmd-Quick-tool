# mmd Quick tool

Refactored package source for `mmd Quick tool` based on `version/mmd_quick_tool_1.1.7.zip`.

The Serpens-generated add-on is split by responsibility:

- `common.py`: shared state, utility functions, update callbacks, and add-on preference lookup.
- `registration.py`: Blender class, callback, icon, and keymap registration order.
- `properties.py`: scene properties.
- `operators_*.py`: feature operators split by IK, UV, MMD workflow, output, viewport tools, constraints, focus/bake, and vertex paint.
- `ui_panels.py`, `ui_hooks.py`, `ui_menus.py`: UI panels, appended menu/header callbacks, and pie menus.
- `preferences.py`: add-on preferences and changelog operator.

Operator identifiers and UI labels are kept compatible with the original add-on.
