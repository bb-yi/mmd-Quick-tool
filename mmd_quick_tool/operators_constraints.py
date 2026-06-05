# This module was split from the Serpens-generated mmd Quick tool source.


from .common import *


class SNA_OT_My_Generic_Operator_Cde4F(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_cde4f"
    bl_label = "添加位置变换约束"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if bpy.context.scene.sna_remove_transform_constraint:
            if (len(bpy.context.view_layer.objects.selected) == 0):
                self.report({'INFO'}, message='没有选中物体')
            else:
                for i_11CEA in range(len(bpy.context.view_layer.objects.selected)):
                    if (len(bpy.context.view_layer.objects.selected[i_11CEA].constraints) == 0):
                        self.report({'INFO'}, message='没有找到约束')
                    else:
                        for i_9C95C in range(len(bpy.context.view_layer.objects.selected[i_11CEA].constraints)):
                            if '变换位置' in bpy.context.view_layer.objects.selected[i_11CEA].constraints[i_9C95C].name:
                                bpy.context.view_layer.objects.selected[i_11CEA].constraints.remove(constraint=bpy.context.view_layer.objects.selected[i_11CEA].constraints[i_9C95C], )
                                self.report({'INFO'}, message='移除了一个位置变换约束')
                                break
                            else:
                                self.report({'INFO'}, message='没有找到位置变换约束')
        else:
            if (len(bpy.context.view_layer.objects.selected) == 0):
                self.report({'INFO'}, message='没有选中物体')
            else:
                for i_73428 in range(len(bpy.context.view_layer.objects.selected)):
                    constraint_5341E = bpy.context.view_layer.objects.selected[i_73428].constraints.new(type='TRANSFORM', )
                    constraint_5341E.name = '变换位置'
                    constraint_5341E.from_max_x = 100.0
                    constraint_5341E.from_min_x = float(100.0 * -1.0)
                    constraint_5341E.from_max_y = 100.0
                    constraint_5341E.from_min_y = float(100.0 * -1.0)
                    constraint_5341E.from_max_z = 100.0
                    constraint_5341E.from_min_z = float(100.0 * -1.0)
                    constraint_5341E.to_max_x = 100.0
                    constraint_5341E.to_min_x = float(100.0 * -1.0)
                    constraint_5341E.to_max_y = 100.0
                    constraint_5341E.to_min_y = float(100.0 * -1.0)
                    constraint_5341E.to_max_z = 100.0
                    constraint_5341E.to_min_z = float(100.0 * -1.0)
                    self.report({'INFO'}, message='已添加位置变换约束')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_2B24E(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_2b24e"
    bl_label = "添加旋转变换约束"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if bpy.context.scene.sna_remove_transform_constraint:
            if (len(bpy.context.view_layer.objects.selected) == 0):
                self.report({'INFO'}, message='没有选中物体')
            else:
                for i_37FC5 in range(len(bpy.context.view_layer.objects.selected)):
                    if (len(bpy.context.view_layer.objects.selected[i_37FC5].constraints) == 0):
                        self.report({'INFO'}, message='没有找到约束')
                    else:
                        for i_6D01C in range(len(bpy.context.view_layer.objects.selected[i_37FC5].constraints)):
                            if '变换旋转' in bpy.context.view_layer.objects.selected[i_37FC5].constraints[i_6D01C].name:
                                bpy.context.view_layer.objects.selected[i_37FC5].constraints.remove(constraint=bpy.context.view_layer.objects.selected[i_37FC5].constraints[i_6D01C], )
                                self.report({'INFO'}, message='移除了一个旋转变换约束')
                                break
                            else:
                                self.report({'INFO'}, message='没有找到旋转变换约束')
        else:
            if (len(bpy.context.view_layer.objects.selected) == 0):
                self.report({'INFO'}, message='没有选中物体')
            else:
                for i_00AAE in range(len(bpy.context.view_layer.objects.selected)):
                    constraint_C50CC = bpy.context.view_layer.objects.selected[i_00AAE].constraints.new(type='TRANSFORM', )
                    constraint_C50CC.name = '变换旋转'
                    constraint_C50CC.map_from = 'ROTATION'
                    constraint_C50CC.map_to = 'ROTATION'
                    constraint_C50CC.from_max_x_rot = 3.1415927410125732
                    constraint_C50CC.from_min_x_rot = float(3.1415927410125732 * -1.0)
                    constraint_C50CC.from_max_y_rot = 3.1415927410125732
                    constraint_C50CC.from_min_y_rot = float(3.1415927410125732 * -1.0)
                    constraint_C50CC.from_max_z_rot = 3.1415927410125732
                    constraint_C50CC.from_min_z_rot = float(3.1415927410125732 * -1.0)
                    constraint_C50CC.to_max_x_rot = 3.1415927410125732
                    constraint_C50CC.to_min_x_rot = float(3.1415927410125732 * -1.0)
                    constraint_C50CC.to_max_y_rot = 3.1415927410125732
                    constraint_C50CC.to_min_y_rot = float(3.1415927410125732 * -1.0)
                    constraint_C50CC.to_max_z_rot = 3.1415927410125732
                    constraint_C50CC.to_min_z_rot = float(3.1415927410125732 * -1.0)
                    self.report({'INFO'}, message='已添加旋转变换约束')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_39Ebf(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_39ebf"
    bl_label = "独立显示曲线"
    bl_description = "独立显示选中曲线"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_E7E99 in range(len(bpy.context.selected_objects)):
            if property_exists("bpy.context.selected_objects[i_E7E99].animation_data.action.fcurves[0]", globals(), locals()):
                for i_D4794 in range(len(bpy.context.selected_objects[i_E7E99].animation_data.action.fcurves)):
                    if bpy.context.selected_objects[i_E7E99].animation_data.action.fcurves[i_D4794].select:
                        bpy.context.selected_objects[i_E7E99].animation_data.action.fcurves[i_D4794].hide = False
                    else:
                        bpy.context.selected_objects[i_E7E99].animation_data.action.fcurves[i_D4794].hide = True
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)
