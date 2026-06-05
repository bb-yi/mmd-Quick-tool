# This module was split from the Serpens-generated mmd Quick tool source.


from .common import *


class SNA_OT_Operator_F1B3D(bpy.types.Operator):
    bl_idname = "sna.operator_f1b3d"
    bl_label = "Operator"
    bl_description = "选中一个相机，为这个相机配置自动对焦和光圈系统"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        node_tree_005['sna_camera'] = None
        node_tree_005['sna_sna_new_variable_001'] = None
        node_tree_005['sna_sna_new_variable'] = None
        node_tree_005['sna_sna_new_variable_002'] = None
        node_tree_005['sna_sna_new_variable_003'] = None
        node_tree_005['sna_sna_new_variable_002'] = None
        node_tree_005['sna_camera'] = bpy.context.view_layer.objects.active
        if os.path.exists(os.path.join(os.path.dirname(__file__), 'assets', '光圈焦点.blend')):
            if (len(bpy.context.view_layer.objects.selected) == 1):
                if (bpy.context.view_layer.objects.active.type == 'CAMERA'):
                    before_data = list(bpy.data.collections)
                    bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', '光圈焦点.blend') + r'\Collection', filename='光圈焦点', link=False)
                    new_data = list(filter(lambda d: not d in before_data, list(bpy.data.collections)))
                    appended_474EA = None if not new_data else new_data[0]
                    print(appended_474EA.name)
                    for i_54FD0 in range(len(appended_474EA.objects)):
                        if '焦点烘焙' in appended_474EA.objects[i_54FD0].name:
                            node_tree_005['sna_sna_new_variable_002'] = appended_474EA.objects[i_54FD0]
                        if '焦点物体' in appended_474EA.objects[i_54FD0].name:
                            node_tree_005['sna_sna_new_variable'] = appended_474EA.objects[i_54FD0]
                        if '光圈物体' in appended_474EA.objects[i_54FD0].name:
                            node_tree_005['sna_sna_new_variable_001'] = appended_474EA.objects[i_54FD0]
                        if ('焦点' in appended_474EA.objects[i_54FD0].name and ('EMPTY' == appended_474EA.objects[i_54FD0].type)):
                            node_tree_005['sna_sna_new_variable_002'] = appended_474EA.objects[i_54FD0]
                        if ('光圈' in appended_474EA.objects[i_54FD0].name and ('EMPTY' == appended_474EA.objects[i_54FD0].type)):
                            node_tree_005['sna_sna_new_variable_003'] = appended_474EA.objects[i_54FD0]
                    print(node_tree_005['sna_sna_new_variable'].name, node_tree_005['sna_sna_new_variable_001'].name, node_tree_005['sna_sna_new_variable_002'].name, node_tree_005['sna_sna_new_variable_003'].name, node_tree_005['sna_camera'].name, node_tree_005['sna_sna_new_variable_002'].name)
                    node_tree_005['sna_sna_new_variable'].modifiers['GeometryNodes'].node_group.nodes['对焦物体'].inputs[2].default_value = node_tree_005['sna_camera']
                    driver_0_eeb89, var_1_eeb89 = sna_in_79644(node_tree_005['sna_sna_new_variable'].modifiers['GeometryNodes'].node_group, '对焦物体', '分辨率X', 'SCENE', bpy.context.scene, 'render.resolution_x')
                    driver_0_2ed19, var_1_2ed19 = sna_in_79644(node_tree_005['sna_sna_new_variable'].modifiers['GeometryNodes'].node_group, '对焦物体', '分辨率Y', 'SCENE', bpy.context.scene, 'render.resolution_y')
                    driver_0_74dc9, var_1_74dc9 = sna_in_79644(node_tree_005['sna_sna_new_variable'].modifiers['GeometryNodes'].node_group, '对焦物体', '焦距', 'CAMERA', node_tree_005['sna_camera'].data, 'lens')
                    node_tree_005['sna_sna_new_variable_001'].modifiers['GeometryNodes'].node_group.nodes['光圈'].inputs[1].default_value = node_tree_005['sna_camera']
                    node_tree_005['sna_sna_new_variable_001'].modifiers['GeometryNodes'].node_group.nodes['光圈'].inputs[2].default_value = node_tree_005['sna_sna_new_variable_002']
                    driver_0_f9206, var_1_f9206 = sna_in_79644(node_tree_005['sna_sna_new_variable_001'].modifiers['GeometryNodes'].node_group, '光圈', '焦距', 'CAMERA', node_tree_005['sna_camera'].data, 'lens')
                    node_tree_005['sna_camera'].data.dof.use_dof = True
                    node_tree_005['sna_camera'].data.dof.focus_object = node_tree_005['sna_sna_new_variable_002']
                    success_7BE7A = node_tree_005['sna_camera'].data.driver_remove('dof.aperture_fstop', )
                    driver_BDF65 = node_tree_005['sna_camera'].data.driver_add('dof.aperture_fstop', )
                    driver_BDF65.driver.type = 'SCRIPTED'
                    var_C8F2F = driver_BDF65.driver.variables.new()
                    var_C8F2F.name = 'var'
                    var_C8F2F.type = 'TRANSFORMS'
                    var_C8F2F.targets[0].id = node_tree_005['sna_sna_new_variable_003']
                    var_C8F2F.targets[0].transform_type = 'LOC_Z'
                    driver_BDF65.driver.expression = 'var'
                    node_tree_005['sna_sna_new_variable_001'].hide_render = True
                    node_tree_005['sna_sna_new_variable'].hide_render = True
                    self.report({'INFO'}, message='配置完成')
                    self.report({'INFO'}, message='记得去几何节点里设置对焦物体（没有报错）')
                else:
                    self.report({'WARNING'}, message='所选物体不是相机')
            else:
                self.report({'WARNING'}, message='选中一个相机')
        else:
            self.report({'ERROR'}, message='光圈焦点资产不存在')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Bake_Tex_F278F(bpy.types.Operator):
    bl_idname = "sna.bake_tex_f278f"
    bl_label = "bake_tex"
    bl_description = "bake"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (getattr(bpy.context.area, 'type', None) == 'NODE_EDITOR'):
            active_object = bpy.context.active_object
            material = getattr(active_object, 'active_material', None)
            node_tree = getattr(material, 'node_tree', None)
            if node_tree is None:
                self.report({'INFO'}, message='活动物体没有可烘焙的节点材质')
                return {"FINISHED"}
            if bpy.context.scene.sna_use_choose_tex:
                active_node = node_tree.nodes.active
                if ((active_node is not None) and ('TEX_IMAGE' == active_node.type) and (active_node.select == True)):
                    bpy.ops.object.bake('INVOKE_DEFAULT', type='EMIT', margin=16, margin_type='ADJACENT_FACES', target='IMAGE_TEXTURES', use_clear=True)
                    self.report({'INFO'}, message='烘焙完成')
                else:
                    self.report({'INFO'}, message='没有选中图像节点')
            else:
                node_tree_004['sna_last_node'] = None
                for i_E93E1 in range(len(node_tree.links)):
                    if (('材质输出' == node_tree.links[i_E93E1].to_node.name) or (node_tree.links[i_E93E1].to_node.name == 'Material Output')):
                        node_tree_004['sna_last_node'] = node_tree.links[i_E93E1].from_node
                        print(node_tree.links[i_E93E1].to_node.name)
                if node_tree_004['sna_last_node'] is None:
                    self.report({'INFO'}, message='没有找到连接到材质输出的节点')
                    return {"FINISHED"}
                node_73893 = node_tree.nodes.new(type='ShaderNodeTexImage', )
                node_73893.location = tuple(mathutils.Vector(node_tree_004['sna_last_node'].location) + mathutils.Vector((0.0, 250.0)))
                image_E6981 = bpy.data.images.new(name='bake_tex', width=bpy.context.scene.sna_bake_tex_size_x, height=bpy.context.scene.sna_bake_tex_size_y, alpha=True, )
                node_73893.image = image_E6981
                for i_3E53F in range(len(node_tree.nodes)):
                    node_tree.nodes[i_3E53F].select = False
                node_73893.select = True
                node_tree.nodes.active = node_73893
                bpy.ops.object.bake('INVOKE_DEFAULT', type='EMIT', margin=16, margin_type='ADJACENT_FACES', target='IMAGE_TEXTURES', use_clear=True)
                self.report({'INFO'}, message='烘焙完成')
        else:
            self.report({'INFO'}, message='活动区域不在节点编辑器')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_7A93E(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_7a93e"
    bl_label = "复制活动骨骼权重到选中骨骼"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}
    sna_new_property: bpy.props.BoolProperty(name='保留目标骨骼的权重', description='', default=False)
    sna_new_property_001: bpy.props.BoolProperty(name='移除源骨骼权重', description='', default=False)

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        node_tree_008['sna_select_obj'] = []
        node_tree_008['sna_bone_obj'] = None
        node_tree_008['sna_bone_weight_from'] = None
        node_tree_008['sna_bone_weight_to'] = []
        node_tree_008['sna_num'] = 0
        for i_7D72D in range(len(bpy.context.selected_objects)):
            if (bpy.context.selected_objects[i_7D72D].type == 'MESH'):
                node_tree_008['sna_select_obj'].append(bpy.context.selected_objects[i_7D72D])
            if (bpy.context.selected_objects[i_7D72D].type == 'ARMATURE'):
                node_tree_008['sna_bone_obj'] = bpy.context.selected_objects[i_7D72D]
                node_tree_008['sna_num'] = int(node_tree_008['sna_num'] + 1.0)
        if (node_tree_008['sna_num'] == 1):
            node_tree_008['sna_num'] = 0
            node_tree_008['sna_bone_weight_from'] = node_tree_008['sna_bone_obj'].data.bones.active
            for i_E5D6B in range(len(node_tree_008['sna_bone_obj'].data.bones)):
                if node_tree_008['sna_bone_obj'].data.bones[i_E5D6B].select:
                    node_tree_008['sna_bone_weight_to'].append(node_tree_008['sna_bone_obj'].data.bones[i_E5D6B])
            print(str(node_tree_008['sna_select_obj']), node_tree_008['sna_bone_obj'].name, node_tree_008['sna_bone_weight_from'].name, str(node_tree_008['sna_bone_weight_to']))
            for i_D8AF4 in range(len(node_tree_008['sna_select_obj'])):
                for i_A491A in range(len(node_tree_008['sna_bone_weight_to'])):
                    if (node_tree_008['sna_bone_weight_from'].name == node_tree_008['sna_bone_weight_to'][i_A491A].name):
                        pass
                    else:
                        if (property_exists("node_tree_008['sna_select_obj'][i_D8AF4].vertex_groups", globals(), locals()) and node_tree_008['sna_bone_weight_to'][i_A491A].name in node_tree_008['sna_select_obj'][i_D8AF4].vertex_groups):
                            if self.sna_new_property:
                                pass
                            else:
                                node_tree_008['sna_select_obj'][i_D8AF4].vertex_groups.remove(group=node_tree_008['sna_select_obj'][i_D8AF4].vertex_groups[node_tree_008['sna_bone_weight_to'][i_A491A].name], )
                                group_A4275 = node_tree_008['sna_select_obj'][i_D8AF4].vertex_groups.new(name=node_tree_008['sna_bone_weight_to'][i_A491A].name, )
                        else:
                            group_6A270 = node_tree_008['sna_select_obj'][i_D8AF4].vertex_groups.new(name=node_tree_008['sna_bone_weight_to'][i_A491A].name, )
                for i_00775 in range(len(node_tree_008['sna_select_obj'][i_D8AF4].data.vertices)):
                    for i_E114B in range(len(node_tree_008['sna_select_obj'][i_D8AF4].data.vertices[i_00775].groups)):
                        if (node_tree_008['sna_select_obj'][i_D8AF4].vertex_groups[node_tree_008['sna_select_obj'][i_D8AF4].data.vertices[i_00775].groups[i_E114B].group].name == node_tree_008['sna_bone_weight_from'].name):
                            for i_2F3E8 in range(len(node_tree_008['sna_bone_weight_to'])):
                                if (node_tree_008['sna_bone_weight_from'].name == node_tree_008['sna_bone_weight_to'][i_2F3E8].name):
                                    pass
                                else:
                                    if self.sna_new_property:
                                        node_tree_008['sna_select_obj'][i_D8AF4].vertex_groups[node_tree_008['sna_bone_weight_to'][i_2F3E8].name].add(index=(i_00775, i_00775, i_00775), weight=node_tree_008['sna_select_obj'][i_D8AF4].data.vertices[i_00775].groups[i_E114B].weight, type='ADD', )
                                    else:
                                        node_tree_008['sna_select_obj'][i_D8AF4].vertex_groups[node_tree_008['sna_bone_weight_to'][i_2F3E8].name].add(index=(i_00775, i_00775, i_00775), weight=node_tree_008['sna_select_obj'][i_D8AF4].data.vertices[i_00775].groups[i_E114B].weight, type='REPLACE', )
                if self.sna_new_property_001:
                    node_tree_008['sna_select_obj'][i_D8AF4].vertex_groups.remove(group=node_tree_008['sna_select_obj'][i_D8AF4].vertex_groups[node_tree_008['sna_bone_weight_from'].name], )
                    group_6C7C6 = node_tree_008['sna_select_obj'][i_D8AF4].vertex_groups.new(name=node_tree_008['sna_bone_weight_from'].name, )
                    self.report({'INFO'}, message='完成')
        else:
            self.report({'WARNING'}, message='选择的骨架超过一个')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)
