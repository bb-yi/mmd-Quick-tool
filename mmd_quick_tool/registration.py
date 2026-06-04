# Thin registration facade matching the package layout used by ParamSnap.
from . import core


def register():
    core.register()


def unregister():
    core.unregister()
