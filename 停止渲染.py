import bpy
import pyautogui

# 启动渲染
#bpy.ops.render.render('INVOKE_DEFAULT', animation=True)

# 模拟按 ESC 键以停止渲染
pyautogui.press('esc')
