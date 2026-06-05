# This module was split from the Serpens-generated mmd Quick tool source.


from .common import *


class SNA_OT_My_Generic_Operator_Bedaf(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_bedaf"
    bl_label = "材质到物体"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_73298 in range(len(bpy.context.view_layer.objects.selected)):
            if (property_exists("bpy.context.view_layer.objects.selected[i_73298].data.materials", globals(), locals()) and len(bpy.context.view_layer.objects.selected[i_73298].data.materials) > 0):
                bpy.context.view_layer.objects.selected[i_73298].name = bpy.context.view_layer.objects.selected[i_73298].data.materials[0].name
            else:
                self.report({'INFO'}, message=bpy.context.view_layer.objects.selected[i_73298].name + '没有材质')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_04Cf5(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_04cf5"
    bl_label = "物体到材质"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_E1144 in range(len(bpy.context.view_layer.objects.selected)):
            if (property_exists("bpy.context.view_layer.objects.selected[i_E1144].data.materials", globals(), locals()) and len(bpy.context.view_layer.objects.selected[i_E1144].data.materials) > 0):
                bpy.context.view_layer.objects.selected[i_E1144].data.materials[0].name = bpy.context.view_layer.objects.selected[i_E1144].name
            else:
                self.report({'INFO'}, message=bpy.context.view_layer.objects.selected[i_E1144].name + '没有材质')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_60634(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_60634"
    bl_label = "贴图到材质"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_F171C in range(len(bpy.context.view_layer.objects.selected)):
            if (property_exists("bpy.context.view_layer.objects.selected[i_F171C].data.materials", globals(), locals()) and len(bpy.context.view_layer.objects.selected[i_F171C].data.materials) > 0):
                for i_000DB in range(len(bpy.context.view_layer.objects.selected[i_F171C].data.materials[0].node_tree.nodes)):
                    if (bpy.context.view_layer.objects.selected[i_F171C].data.materials[0].node_tree.nodes[i_000DB].type == 'TEX_IMAGE'):
                        for i_E8F57 in range(len(bpy.context.view_layer.objects.selected[i_F171C].data.materials[0].node_tree.nodes[i_000DB].id_data.links)):
                            for i_85594 in range(len(['Color', 'Base Color', 'Diffuse Color', 'Albedo', 'Base Tex'])):
                                if ((bpy.context.view_layer.objects.selected[i_F171C].data.materials[0].node_tree.nodes[i_000DB].id_data.links[i_E8F57].to_socket.name == ['Color', 'Base Color', 'Diffuse Color', 'Albedo', 'Base Tex'][i_85594]) and (bpy.context.view_layer.objects.selected[i_F171C].data.materials[0].node_tree.nodes[i_000DB].id_data.links[i_E8F57].from_node == bpy.context.view_layer.objects.selected[i_F171C].data.materials[0].node_tree.nodes[i_000DB])):
                                    bpy.context.view_layer.objects.selected[i_F171C].name = bpy.context.view_layer.objects.selected[i_F171C].data.materials[0].node_tree.nodes[i_000DB].image.name
            else:
                self.report({'INFO'}, message=bpy.context.view_layer.objects.selected[i_F171C].name + '没有材质')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_Dd728(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_dd728"
    bl_label = "分离临时合并"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        node_tree['sna_sna_new_variable_001'] = 0
        node_tree['sna_sna_new_variable'] = []
        for i_F242D in range(len(bpy.context.view_layer.objects.active.vertex_groups)-1,-1,-1):
            if '_临时合并' in bpy.context.view_layer.objects.active.vertex_groups[i_F242D].name:
                node_tree['sna_sna_new_variable'].append(bpy.context.view_layer.objects.active.vertex_groups[i_F242D].name)
        if (len(node_tree['sna_sna_new_variable']) == 0):
            self.report({'WARNING'}, message='不存在临时合并顶点组数据')
        else:
            node_tree['sna_sna_new_variable_001'] = len(node_tree['sna_sna_new_variable'])
            node_tree['sna_sna_new_variable'] = []
            for i_583AB in range(len(bpy.context.view_layer.objects.active.data.attributes)-1,-1,-1):
                if '_临时合并' in bpy.context.view_layer.objects.active.data.attributes[i_583AB].name:
                    node_tree['sna_sna_new_variable'].append(None)
            if (len(node_tree['sna_sna_new_variable']) == 0):
                self.report({'WARNING'}, message='不存在临时合并属性数据')
            else:
                if (len(node_tree['sna_sna_new_variable']) == int(node_tree['sna_sna_new_variable_001'] * 3.0)):
                    for i_5CA6A in range(len(bpy.context.view_layer.objects.active.vertex_groups)-1,-1,-1):
                        if '_临时合并' in bpy.context.view_layer.objects.active.vertex_groups[i_5CA6A].name:
                            bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='EDIT')
                            bpy.ops.mesh.select_all('INVOKE_DEFAULT', action='DESELECT')
                            bpy.context.view_layer.objects.active.vertex_groups.active = bpy.context.view_layer.objects.active.vertex_groups[i_5CA6A]
                            bpy.ops.object.vertex_group_select('INVOKE_DEFAULT', )
                            if (i_5CA6A == 0):
                                pass
                            else:
                                bpy.ops.mesh.separate('INVOKE_DEFAULT', type='SELECTED')
                            bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='OBJECT')
                            node_tree['sna_act_obj'] = None
                            node_tree['sna_act_obj'] = bpy.context.view_layer.objects.active
                            bpy.context.view_layer.objects.active = ((bpy.context.view_layer.objects.active if (len(bpy.context.view_layer.objects.selected) == 1) else bpy.context.view_layer.objects.selected[1]) if (bpy.context.view_layer.objects.active == bpy.context.view_layer.objects.selected[0]) else bpy.context.view_layer.objects.selected[0])
                            bpy.context.view_layer.objects.active.name = bpy.context.view_layer.objects.active.vertex_groups.active.name.replace('_临时合并', '')
                            bpy.context.scene.tool_settings.use_transform_data_origin = True
                            print(str(tuple(bpy.context.view_layer.objects.active.data.attributes[bpy.context.view_layer.objects.active.name + '_临时合并_locatiion'].data[0].vector)), str(tuple(bpy.context.view_layer.objects.active.data.attributes[bpy.context.view_layer.objects.active.name + '_临时合并_rotation'].data[0].vector)), str(tuple(bpy.context.view_layer.objects.active.data.attributes[bpy.context.view_layer.objects.active.name + '_临时合并_scale'].data[0].vector)))
                            bpy.context.scene.cursor.location = bpy.context.view_layer.objects.active.data.attributes[bpy.context.view_layer.objects.active.name + '_临时合并_locatiion'].data[0].vector
                            bpy.context.scene.cursor.rotation_mode = 'XYZ'
                            bpy.context.scene.cursor.rotation_euler = bpy.context.view_layer.objects.active.data.attributes[bpy.context.view_layer.objects.active.name + '_临时合并_rotation'].data[0].vector
                            for i_2835C in range(len(bpy.context.screen.areas)):
                                if (bpy.context.screen.areas[i_2835C].type == 'VIEW_3D'):
                                    for i_8CD55 in range(len(bpy.context.screen.areas[i_2835C].regions)):
                                        if (bpy.context.screen.areas[i_2835C].regions[i_8CD55].type == 'WINDOW'):
                                            area_A79EE = bpy.context.screen.areas[i_2835C]
                                            region_A79EE = bpy.context.screen.areas[i_2835C].regions[i_8CD55]
                                            with bpy.context.temp_override(area=area_A79EE, region=region_A79EE, ):
                                                bpy.ops.transform.transform(mode='ALIGN', orient_type='CURSOR')
                                                bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
                                                bpy.ops.transform.resize(value=(float(bpy.context.view_layer.objects.active.data.attributes[bpy.context.view_layer.objects.active.name + '_临时合并_scale'].data[0].vector[0] / bpy.context.view_layer.objects.active.scale[0]), float(bpy.context.view_layer.objects.active.data.attributes[bpy.context.view_layer.objects.active.name + '_临时合并_scale'].data[0].vector[1] / bpy.context.view_layer.objects.active.scale[1]), float(bpy.context.view_layer.objects.active.data.attributes[bpy.context.view_layer.objects.active.name + '_临时合并_scale'].data[0].vector[2] / bpy.context.view_layer.objects.active.scale[2])), orient_type='LOCAL')
                                                bpy.context.scene.tool_settings.use_transform_data_origin = False
                                                for i_A23D9 in range(len(bpy.context.view_layer.objects.active.vertex_groups)-1,-1,-1):
                                                    if '_临时合并' in bpy.context.view_layer.objects.active.vertex_groups[i_A23D9].name:
                                                        bpy.context.view_layer.objects.active.vertex_groups.remove(group=bpy.context.view_layer.objects.active.vertex_groups[i_A23D9], )
                                                for i_DAB1C in range(len(bpy.context.view_layer.objects.active.data.attributes)-1,-1,-1):
                                                    if '_临时合并' in bpy.context.view_layer.objects.active.data.attributes[i_DAB1C].name:
                                                        bpy.context.view_layer.objects.active.data.attributes.remove(attribute=bpy.context.view_layer.objects.active.data.attributes[i_DAB1C], )
                                                bpy.context.view_layer.objects.active.select = False
                                                bpy.context.view_layer.objects.active = node_tree['sna_act_obj']
                    bpy.context.scene.cursor.location = (1.0, 1.0, 1.0)
                    self.report({'INFO'}, message='已分离临时合并')
                else:
                    self.report({'WARNING'}, message='顶点组数据与属性数据不匹配')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_Fb95F(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_fb95f"
    bl_label = "临时合并.001"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_7420F in range(len(bpy.context.view_layer.objects.selected)):
            bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.selected[i_7420F]
            group_AFFA2 = bpy.context.view_layer.objects.selected[i_7420F].vertex_groups.new(name=bpy.context.view_layer.objects.selected[i_7420F].name + '_' + '临时合并', )
            bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='EDIT')
            bpy.ops.mesh.select_all('INVOKE_DEFAULT', action='SELECT')
            bpy.ops.object.vertex_group_assign('INVOKE_DEFAULT', )
            bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='OBJECT')
            for i_A100E in range(3):
                output_data_0_ab157 = sna_switch_datain_C5A17(i_A100E, 'locatiion', 'rotation', 'scale', None, None)
                output_data_0_88913 = sna_switch_datain_C5A17(i_A100E, bpy.context.view_layer.objects.selected[i_7420F].location, bpy.context.view_layer.objects.selected[i_7420F].rotation_euler, bpy.context.view_layer.objects.selected[i_7420F].scale, None, None)
                bpy.ops.geometry.attribute_add(name=bpy.context.view_layer.objects.selected[i_7420F].name + '_' + '临时合并' + '_' + output_data_0_ab157, domain='POINT', data_type='FLOAT_VECTOR')
                for i_0948D in range(len(bpy.context.view_layer.objects.selected[i_7420F].data.attributes[bpy.context.view_layer.objects.selected[i_7420F].name + '_' + '临时合并' + '_' + output_data_0_ab157].data)):
                    bpy.context.view_layer.objects.selected[i_7420F].data.attributes[bpy.context.view_layer.objects.selected[i_7420F].name + '_' + '临时合并' + '_' + output_data_0_ab157].data[i_0948D].vector = output_data_0_88913
        bpy.ops.object.join('INVOKE_DEFAULT', )
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Abc_B0Bf3(bpy.types.Operator, ImportHelper):
    bl_idname = "sna.abc_b0bf3"
    bl_label = "为abc添加材质"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}
    filter_glob: bpy.props.StringProperty( default='*.mtl', options={'HIDDEN'} )

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if os.path.exists(self.filepath):
            if (os.path.splitext(self.filepath)[1] == '.mtl'):
                a = self.filepath
                mtl_file_path = None
                tex_name = None
                obj_name = None
                for i_00339 in range(len(tex_name)):
                    abc['sna_sna_new_variable'] = False
                    for i_910C4 in range(len(bpy.data.materials)):
                        if (bpy.data.materials[i_910C4].name == tex_name[i_00339]):
                            abc['sna_sna_new_variable'] = True
                            break
                    if abc['sna_sna_new_variable']:
                        bpy.context.view_layer.objects['xform_0_material_' + str(i_00339)].data.materials.append(material=bpy.data.materials[tex_name[i_00339]], )
                    else:
                        if (len(bpy.context.view_layer.objects['xform_0_material_' + str(i_00339)].material_slots) == 0):
                            material_2593F = bpy.data.materials.new(name=tex_name[i_00339], )
                            material_2593F.use_nodes = True
                            if (os.path.exists(os.path.join(os.path.dirname(self.filepath),tex_name[i_00339])) and ('' != tex_name[i_00339])):
                                node_E38B9 = material_2593F.node_tree.nodes.new(type='ShaderNodeTexImage', )
                                node_E38B9.location = (-300.0, 300.0)
                            if (os.path.exists(os.path.join(os.path.dirname(self.filepath),tex_name[i_00339])) and ('' != tex_name[i_00339])):
                                image_7D5F6 = bpy.data.images.load(filepath=os.path.join(os.path.dirname(self.filepath),tex_name[i_00339]), check_existing=True, )
                                node_E38B9.image = image_7D5F6
                                link_92E7A = material_2593F.node_tree.links.new(input=material_2593F.node_tree.nodes[('原理化BSDF' if bpy.context.preferences.view.use_translate_new_dataname else 'Principled BSDF')].inputs['Base Color'], output=node_E38B9.outputs['Color'], )
                                link_72978 = material_2593F.node_tree.links.new(input=material_2593F.node_tree.nodes[('原理化BSDF' if bpy.context.preferences.view.use_translate_new_dataname else 'Principled BSDF')].inputs['Alpha'], output=node_E38B9.outputs['Alpha'], )
                            else:
                                self.report({'WARNING'}, message='贴图' + tex_name[i_00339] + '不存在')
                            bpy.context.view_layer.objects['xform_0_material_' + str(i_00339)].data.materials.append(material=material_2593F, )
                        else:
                            self.report({'WARNING'}, message=bpy.context.view_layer.objects['xform_0_material_' + str(i_00339)].name + '已存在材质')
                self.report({'INFO'}, message='成功添加材质')
            else:
                self.report({'WARNING'}, message='选中文件不是mtl')
        else:
            self.report({'WARNING'}, message='输入路径为空')
        return {"FINISHED"}

