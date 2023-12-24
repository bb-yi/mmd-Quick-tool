import bpy

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
