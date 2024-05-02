import bpy
import random

def set_random_light_colors():
    # 获取当前选择的灯光对象
    selected_lights = [obj for obj in bpy.context.selected_objects if obj.type == 'LIGHT']

    for light in selected_lights:
        # 检查灯光是否有 color 属性
        if hasattr(light.data, 'color'):
            # 生成随机颜色
            random_color = [random.uniform(0, 1) for _ in range(3)]

            # 设置灯光的颜色
            light.data.color = random_color

if __name__ == "__main__":
    set_random_light_colors()
