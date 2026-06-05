# This module was split from the Serpens-generated mmd Quick tool source.


from .common import *


class SNA_OT_My_Generic_Operator_C8494(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_c8494"
    bl_label = "生成骨骼约束"
    bl_description = "选中骨架和abc(会自动识别顶点组包含的骨骼)"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (len(bpy.context.view_layer.objects.selected) == 2):
            for i_9F071 in range(len(bpy.context.view_layer.objects.selected)):
                if (bpy.context.view_layer.objects.selected[i_9F071].type == 'ARMATURE'):
                    ikfix['sna_constraint_obj'] = bpy.context.view_layer.objects.selected[i_9F071]
                else:
                    ikfix['sna_abc'] = bpy.context.view_layer.objects.selected[i_9F071]
            for i_78390 in range(len(ikfix['sna_abc'].vertex_groups)):
                if '_x' in ikfix['sna_abc'].vertex_groups[i_78390].name:
                    ikfix['sna_bone_list'].append(ikfix['sna_abc'].vertex_groups[i_78390].name[:int(len(ikfix['sna_abc'].vertex_groups[i_78390].name) - 2.0)])
            bpy.context.view_layer.objects.active = ikfix['sna_constraint_obj']
            bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='POSE')
            for i_293E9 in range(len(ikfix['sna_constraint_obj'].data.bones)):
                if ikfix['sna_constraint_obj'].data.bones[i_293E9].name in ikfix['sna_bone_list']:
                    ikfix['sna_constraint_obj'].data.bones.active = ikfix['sna_constraint_obj'].data.bones[i_293E9]
                    constraint_52BAD = ikfix['sna_constraint_obj'].pose.bones[ikfix['sna_constraint_obj'].data.bones.active.name].constraints.new(type='COPY_LOCATION', )
                    constraint_52BAD.name = 'Copy Location_P'
                    constraint_52BAD.target = ikfix['sna_abc']
                    constraint_52BAD.subtarget = ikfix['sna_constraint_obj'].data.bones[i_293E9].name + '_p'
                    constraint_BBB91 = ikfix['sna_constraint_obj'].pose.bones[ikfix['sna_constraint_obj'].data.bones.active.name].constraints.new(type='DAMPED_TRACK', )
                    constraint_BBB91.name = 'Damped Track_X'
                    constraint_BBB91.target = ikfix['sna_abc']
                    constraint_BBB91.subtarget = ikfix['sna_constraint_obj'].data.bones[i_293E9].name + '_x'
                    constraint_BBB91.track_axis = 'TRACK_X'
                    constraint_FA476 = ikfix['sna_constraint_obj'].pose.bones[ikfix['sna_constraint_obj'].data.bones.active.name].constraints.new(type='DAMPED_TRACK', )
                    constraint_FA476.name = 'Damped Track_Z'
                    constraint_FA476.target = ikfix['sna_abc']
                    constraint_FA476.subtarget = ikfix['sna_constraint_obj'].data.bones[i_293E9].name + '_z'
                    constraint_FA476.track_axis = 'TRACK_Z'
                    self.report({'INFO'}, message='添加约束完成')
        else:
            self.report({'WARNING'}, message='没有选中两个物体')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Ik_B204A(bpy.types.Operator):
    bl_idname = "sna.ik_b204a"
    bl_label = "切换ik"
    bl_description = "关闭/打开IK"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if ((len(bpy.context.view_layer.objects.selected) == 1) and (bpy.context.view_layer.objects.active.type == 'ARMATURE')):
            for i_74BC2 in range(len(bpy.context.view_layer.objects.active.data.bones)):
                for i_DC99E in range(len(bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_74BC2].name].constraints)-1,-1,-1):
                    if 'IK' in bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_74BC2].name].constraints[i_DC99E].name:
                        bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_74BC2].name].constraints[i_DC99E].enabled =  not bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_74BC2].name].constraints[i_DC99E].enabled
                        self.report({'INFO'}, message=('已打开ik' if bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_74BC2].name].constraints[i_DC99E].enabled else '已关闭ik'))
        else:
            self.report({'WARNING'}, message='没有选中骨骼')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_C3269(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_c3269"
    bl_label = "添加骨骼物体"
    bl_description = "选中需要添加骨骼物体的骨架"
    bl_options = {"REGISTER", "UNDO"}
    sna_new_property: bpy.props.BoolProperty(name='自定义骨骼物体', description='', default=False)

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (len(bpy.context.view_layer.objects.selected) == 1):
            if (bpy.context.view_layer.objects.active.type == 'ARMATURE'):
                ikfix['sna_bone'] = []
                for i_6AD46 in range(len(bpy.context.view_layer.objects.active.data.bones)):
                    if bpy.context.view_layer.objects.active.data.bones[i_6AD46].select:
                        ikfix['sna_bone'].append(bpy.context.view_layer.objects.active.data.bones[i_6AD46].name)
                if self.sna_new_property:
                    for i_CAD53 in range(len(bpy.context.view_layer.objects.active.data.bones)):
                        if bpy.context.view_layer.objects.active.data.bones[i_CAD53].name in ikfix['sna_bone']:
                            bpy.context.view_layer.objects.active.data.bones[i_CAD53].select = True
                else:
                    bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='POSE')
                    bpy.ops.pose.select_all('INVOKE_DEFAULT', action='DESELECT')
                    for i_F4341 in range(len(['足.L', 'ひざ.L', '足首.L', '足先EX.L', '足.R', 'ひざ.R', '足首.R', '足先EX.R'])):
                        bpy.ops.object.select_pattern(pattern=['足.L', 'ひざ.L', '足首.L', '足先EX.L', '足.R', 'ひざ.R', '足首.R', '足先EX.R'][i_F4341])
                if (self.sna_new_property and (len(ikfix['sna_bone']) == 0)):
                    self.report({'WARNING'}, message='没有选中骨骼')
                else:
                    ikfix['sna_bone_obj'] = bpy.context.view_layer.objects.active
                    if (ikfix['sna_bone_obj'].type == 'ARMATURE'):
                        bpy.ops.mesh.primitive_cube_add('INVOKE_DEFAULT', )
                        bpy.context.view_layer.objects.active.name = '骨骼坐标系'
                        ikfix['sna_base_obj'] = bpy.context.view_layer.objects.active
                        bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='EDIT')
                        bpy.ops.mesh.select_all(action='SELECT')
                        bpy.ops.transform.transform(value=(0.05000000074505806, 0.05000000074505806, 0.05000000074505806, 0.0))
                        bpy.ops.transform.resize(value=(0.05000000074505806, 0.05000000074505806, 0.05000000074505806), orient_type='GLOBAL')
                        bpy.ops.mesh.select_all(action='DESELECT')
                        bpy.ops.object.mode_set(mode='OBJECT')
                        bpy.context.view_layer.objects.active.data.vertices[7].select = True
                        bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='EDIT')
                        bpy.ops.mesh.delete(type='VERT')
                        sna_select_vertex_9E7EA(0)
                        sna_select_vertex_groups_8448B('p')
                        sna_select_vertex_9E7EA(4)
                        sna_select_vertex_groups_8448B('x')
                        sna_select_vertex_9E7EA(2)
                        sna_select_vertex_groups_8448B('y')
                        sna_select_vertex_9E7EA(1)
                        sna_select_vertex_groups_8448B('z')
                        bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='OBJECT')
                        bpy.context.view_layer.objects.active = ikfix['sna_bone_obj']
                        bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='POSE')
                        for i_7D9BF in range(len(ikfix['sna_bone_obj'].data.bones)):
                            if ikfix['sna_bone_obj'].data.bones[i_7D9BF].select:
                                id_C2AF2 = ikfix['sna_base_obj'].copy()
                                id_1CE8E = id_C2AF2.data.copy()
                                id_C2AF2.data = id_1CE8E
                                bpy.context.collection.objects.link(object=id_C2AF2, )
                                id_C2AF2.name = ikfix['sna_bone_obj'].data.bones[i_7D9BF].name
                                id_C2AF2.matrix_world = ikfix['sna_bone_obj'].data.bones[i_7D9BF].matrix_local
                                for i_A9C43 in range(len(id_C2AF2.vertex_groups)):
                                    id_C2AF2.vertex_groups[i_A9C43].name = ikfix['sna_bone_obj'].data.bones[i_7D9BF].name + '_' + id_C2AF2.vertex_groups[i_A9C43].name
                                group_01804 = id_C2AF2.vertex_groups.new(name=ikfix['sna_bone_obj'].data.bones[i_7D9BF].name, )
                                for i_37E11 in range(len(id_C2AF2.data.vertices)):
                                    group_01804.add(index=(id_C2AF2.data.vertices[i_37E11].index, 0, 0), weight=1.0, type='REPLACE', )
                                modifier_130DA = id_C2AF2.modifiers.new(name='Armature Modifier', type='ARMATURE', )
                                modifier_130DA.object = ikfix['sna_bone_obj']
                                bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='OBJECT')
                                bpy.ops.object.parent_set('INVOKE_DEFAULT', type='OBJECT')
                        bpy.data.objects.remove(object=ikfix['sna_base_obj'], )
                        bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.selected[int(len(bpy.context.view_layer.objects.selected) - 1.0)]
                        for i_D9642 in range(len(bpy.context.screen.areas)):
                            if (bpy.context.screen.areas[i_D9642].type == 'VIEW_3D'):
                                for i_09F37 in range(len(bpy.context.screen.areas[i_D9642].regions)):
                                    if (bpy.context.screen.areas[i_D9642].regions[i_09F37].type == 'WINDOW'):
                                        area_5AE5A = bpy.context.screen.areas[i_D9642]
                                        region_5AE5A = bpy.context.screen.areas[i_D9642].regions[i_09F37]
                                        with bpy.context.temp_override(area=area_5AE5A, region=region_5AE5A, ):
                                            if (None == bpy.context.view_layer.objects.active):
                                                self.report({'WARNING'}, message='未生成骨骼物体')
                                            else:
                                                if (bpy.context.view_layer.objects.active.type == 'MESH'):
                                                    bpy.ops.object.join('INVOKE_DEFAULT', )
                                                    bpy.context.scene.cursor.location = (0.0, 0.0, 0.0)
                                                    bpy.ops.object.origin_set('INVOKE_DEFAULT', type='ORIGIN_CURSOR')
                    else:
                        self.report({'WARNING'}, message='所选物体不是骨骼')
            else:
                self.report({'WARNING'}, message='没有选中骨骼')
        else:
            self.report({'WARNING'}, message='没有选中骨骼')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_Cc136(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_cc136"
    bl_label = "传递顶点组"
    bl_description = "选中abc和骨骼物体"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (len(bpy.context.view_layer.objects.selected) == 2):
            if (len(bpy.context.view_layer.objects.active.vertex_groups) == 0):
                # 获取当前的活动物体
                abc_object = bpy.context.active_object
                # 获取当前激活的对象（骨架和物体）
                selected_objects = bpy.context.selected_objects
                # 遍历所有选中的物体
                for obj in selected_objects:
                    # 检查物体是否不是当前的活动物体
                    if obj != abc_object:
                        bone_axes_object = obj
                print(selected_objects)
                print("abc物体"+abc_object.name)
                print("骨骼物体"+bone_axes_object.name)
                # 检查是否有活动物体
                if abc_object is not None:
                    # 添加数据传递修改器
                    modifier = abc_object.modifiers.new(name="Data Transfer", type='DATA_TRANSFER')
                    # 设置传递的目标对象
                    if bone_axes_object is not None:
                        modifier.object = bone_axes_object
                    else:
                        print("找不到源对象")
                    # 设置传递数据类型为顶点数据和顶点组数据
                    modifier.use_vert_data = True
                    modifier.data_types_verts = {'VGROUP_WEIGHTS'}  # 设置为您需要的数据类型
                    #bpy.context.view_layer.objects.active = abc_object
                    bpy.ops.object.datalayout_transfer(modifier="Data Transfer")
                    # 应用修改器
                    bpy.ops.object.modifier_apply(modifier=modifier.name)
                    abc_object.select_set(True)  # 选中abc
                    # 更新视图以反映选择的更改
                    bpy.context.view_layer.objects.active = abc_object
                    bpy.context.view_layer.update()
                else:
                    print("没有找到活动物体")
            else:
                self.report({'WARNING'}, message='活动物体含有顶点组')
        else:
            self.report({'WARNING'}, message='没有选中两个物体')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_89058(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_89058"
    bl_label = "清除骨骼约束"
    bl_description = "选中骨骼，将清除生成的骨骼约束"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if ((len(bpy.context.view_layer.objects.selected) == 1) and (bpy.context.view_layer.objects.active.type == 'ARMATURE')):
            for i_751D8 in range(len(bpy.context.view_layer.objects.active.data.bones)):
                for i_70648 in range(len(bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_751D8].name].constraints)-1,-1,-1):
                    if ('Copy Location_P' in bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_751D8].name].constraints[i_70648].name or 'Damped Track_X' in bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_751D8].name].constraints[i_70648].name or 'Damped Track_Z' in bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_751D8].name].constraints[i_70648].name):
                        bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_751D8].name].constraints.remove(constraint=bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_751D8].name].constraints[i_70648], )
                        self.report({'INFO'}, message='已移除约束')
        else:
            self.report({'WARNING'}, message='没有选中骨骼')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_C034B(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_c034b"
    bl_label = "烘焙约束"
    bl_description = "将ik约束烘焙为关键帧"
    bl_options = {"REGISTER", "UNDO"}
    sna_new_property: bpy.props.IntProperty(name='起始帧', description='', default=0, subtype='NONE', min=0)
    sna_new_property_001: bpy.props.IntProperty(name='结束帧', description='', default=250, subtype='NONE', min=0)

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (bpy.context.view_layer.objects.active.type == 'ARMATURE'):
            bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='POSE')
            bpy.ops.sna.my_generic_operator_400a9('INVOKE_DEFAULT', sna_new_property='腿ik骨')
            bpy.ops.nla.bake(frame_start=self.sna_new_property, frame_end=self.sna_new_property_001, only_selected=True, visual_keying=True, clear_constraints=True, use_current_action=True, bake_types={'POSE'})
            self.report({'INFO'}, message='烘焙完成')
        else:
            self.report({'WARNING'}, message='活动物体不是骨骼')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)
