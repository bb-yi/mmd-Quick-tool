# This module was split from the Serpens-generated mmd Quick tool source.


from .common import *


class SNA_PT_MMD_0B0AC(bpy.types.Panel):
    bl_label = 'mmd快速工具'
    bl_idname = 'SNA_PT_MMD_0B0AC'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'MMD'
    bl_order = 0
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout

class SNA_PT_MMD_5DD0C(bpy.types.Panel):
    bl_label = 'MMD工具'
    bl_idname = 'SNA_PT_MMD_5DD0C'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 2
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'SNA_PT_MMD_0B0AC'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout

class SNA_PT_MMD_QUICK_TOOL_MATERIAL_67F0C(bpy.types.Panel):
    bl_label = 'mmd Quick tool Material'
    bl_idname = 'SNA_PT_MMD_QUICK_TOOL_MATERIAL_67F0C'
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'QT MMD'
    bl_order = 0
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        space_data = getattr(context, 'space_data', None)
        preferences = get_addon_preferences()
        return (
            space_data is not None and
            space_data.type == 'NODE_EDITOR' and
            space_data.tree_type == 'ShaderNodeTree' and
            preferences is not None and
            preferences.sna_new_property_003
        )

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout

class SNA_PT_IK_CC508(bpy.types.Panel):
    bl_label = 'ik修复'
    bl_idname = 'SNA_PT_IK_CC508'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 0
    bl_parent_id = 'SNA_PT_MMD_0B0AC'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        col_79ECE = layout.column(heading='', align=False)
        col_79ECE.alert = False
        col_79ECE.enabled = True
        col_79ECE.active = True
        col_79ECE.use_property_split = False
        col_79ECE.use_property_decorate = False
        col_79ECE.scale_x = 1.0
        col_79ECE.scale_y = 1.0
        col_79ECE.alignment = 'Expand'.upper()
        col_79ECE.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = col_79ECE.operator('sna.my_generic_operator_c3269', text='添加骨骼物体', icon_value=string_to_icon('BONE_DATA'), emboss=True, depress=False)
        op.sna_new_property = True
        op = col_79ECE.operator('sna.my_generic_operator_cc136', text='传递顶点组', icon_value=string_to_icon('MESH_DATA'), emboss=True, depress=False)
        op = col_79ECE.operator('sna.my_generic_operator_c8494', text='生成骨骼约束', icon_value=string_to_icon('CONSTRAINT_BONE'), emboss=True, depress=False)
        row_4175F = col_79ECE.row(heading='', align=False)
        row_4175F.alert = False
        row_4175F.enabled = True
        row_4175F.active = True
        row_4175F.use_property_split = False
        row_4175F.use_property_decorate = False
        row_4175F.scale_x = 1.0
        row_4175F.scale_y = 1.0
        row_4175F.alignment = 'Expand'.upper()
        row_4175F.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_4175F.prop(bpy.context.scene, 'sna_ik_fix_on', text=('开启' if bpy.context.scene.sna_ik_fix_on else '关闭'), icon_value=(string_to_icon('HIDE_OFF') if bpy.context.scene.sna_ik_fix_on else string_to_icon('HIDE_ON')), emboss=True)
        op = row_4175F.operator('sna.my_generic_operator_89058', text='清除骨骼约束', icon_value=string_to_icon('DECORATE_OVERRIDE'), emboss=True, depress=False)
        op = col_79ECE.operator('sna.ik_b204a', text='关闭/打开IK', icon_value=string_to_icon('CON_SPLINEIK'), emboss=True, depress=False)
        op = col_79ECE.operator('sna.my_generic_operator_c034b', text='烘焙约束', icon_value=string_to_icon('KEYTYPE_KEYFRAME_VEC'), emboss=True, depress=False)
        op.sna_new_property = bpy.context.scene.frame_start
        op.sna_new_property_001 = bpy.context.scene.frame_end

