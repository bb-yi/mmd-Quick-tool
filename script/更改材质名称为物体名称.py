import bpy


# 获取当前选择的物体
selected_objects = bpy.context.selected_objects

for obj in selected_objects:
    # 获取物体的第一个材质
    material = obj.active_material
    
    if material:
        # 将材质的名称设置为物体的名称
        material.name = obj.name
    else:
        print(f"Object {obj.name} has no material.")