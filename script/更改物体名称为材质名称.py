import bpy

# 获取当前场景
scene = bpy.context.scene

# 获取所选物体列表
selected_objects = bpy.context.selected_objects

# 循环遍历所选物体
for obj in selected_objects:
    # 获取物体的第一个材质
    material = obj.data.materials[0] if obj.data.materials else None
    
    # 如果物体有材质，则将物体名称更改为材质名称
    if material:
        obj.name = material.name
        print(f"Object {obj.name} renamed to {material.name}")
    else:
        print(f"Object {obj.name} has no materials")

# 更新场景
bpy.context.view_layer.update()