class SNA_PT_UV_5331C(bpy.types.Panel):
    bl_label = 'UV'
    bl_idname = 'SNA_PT_UV_5331C'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 2
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'SNA_PT_MMD_5DD0C'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        col_8BB61 = layout.column(heading='', align=False)
        col_8BB61.alert = False
        col_8BB61.enabled = True
        col_8BB61.active = True
        col_8BB61.use_property_split = False
        col_8BB61.use_property_decorate = False
        col_8BB61.scale_x = 1.0
        col_8BB61.scale_y = 1.0
        col_8BB61.alignment = 'Expand'.upper()
        col_8BB61.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_4EF87 = col_8BB61.row(heading='', align=False)
        row_4EF87.alert = False
        row_4EF87.enabled = True
        row_4EF87.active = True
        row_4EF87.use_property_split = False
        row_4EF87.use_property_decorate = False
        row_4EF87.scale_x = 1.0
        row_4EF87.scale_y = 1.0
        row_4EF87.alignment = 'Expand'.upper()
        row_4EF87.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_4EF87.operator('sna.uv_9201e', text='生成位置uv', icon_value=0, emboss=True, depress=False)
        op.sna_new_property = 'FRONT'
        op = row_4EF87.operator('sna.uv_94b57', text='移除位置uv', icon_value=0, emboss=True, depress=False)

class SNA_PT__35D62(bpy.types.Panel):
    bl_label = '名称编辑'
    bl_idname = 'SNA_PT__35D62'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'SNA_PT_MMD_5DD0C'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        row_02724 = layout.row(heading='', align=False)
        row_02724.alert = False
        row_02724.enabled = True
        row_02724.active = True
        row_02724.use_property_split = False
        row_02724.use_property_decorate = False
        row_02724.scale_x = 1.0
        row_02724.scale_y = 1.0
        row_02724.alignment = 'Expand'.upper()
        row_02724.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_02724.operator('sna.my_generic_operator_bedaf', text='材质到物体', icon_value=0, emboss=True, depress=False)
        op = row_02724.operator('sna.my_generic_operator_04cf5', text='物体到材质', icon_value=0, emboss=True, depress=False)
        op = row_02724.operator('sna.my_generic_operator_60634', text='贴图到材质', icon_value=0, emboss=True, depress=False)

class SNA_PT__E26FF(bpy.types.Panel):
    bl_label = '物体操作'
    bl_idname = 'SNA_PT__E26FF'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'SNA_PT_MMD_0B0AC'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        op = layout.operator('sna.operator015_0ebb1', text='位姿归零', icon_value=0, emboss=True, depress=False)
        op.sna_x = True
        op.sna_y = True
        op.sna_z = True

class SNA_PT__668A7(bpy.types.Panel):
    bl_label = '临时合并'
    bl_idname = 'SNA_PT__668A7'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'SNA_PT__E26FF'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        col_3CAA1 = layout.column(heading='', align=False)
        col_3CAA1.alert = False
        col_3CAA1.enabled = True
        col_3CAA1.active = True
        col_3CAA1.use_property_split = False
        col_3CAA1.use_property_decorate = False
        col_3CAA1.scale_x = 1.0
        col_3CAA1.scale_y = 1.0
        col_3CAA1.alignment = 'Expand'.upper()
        col_3CAA1.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_7247F = col_3CAA1.row(heading='', align=False)
        row_7247F.alert = False
        row_7247F.enabled = True
        row_7247F.active = True
        row_7247F.use_property_split = False
        row_7247F.use_property_decorate = False
        row_7247F.scale_x = 1.0
        row_7247F.scale_y = 1.0
        row_7247F.alignment = 'Expand'.upper()
        row_7247F.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_7247F.operator('sna.my_generic_operator_fb95f', text='临时合并', icon_value=0, emboss=True, depress=False)
        op = row_7247F.operator('sna.my_generic_operator_dd728', text='分离临时合并', icon_value=0, emboss=True, depress=False)

