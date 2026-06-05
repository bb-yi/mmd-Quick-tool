# This module owns Blender registration order for mmd Quick tool.
import os
import bpy

from . import common
from . import properties
from . import ui_hooks
from . import (
    operators_ik,
    operators_uv,
    operators_mmd_workflow,
    operators_output,
    operators_view_tools,
    operators_constraints,
    operators_focus_bake,
    operators_vertex_paint,
    operators_misc,
    ui_menus,
    ui_panels,
    preferences,
)

CLASS_MODULES = (
    operators_ik,
    operators_uv,
    operators_mmd_workflow,
    operators_output,
    operators_view_tools,
    operators_constraints,
    operators_focus_bake,
    operators_vertex_paint,
    operators_misc,
    ui_menus,
    ui_panels,
    preferences,
)
CLASS_NAMES = (
    'SNA_OT_My_Generic_Operator_C8494',
    'SNA_OT_Ik_B204A',
    'SNA_OT_My_Generic_Operator_C3269',
    'SNA_OT_My_Generic_Operator_Cc136',
    'SNA_OT_My_Generic_Operator_89058',
    'SNA_OT_My_Generic_Operator_C034B',
    'SNA_OT_Uv_94B57',
    'SNA_OT_Uv_9201E',
    'SNA_OT_My_Generic_Operator_Bedaf',
    'SNA_OT_My_Generic_Operator_04Cf5',
    'SNA_OT_My_Generic_Operator_60634',
    'SNA_OT_My_Generic_Operator_Dd728',
    'SNA_OT_My_Generic_Operator_Fb95F',
    'SNA_OT_Abc_B0Bf3',
    'SNA_OT_My_Generic_Operator_Abaaa',
    'SNA_OT_Operator015_0Ebb1',
    'SNA_OT_Operator024_D37Ce',
    'SNA_OT_Operator023_Dc120',
    'SNA_OT_Operator021_0D655',
    'SNA_OT_Operator005_9368B',
    'SNA_OT_Operator004_Fa32A',
    'SNA_OT_Operator025_4038C',
    'SNA_OT_Operator001_64C4A',
    'SNA_OT_Operator_B46A6',
    'SNA_OT_Operator007_85779',
    'SNA_OT_Operator008_F7B4C',
    'SNA_OT_Operator002_7Dbd9',
    'SNA_OT_Operator014_47F89',
    'SNA_OT_Operator009_F9Bf5',
    'SNA_PT_MMD_0B0AC',
    'SNA_OT_Operator003_Da1Be',
    'SNA_OT_Operator010_18497',
    'SNA_OT_My_Generic_Operator_83D28',
    'SNA_PT_MMD_5DD0C',
    'SNA_OT_Operator020_173C4',
    'SNA_OT_Operator022_D211D',
    'SNA_OT_Operator023_9E188',
    'SNA_OT_Operator024_1Bdb7',
    'SNA_OT_Operator025_C68F6',
    'SNA_OT_Operator002_Ac0A6',
    'SNA_OT_Operator001_1136E',
    'SNA_OT_Operator_5Ed64',
    'SNA_OT_My_Generic_Operator_400A9',
    'SNA_OT_My_Generic_Operator_E6Bd2',
    'SNA_OT_My_Generic_Operator_E9B48',
    'SNA_OT_My_Generic_Operator_0C8D6',
    'SNA_OT_My_Generic_Operator_4A59F',
    'SNA_OT_My_Generic_Operator_Acbd7',
    'SNA_OT_My_Generic_Operator_4Bd78',
    'SNA_OT_My_Generic_Operator_C68A2',
    'SNA_OT_My_Generic_Operator_32F6A',
    'SNA_OT_My_Generic_Operator_16Cb7',
    'SNA_OT_My_Generic_Operator_A5A90',
    'SNA_OT_My_Generic_Operator_Cde4F',
    'SNA_OT_My_Generic_Operator_2B24E',
    'SNA_OT_My_Generic_Operator_39Ebf',
    'SNA_OT_Operator_F1B3D',
    'SNA_PT_MMD_QUICK_TOOL_MATERIAL_67F0C',
    'SNA_OT_Bake_Tex_F278F',
    'SNA_OT_My_Generic_Operator_7A93E',
    'SNA_OT_Operator001_05281',
    'SNA_OT_Operator003_D462C',
    'SNA_OT_Operator004_D6Bee',
    'SNA_OT_Operator005_2A676',
    'SNA_OT_Operator006_Dda67',
    'SNA_OT_Operator007_17Ad2',
    'SNA_OT_Operator008_A3Fb7',
    'SNA_OT_Operator002_2A623',
    'SNA_OT_Operator_6Aa4F',
    'SNA_OT_My_Generic_Operator_48003',
    'SNA_MT_3BB6D',
    'SNA_OT_My_Generic_Operator_8Ad72',
    'SNA_OT_My_Generic_Operator_A52B1',
    'SNA_AddonPreferences_C113E',
    'SNA_OT_My_Generic_Operator_763Af',
    'SNA_PT_IK_CC508',
    'SNA_PT_UV_5331C',
    'SNA_PT__35D62',
    'SNA_PT__E26FF',
    'SNA_PT__668A7',
    'SNA_PT__023F8',
    'SNA_PT__6062D',
    'SNA_PT_MMD_B11D3',
    'SNA_PT__30162',
    'SNA_PT__D880A',
    'SNA_PT__92512',
    'SNA_PT_bake_tex_0E9C6',
)
ICON_FILES = ('white.png', 'black.png', 'red.png', 'green.png', 'blue.png', 'yellow.png', 'purple.png', 'cyan.png')

