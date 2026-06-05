# This module was split from the Serpens-generated mmd Quick tool source.


from .common import *


class SNA_OT_Uv_94B57(bpy.types.Operator):
    bl_idname = "sna.uv_94b57"
    bl_label = "移除位置uv"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_EE5B8 in range(len(bpy.context.view_layer.objects.selected)):
            bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.selected[i_EE5B8]
            bpy.context.view_layer.objects.active.data.uv_layers.active = bpy.context.view_layer.objects.active.data.uv_layers[int(len(bpy.context.view_layer.objects.active.data.uv_layers) - 1.0)]
            if 'pos' in bpy.context.view_layer.objects.active.data.uv_layers.active.name:
                bpy.ops.mesh.uv_texture_remove('INVOKE_DEFAULT', )
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Uv_9201E(bpy.types.Operator):
    bl_idname = "sna.uv_9201e"
    bl_label = "生成视图uv"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    def sna_new_property_enum_items(self, context):
        return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]
    sna_new_property: bpy.props.EnumProperty(name='视图方向', description='', items=[('FRONT', 'FRONT', '', 0, 0), ('LEFT', 'LEFT', '', 0, 1), ('TOP', 'TOP', '', 0, 2)])

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_7227A in range(len(bpy.context.view_layer.objects.selected)):
            bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.selected[i_7227A]
            bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='EDIT')
            bpy.ops.view3d.view_axis('INVOKE_DEFAULT', type=self.sna_new_property)
            bpy.ops.mesh.select_all('INVOKE_DEFAULT', action='SELECT')
            bpy.ops.mesh.uv_texture_add('INVOKE_DEFAULT', )
            bpy.context.view_layer.objects.active.data.uv_layers[int(len(bpy.context.view_layer.objects.active.data.uv_layers) - 1.0)].name = 'pos_' + self.sna_new_property
            bpy.context.view_layer.objects.active.data.uv_layers.active = bpy.context.view_layer.objects.active.data.uv_layers[int(len(bpy.context.view_layer.objects.active.data.uv_layers) - 1.0)]
        for i_F23AC in range(len(bpy.context.screen.areas)):
            if (bpy.context.screen.areas[i_F23AC].type == 'VIEW_3D'):
                for i_94977 in range(len(bpy.context.screen.areas[i_F23AC].regions)):
                    if (bpy.context.screen.areas[i_F23AC].regions[i_94977].type == 'WINDOW'):
                        area_9235B = bpy.context.screen.areas[i_F23AC]
                        region_9235B = bpy.context.screen.areas[i_F23AC].regions[i_94977]
                        with bpy.context.temp_override(area=area_9235B, region=region_9235B, ):
                            bpy.ops.uv.project_from_view('INVOKE_DEFAULT', )
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)