class SNA_PT__023F8(bpy.types.Panel):
    bl_label = '分辨率调整'
    bl_idname = 'SNA_PT__023F8'
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'output'
    bl_order = 0
    bl_parent_id = 'RENDER_PT_format'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        row_9A4A1 = layout.row(heading='', align=False)
        row_9A4A1.alert = False
        row_9A4A1.enabled = True
        row_9A4A1.active = True
        row_9A4A1.use_property_split = False
        row_9A4A1.use_property_decorate = False
        row_9A4A1.scale_x = 1.0
        row_9A4A1.scale_y = 1.0
        row_9A4A1.alignment = 'Left'.upper()
        row_9A4A1.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_9A4A1.operator('sna.operator_b46a6', text='1080p', icon_value=0, emboss=True, depress=False)
        op = row_9A4A1.operator('sna.operator001_64c4a', text='2k', icon_value=0, emboss=True, depress=False)
        op = row_9A4A1.operator('sna.operator002_7dbd9', text='4k', icon_value=0, emboss=True, depress=False)
        op = row_9A4A1.operator('sna.operator007_85779', text='交换', icon_value=string_to_icon('FILE_REFRESH'), emboss=True, depress=False)
        op.sna_ax = 7
        op = row_9A4A1.operator('sna.operator008_f7b4c', text='*0.5', icon_value=0, emboss=True, depress=False)
        op = row_9A4A1.operator('sna.operator010_18497', text='*0.75', icon_value=0, emboss=True, depress=False)
        op = row_9A4A1.operator('sna.operator003_da1be', text='*1.5', icon_value=0, emboss=True, depress=False)
        op = row_9A4A1.operator('sna.operator009_f9bf5', text='*2', icon_value=0, emboss=True, depress=False)
        row_3E7EE = layout.row(heading='', align=False)
        row_3E7EE.alert = False
        row_3E7EE.enabled = True
        row_3E7EE.active = True
        row_3E7EE.use_property_split = False
        row_3E7EE.use_property_decorate = False
        row_3E7EE.scale_x = 1.0
        row_3E7EE.scale_y = 1.0
        row_3E7EE.alignment = 'Left'.upper()
        row_3E7EE.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_3E7EE.prop(bpy.context.scene, 'sna_bili', text='比例', icon_value=0, emboss=True, expand=True)

class SNA_PT__6062D(bpy.types.Panel):
    bl_label = '相机设置'
    bl_idname = 'SNA_PT__6062D'
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'output'
    bl_order = 0
    bl_parent_id = 'RENDER_PT_format'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not ((not property_exists("bpy.context.scene.camera.data", globals(), locals())))

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        row_854C3 = layout.row(heading='', align=False)
        row_854C3.alert = False
        row_854C3.enabled = True
        row_854C3.active = True
        row_854C3.use_property_split = False
        row_854C3.use_property_decorate = False
        row_854C3.scale_x = 1.0
        row_854C3.scale_y = 1.0
        row_854C3.alignment = 'Left'.upper()
        row_854C3.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_854C3.prop(bpy.context.scene.camera.data, 'lens', text='焦距', icon_value=0, emboss=True)
        row_854C3.prop(bpy.context.scene.camera.data.dof, 'aperture_fstop', text='光圈', icon_value=0, emboss=True)

class SNA_PT_MMD_B11D3(bpy.types.Panel):
    bl_label = 'MMD流程'
    bl_idname = 'SNA_PT_MMD_B11D3'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 1
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'SNA_PT_MMD_5DD0C'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        col_85326 = layout.column(heading='', align=False)
        col_85326.alert = False
        col_85326.enabled = True
        col_85326.active = True
        col_85326.use_property_split = False
        col_85326.use_property_decorate = False
        col_85326.scale_x = 1.0
        col_85326.scale_y = 1.0
        col_85326.alignment = 'Expand'.upper()
        col_85326.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = col_85326.operator('sna.operator021_0d655', text='删除材质变形节点组', icon_value=0, emboss=True, depress=False)
        op = col_85326.operator('sna.operator004_fa32a', text='合并相同贴图的材质', icon_value=0, emboss=True, depress=False)
        op = col_85326.operator('sna.operator005_9368b', text='替换mmd材质节点组', icon_value=0, emboss=True, depress=False)
        op = col_85326.operator('sna.abc_b0bf3', text='为abc添加材质', icon_value=0, emboss=True, depress=False)
        op = col_85326.operator('sna.my_generic_operator_abaaa', text='移除选中物体所有材质', icon_value=0, emboss=True, depress=False)
        op = col_85326.operator('sna.operator025_4038c', text='为选中物体导入表情', icon_value=0, emboss=True, depress=False)
        row_F2AD3 = col_85326.row(heading='', align=True)
        row_F2AD3.alert = False
        row_F2AD3.enabled = True
        row_F2AD3.active = True
        row_F2AD3.use_property_split = False
        row_F2AD3.use_property_decorate = False
        row_F2AD3.scale_x = 1.0
        row_F2AD3.scale_y = 2.190999984741211
        row_F2AD3.alignment = 'Expand'.upper()
        row_F2AD3.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_F2AD3.operator('sna.operator_f1b3d', text='添加自动光圈焦点', icon_value=string_to_icon('CON_CAMERASOLVER'), emboss=True, depress=False)

