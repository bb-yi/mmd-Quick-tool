import bpy

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
