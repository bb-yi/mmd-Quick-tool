import bpy

# 获取当前的活动物体
abc_object = bpy.context.active_object

# 获取当前激活的对象（骨架和物体）
selected_objects = bpy.context.selected_objects

# 遍历所有选中的物体
for obj in selected_objects:
    # 检查物体是否不是当前的活动物体
    if obj != abc_object:
        bone_axes_object = obj




print(selected_objects)
print("abc物体"+abc_object.name)
print("骨骼物体"+bone_axes_object.name)
# 检查是否有活动物体

if abc_object is not None:
    # 添加数据传递修改器
    modifier = abc_object.modifiers.new(name="Data Transfer", type='DATA_TRANSFER')

    # 设置传递的目标对象
    if bone_axes_object is not None:
        modifier.object = bone_axes_object
    else:
        print("找不到源对象")

    # 设置传递数据类型为顶点数据和顶点组数据
    modifier.use_vert_data = True
    modifier.data_types_verts = {'VGROUP_WEIGHTS'}  # 设置为您需要的数据类型


    #bpy.context.view_layer.objects.active = abc_object
    bpy.ops.object.datalayout_transfer(modifier="Data Transfer")

    # 应用修改器
    bpy.ops.object.modifier_apply(modifier=modifier.name)

    abc_object.select_set(True)  # 选中abc
    # 更新视图以反映选择的更改
    bpy.context.view_layer.objects.active = abc_object
    bpy.context.view_layer.update()
else:
    print("没有找到活动物体")