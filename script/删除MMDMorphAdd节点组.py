import bpy

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
