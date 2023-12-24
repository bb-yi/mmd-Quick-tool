import bpy

def rename_materials_to_base_color_texture():
    # 获取当前选择的物体
    selected_objects = bpy.context.selected_objects
    
    for obj in selected_objects:
        # 获取物体的第一个材质
        material = obj.active_material
        base_color_texture_node = None
        
        # 定义可能的基础色输入端口名称列表
        possible_base_color_input_names = ["Color", "Base Color", "Diffuse Color", "Albedo","Base Tex"]
        
        if material:
            # 遍历节点图中的所有节点
            for node in material.node_tree.nodes:
                # 检查节点是否是 'TEX_IMAGE' 类型
                if node.type == 'TEX_IMAGE':
                    # 遍历可能的基础色输入端口名称
                    for base_color_input_name in possible_base_color_input_names:
                        # 检查节点的 "Color" 输出端口是否连接到其他节点的基础色输入端口
                        if any(link.to_socket.name == base_color_input_name for link in node.outputs['Color'].links):
                            base_color_texture_node = node
                            break
                    if base_color_texture_node:
                        break  # 如果找到匹配的节点，退出外层循环
            
            if base_color_texture_node:
                # 获取贴图的名称并设置为材质的名称
                texture_name = base_color_texture_node.image.name
                material.name = texture_name
        else:
            print(f"Object {obj.name} has no material.")

if __name__ == "__main__":
    rename_materials_to_base_color_texture()
