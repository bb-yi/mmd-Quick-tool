import bpy

# 获取当前选中的对象
selected_objects = bpy.context.selected_objects

for obj in selected_objects:
    # 检查对象是否有材质
    if obj.material_slots:
        for slot in obj.material_slots:
            # 检查材质是否有节点
            if slot.material.use_nodes:
                # 遍历节点
                for node in slot.material.node_tree.nodes:
                    # 检查节点是否为 MMDMorphAdd 节点组
                    if node.type == 'GROUP' and node.node_tree.name == 'MMDMorphAdd':
                        # 获取连接到 Base1 RGB 输入的贴图节点
                        base1_rgb_texture = None
                        for link in node.inputs['Base1 RGB'].links:
                            if link.from_node.type == 'TEX_IMAGE':
                                base1_rgb_texture = link.from_node

                        # 如果找到连接的贴图节点
                        if base1_rgb_texture:
                            # 找到目标节点组 MMDShaderDev
                            target_node_group = None
                            for target_node in slot.material.node_tree.nodes:
                                if target_node.type == 'GROUP' and target_node.node_tree.name == 'MMDShaderDev':
                                    target_node_group = target_node

                            # 如果找到目标节点组
                            if target_node_group:
                                # 连接贴图到目标节点组的 Base Tex 输入
                                link = slot.material.node_tree.links.new
                                link(target_node_group.inputs['Base Tex'], base1_rgb_texture.outputs['Color'])

                                # 删除 MMDMorphAdd 节点组
                                slot.material.node_tree.nodes.remove(node)

# 更新场景
bpy.context.view_layer.update()
