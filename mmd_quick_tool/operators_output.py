# This module was split from the Serpens-generated mmd Quick tool source.


from .common import *


class SNA_OT_Operator009_F9Bf5(bpy.types.Operator):
    bl_idname = "sna.operator009_f9bf5"
    bl_label = "Operator.009"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.render.resolution_x = int(bpy.context.scene.render.resolution_x * 2.0)
        bpy.context.scene.render.resolution_y = int(bpy.context.scene.render.resolution_y * 2.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator003_Da1Be(bpy.types.Operator):
    bl_idname = "sna.operator003_da1be"
    bl_label = "Operator.003"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.render.resolution_x = int(bpy.context.scene.render.resolution_x * float(1.5 + 0.0))
        bpy.context.scene.render.resolution_y = int(bpy.context.scene.render.resolution_y * float(1.5 + 0.0))
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator010_18497(bpy.types.Operator):
    bl_idname = "sna.operator010_18497"
    bl_label = "Operator.010"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.render.resolution_x = int(bpy.context.scene.render.resolution_x * float(0.75 + 0.0))
        bpy.context.scene.render.resolution_y = int(bpy.context.scene.render.resolution_y * float(0.75 + 0.0))
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_83D28(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_83d28"
    bl_label = "跳转到指定时间"
    bl_description = "跳转到指定时间"
    bl_options = {"REGISTER", "UNDO"}
    sna_new_property: bpy.props.IntProperty(name='分', description='', default=0, subtype='NONE', min=0)
    sna_new_property_001: bpy.props.IntProperty(name='秒', description='', default=0, subtype='NONE', min=0, max=60)

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.frame_current = int(int(self.sna_new_property_001 + int(self.sna_new_property * 60.0)) * bpy.context.scene.render.fps)
        self.report({'INFO'}, message='跳转到' + str(int(int(self.sna_new_property_001 + int(self.sna_new_property * 60.0)) * bpy.context.scene.render.fps)) + '帧')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)
