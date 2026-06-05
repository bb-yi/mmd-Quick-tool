# This module was split from the Serpens-generated mmd Quick tool source.


from .common import *


class SNA_OT_Operator020_173C4(bpy.types.Operator):
    bl_idname = "sna.operator020_173c4"
    bl_label = "Operator.020"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_DBE3D in range(len(bpy.context.view_layer.objects.selected)):
            bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.selected[i_DBE3D]
            bpy.ops.mesh.customdata_custom_splitnormals_clear('INVOKE_DEFAULT', )
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator022_D211D(bpy.types.Operator):
    bl_idname = "sna.operator022_d211d"
    bl_label = "Operator.022"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_687B4 in range(len(bpy.context.view_layer.objects.selected)-1,-1,-1):
            bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.selected[i_687B4]
            shape_keys = getattr(getattr(bpy.context.active_object, 'data', None), 'shape_keys', None)
            animation_data = getattr(shape_keys, 'animation_data', None)
            action = getattr(animation_data, 'action', None)
            if action is None:
                continue
            for i_3F2FD in range(len(action.fcurves)-1,-1,-1):
                if (len(action.fcurves[i_3F2FD].keyframe_points) == 1):
                    action.fcurves.remove(fcurve=action.fcurves[i_3F2FD], )
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator023_9E188(bpy.types.Operator):
    bl_idname = "sna.operator023_9e188"
    bl_label = "Operator.023"
    bl_description = "清理形态键上的驱动器"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        # 获取当前选中的所有物体
        selected_objects = bpy.context.selected_objects
        # 遍历选中的物体
        for obj in selected_objects:
            # 检查对象是否有形态键
            shape_keys = getattr(getattr(obj, 'data', None), 'shape_keys', None)
            animation_data = getattr(shape_keys, 'animation_data', None)
            if shape_keys and animation_data:
                # 遍历所有形态键
                for key_block in shape_keys.key_blocks:
                    # 获取形态键的驱动器数据路径
                    data_path = 'key_blocks["{}"].value'.format(key_block.name)
                    # 尝试获取驱动器
                    driver = animation_data.drivers.find(data_path)
                    # 如果驱动器存在，移除它
                    if driver:
                        animation_data.drivers.remove(driver)
        print("完成对选中物体形态键驱动器的移除")
        # 更新视图，以便立即看到更改的效果
        bpy.context.view_layer.update()
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator024_1Bdb7(bpy.types.Operator):
    bl_idname = "sna.operator024_1bdb7"
    bl_label = "Operator.024"
    bl_description = "清除选中物体材质中未使用的节点"
    bl_options = {"REGISTER", "UNDO"}
    sna_new_property: bpy.props.IntProperty(name='深度', description='', default=1, subtype='NONE', min=1)

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        x = self.sna_new_property

        def delete_unconnected_nodes(material):
            # 遍历材质中的所有节点
            for node in material.node_tree.nodes:
                # 跳过材质输出节点
                if node.type == 'OUTPUT_MATERIAL':
                    continue
                # 检查节点的每个输出是否连接到其他节点
                if all(output.is_linked == False for output in node.outputs):
                    # 删除未连接的节点
                    material.node_tree.nodes.remove(node)

        def main():
            # 确保有物体被选中
            if bpy.context.selected_objects:
                for obj in bpy.context.selected_objects:
                    # 确保物体有材质
                    if obj.data.materials:
                        for mat in obj.data.materials:
                            # 如果材质存在节点，则调用函数
                            if mat and mat.node_tree:
                                delete_unconnected_nodes(mat)
        # 调用主函数
        #x = 3 #删除深度
        for i in range(x):
            main()
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator025_C68F6(bpy.types.Operator):
    bl_idname = "sna.operator025_c68f6"
    bl_label = "Operator.025"
    bl_description = "清除选中物体的骨骼修改器"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_A9AE5 in range(len(bpy.context.view_layer.objects.selected)):
            if (bpy.context.view_layer.objects.selected[i_A9AE5].type == 'MESH'):
                for i_02857 in range(len(bpy.context.view_layer.objects.selected[i_A9AE5].modifiers)):
                    print(bpy.context.view_layer.objects.selected[i_A9AE5].modifiers[i_02857].type)
                    if (bpy.context.view_layer.objects.selected[i_A9AE5].modifiers[i_02857].type == 'ARMATURE'):
                        bpy.context.view_layer.objects.selected[i_A9AE5].modifiers.remove(modifier=bpy.context.view_layer.objects.selected[i_A9AE5].modifiers[i_02857], )
                        break
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator002_Ac0A6(bpy.types.Operator):
    bl_idname = "sna.operator002_ac0a6"
    bl_label = "Operator.002"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.sna_view_tex = (not bpy.context.scene.sna_view_tex)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator001_1136E(bpy.types.Operator):
    bl_idname = "sna.operator001_1136e"
    bl_label = "Operator.001"
    bl_description = "选中相同材质的物体"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        # 获取当前场景
        scene = bpy.context.scene
        # 获取当前选中的物体
        active_obj = bpy.context.active_object
        # 检查是否有选中物体和它是否有材质
        if active_obj and active_obj.material_slots:
            # 获取选中物体的所有材质
            active_materials = set(slot.material for slot in active_obj.material_slots if slot.material)
            # 遍历场景中的所有物体
            for obj in scene.objects:
                # 只对网格物体进行操作
                if obj.type == 'MESH':
                    # 遍历物体的所有材质插槽
                    for slot in obj.material_slots:
                        # 如果物体使用了与选中物体相同的材质之一
                        if slot.material in active_materials:
                            # 选择物体
                            obj.select_set(True)
                            # 一旦找到匹配的材质，无需检查其余材质
                            break
        else:
            print("No active mesh object with materials selected.")
        # 更新视图层以反映物体的选择变化
        bpy.context.view_layer.update()
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_Operator_5Ed64(bpy.types.Operator):
    bl_idname = "sna.operator_5ed64"
    bl_label = "Operator"
    bl_description = "在材质编辑器中选择一个贴图节点，就选中相同使用了这张贴图的物体"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        import bpy
        # 此函数用于在Blender中显示提示信息

        def show_message_box(message = "", title = "Message Box", icon = 'INFO'):

            def draw(self, context):
                self.layout.label(text=message)
            bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)
        # 使用示例
        show_message_box("未选中纹理节点", "提示", 'ERROR')
        # 初始化变量
        selected_image = None
        node_editor = None
        # 尝试获取当前节点编辑器的上下文
        for area in bpy.context.screen.areas:
            if area.type == 'NODE_EDITOR':
                node_editor = area.spaces.active
                break
        # 如果找到节点编辑器
        if node_editor and node_editor.tree_type == 'ShaderNodeTree' and node_editor.edit_tree:
            # 获取选中的节点
            selected_nodes = [node for node in node_editor.edit_tree.nodes if node.select and node.type == 'TEX_IMAGE']
            # 如果选中了纹理节点，获取它的图像数据
            if selected_nodes:
                selected_image = selected_nodes[0].image
            else:
                show_message_box("未选中纹理节点", "提示", 'ERROR')
        # 如果有选中的纹理
        if selected_image:
            # 遍历所有物体
            for obj in bpy.data.objects:
                # 只检查具有材质的网格物体
                if obj.type == 'MESH' and obj.material_slots:
                    # 遍历所有材质插槽
                    for slot in obj.material_slots:
                        if slot.material and slot.material.use_nodes:
                            # 遍历所有材质节点
                            for node in slot.material.node_tree.nodes:
                                if node.type == 'TEX_IMAGE' and node.image == selected_image:
                                    # 如果该材质使用了选中的纹理，选中物体
                                    obj.select_set(True)
                                    break  # 跳出节点循环
        else:
            print("No texture node selected in the active Node Editor.")
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_400A9(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_400a9"
    bl_label = "选中骨架"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    def sna_new_property_enum_items(self, context):
        return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]
    sna_new_property: bpy.props.EnumProperty(name='选择', description='', items=[('腿ik骨', '腿ik骨', '', 0, 0), ('全部身体骨', '全部身体骨', '', 0, 1), ('身体骨', '身体骨', '', 0, 2), ('手骨', '手骨', '', 0, 3), ('调整骨', '调整骨', '', 0, 4), ('d骨', 'd骨', '', 0, 5), ('捩骨', '捩骨', '', 0, 6)])

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if self.sna_new_property == "全部身体骨":
            for i_30AF0 in range(len(['足.L', 'ひざ.L', '足首.L', '足先EX.L', '足.R', 'ひざ.R', '足首.R', '足先EX.R'])):
                bpy.ops.object.select_pattern(pattern=['足.L', 'ひざ.L', '足首.L', '足先EX.L', '足.R', 'ひざ.R', '足首.R', '足先EX.R'][i_30AF0])
            for i_FCA08 in range(len(['下半身', '上半身2', '上半身', '上半身3', '首', '頭', '肩.R', '肩.L', '腕.R', '腕.L', 'ひじ.R', 'ひじ.L', '手首.R', '手首.L'])):
                bpy.ops.object.select_pattern(pattern=['下半身', '上半身2', '上半身', '上半身3', '首', '頭', '肩.R', '肩.L', '腕.R', '腕.L', 'ひじ.R', 'ひじ.L', '手首.R', '手首.L'][i_FCA08])
            for i_AA1B7 in range(len(['親指０.R', '親指１.R', '親指２.R', '人指０.R', '人指１.R', '人指２.R', '人指３.R', '中指０.R', '中指１.R', '中指２.R', '中指３.R', '薬指０.R', '薬指１.R', '薬指２.R', '薬指３.R', '小指０.R', '小指１.R', '小指２.R', '小指３.R'])):
                bpy.ops.object.select_pattern(pattern=['親指０.R', '親指１.R', '親指２.R', '人指０.R', '人指１.R', '人指２.R', '人指３.R', '中指０.R', '中指１.R', '中指２.R', '中指３.R', '薬指０.R', '薬指１.R', '薬指２.R', '薬指３.R', '小指０.R', '小指１.R', '小指２.R', '小指３.R'][i_AA1B7])
            for i_844DC in range(len(['親指０.L', '親指１.L', '親指２.L', '人指０.L', '人指１.L', '人指２.L', '人指３.L', '中指０.L', '中指１.L', '中指２.L', '中指３.L', '薬指０.L', '薬指１.L', '薬指２.L', '薬指３.L', '小指０.L', '小指１.L', '小指２.L', '小指３.L'])):
                bpy.ops.object.select_pattern(pattern=['親指０.L', '親指１.L', '親指２.L', '人指０.L', '人指１.L', '人指２.L', '人指３.L', '中指０.L', '中指１.L', '中指２.L', '中指３.L', '薬指０.L', '薬指１.L', '薬指２.L', '薬指３.L', '小指０.L', '小指１.L', '小指２.L', '小指３.L'][i_844DC])
        elif self.sna_new_property == "身体骨":
            for i_1B62D in range(len(['足.L', 'ひざ.L', '足首.L', '足先EX.L', '足.R', 'ひざ.R', '足首.R', '足先EX.R'])):
                bpy.ops.object.select_pattern(pattern=['足.L', 'ひざ.L', '足首.L', '足先EX.L', '足.R', 'ひざ.R', '足首.R', '足先EX.R'][i_1B62D])
            for i_EFC29 in range(len(['下半身', '上半身2', '上半身', '上半身3', '首', '頭', '肩.R', '肩.L', '腕.R', '腕.L', 'ひじ.R', 'ひじ.L', '手首.R', '手首.L'])):
                bpy.ops.object.select_pattern(pattern=['下半身', '上半身2', '上半身', '上半身3', '首', '頭', '肩.R', '肩.L', '腕.R', '腕.L', 'ひじ.R', 'ひじ.L', '手首.R', '手首.L'][i_EFC29])
        elif self.sna_new_property == "腿ik骨":
            for i_FA29C in range(len(['足.L', 'ひざ.L', '足首.L', '足先EX.L', '足.R', 'ひざ.R', '足首.R', '足先EX.R'])):
                bpy.ops.object.select_pattern(pattern=['足.L', 'ひざ.L', '足首.L', '足先EX.L', '足.R', 'ひざ.R', '足首.R', '足先EX.R'][i_FA29C])
        elif self.sna_new_property == "手骨":
            for i_256E3 in range(len(['親指０.R', '親指１.R', '親指２.R', '人指０.R', '人指１.R', '人指２.R', '人指３.R', '中指０.R', '中指１.R', '中指２.R', '中指３.R', '薬指０.R', '薬指１.R', '薬指２.R', '薬指３.R', '小指０.R', '小指１.R', '小指２.R', '小指３.R'])):
                bpy.ops.object.select_pattern(pattern=['親指０.R', '親指１.R', '親指２.R', '人指０.R', '人指１.R', '人指２.R', '人指３.R', '中指０.R', '中指１.R', '中指２.R', '中指３.R', '薬指０.R', '薬指１.R', '薬指２.R', '薬指３.R', '小指０.R', '小指１.R', '小指２.R', '小指３.R'][i_256E3])
            for i_6EC5E in range(len(['親指０.L', '親指１.L', '親指２.L', '人指０.L', '人指１.L', '人指２.L', '人指３.L', '中指０.L', '中指１.L', '中指２.L', '中指３.L', '薬指０.L', '薬指１.L', '薬指２.L', '薬指３.L', '小指０.L', '小指１.L', '小指２.L', '小指３.L'])):
                bpy.ops.object.select_pattern(pattern=['親指０.L', '親指１.L', '親指２.L', '人指０.L', '人指１.L', '人指２.L', '人指３.L', '中指０.L', '中指１.L', '中指２.L', '中指３.L', '薬指０.L', '薬指１.L', '薬指２.L', '薬指３.L', '小指０.L', '小指１.L', '小指２.L', '小指３.L'][i_6EC5E])
        elif self.sna_new_property == "调整骨":
            bpy.ops.object.select_pattern(pattern='*調整*', extend=True)
        elif self.sna_new_property == "d骨":
            for i_A62E2 in range(len(['足D.L', 'ひざD.L', '足首D.L', '足D.R', 'ひざD.R', '足首D.R'])):
                bpy.ops.object.select_pattern(pattern=['足D.L', 'ひざD.L', '足首D.L', '足D.R', 'ひざD.R', '足首D.R'][i_A62E2])
        elif self.sna_new_property == "捩骨":
            bpy.ops.object.select_pattern(pattern='*捩*', extend=True)
        else:
            pass
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_E6Bd2(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_e6bd2"
    bl_label = "添加顶点色属性"
    bl_description = "为选中的物体添加顶点色"
    bl_options = {"REGISTER", "UNDO"}
    sna_new_property: bpy.props.StringProperty(name='顶点色名称', description='', default='顶点色', subtype='NONE', maxlen=0)

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        node_tree_001['sna_old_active_objects'] = bpy.context.view_layer.objects.active.name
        for i_58412 in range(len(bpy.context.view_layer.objects.selected)):
            bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.selected[i_58412]
            bpy.ops.geometry.color_attribute_add(name=self.sna_new_property, domain='POINT', data_type='FLOAT_COLOR', color=(0.0, 0.0, 0.0, 1.0))
            bpy.context.view_layer.objects.active = bpy.context.view_layer.objects[node_tree_001['sna_old_active_objects']]
            self.report({'INFO'}, message='已添加顶点色')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_E9B48(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_e9b48"
    bl_label = "移除顶点色属性"
    bl_description = "移除选中物体指定名称的顶点色，如果为空则移除最后一个"
    bl_options = {"REGISTER", "UNDO"}
    sna_new_property: bpy.props.StringProperty(name='删除名称', description='', default='', subtype='NONE', maxlen=0)

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        node_tree_001['sna_old_active_objects'] = bpy.context.view_layer.objects.active.name
        for i_76711 in range(len(bpy.context.view_layer.objects.selected)):
            bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.selected[i_76711]
            if (len(bpy.context.view_layer.objects.active.data.color_attributes) != 0):
                for i_9755E in range(len(bpy.context.view_layer.objects.active.data.color_attributes)-1,-1,-1):
                    if (self.sna_new_property == bpy.context.view_layer.objects.active.data.color_attributes[i_9755E].name):
                        bpy.context.view_layer.objects.active.data.color_attributes.active_color = bpy.context.view_layer.objects.active.data.color_attributes[i_9755E]
                        bpy.ops.geometry.color_attribute_remove('INVOKE_DEFAULT', )
                        bpy.context.view_layer.objects.active = bpy.context.view_layer.objects[node_tree_001['sna_old_active_objects']]
                        self.report({'INFO'}, message='已移除指定名称顶点色')
                if (self.sna_new_property == ''):
                    bpy.context.view_layer.objects.active.data.color_attributes.active_color = bpy.context.view_layer.objects.active.data.color_attributes[int(len(bpy.context.view_layer.objects.active.data.color_attributes) - 1.0)]
                    bpy.ops.geometry.color_attribute_remove('INVOKE_DEFAULT', )
                    bpy.context.view_layer.objects.active = bpy.context.view_layer.objects[node_tree_001['sna_old_active_objects']]
                    self.report({'INFO'}, message='已移除最后一个顶点色')
            else:
                bpy.context.view_layer.objects.active = bpy.context.view_layer.objects[node_tree_001['sna_old_active_objects']]
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_0C8D6(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_0c8d6"
    bl_label = "快捷键切换中英文"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.sna_new_property_003 = (not bpy.context.scene.sna_new_property_003)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_4A59F(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_4a59f"
    bl_label = "清理数据"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
        self.report({'INFO'}, message='已清理未使用数据')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_Acbd7(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_acbd7"
    bl_label = "按位置选择顶点"
    bl_description = "编辑模式中选择顶点"
    bl_options = {"REGISTER", "UNDO"}

    def sna_new_property_enum_items(self, context):
        return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]
    sna_new_property: bpy.props.EnumProperty(name='轴向', description='', items=[('X', 'X', '', 0, 0), ('Y', 'Y', '', 0, 1), ('Z', 'Z', '', 0, 2)])

    def sna_new_property_001_enum_items(self, context):
        return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]
    sna_new_property_001: bpy.props.EnumProperty(name='条件', description='', items=[('大于', '大于', '', 0, 0), ('等于', '等于', '', 0, 1), ('小于', '小于', '', 0, 2)])
    sna_new_property_002: bpy.props.FloatProperty(name='分界', description='', default=0.0, subtype='NONE', unit='NONE', step=3, precision=2)

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        active_object = bpy.context.active_object
        if (active_object is not None and active_object.mode == 'EDIT'):
            if (bpy.context.active_object.type == 'MESH'):
                bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='OBJECT')
                for i_75CC7 in range(len(bpy.context.active_object.data.vertices)):
                    if (((bpy.context.active_object.data.vertices[i_75CC7].co[0] if (self.sna_new_property == 'X') else (bpy.context.active_object.data.vertices[i_75CC7].co[1] if ('Y' == self.sna_new_property) else (bpy.context.active_object.data.vertices[i_75CC7].co[2] if (self.sna_new_property == 'Z') else None))) > self.sna_new_property_002) if (self.sna_new_property_001 == '大于') else (((bpy.context.active_object.data.vertices[i_75CC7].co[0] if (self.sna_new_property == 'X') else (bpy.context.active_object.data.vertices[i_75CC7].co[1] if ('Y' == self.sna_new_property) else (bpy.context.active_object.data.vertices[i_75CC7].co[2] if (self.sna_new_property == 'Z') else None))) == self.sna_new_property_002) if ('等于' == self.sna_new_property_001) else (((bpy.context.active_object.data.vertices[i_75CC7].co[0] if (self.sna_new_property == 'X') else (bpy.context.active_object.data.vertices[i_75CC7].co[1] if ('Y' == self.sna_new_property) else (bpy.context.active_object.data.vertices[i_75CC7].co[2] if (self.sna_new_property == 'Z') else None))) < self.sna_new_property_002) if (self.sna_new_property_001 == '小于') else None))):
                        bpy.context.active_object.data.vertices[i_75CC7].select = True
                result_1E786 = bpy.context.active_object.update_from_editmode()
                bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='EDIT')
            else:
                self.report({'INFO'}, message='所选不是网格')
        else:
            self.report({'INFO'}, message='不在编辑模式')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_4Bd78(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_4bd78"
    bl_label = "按编号选择顶点"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}
    sna_new_property: bpy.props.IntProperty(name='编号', description='', default=0, subtype='NONE', min=0)

    def sna_new_property_001_enum_items(self, context):
        return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]
    sna_new_property_001: bpy.props.EnumProperty(name='条件', description='', items=[('等于', '等于', '', 0, 0), ('大于', '大于', '', 0, 1), ('小于', '小于', '', 0, 2)])

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        active_object = bpy.context.active_object
        if (active_object is not None and active_object.mode == 'EDIT'):
            if (bpy.context.active_object.type == 'MESH'):
                bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='OBJECT')
                for i_863A2 in range(len(bpy.context.active_object.data.vertices)):
                    if ((i_863A2 == self.sna_new_property) if (self.sna_new_property_001 == '等于') else ((i_863A2 > self.sna_new_property) if ('大于' == self.sna_new_property_001) else ((i_863A2 < self.sna_new_property) if ('小于' == self.sna_new_property_001) else None))):
                        bpy.context.active_object.data.vertices[i_863A2].select = True
                result_05FA6 = bpy.context.active_object.update_from_editmode()
                bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='EDIT')
            else:
                self.report({'INFO'}, message='所选不是网格')
        else:
            self.report({'INFO'}, message='不在编辑模式')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_C68A2(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_c68a2"
    bl_label = "原点到选中项"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected('INVOKE_DEFAULT', )
        bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='OBJECT')
        bpy.ops.object.origin_set('INVOKE_DEFAULT', type='ORIGIN_CURSOR')
        bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='EDIT')
        bpy.ops.view3d.snap_cursor_to_center('INVOKE_DEFAULT', )
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_32F6A(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_32f6a"
    bl_label = "对称两个顶点"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    def sna_new_property_enum_items(self, context):
        return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]
    sna_new_property: bpy.props.EnumProperty(name='轴向', description='', items=[('X', 'X', '', 0, 0), ('Y', 'Y', '', 0, 1), ('Z', 'Z', '', 0, 2)])

    def sna_new_property_001_enum_items(self, context):
        return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]
    sna_new_property_001: bpy.props.EnumProperty(name='方式', description='', items=[('第一个顶点', '第一个顶点', '', 0, 0), ('第二个顶点', '第二个顶点', '', 0, 1), ('平均', '平均', '', 0, 2)])

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        node_tree_004['sna_select_ver'] = []
        node_tree_004['sna_select_ver_pos'] = []
        active_object = bpy.context.active_object
        if (active_object is not None and active_object.mode == 'EDIT'):
            if (bpy.context.active_object.type == 'MESH'):
                bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='OBJECT')
                for i_581AD in range(len(bpy.context.active_object.data.vertices)):
                    if bpy.context.active_object.data.vertices[i_581AD].select:
                        node_tree_004['sna_select_ver'].append(i_581AD)
                    if (len(node_tree_004['sna_select_ver']) > 2):
                        self.report({'WARNING'}, message='没有选中两个顶点')
                        break
                if (len(node_tree_004['sna_select_ver']) == 2):
                    node_tree_004['sna_select_ver_pos'].append(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co)
                    node_tree_004['sna_select_ver_pos'].append(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][1]].co)
                    if property_exists("bpy.context.active_object.data.shape_keys.key_blocks[0]", globals(), locals()):
                        if self.sna_new_property_001 == "平均":
                            bpy.context.active_object.data.shape_keys.key_blocks[0].data[node_tree_004['sna_select_ver'][0]].co = (((eval("(sna_absin_C9F6D_46D54(node_tree_004['sna_select_ver_pos'][0][0]) + sna_absin_C9F6D_E198F(node_tree_004['sna_select_ver_pos'][1][0]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'X') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(sna_absin_C9F6D_CCBBB(node_tree_004['sna_select_ver_pos'][0][1]) + sna_absin_C9F6D_880B5(node_tree_004['sna_select_ver_pos'][1][1]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'Y') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(sna_absin_C9F6D_724FA(node_tree_004['sna_select_ver_pos'][0][2]) + sna_absin_C9F6D_188B6(node_tree_004['sna_select_ver_pos'][1][2]))/2")) if (self.sna_new_property == 'Z') else None))) if ((node_tree_004['sna_select_ver_pos'][0][0] > node_tree_004['sna_select_ver_pos'][1][0]) if (self.sna_new_property == 'X') else ((node_tree_004['sna_select_ver_pos'][0][1] > node_tree_004['sna_select_ver_pos'][1][1]) if (self.sna_new_property == 'Y') else ((node_tree_004['sna_select_ver_pos'][0][2] > node_tree_004['sna_select_ver_pos'][1][2]) if (self.sna_new_property == 'Z') else None))) else (tuple(mathutils.Vector(((eval("(sna_absin_C9F6D_46D54(node_tree_004['sna_select_ver_pos'][0][0]) + sna_absin_C9F6D_E198F(node_tree_004['sna_select_ver_pos'][1][0]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'X') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(sna_absin_C9F6D_CCBBB(node_tree_004['sna_select_ver_pos'][0][1]) + sna_absin_C9F6D_880B5(node_tree_004['sna_select_ver_pos'][1][1]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'Y') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(sna_absin_C9F6D_724FA(node_tree_004['sna_select_ver_pos'][0][2]) + sna_absin_C9F6D_188B6(node_tree_004['sna_select_ver_pos'][1][2]))/2")) if (self.sna_new_property == 'Z') else None)))) * mathutils.Vector((-1.0, 1.0, 1.0))) if (self.sna_new_property == 'X') else (tuple(mathutils.Vector(((eval("(sna_absin_C9F6D_46D54(node_tree_004['sna_select_ver_pos'][0][0]) + sna_absin_C9F6D_E198F(node_tree_004['sna_select_ver_pos'][1][0]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'X') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(sna_absin_C9F6D_CCBBB(node_tree_004['sna_select_ver_pos'][0][1]) + sna_absin_C9F6D_880B5(node_tree_004['sna_select_ver_pos'][1][1]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'Y') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(sna_absin_C9F6D_724FA(node_tree_004['sna_select_ver_pos'][0][2]) + sna_absin_C9F6D_188B6(node_tree_004['sna_select_ver_pos'][1][2]))/2")) if (self.sna_new_property == 'Z') else None)))) * mathutils.Vector((1.0, -1.0, 1.0))) if (self.sna_new_property == 'Y') else (tuple(mathutils.Vector(((eval("(sna_absin_C9F6D_46D54(node_tree_004['sna_select_ver_pos'][0][0]) + sna_absin_C9F6D_E198F(node_tree_004['sna_select_ver_pos'][1][0]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'X') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(sna_absin_C9F6D_CCBBB(node_tree_004['sna_select_ver_pos'][0][1]) + sna_absin_C9F6D_880B5(node_tree_004['sna_select_ver_pos'][1][1]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'Y') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(sna_absin_C9F6D_724FA(node_tree_004['sna_select_ver_pos'][0][2]) + sna_absin_C9F6D_188B6(node_tree_004['sna_select_ver_pos'][1][2]))/2")) if (self.sna_new_property == 'Z') else None)))) * mathutils.Vector((1.0, 1.0, -1.0))) if (self.sna_new_property == 'Z') else None))))
                            bpy.context.active_object.data.shape_keys.key_blocks[0].data[node_tree_004['sna_select_ver'][1]].co = (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co) * mathutils.Vector((-1.0, 1.0, 1.0))) if (self.sna_new_property == 'X') else (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co) * mathutils.Vector((1.0, -1.0, 1.0))) if (self.sna_new_property == 'Y') else (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co) * mathutils.Vector((1.0, 1.0, -1.0))) if (self.sna_new_property == 'Z') else None)))
                        elif self.sna_new_property_001 == "第一个顶点":
                            bpy.context.active_object.data.shape_keys.key_blocks[0].data[node_tree_004['sna_select_ver'][1]].co = (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co) * mathutils.Vector((-1.0, 1.0, 1.0))) if (self.sna_new_property == 'X') else (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co) * mathutils.Vector((1.0, -1.0, 1.0))) if (self.sna_new_property == 'Y') else (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co) * mathutils.Vector((1.0, 1.0, -1.0))) if (self.sna_new_property == 'Z') else None)))
                        elif self.sna_new_property_001 == "第二个顶点":
                            bpy.context.active_object.data.shape_keys.key_blocks[0].data[node_tree_004['sna_select_ver'][0]].co = (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][1]].co) * mathutils.Vector((-1.0, 1.0, 1.0))) if (self.sna_new_property == 'X') else (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][1]].co) * mathutils.Vector((1.0, -1.0, 1.0))) if (self.sna_new_property == 'Y') else (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][1]].co) * mathutils.Vector((1.0, 1.0, -1.0))) if (self.sna_new_property == 'Z') else None)))
                        else:
                            pass
                    else:
                        if self.sna_new_property_001 == "平均":
                            bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co = (((eval("(sna_absin_C9F6D_46D54(node_tree_004['sna_select_ver_pos'][0][0]) + sna_absin_C9F6D_E198F(node_tree_004['sna_select_ver_pos'][1][0]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'X') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(sna_absin_C9F6D_CCBBB(node_tree_004['sna_select_ver_pos'][0][1]) + sna_absin_C9F6D_880B5(node_tree_004['sna_select_ver_pos'][1][1]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'Y') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(sna_absin_C9F6D_724FA(node_tree_004['sna_select_ver_pos'][0][2]) + sna_absin_C9F6D_188B6(node_tree_004['sna_select_ver_pos'][1][2]))/2")) if (self.sna_new_property == 'Z') else None))) if ((node_tree_004['sna_select_ver_pos'][0][0] > node_tree_004['sna_select_ver_pos'][1][0]) if (self.sna_new_property == 'X') else ((node_tree_004['sna_select_ver_pos'][0][1] > node_tree_004['sna_select_ver_pos'][1][1]) if (self.sna_new_property == 'Y') else ((node_tree_004['sna_select_ver_pos'][0][2] > node_tree_004['sna_select_ver_pos'][1][2]) if (self.sna_new_property == 'Z') else None))) else (tuple(mathutils.Vector(((eval("(sna_absin_C9F6D_46D54(node_tree_004['sna_select_ver_pos'][0][0]) + sna_absin_C9F6D_E198F(node_tree_004['sna_select_ver_pos'][1][0]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'X') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(sna_absin_C9F6D_CCBBB(node_tree_004['sna_select_ver_pos'][0][1]) + sna_absin_C9F6D_880B5(node_tree_004['sna_select_ver_pos'][1][1]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'Y') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(sna_absin_C9F6D_724FA(node_tree_004['sna_select_ver_pos'][0][2]) + sna_absin_C9F6D_188B6(node_tree_004['sna_select_ver_pos'][1][2]))/2")) if (self.sna_new_property == 'Z') else None)))) * mathutils.Vector((-1.0, 1.0, 1.0))) if (self.sna_new_property == 'X') else (tuple(mathutils.Vector(((eval("(sna_absin_C9F6D_46D54(node_tree_004['sna_select_ver_pos'][0][0]) + sna_absin_C9F6D_E198F(node_tree_004['sna_select_ver_pos'][1][0]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'X') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(sna_absin_C9F6D_CCBBB(node_tree_004['sna_select_ver_pos'][0][1]) + sna_absin_C9F6D_880B5(node_tree_004['sna_select_ver_pos'][1][1]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'Y') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(sna_absin_C9F6D_724FA(node_tree_004['sna_select_ver_pos'][0][2]) + sna_absin_C9F6D_188B6(node_tree_004['sna_select_ver_pos'][1][2]))/2")) if (self.sna_new_property == 'Z') else None)))) * mathutils.Vector((1.0, -1.0, 1.0))) if (self.sna_new_property == 'Y') else (tuple(mathutils.Vector(((eval("(sna_absin_C9F6D_46D54(node_tree_004['sna_select_ver_pos'][0][0]) + sna_absin_C9F6D_E198F(node_tree_004['sna_select_ver_pos'][1][0]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'X') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(sna_absin_C9F6D_CCBBB(node_tree_004['sna_select_ver_pos'][0][1]) + sna_absin_C9F6D_880B5(node_tree_004['sna_select_ver_pos'][1][1]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'Y') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(sna_absin_C9F6D_724FA(node_tree_004['sna_select_ver_pos'][0][2]) + sna_absin_C9F6D_188B6(node_tree_004['sna_select_ver_pos'][1][2]))/2")) if (self.sna_new_property == 'Z') else None)))) * mathutils.Vector((1.0, 1.0, -1.0))) if (self.sna_new_property == 'Z') else None))))
                            bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][1]].co = (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co) * mathutils.Vector((-1.0, 1.0, 1.0))) if (self.sna_new_property == 'X') else (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co) * mathutils.Vector((1.0, -1.0, 1.0))) if (self.sna_new_property == 'Y') else (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co) * mathutils.Vector((1.0, 1.0, -1.0))) if (self.sna_new_property == 'Z') else None)))
                        elif self.sna_new_property_001 == "第一个顶点":
                            bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][1]].co = (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co) * mathutils.Vector((-1.0, 1.0, 1.0))) if (self.sna_new_property == 'X') else (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co) * mathutils.Vector((1.0, -1.0, 1.0))) if (self.sna_new_property == 'Y') else (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co) * mathutils.Vector((1.0, 1.0, -1.0))) if (self.sna_new_property == 'Z') else None)))
                        elif self.sna_new_property_001 == "第二个顶点":
                            bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co = (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][1]].co) * mathutils.Vector((-1.0, 1.0, 1.0))) if (self.sna_new_property == 'X') else (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][1]].co) * mathutils.Vector((1.0, -1.0, 1.0))) if (self.sna_new_property == 'Y') else (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][1]].co) * mathutils.Vector((1.0, 1.0, -1.0))) if (self.sna_new_property == 'Z') else None)))
                        else:
                            pass
                else:
                    self.report({'WARNING'}, message='没有选中两个顶点')
                bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='EDIT')
            else:
                self.report({'INFO'}, message='所选不是网格')
        else:
            self.report({'INFO'}, message='不在编辑模式')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_16Cb7(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_16cb7"
    bl_label = "对齐物体"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}
    sna_new_property: bpy.props.BoolProperty(name='位置', description='', default=False)
    sna_new_property_001: bpy.props.BoolProperty(name='旋转', description='', default=False)
    sna_new_property_002: bpy.props.BoolProperty(name='缩放', description='', default=False)

    def sna_new_property_003_enum_items(self, context):
        return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]
    sna_new_property_003: bpy.props.EnumProperty(name='轴向', description='', items=[('全部', '全部', '', 0, 0), ('X', 'X', '', 0, 1), ('Y', 'Y', '', 0, 2), ('Z', 'Z', '', 0, 3), ('YZ', 'YZ', '', 0, 4), ('XZ', 'XZ', '', 0, 5), ('XY', 'XY', '', 0, 6)])

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_D0D1D in range(len(bpy.context.selected_objects)):
            if (bpy.context.selected_objects[i_D0D1D].name != bpy.context.active_object.name):
                if self.sna_new_property:
                    bpy.context.selected_objects[i_D0D1D].location = ((bpy.context.active_object.location[0], bpy.context.active_object.location[1], bpy.context.active_object.location[2]) if (self.sna_new_property_003 == '全部') else ((bpy.context.active_object.location[0], 0.0, 0.0) if (self.sna_new_property_003 == 'X') else ((0.0, bpy.context.active_object.location[1], 0.0) if (self.sna_new_property_003 == 'Y') else ((0.0, 0.0, bpy.context.active_object.location[2]) if (self.sna_new_property_003 == 'Z') else ((0.0, bpy.context.active_object.location[1], bpy.context.active_object.location[2]) if (self.sna_new_property_003 == 'YZ') else ((bpy.context.active_object.location[0], 0.0, bpy.context.active_object.location[2]) if (self.sna_new_property_003 == 'XZ') else ((bpy.context.active_object.location[0], bpy.context.active_object.location[1], 0.0) if (self.sna_new_property_003 == 'XY') else None)))))))
                if self.sna_new_property_001:
                    bpy.context.selected_objects[i_D0D1D].rotation_euler = ((bpy.context.active_object.rotation_euler[0], bpy.context.active_object.rotation_euler[1], bpy.context.active_object.rotation_euler[2]) if (self.sna_new_property_003 == '全部') else ((bpy.context.active_object.rotation_euler[0], 0.0, 0.0) if (self.sna_new_property_003 == 'X') else ((0.0, bpy.context.active_object.rotation_euler[1], 0.0) if (self.sna_new_property_003 == 'Y') else ((0.0, 0.0, bpy.context.active_object.rotation_euler[2]) if (self.sna_new_property_003 == 'Z') else ((0.0, bpy.context.active_object.rotation_euler[1], bpy.context.active_object.rotation_euler[2]) if (self.sna_new_property_003 == 'YZ') else ((bpy.context.active_object.rotation_euler[0], 0.0, bpy.context.active_object.rotation_euler[2]) if (self.sna_new_property_003 == 'XZ') else ((bpy.context.active_object.rotation_euler[0], bpy.context.active_object.rotation_euler[1], 0.0) if (self.sna_new_property_003 == 'XY') else None)))))))
                if self.sna_new_property_002:
                    bpy.context.selected_objects[i_D0D1D].scale = ((bpy.context.active_object.scale[0], bpy.context.active_object.scale[1], bpy.context.active_object.scale[2]) if (self.sna_new_property_003 == '全部') else ((bpy.context.active_object.scale[0], 0.0, 0.0) if (self.sna_new_property_003 == 'X') else ((0.0, bpy.context.active_object.scale[1], 0.0) if (self.sna_new_property_003 == 'Y') else ((0.0, 0.0, bpy.context.active_object.scale[2]) if (self.sna_new_property_003 == 'Z') else ((0.0, bpy.context.active_object.scale[1], bpy.context.active_object.scale[2]) if (self.sna_new_property_003 == 'YZ') else ((bpy.context.active_object.scale[0], 0.0, bpy.context.active_object.scale[2]) if (self.sna_new_property_003 == 'XZ') else ((bpy.context.active_object.scale[0], bpy.context.active_object.scale[1], 0.0) if (self.sna_new_property_003 == 'XY') else None)))))))
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_OT_My_Generic_Operator_A5A90(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_a5a90"
    bl_label = "批量传递形态键"
    bl_description = "将形态键复制到激活物体(按编号传递位置)"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        node_tree_005['sna_act_obj'] = None
        node_tree_005['sna_base_obj'] = None
        if bpy.context.active_object is None:
            self.report({'INFO'}, message='活动物体为空')
            return {"FINISHED"}
        for i_192DE in range(len(bpy.context.selected_objects)):
            if (bpy.context.selected_objects[i_192DE].name == bpy.context.active_object.name):
                node_tree_005['sna_act_obj'] = bpy.context.selected_objects[i_192DE]
            else:
                node_tree_005['sna_base_obj'] = bpy.context.selected_objects[i_192DE]
        if (node_tree_005['sna_act_obj'] != None):
            if (node_tree_005['sna_base_obj'] != None):
                active_data = getattr(node_tree_005['sna_act_obj'], 'data', None)
                base_data = getattr(node_tree_005['sna_base_obj'], 'data', None)
                if not hasattr(active_data, 'shape_keys') or not hasattr(base_data, 'shape_keys'):
                    self.report({'INFO'}, message='只支持带形态键数据的物体')
                    return {"FINISHED"}
                if (base_data.shape_keys == None):
                    self.report({'INFO'}, message='形态键来源物体没有形态键')
                    return {"FINISHED"}
                if (active_data.shape_keys == None):
                    bpy.ops.object.shape_key_add('INVOKE_DEFAULT', )
                for i_35552 in range(len(base_data.shape_keys.key_blocks)):
                    node_tree_005['sna_base_obj'].active_shape_key_index = i_35552
                    if (i_35552 != 0):
                        print(node_tree_005['sna_base_obj'].active_shape_key.name)
                        bpy.ops.object.shape_key_transfer('INVOKE_DEFAULT', )
                        node_tree_005['sna_act_obj'].show_only_shape_key = False
            else:
                self.report({'INFO'}, message='形态键来源物体为空')
        else:
            self.report({'INFO'}, message='活动物体为空')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)
