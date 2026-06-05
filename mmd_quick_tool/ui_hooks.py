# This module was split from the Serpens-generated mmd Quick tool source.


from .common import *


def sna_add_to_dopesheet_ht_header_E775E(self, context):
    if not (False):
        layout = self.layout
        row_85DC3 = layout.row(heading='', align=True)
        row_85DC3.alert = False
        row_85DC3.enabled = True
        row_85DC3.active = True
        row_85DC3.use_property_split = False
        row_85DC3.use_property_decorate = False
        row_85DC3.scale_x = 1.0
        row_85DC3.scale_y = 1.0
        row_85DC3.alignment = 'Expand'.upper()
        row_85DC3.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_85DC3.operator('sna.operator023_dc120', text='', icon_value=string_to_icon('TRIA_LEFT'), emboss=True, depress=False)
        op = row_85DC3.operator('sna.operator024_d37ce', text='', icon_value=string_to_icon('TRIA_RIGHT'), emboss=True, depress=False)

def sna_add_to_render_pt_format_54259(self, context):
    if not ( not get_addon_preferences().sna_new_property):
        layout = self.layout
        row_96091 = layout.row(heading='', align=False)
        row_96091.alert = False
        row_96091.enabled = True
        row_96091.active = True
        row_96091.use_property_split = False
        row_96091.use_property_decorate = False
        row_96091.scale_x = 1.0
        row_96091.scale_y = 1.0
        row_96091.alignment = 'Center'.upper()
        row_96091.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_96091.prop(bpy.context.scene.render, 'film_transparent', text='透明', icon_value=0, emboss=True)
        row_96091.prop(bpy.context.scene.render, 'use_persistent_data', text='持久数据', icon_value=0, emboss=True)
        row_96091.prop(bpy.context.scene.cycles, 'use_auto_tile', text='使用平铺', icon_value=0, emboss=True)
        row_96091.prop(bpy.context.scene.cycles, 'tile_size', text='平铺尺寸', icon_value=0, emboss=True)

def sna_add_to_time_mt_editor_menus_A1C9F(self, context):
    if not ((not get_addon_preferences().sna_display_time)):
        layout = self.layout
        box_0652E = layout.box()
        box_0652E.alert = False
        box_0652E.enabled = True
        box_0652E.active = True
        box_0652E.use_property_split = False
        box_0652E.use_property_decorate = False
        box_0652E.alignment = 'Expand'.upper()
        box_0652E.scale_x = 1.0
        box_0652E.scale_y = 1.0
        if not True: box_0652E.operator_context = "EXEC_DEFAULT"
        row_89995 = box_0652E.row(heading='', align=False)
        row_89995.alert = False
        row_89995.enabled = True
        row_89995.active = True
        row_89995.use_property_split = False
        row_89995.use_property_decorate = False
        row_89995.scale_x = 1.0
        row_89995.scale_y = 1.0
        row_89995.alignment = 'Expand'.upper()
        row_89995.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_89995.label(text=str(('0' + str(int(int(bpy.context.scene.frame_current / bpy.context.scene.render.fps) / 60.0)) if (int(int(bpy.context.scene.frame_current / bpy.context.scene.render.fps) / 60.0) < 10) else int(int(bpy.context.scene.frame_current / bpy.context.scene.render.fps) / 60.0))) + ':' + str(('0' + str(int(bpy.context.scene.frame_current / bpy.context.scene.render.fps)) if (int(bpy.context.scene.frame_current / bpy.context.scene.render.fps) < 10) else int(bpy.context.scene.frame_current / bpy.context.scene.render.fps))) + ':' + str(('0' + str(int(float(int(bpy.context.scene.frame_current - int(int(bpy.context.scene.frame_current / bpy.context.scene.render.fps) * bpy.context.scene.render.fps)) * 100.0) / bpy.context.scene.render.fps)) if (int(float(int(bpy.context.scene.frame_current - int(int(bpy.context.scene.frame_current / bpy.context.scene.render.fps) * bpy.context.scene.render.fps)) * 100.0) / bpy.context.scene.render.fps) < 10) else int(float(int(bpy.context.scene.frame_current - int(int(bpy.context.scene.frame_current / bpy.context.scene.render.fps) * bpy.context.scene.render.fps)) * 100.0) / bpy.context.scene.render.fps))) + '+' + str(('0' + str(int(bpy.context.scene.frame_current - int(int(bpy.context.scene.frame_current / bpy.context.scene.render.fps) * bpy.context.scene.render.fps))) if (int(bpy.context.scene.frame_current - int(int(bpy.context.scene.frame_current / bpy.context.scene.render.fps) * bpy.context.scene.render.fps)) < 10) else int(bpy.context.scene.frame_current - int(int(bpy.context.scene.frame_current / bpy.context.scene.render.fps) * bpy.context.scene.render.fps)))), icon_value=string_to_icon('TIME'))
        op = row_89995.operator('sna.my_generic_operator_83d28', text='', icon_value=string_to_icon('KEY_RETURN'), emboss=True, depress=False)
        op.sna_new_property = 0
        op.sna_new_property_001 = 0

