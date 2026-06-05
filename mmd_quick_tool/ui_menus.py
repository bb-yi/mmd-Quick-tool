# This module was split from the Serpens-generated mmd Quick tool source.


from .common import *


class SNA_MT_3BB6D(bpy.types.Menu):
    bl_idname = "SNA_MT_3BB6D"
    bl_label = ""

    @classmethod
    def poll(cls, context):
        return not ((not get_addon_preferences().sna_new_property_005))

    def draw(self, context):
        layout = self.layout.menu_pie()
        op = layout.operator('wm.tool_set_by_id', text='标注', icon_value=string_to_icon('GREASEPENCIL'), emboss=True, depress=False)
        op.name = 'builtin.annotate'
        op = layout.operator('wm.tool_set_by_id', text='框选', icon_value=string_to_icon('CHECKBOX_DEHLT'), emboss=True, depress=False)
        op.name = 'builtin.select_box'
        op = layout.operator('view3d.localview', text='独立显示', icon_value=0, emboss=True, depress=False)
        op = layout.operator('wm.tool_set_by_id', text='标注橡皮擦', icon_value=string_to_icon('SNAP_FACE'), emboss=True, depress=False)
        op.name = 'builtin.annotate_eraser'
        op = layout.operator('gpencil.layer_annotation_remove', text='清除标注层', icon_value=0, emboss=True, depress=False)
        op = layout.operator('sna.my_generic_operator_8ad72', text='添加预览灯光', icon_value=0, emboss=True, depress=False)
        area = bpy.context.area
        if ((area is not None and area.type == 'VIEW_3D') and 'EDIT_MESH'==bpy.context.mode):
            op = layout.operator('sna.my_generic_operator_a52b1', text='合并所选顶点', icon_value=0, emboss=True, depress=False)
            op.sna_new_property = 'CENTER'
