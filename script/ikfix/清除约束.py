import bpy

# 获取当前的活动物体
active_object = bpy.context.active_object

# 检查当前激活的对象是否是骨架类型
if active_object and active_object.type == 'ARMATURE':
    # 获取选中的骨骼
    selected_bones = [bone for bone in active_object.data.bones if bone.select]
    
    # 遍历选中的骨骼
    for bone in selected_bones:
        # 切换到姿态模式
        bpy.ops.object.mode_set(mode='POSE')
        
        # 选中当前骨骼
        active_object.data.bones.active = active_object.data.bones[bone.name]
        bpy.ops.pose.select_all(action='SELECT')
        
        # 获取骨骼的所有约束
        bone_constraints = active_object.pose.bones[bone.name].constraints
        # 要删除的约束名称列表
        constraints_to_delete = ["Copy Location_P", "Damped Track_X", "Damped Track_Z"]
        
        # 遍历并删除指定名称的约束
        for constraint_name in constraints_to_delete:
            for constraint in bone_constraints:
                if constraint.name == constraint_name or constraint.name.startswith(constraint_name + "."):
                    bone_constraints.remove(constraint)
        # 切换回对象模式
        bpy.ops.object.mode_set(mode='OBJECT')
        
        print(f"已删除骨骼 '{bone.name}' 上的指定约束")

else:
    print("当前没有选中的骨架对象或者选中的不是骨骼对象")
