import bpy

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