class SNA_PT__30162(bpy.types.Panel):
    bl_label = '清理'
    bl_idname = 'SNA_PT__30162'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 1
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'SNA_PT_MMD_5DD0C'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        col_E927A = layout.column(heading='', align=False)
        col_E927A.alert = False
        col_E927A.enabled = True
        col_E927A.active = True
        col_E927A.use_property_split = False
        col_E927A.use_property_decorate = False
        col_E927A.scale_x = 1.0
        col_E927A.scale_y = 1.0
        col_E927A.alignment = 'Expand'.upper()
        col_E927A.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = col_E927A.operator('sna.operator020_173c4', text='清理自定义几何数据', icon_value=0, emboss=True, depress=False)
        op = col_E927A.operator('sna.operator022_d211d', text='清理空形态键关键帧', icon_value=0, emboss=True, depress=False)
        op = col_E927A.operator('sna.operator023_9e188', text='清除形态键上的驱动器', icon_value=0, emboss=True, depress=False)
        op = col_E927A.operator('sna.operator024_1bdb7', text='清除无用材质节点', icon_value=0, emboss=True, depress=False)
        op.sna_new_property = 0
        op = col_E927A.operator('sna.operator025_c68f6', text='清除骨骼修改器', icon_value=0, emboss=True, depress=False)

class SNA_PT__D880A(bpy.types.Panel):
    bl_label = '选择'
    bl_idname = 'SNA_PT__D880A'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 1
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'SNA_PT_MMD_5DD0C'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_7FD55 = layout.box()
        box_7FD55.alert = False
        box_7FD55.enabled = True
        box_7FD55.active = True
        box_7FD55.use_property_split = False
        box_7FD55.use_property_decorate = False
        box_7FD55.alignment = 'Expand'.upper()
        box_7FD55.scale_x = 1.0
        box_7FD55.scale_y = 1.0
        if not True: box_7FD55.operator_context = "EXEC_DEFAULT"
        col_BA6C8 = box_7FD55.column(heading='', align=False)
        col_BA6C8.alert = False
        col_BA6C8.enabled = True
        col_BA6C8.active = True
        col_BA6C8.use_property_split = False
        col_BA6C8.use_property_decorate = False
        col_BA6C8.scale_x = 1.0
        col_BA6C8.scale_y = 1.0
        col_BA6C8.alignment = 'Expand'.upper()
        col_BA6C8.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_4AFCF = col_BA6C8.row(heading='', align=False)
        row_4AFCF.alert = False
        row_4AFCF.enabled = True
        row_4AFCF.active = True
        row_4AFCF.use_property_split = False
        row_4AFCF.use_property_decorate = False
        row_4AFCF.scale_x = 1.0
        row_4AFCF.scale_y = 1.0
        row_4AFCF.alignment = 'Expand'.upper()
        row_4AFCF.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_4AFCF.operator('sna.operator_5ed64', text='根据贴图选择物体', icon_value=0, emboss=True, depress=False)
        op = row_4AFCF.operator('sna.operator001_1136e', text='选中相同材质的物体', icon_value=0, emboss=True, depress=False)
        row_0DF0B = col_BA6C8.row(heading='', align=False)
        row_0DF0B.alert = False
        row_0DF0B.enabled = True
        row_0DF0B.active = True
        row_0DF0B.use_property_split = False
        row_0DF0B.use_property_decorate = False
        row_0DF0B.scale_x = 1.0
        row_0DF0B.scale_y = 1.0
        row_0DF0B.alignment = 'Expand'.upper()
        row_0DF0B.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_0DF0B.operator('sna.my_generic_operator_400a9', text='选中骨架', icon_value=0, emboss=True, depress=False)
        op.sna_new_property = '腿ik骨'
        row_778C2 = col_BA6C8.row(heading='', align=False)
        row_778C2.alert = False
        active_object = bpy.context.object
        row_778C2.enabled = (active_object is not None and active_object.type == 'MESH' and active_object.mode == 'EDIT')
        row_778C2.active = True
        row_778C2.use_property_split = False
        row_778C2.use_property_decorate = False
        row_778C2.scale_x = 1.0
        row_778C2.scale_y = 1.0
        row_778C2.alignment = 'Expand'.upper()
        row_778C2.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_778C2.operator('sna.my_generic_operator_acbd7', text='按位置选择顶点', icon_value=0, emboss=True, depress=False)
        op.sna_new_property_002 = 0.0
        op = row_778C2.operator('sna.my_generic_operator_4bd78', text='按编号选择顶点', icon_value=0, emboss=True, depress=False)
        op.sna_new_property = 0

