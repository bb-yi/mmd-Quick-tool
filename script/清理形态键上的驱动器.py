import bpy

# 获取当前选中的所有物体
selected_objects = bpy.context.selected_objects

# 遍历选中的物体
for obj in selected_objects:
    # 检查对象是否有形态键
    if obj.data.shape_keys:
        # 遍历所有形态键
        for key_block in obj.data.shape_keys.key_blocks:
            # 获取形态键的驱动器数据路径
            data_path = 'key_blocks["{}"].value'.format(key_block.name)

            # 尝试获取驱动器
            driver = obj.data.shape_keys.animation_data.drivers.find(data_path)

            # 如果驱动器存在，移除它
            if driver:
                obj.data.shape_keys.animation_data.drivers.remove(driver)

print("完成对选中物体形态键驱动器的移除")

# 更新视图，以便立即看到更改的效果
bpy.context.view_layer.update()