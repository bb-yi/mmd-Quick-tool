# This module was split from the Serpens-generated mmd Quick tool source.

from .common import *


SCENE_PROPERTY_NAMES = (
    'sna_display_time',
    'sna_ik_fix_on',
    'sna_use_choose_tex',
    'sna_bake_tex_size_y',
    'sna_bake_tex_size_x',
    'sna_remove_transform_constraint',
    'sna_view_tex',
    'sna_time_show_is_change',
    'sna_new_property_003',
    'sna_bili',
)


def register_scene_properties():
    bpy.types.Scene.sna_bili = bpy.props.EnumProperty(name='bili', description='', items=[('自定义', '自定义', '', 0, 0), ('1:1', '1:1', '', 0, 1), ('3:2', '3:2', '', 0, 2), ('4:3', '4:3', '', 0, 3), ('16:9', '16:9', '', 0, 4), ('14:9', '14:9', '', 0, 5), ('1.85:1', '1.85:1', '', 0, 6), ('2.39:1', '2.39:1', '', 0, 7)], update=sna_update_sna_bili_31149)
    bpy.types.Scene.sna_new_property_003 = bpy.props.BoolProperty(name='切换中英文', description='切换中英文，快捷键ctrl+shift+e', default=True, update=sna_update_sna_new_property_003_B42B0)
    bpy.types.Scene.sna_time_show_is_change = bpy.props.BoolProperty(name='time_show_is_change', description='', default=True)
    bpy.types.Scene.sna_view_tex = bpy.props.BoolProperty(name='view_tex', description='贴图预览模式，快捷键ctrl+shift+t', default=False, update=sna_update_sna_view_tex_632AA)
    bpy.types.Scene.sna_remove_transform_constraint = bpy.props.BoolProperty(name='Remove_transform_constraint', description='', default=False)
    bpy.types.Scene.sna_bake_tex_size_x = bpy.props.IntProperty(name='bake_tex_size_x', description='', default=1024, subtype='NONE')
    bpy.types.Scene.sna_bake_tex_size_y = bpy.props.IntProperty(name='bake_tex_size_y', description='', default=1024, subtype='NONE')
    bpy.types.Scene.sna_use_choose_tex = bpy.props.BoolProperty(name='use_choose_tex', description='', default=False)
    bpy.types.Scene.sna_ik_fix_on = bpy.props.BoolProperty(name='ik_fix_on', description='', default=True, update=sna_update_sna_ik_fix_on_057DD)
    bpy.types.Scene.sna_display_time = bpy.props.BoolProperty(name='display_time', description='打开分秒显示', default=True)


def unregister_scene_properties():
    for property_name in SCENE_PROPERTY_NAMES:
        if hasattr(bpy.types.Scene, property_name):
            delattr(bpy.types.Scene, property_name)