def sna_add_to_view3d_ht_tool_header_80556(self, context):
    if not (False):
        layout = self.layout
        row_1F802 = layout.row(heading='', align=False)
        row_1F802.alert = False
        row_1F802.enabled = True
        row_1F802.active = True
        row_1F802.use_property_split = False
        row_1F802.use_property_decorate = False
        row_1F802.scale_x = 1.0
        row_1F802.scale_y = 1.0
        row_1F802.alignment = 'Center'.upper()
        row_1F802.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_1F802.prop(bpy.context.scene, 'sna_new_property_003', text=('中' if bpy.context.scene.sna_new_property_003 else '英'), icon_value=(string_to_icon('EVENT_C') if bpy.context.scene.sna_new_property_003 else string_to_icon('EVENT_E')), emboss=True)
        row_1F802.prop(bpy.context.scene, 'sna_view_tex', text='', icon_value=string_to_icon('TEXTURE'), emboss=True)
        op = row_1F802.operator('sna.my_generic_operator_4a59f', text='清理数据', icon_value=string_to_icon('ORPHAN_DATA'), emboss=True, depress=False)

def sna_add_to_view3d_mt_select_edit_mesh_C0326(self, context):
    if not (False):
        layout = self.layout
        col_61C3C = layout.column(heading='', align=False)
        col_61C3C.alert = False
        col_61C3C.enabled = True
        col_61C3C.active = True
        col_61C3C.use_property_split = False
        col_61C3C.use_property_decorate = False
        col_61C3C.scale_x = 1.0
        col_61C3C.scale_y = 1.0
        col_61C3C.alignment = 'Expand'.upper()
        col_61C3C.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = col_61C3C.operator('sna.my_generic_operator_acbd7', text='按位置选择顶点', icon_value=0, emboss=True, depress=False)
        op.sna_new_property_002 = 0.0
        op = col_61C3C.operator('sna.my_generic_operator_4bd78', text='按编号选择顶点', icon_value=0, emboss=True, depress=False)
        op.sna_new_property = 0

def sna_add_to_view3d_mt_edit_mesh_context_menu_48850(self, context):
    if not (False):
        layout = self.layout
        op = layout.operator('sna.my_generic_operator_c68a2', text='原点到选中项', icon_value=0, emboss=True, depress=False)

def sna_add_to_view3d_mt_edit_mesh_vertices_D20F4(self, context):
    if not (False):
        layout = self.layout
        op = layout.operator('sna.my_generic_operator_32f6a', text='对称两个顶点', icon_value=0, emboss=True, depress=False)
        op.sna_new_property = 'X'
        op.sna_new_property_001 = '第一个顶点'

def sna_add_to_view3d_mt_transform_object_E49E0(self, context):
    if not (False):
        layout = self.layout
        op = layout.operator('sna.my_generic_operator_16cb7', text='对齐物体到活动项', icon_value=0, emboss=True, depress=False)
        op.sna_new_property = True
        op.sna_new_property_001 = False
        op.sna_new_property_002 = False

def sna_add_to_mesh_mt_shape_key_context_menu_B7E3D(self, context):
    if not (False):
        layout = self.layout
        op = layout.operator('sna.my_generic_operator_a5a90', text='传递所有形态键', icon_value=string_to_icon('CHECKMARK'), emboss=True, depress=False)

