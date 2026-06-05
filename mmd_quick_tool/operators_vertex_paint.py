# This module was split from the Serpens-generated mmd Quick tool source.


from .common import *


class SNA_OT_Operator001_05281(bpy.types.Operator):
    bl_idname = "sna.operator001_05281"
    bl_label = "Operator.001"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        brush = getattr(bpy.context.tool_settings.vertex_paint, 'brush', None)
        if brush is None:
            self.report({'WARNING'}, message='No active vertex paint brush')
            return {"CANCELLED"}
        brush.color = (1.0, 1.0, 1.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator003_D462C(bpy.types.Operator):
    bl_idname = "sna.operator003_d462c"
    bl_label = "Operator.003"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.tool_settings.vertex_paint.brush.color = (1.0, 0.0, 0.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator004_D6Bee(bpy.types.Operator):
    bl_idname = "sna.operator004_d6bee"
    bl_label = "Operator.004"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.tool_settings.vertex_paint.brush.color = (0.0, 1.0, 0.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator005_2A676(bpy.types.Operator):
    bl_idname = "sna.operator005_2a676"
    bl_label = "Operator.005"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.tool_settings.vertex_paint.brush.color = (0.0, 0.0, 1.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator006_Dda67(bpy.types.Operator):
    bl_idname = "sna.operator006_dda67"
    bl_label = "Operator.006"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.tool_settings.vertex_paint.brush.color = (1.0, 1.0, 0.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator007_17Ad2(bpy.types.Operator):
    bl_idname = "sna.operator007_17ad2"
    bl_label = "Operator.007"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.tool_settings.vertex_paint.brush.color = (1.0, 0.0, 1.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator008_A3Fb7(bpy.types.Operator):
    bl_idname = "sna.operator008_a3fb7"
    bl_label = "Operator.008"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.tool_settings.vertex_paint.brush.color = (0.0, 1.0, 1.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator002_2A623(bpy.types.Operator):
    bl_idname = "sna.operator002_2a623"
    bl_label = "Operator.002"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.tool_settings.vertex_paint.brush.color = (0.0, 0.0, 0.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator_6Aa4F(bpy.types.Operator):
    bl_idname = "sna.operator_6aa4f"
    bl_label = "Operator"
    bl_description = "设置选中物体的顶点色为画笔颜色"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        node_tree_002['sna_sna_new_variable'] = bpy.context.view_layer.objects.active.name
        bpy.ops.paint.vertex_color_set('INVOKE_DEFAULT', )
        bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='OBJECT')
        for i_44E9C in range(len(bpy.context.view_layer.objects.selected)):
            bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.selected[i_44E9C]
            bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='VERTEX_PAINT')
            bpy.ops.paint.vertex_color_set('INVOKE_DEFAULT', )
            bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='OBJECT')
            if (i_44E9C == int(len(bpy.context.view_layer.objects.selected) - 1.0)):
                bpy.context.view_layer.objects.active = bpy.context.view_layer.objects[node_tree_002['sna_sna_new_variable']]
                bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='VERTEX_PAINT')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_48003(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_48003"
    bl_label = "标注工具"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        area = bpy.context.area
        if (area is not None and area.type in {'NODE_EDITOR', 'IMAGE_EDITOR', 'VIEW_3D'}):
            bpy.ops.wm.call_menu_pie(name="SNA_MT_3BB6D")
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_8Ad72(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_8ad72"
    bl_label = "添加预览灯光"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        node_tree_005['sna_light_obj'] = []
        bpy.ops.object.light_add('INVOKE_DEFAULT', type='AREA', radius=1.0, location=(-1.7913199663162231, -1.0733000040054321, 1.4290000200271606), rotation=(1.3820528984069824, 0.0, -1.0796327590942383), scale=(1.0, 1.0, 1.0))
        bpy.context.view_layer.objects.active.scale = (1.9769999980926514, 1.9769999980926514, 1.9769999980926514)
        bpy.context.view_layer.objects.active.name = '副光'
        bpy.context.view_layer.objects.active.data.name = '副光'
        bpy.context.view_layer.objects.active.data.energy = 15.0
        node_tree_005['sna_light_obj'].append(bpy.context.view_layer.objects.active)
        bpy.ops.object.light_add('INVOKE_DEFAULT', type='AREA', radius=1.0, location=(0.2778179943561554, 1.6447900533676147, 2.0871999263763428), rotation=(1.3820528984069824, 0.0, -3.2447938919067383), scale=(1.0, 1.0, 1.0))
        bpy.context.view_layer.objects.active.scale = (5.754690170288086, 2.634190082550049, 1.9773199558258057)
        bpy.context.view_layer.objects.active.name = '背光'
        bpy.context.view_layer.objects.active.data.name = '背光'
        bpy.context.view_layer.objects.active.data.energy = 240.0
        node_tree_005['sna_light_obj'].append(bpy.context.view_layer.objects.active)
        bpy.ops.object.light_add('INVOKE_DEFAULT', type='AREA', radius=1.0, location=(2.334399938583374, -0.8916320204734802, 1.4290000200271606), rotation=(1.492418885231018, 0.0, 1.2703763246536255), scale=(1.0, 1.0, 1.0))
        bpy.context.view_layer.objects.active.scale = (1.9773199558258057, 1.9773199558258057, 1.9773199558258057)
        bpy.context.view_layer.objects.active.name = '主光'
        bpy.context.view_layer.objects.active.data.name = '主光'
        bpy.context.view_layer.objects.active.data.energy = 60.0
        bpy.context.view_layer.objects.active.data.spread = 2.094395160675049
        node_tree_005['sna_light_obj'].append(bpy.context.view_layer.objects.active)
        bpy.ops.object.empty_add('INVOKE_DEFAULT', type='PLAIN_AXES', radius=1.0, align='WORLD', location=(0.0, 0.0, 0.0))
        bpy.context.view_layer.objects.active.name = '快速灯光'
        for i_CAE75 in range(len(node_tree_005['sna_light_obj'])):
            node_tree_005['sna_light_obj'][i_CAE75].select = True
        bpy.ops.object.parent_set('INVOKE_DEFAULT', type='OBJECT', keep_transform=True)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_A52B1(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_a52b1"
    bl_label = "合并所选顶点"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    def sna_new_property_enum_items(self, context):
        return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]
    sna_new_property: bpy.props.EnumProperty(name='类型', description='', items=[('CENTER', 'CENTER', '', 0, 0), ('CURSOR', 'CURSOR', '', 0, 1), ('COLLAPSE', 'COLLAPSE', '', 0, 2), ('FIRST', 'FIRST', '', 0, 3), ('LAST', 'LAST', '', 0, 4)])

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.ops.mesh.merge('INVOKE_DEFAULT', type=self.sna_new_property)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)
