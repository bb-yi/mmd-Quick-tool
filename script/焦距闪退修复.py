import bpy
'''
camera_name="Camera"
Advance_frame=30
MMD_Camera='MMD_Camera'
'''
#选中物体
def selected_object(Selected_object_name):
# 检查物体是否存在
    if Selected_object_name in bpy.data.objects:
        obj = bpy.data.objects[Selected_object_name]
        
        # 将指定物体设置为活动物体
        bpy.context.view_layer.objects.active = obj
        
        # 清除选择
        bpy.ops.object.select_all(action='DESELECT')
        
        # 选择指定物体
        obj.select_set(True)
    else:
        print(f"找不到名为 '{Selected_object_name}' 的物体。")


#选中通道
def select_channel(channel_name):
    # 获取当前激活的动作
    current_action = bpy.context.object.animation_data.action

    if current_action:
        # 遍历当前动作的 F-Curves（通道）
        for fcurve in current_action.fcurves:
            if fcurve.data_path.endswith(channel_name):
                fcurve.select = True
            else:
                fcurve.select = False

def set_workspace_to_3d_view():
    # 获取当前激活的工作区域
    current_area = bpy.context.area

    if current_area:
        # 设置当前工作区域为3D视图
        current_area.type = 'VIEW_3D'
        print("Switched to 3D View.")
    else:
        print("No active workspace.")

bpy.context.preferences.view.language = 'en_US'#设置语言为英文

bpy.ops.object.select_all(action='DESELECT')#取消所有选择

selected_object(MMD_Camera)

bpy.context.area.type = 'DOPESHEET_EDITOR'#切换工作区域为动画摄影表

bpy.context.area.spaces.active.dopesheet.show_only_selected = False#取消显示所有关键帧

#选择名为angle的关键帧
bpy.context.area.spaces.active.dopesheet.filter_text = "angle"#搜索通道名
bpy.ops.action.select_all(action='SELECT')#全选关键帧
bpy.ops.action.copy()
select_channel("angle")#选中通道
bpy.context.scene.frame_set(Advance_frame)#回到第0帧
bpy.ops.anim.channels_setting_toggle(type='MUTE')#禁用通道


bpy.context.area.spaces.active.dopesheet.filter_text = "perspective"
select_channel("perspective")
bpy.ops.anim.channels_setting_toggle(type='MUTE')


#新建空物体
empty = bpy.data.objects.new("焦距", None)
bpy.context.scene.collection.objects.link(empty)

selected_object("焦距")

# 设置要操作的物体名称
object_name = empty.name

# 检查物体是否存在
if object_name in bpy.data.objects:
    obj = bpy.data.objects[object_name]

    # 在时间轴中的特定帧设置物体的位置
    frame = 0  # 替换为您要创建关键帧的帧数
    print(f"在帧 {frame} 上为物体 '{object_name}' 创建了关键帧。")
    # 在时间轴中的特定帧设置物体的位置
    # 替换为您要创建关键帧的帧数
    obj.location.x = 0.2  # 替换为您要设置的位置值
    #obj.location.y = 0.0
    #obj.location.z = 0.0

    # 在指定帧上为位置属性创建关键帧
    obj.keyframe_insert(data_path="location", frame=frame,index=0)


    bpy.context.area.spaces.active.dopesheet.filter_text = "X Location"
    bpy.ops.action.select_all(action='SELECT')

    #粘贴关键帧
    bpy.ops.action.paste(flipped=True)
    bpy.context.area.spaces.active.dopesheet.filter_text = ""
    print(f"在帧 {frame} 上为物体 '{object_name}' 创建了关键帧。")

    bpy.context.preferences.view.language = 'zh_CN'#回到中文
    bpy.context.area.type = 'TEXT_EDITOR'
    #bpy.context.area.type = 'TEXT_EDITOR'
    set_workspace_to_3d_view()


    empty_obj = bpy.data.objects[object_name]
    # 创建一个新的驱动器
    driver = empty_obj.driver_add('location', 2)  # 在这里，将驱动器添加到目标物体的 Y 缩放属性（索引为 1）
    # 设置驱动器的类型为 "Scripted Expression"，以自定义表达式
    driver.driver.type = 'SCRIPTED'

    # 创建一个自定义变量，用于控制驱动器
    var = driver.driver.variables.new()
    var.name = "var"  # 变量名称
    var.type = 'SINGLE_PROP'
    var.targets[0].id = empty_obj
    var.targets[0].data_path = "location.x"  # 引用源物体的 X 位置属性

    # 设置驱动器的表达式，以引用自定义变量 var
    driver.driver.expression = "12/tan(var/2)"  # 使目标物体的 Y 缩放属性等于源物体的 X 位置属性的两倍

    target_object = empty_obj

    selected_object(camera_name)
    # 通过名称获取相机对象
    camera = bpy.data.objects.get(camera_name) 
    if camera and target_object:
        # 创建一个新的驱动器对象
        driver = camera.data.driver_add("lens")  # "lens" 是焦距属性的名称

        # 设置驱动器的类型为 "Scripted Expression"
        driver.driver.type = "SCRIPTED"

        # 创建一个自定义变量，并将其设置为控制驱动器的输入
        var = driver.driver.variables.new()
        var.name = "var"  # 自定义变量的名称
        var.type = "SINGLE_PROP"
        var.targets[0].id = target_object
        var.targets[0].data_path = "location.z"  # 引用目标物体的 X 位置属性作为输入

        # 设置驱动器的表达式，以引用自定义变量并计算焦距
        driver.driver.expression = "var"  # 例如，这里是一个示例表达式
    else:
        print("找不到相机或目标物体。")

else:
    print(f"找不到名为 '{object_name}' 的物体。")


set_workspace_to_3d_view()

