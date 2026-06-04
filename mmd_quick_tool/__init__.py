# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.

ADDON_VERSION = (1, 1, 7)

bl_info = {
    "name": "mmd Quick tool",
    "author": "SFY",
    "description": "MMD workflow helper tools",
    "blender": (3, 0, 0),
    "version": ADDON_VERSION,
    "location": "3D View > MMD",
    "warning": "",
    "doc_url": "https://github.com/bb-yi/mmd-Quick-tool",
    "tracker_url": "",
    "category": "3D View",
}

from . import registration


def register():
    registration.register()


def unregister():
    registration.unregister()