UI_CALLBACKS = (
    (bpy.types.DOPESHEET_HT_header, 'append', ui_hooks.sna_add_to_dopesheet_ht_header_E775E),
    (bpy.types.RENDER_PT_format, 'append', ui_hooks.sna_add_to_render_pt_format_54259),
    (bpy.types.VIEW3D_HT_tool_header, 'append', ui_hooks.sna_add_to_view3d_ht_tool_header_80556),
    (bpy.types.VIEW3D_MT_select_edit_mesh, 'append', ui_hooks.sna_add_to_view3d_mt_select_edit_mesh_C0326),
    (bpy.types.VIEW3D_MT_edit_mesh_context_menu, 'append', ui_hooks.sna_add_to_view3d_mt_edit_mesh_context_menu_48850),
    (bpy.types.VIEW3D_MT_edit_mesh_vertices, 'append', ui_hooks.sna_add_to_view3d_mt_edit_mesh_vertices_D20F4),
    (bpy.types.VIEW3D_MT_transform_object, 'append', ui_hooks.sna_add_to_view3d_mt_transform_object_E49E0),
    (bpy.types.MESH_MT_shape_key_context_menu, 'append', ui_hooks.sna_add_to_mesh_mt_shape_key_context_menu_B7E3D),
    (bpy.types.DATA_PT_modifiers, 'prepend', ui_hooks.sna_add_to_data_pt_modifiers_55FB3),
    (bpy.types.OBJECT_PT_constraints, 'prepend', ui_hooks.sna_add_to_object_pt_constraints_16F76),
    (bpy.types.GRAPH_MT_editor_menus, 'append', ui_hooks.sna_add_to_graph_mt_editor_menus_9BAD1),
    (bpy.types.VIEW3D_MT_paint_weight, 'append', ui_hooks.sna_add_to_view3d_mt_paint_weight_1FE39),
    (bpy.types.VIEW3D_HT_tool_header, 'prepend', ui_hooks.sna_add_to_view3d_ht_tool_header_CFA13),
)

def _class_by_name(name):
    for module in CLASS_MODULES:
        cls = getattr(module, name, None)
        if cls is not None:
            return cls
    raise KeyError(f'Class not found: {name}')


def _register_class(cls):
    bpy.utils.register_class(cls)


def _unregister_class(cls):
    try:
        bpy.utils.unregister_class(cls)
    except RuntimeError:
        pass


def _append_callbacks():
    for owner, method_name, callback in UI_CALLBACKS:
        getattr(owner, method_name)(callback)


def _remove_callbacks():
    for owner, _method_name, callback in reversed(UI_CALLBACKS):
        try:
            owner.remove(callback)
        except (ReferenceError, RuntimeError, ValueError):
            pass


def _load_icons():
    common.create_icons()
    icon_dir = os.path.join(os.path.dirname(__file__), 'icons')
    for icon_name in ICON_FILES:
        if icon_name not in common._icons:
            common._icons.load(icon_name, os.path.join(icon_dir, icon_name), 'IMAGE')


def _register_keymaps():
    kc = bpy.context.window_manager.keyconfigs.addon
    if kc is None:
        return
    km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
    kmi = km.keymap_items.new('sna.operator002_ac0a6', 'T', 'PRESS', ctrl=True, alt=False, shift=True, repeat=False)
    common.addon_keymaps['21D05'] = (km, kmi)

    km = kc.keymaps.new(name='Window', space_type='EMPTY')
    kmi = km.keymap_items.new('sna.my_generic_operator_0c8d6', 'E', 'PRESS', ctrl=True, alt=False, shift=True, repeat=False)
    common.addon_keymaps['3C33E'] = (km, kmi)

    km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
    kmi = km.keymap_items.new('sna.operator_6aa4f', 'NUMPAD_1', 'PRESS', ctrl=False, alt=True, shift=False, repeat=False)
    common.addon_keymaps['FCCB2'] = (km, kmi)

    km = kc.keymaps.new(name='Window', space_type='EMPTY')
    kmi = km.keymap_items.new('sna.my_generic_operator_48003', 'Q', 'PRESS', ctrl=True, alt=False, shift=True, repeat=False)
    common.addon_keymaps['D7D72'] = (km, kmi)


def _unregister_keymaps():
    for km, kmi in common.addon_keymaps.values():
        try:
            km.keymap_items.remove(kmi)
        except Exception:
            pass
    common.addon_keymaps.clear()


def register():
    _load_icons()
    properties.register_scene_properties()
    for class_name in CLASS_NAMES:
        _register_class(_class_by_name(class_name))
    _append_callbacks()
    _register_keymaps()


def unregister():
    _unregister_keymaps()
    _remove_callbacks()
    properties.unregister_scene_properties()
    for class_name in reversed(CLASS_NAMES):
        _unregister_class(_class_by_name(class_name))
    common.remove_icons()
