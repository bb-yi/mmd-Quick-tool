import bpy

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