class SNA_PT__92512(bpy.types.Panel):
    bl_label = '顶点色'
    bl_idname = 'SNA_PT__92512'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 3
    bl_parent_id = 'SNA_PT_MMD_5DD0C'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not ((not get_addon_preferences().sna_new_property_001))

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        col_222AF = layout.column(heading='', align=False)
        col_222AF.alert = False
        col_222AF.enabled = True
        col_222AF.active = True
        col_222AF.use_property_split = False
        col_222AF.use_property_decorate = False
        col_222AF.scale_x = 1.0
        col_222AF.scale_y = 1.0
        col_222AF.alignment = 'Expand'.upper()
        col_222AF.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_BFA66 = col_222AF.row(heading='', align=False)
        row_BFA66.alert = False
        row_BFA66.enabled = True
        row_BFA66.active = True
        row_BFA66.use_property_split = False
        row_BFA66.use_property_decorate = False
        row_BFA66.scale_x = 1.0
        row_BFA66.scale_y = 1.0
        row_BFA66.alignment = 'Expand'.upper()
        row_BFA66.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_BFA66.operator('sna.my_generic_operator_e6bd2', text='添加顶点色属性', icon_value=0, emboss=True, depress=False)
        op.sna_new_property = '顶点色'
        op = row_BFA66.operator('sna.my_generic_operator_e9b48', text='移除顶点色属性', icon_value=0, emboss=True, depress=False)
        op.sna_new_property = ''

class SNA_PT_bake_tex_0E9C6(bpy.types.Panel):
    bl_label = '烘焙贴图'
    bl_idname = 'SNA_PT_bake_tex_0E9C6'
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 0
    bl_parent_id = 'SNA_PT_MMD_QUICK_TOOL_MATERIAL_67F0C'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        op = layout.operator('sna.bake_tex_f278f', text='烘焙当前预览', icon_value=0, emboss=True, depress=False)
        col_2ED0C = layout.column(heading='', align=True)
        col_2ED0C.alert = False
        col_2ED0C.enabled = True
        col_2ED0C.active = True
        col_2ED0C.use_property_split = False
        col_2ED0C.use_property_decorate = False
        col_2ED0C.scale_x = 1.0
        col_2ED0C.scale_y = 1.0
        col_2ED0C.alignment = 'Expand'.upper()
        col_2ED0C.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_2ED0C.prop(bpy.context.scene, 'sna_bake_tex_size_x', text='X', icon_value=0, emboss=True)
        col_2ED0C.prop(bpy.context.scene, 'sna_bake_tex_size_y', text='Y', icon_value=0, emboss=True)
        layout.prop(bpy.context.scene, 'sna_use_choose_tex', text='使用当前选中图像节点', icon_value=0, emboss=True)