def sna_add_to_data_pt_modifiers_55FB3(self, context):
    active_object = getattr(context, 'object', None)
    if active_object is None or active_object.type != 'MESH':
        return
    if not (False):
        layout = self.layout
        box_34AAE = layout.box()
        box_34AAE.alert = False
        box_34AAE.enabled = True
        box_34AAE.active = True
        box_34AAE.use_property_split = False
        box_34AAE.use_property_decorate = False
        box_34AAE.alignment = 'Expand'.upper()
        box_34AAE.scale_x = 1.0
        box_34AAE.scale_y = 1.0
        if not True: box_34AAE.operator_context = "EXEC_DEFAULT"
        col_6D143 = box_34AAE.column(heading='', align=False)
        col_6D143.alert = False
        col_6D143.enabled = True
        col_6D143.active = True
        col_6D143.use_property_split = False
        col_6D143.use_property_decorate = False
        col_6D143.scale_x = 1.0
        col_6D143.scale_y = 1.0
        col_6D143.alignment = 'Expand'.upper()
        col_6D143.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_15203 = col_6D143.row(heading='', align=False)
        row_15203.alert = False
        row_15203.enabled = True
        row_15203.active = True
        row_15203.use_property_split = False
        row_15203.use_property_decorate = False
        row_15203.scale_x = 1.0
        row_15203.scale_y = 1.0
        row_15203.alignment = 'Expand'.upper()
        row_15203.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_15203.operator('object.modifier_add', text='几何节点', icon_value=string_to_icon('GEOMETRY_NODES'), emboss=True, depress=False)
        op.type = 'NODES'
        op = row_15203.operator('object.modifier_add', text='遮罩', icon_value=string_to_icon('MOD_MASK'), emboss=True, depress=False)
        op.type = 'MASK'
        op = row_15203.operator('object.modifier_add', text='镜像', icon_value=string_to_icon('MOD_MIRROR'), emboss=True, depress=False)
        op.type = 'MIRROR'
        op = row_15203.operator('object.modifier_add', text='细分', icon_value=string_to_icon('MOD_SUBSURF'), emboss=True, depress=False)
        op.type = 'SUBSURF'
        row_49F3B = col_6D143.row(heading='', align=False)
        row_49F3B.alert = False
        row_49F3B.enabled = True
        row_49F3B.active = True
        row_49F3B.use_property_split = False
        row_49F3B.use_property_decorate = False
        row_49F3B.scale_x = 1.0
        row_49F3B.scale_y = 1.0
        row_49F3B.alignment = 'Expand'.upper()
        row_49F3B.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_49F3B.operator('object.modifier_add', text='实体化', icon_value=string_to_icon('MOD_SOLIDIFY'), emboss=True, depress=False)
        op.type = 'SOLIDIFY'
        op = row_49F3B.operator('object.modifier_add', text='焊接', icon_value=string_to_icon('AUTOMERGE_OFF'), emboss=True, depress=False)
        op.type = 'WELD'
        op = row_49F3B.operator('object.modifier_add', text='骨架', icon_value=string_to_icon('MOD_ARMATURE'), emboss=True, depress=False)
        op.type = 'ARMATURE'
        op = row_49F3B.operator('object.modifier_add', text='矫正平滑', icon_value=string_to_icon('MOD_SMOOTH'), emboss=True, depress=False)
        op.type = 'CORRECTIVE_SMOOTH'
        row_4E969 = col_6D143.row(heading='', align=False)
        row_4E969.alert = False
        row_4E969.enabled = True
        row_4E969.active = True
        row_4E969.use_property_split = False
        row_4E969.use_property_decorate = False
        row_4E969.scale_x = 1.0
        row_4E969.scale_y = 1.0
        row_4E969.alignment = 'Expand'.upper()
        row_4E969.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_4E969.operator('object.modifier_add', text='数据传递', icon_value=string_to_icon('MESH_DATA'), emboss=True, depress=False)
        op.type = 'DATA_TRANSFER'
        op = row_4E969.operator('object.modifier_add', text='精简', icon_value=string_to_icon('MOD_DECIM'), emboss=True, depress=False)
        op.type = 'DECIMATE'
        op = row_4E969.operator('object.modifier_add', text='倒角', icon_value=string_to_icon('MOD_BEVEL'), emboss=True, depress=False)
        op.type = 'BEVEL'
        op = row_4E969.operator('object.modifier_add', text='缩裹', icon_value=string_to_icon('MOD_SHRINKWRAP'), emboss=True, depress=False)
        op.type = 'SHRINKWRAP'