class SNA_OT_My_Generic_Operator_Abaaa(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_abaaa"
    bl_label = "移除选中物体所有材质"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_F4DCC in range(len(bpy.context.view_layer.objects.selected)):
            bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.selected[i_F4DCC]
            for i_356FC in range(len(bpy.context.view_layer.objects.selected[i_F4DCC].material_slots)):
                bpy.ops.object.material_slot_remove('INVOKE_DEFAULT', )
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator015_0Ebb1(bpy.types.Operator):
    bl_idname = "sna.operator015_0ebb1"
    bl_label = "Operator.015"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    def sna_new_property_enum_items(self, context):
        return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]
    sna_new_property: bpy.props.EnumProperty(name='位姿', description='', items=[('位置', '位置', '', 0, 0), ('旋转', '旋转', '', 0, 1), ('缩放', '缩放', '', 0, 2)])
    sna_x: bpy.props.BoolProperty(name='x', description='', default=True)
    sna_y: bpy.props.BoolProperty(name='y', description='', default=True)
    sna_z: bpy.props.BoolProperty(name='z', description='', default=True)

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_37CB5 in range(len(bpy.context.selected_objects)):
            if (self.sna_new_property == '位置'):
                if property_exists("bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].location", globals(), locals()):
                    bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].location = tuple(mathutils.Vector((bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].location if (self.sna_new_property == '位置') else (bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].rotation_euler if (self.sna_new_property == '旋转') else None))) * mathutils.Vector(((0 if self.sna_x else 1), (0 if self.sna_y else 1), (0 if self.sna_z else 1))))
            else:
                if (self.sna_new_property == '旋转'):
                    if property_exists("bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].rotation_euler", globals(), locals()):
                        bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].rotation_euler = tuple(mathutils.Vector((bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].location if (self.sna_new_property == '位置') else (bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].rotation_euler if (self.sna_new_property == '旋转') else None))) * mathutils.Vector(((0 if self.sna_x else 1), (0 if self.sna_y else 1), (0 if self.sna_z else 1))))
                else:
                    if (self.sna_new_property == '缩放'):
                        if property_exists("bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].scale", globals(), locals()):
                            bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].scale = ((1.0 if self.sna_x else bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].scale[0]), (1.0 if self.sna_y else bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].scale[1]), (1.0 if self.sna_z else bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].scale[2]))
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator024_D37Ce(bpy.types.Operator):
    bl_idname = "sna.operator024_d37ce"
    bl_label = "Operator.024"
    bl_description = "将当前帧设置为结束帧"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.frame_end = bpy.context.scene.frame_current
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator023_Dc120(bpy.types.Operator):
    bl_idname = "sna.operator023_dc120"
    bl_label = "Operator.023"
    bl_description = "将当前帧设置为起始帧"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.frame_start = bpy.context.scene.frame_current
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator021_0D655(bpy.types.Operator):
    bl_idname = "sna.operator021_0d655"
    bl_label = "Operator.021"
    bl_description = "删除装配产生的材质变形节点组"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        # 获取当前选中的对象
        selected_objects = bpy.context.selected_objects
        for obj in selected_objects:
            # 检查对象是否有材质
            if obj.material_slots:
                for slot in obj.material_slots:
                    # 检查材质是否有节点
                    if slot.material.use_nodes:
                        # 初始化要删除的节点列表
                        nodes_to_remove = []
                        # 初始化贴图节点变量
                        base1_rgb_texture_node = None
                        # 遍历节点，收集所有MMDMorphAdd和MMDMorphMul节点，并找到初始的贴图节点
                        for node in slot.material.node_tree.nodes:
                            if node.type == 'GROUP' and ('MMDMorphAdd' in node.node_tree.name or 'MMDMorphMul' in node.node_tree.name):
                                # 如果是第一个MMDMorph节点组，获取它的贴图
                                if base1_rgb_texture_node is None:
                                    for link in node.inputs['Base1 RGB'].links:
                                        if link.from_node.type == 'TEX_IMAGE':
                                            base1_rgb_texture_node = link.from_node
                                            break
                                # 添加节点到待删除列表
                                nodes_to_remove.append(node)
                        # 删除所有MMDMorphAdd和MMDMorphMul节点
                        for node in nodes_to_remove:
                            slot.material.node_tree.nodes.remove(node)
                        # 如果找到贴图节点，连接到MMDShaderDev的Base Tex输入
                        if base1_rgb_texture_node:
                            # 找到MMDShaderDev节点组
                            target_node_group = next((node for node in slot.material.node_tree.nodes if node.type == 'GROUP' and 'MMDShaderDev' in node.node_tree.name), None)
                            # 连接贴图节点到MMDShaderDev的Base Tex
                            if target_node_group:
                                slot.material.node_tree.links.new(target_node_group.inputs['Base Tex'], base1_rgb_texture_node.outputs['Color'])
        # 更新场景，以反映节点更改
        bpy.context.view_layer.update()
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator005_9368B(bpy.types.Operator):
    bl_idname = "sna.operator005_9368b"
    bl_label = "Operator.005"
    bl_description = "将替换mmd自带节点组为原理化节点组"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        # 获取当前选中的物体
        selected_objects = bpy.context.selected_objects
        # 遍历选中的物体
        for obj in selected_objects:
            # 遍历物体的所有材质槽
            for material_slot in obj.material_slots:
                material = material_slot.material
                # 遍历材质的所有节点
                for node in material.node_tree.nodes:
                    # 检查节点的类型和名称
                    if node.type == 'GROUP' and node.node_tree.name == 'MMDShaderDev':  # 替换为你的节点组名称
                        # 获取节点组的输入
                        base_tex_input = node.inputs.get('Base Tex')
                        base_alpha_input = node.inputs.get('Base Alpha')
                        # 如果找到对应的输入，继续处理
                        if base_tex_input and base_alpha_input:
                            # 获取连接到 Base Tex 和 Base Alpha 的连接
                            base_tex_link = base_tex_input.links[0] if base_tex_input.links else None
                            base_alpha_link = base_alpha_input.links[0] if base_alpha_input.links else None
                            # 创建新的原理化节点
                            principled_node = material.node_tree.nodes.new(type='ShaderNodeBsdfPrincipled')
                            principled_node.location = node.location
                            # 连接 Base Tex
                            if base_tex_link:
                                material.node_tree.links.new(principled_node.inputs['Base Color'], base_tex_link.from_socket)
                            # 连接 Base Alpha
                            if base_alpha_link:
                                material.node_tree.links.new(principled_node.inputs['Alpha'], base_alpha_link.from_socket)
                            # 连接新原理化节点到材质输出
                            material_output_node = material.node_tree.nodes.get("Material Output")
                            if material_output_node:
                                material.node_tree.links.new(material_output_node.inputs['Surface'], principled_node.outputs['BSDF'])
                            # 删除旧的节点
                            material.node_tree.nodes.remove(node)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator004_Fa32A(bpy.types.Operator):
    bl_idname = "sna.operator004_fa32a"
    bl_label = "Operator.004"
    bl_description = "合并使用同一基础色贴图的材质"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        # 存储贴图的字典
        texture_dict = {}
        color_input_name=["Color", "Base Color", "Diffuse Color", "Albedo","Base Tex"]
        # 获取所选物体列表
        selected_objects = bpy.context.selected_objects
        # 循环遍历所选物体
        for obj in selected_objects:
            # 检查物体是否为网格对象
            if isinstance(obj.data, bpy.types.Mesh):
                # 遍历物体的材质列表
                for material in obj.data.materials:
                    # 获取材质的节点树
                    tree = material.node_tree
                    # 遍历节点树中的所有节点
                    for node in tree.nodes:
                        # 检查节点类型是否为ShaderNodeTexImage（贴图节点）
                        if node.type == 'TEX_IMAGE':
                            # 检查节点的输出连接是否存在
                            if node.outputs['Color'].is_linked:
                                # 遍历节点的输出连接
                                for link in node.outputs['Color'].links:
                                    # 检查连接的输入端口名称是否为"基础颜色"
                                    for input_name in color_input_name:
                                        if link.to_socket.name == input_name:
                                            # 检查贴图是否已经在字典中
                                            if node.image.name not in texture_dict:
                                                # 将贴图节点添加到字典
                                                texture_dict[node.image.name] = material
                                                print('贴图已经在字典中', node.image.name)
                                            else:
                                                # 替换材质为字典中的材质
                                                new_material = texture_dict[node.image.name]
                                                # 将物体的材质更改为新的材质
                                                obj.data.materials[0] = new_material
                                                print('贴图不在字典中', node.image.name, '替换材质:', new_material.name)
                                    else:
                                        print('连接端口的贴图没找到')
                        else:
                            print("没有找到贴图")
            else:
                print('没有找到网格对象')
        #清理未使用数据块
        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
        # 设置材质的名称为贴图名称
        for tex_name, material in texture_dict.items():
            material.name = tex_name
        # 打印贴图字典
        print(texture_dict)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator025_4038C(bpy.types.Operator):
    bl_idname = "sna.operator025_4038c"
    bl_label = "Operator.025"
    bl_description = "为选中物体添加表情(需要安装mmd插件)"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        try:
            import_vmd = bpy.ops.mmd_tools.import_vmd
        except AttributeError:
            self.report({'INFO'}, message='需要先安装并启用 mmd_tools 插件')
            return {"FINISHED"}
        for i_0D15C in range(len(bpy.context.view_layer.objects.selected)):
            bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.selected[i_0D15C]
            try:
                import_vmd('INVOKE_DEFAULT', )
            except (RuntimeError, AttributeError) as ex:
                if 'could not be found' in str(ex):
                    self.report({'INFO'}, message='需要先安装并启用 mmd_tools 插件')
                    return {"FINISHED"}
                raise
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator001_64C4A(bpy.types.Operator):
    bl_idname = "sna.operator001_64c4a"
    bl_label = "Operator.001"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.render.resolution_x = 2560
        bpy.context.scene.render.resolution_y = 1440
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator_B46A6(bpy.types.Operator):
    bl_idname = "sna.operator_b46a6"
    bl_label = "Operator"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.render.resolution_x = 1920
        bpy.context.scene.render.resolution_y = 1080
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator007_85779(bpy.types.Operator):
    bl_idname = "sna.operator007_85779"
    bl_label = "Operator.007"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}
    sna_ax: bpy.props.IntProperty(name='ax', description='', default=0, subtype='NONE')

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        self.sna_ax = bpy.context.scene.render.resolution_x
        bpy.context.scene.render.resolution_x = bpy.context.scene.render.resolution_y
        bpy.context.scene.render.resolution_y = self.sna_ax
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator008_F7B4C(bpy.types.Operator):
    bl_idname = "sna.operator008_f7b4c"
    bl_label = "Operator.008"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.render.resolution_x = int(bpy.context.scene.render.resolution_x / 2.0)
        bpy.context.scene.render.resolution_y = int(bpy.context.scene.render.resolution_y / 2.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator002_7Dbd9(bpy.types.Operator):
    bl_idname = "sna.operator002_7dbd9"
    bl_label = "Operator.002"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.render.resolution_x = 3840
        bpy.context.scene.render.resolution_y = 2160
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator014_47F89(bpy.types.Operator):
    bl_idname = "sna.operator014_47f89"
    bl_label = "Operator.014"
    bl_description = "方形"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.render.resolution_x = 1920
        bpy.context.scene.render.resolution_y = 1920
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)
