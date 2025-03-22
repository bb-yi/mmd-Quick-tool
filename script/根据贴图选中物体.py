import bpy
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