def sna_add_to_object_pt_constraints_16F76(self, context):
    if not ((not get_addon_preferences().sna_new_property_002)):
        layout = self.layout
        col_24E34 = layout.column(heading='', align=False)
        col_24E34.alert = False
        col_24E34.enabled = True
        col_24E34.active = True
        col_24E34.use_property_split = False
        col_24E34.use_property_decorate = False
        col_24E34.scale_x = 1.0
        col_24E34.scale_y = 1.0
        col_24E34.alignment = 'Expand'.upper()
        col_24E34.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_D8E68 = col_24E34.row(heading='', align=True)
        row_D8E68.alert = bpy.context.scene.sna_remove_transform_constraint
        row_D8E68.enabled = True
        row_D8E68.active = True
        row_D8E68.use_property_split = False
        row_D8E68.use_property_decorate = False
        row_D8E68.scale_x = 1.0
        row_D8E68.scale_y = 1.0
        row_D8E68.alignment = 'Expand'.upper()
        row_D8E68.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_D8E68.prop(bpy.context.scene, 'sna_remove_transform_constraint', text='', icon_value=21, emboss=True)
        op = row_D8E68.operator('sna.my_generic_operator_cde4f', text='位置变换约束', icon_value=string_to_icon('CON_LOCLIKE'), emboss=True, depress=False)
        op = row_D8E68.operator('sna.my_generic_operator_2b24e', text='旋转变换约束', icon_value=string_to_icon('CON_ROTLIKE'), emboss=True, depress=False)

def sna_add_to_graph_mt_editor_menus_9BAD1(self, context):
    if not (False):
        layout = self.layout
        op = layout.operator('sna.my_generic_operator_39ebf', text='', icon_value=string_to_icon('HIDE_OFF'), emboss=True, depress=False)

def sna_add_to_view3d_mt_paint_weight_1FE39(self, context):
    if not (False):
        layout = self.layout
        op = layout.operator('sna.my_generic_operator_7a93e', text='复制激活骨骼权重到选中骨骼', icon_value=0, emboss=True, depress=False)
        op.sna_new_property = False
        op.sna_new_property_001 = False

def sna_add_to_view3d_ht_tool_header_CFA13(self, context):
    if not ( not 'PAINT_VERTEX'==bpy.context.mode):
        layout = self.layout
        row_9B98E = layout.row(heading='', align=True)
        row_9B98E.alert = False
        row_9B98E.enabled = True
        row_9B98E.active = True
        row_9B98E.use_property_split = False
        row_9B98E.use_property_decorate = False
        row_9B98E.scale_x = 1.0
        row_9B98E.scale_y = 1.0
        row_9B98E.alignment = 'Left'.upper()
        row_9B98E.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_9B98E.operator('sna.operator_6aa4f', text='', icon_value=string_to_icon('BRUSHES_ALL'), emboss=True, depress=False)
        op = row_9B98E.operator('sna.operator001_05281', text='', icon_value=_icons['white.png'].icon_id, emboss=True, depress=False)
        op = row_9B98E.operator('sna.operator002_2a623', text='', icon_value=_icons['black.png'].icon_id, emboss=True, depress=False)
        op = row_9B98E.operator('sna.operator003_d462c', text='', icon_value=_icons['red.png'].icon_id, emboss=True, depress=False)
        op = row_9B98E.operator('sna.operator004_d6bee', text='', icon_value=_icons['green.png'].icon_id, emboss=True, depress=False)
        op = row_9B98E.operator('sna.operator005_2a676', text='', icon_value=_icons['blue.png'].icon_id, emboss=True, depress=False)
        op = row_9B98E.operator('sna.operator006_dda67', text='', icon_value=_icons['yellow.png'].icon_id, emboss=True, depress=False)
        op = row_9B98E.operator('sna.operator007_17ad2', text='', icon_value=_icons['purple.png'].icon_id, emboss=True, depress=False)
        op = row_9B98E.operator('sna.operator008_a3fb7', text='', icon_value=_icons['cyan.png'].icon_id, emboss=True, depress=False)
