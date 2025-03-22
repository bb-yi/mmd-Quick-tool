import bpy
import bmesh
fk_bone_name = ["足.L", "ひざ.L", "足首.L", "足先EX.L", "足.R", "ひざ.R", "足首.R", "足先EX.R"]

# 获取当前的活动物体
bone_object = bpy.context.active_object
# 创建一个立方体
bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0))
# 获取活动对象
cube_obj = bpy.context.active_object

cube_size=0.05#生成物体大小

def select_vertex(obj,v_i):#选中指定索引顶点
    # 清除现有选择
    bpy.ops.mesh.select_all(action='DESELECT')
    bm = bmesh.from_edit_mesh(obj.data)
    # 确保索引表已更新
    bm.verts.ensure_lookup_table()
    # 选择特定顶点（例如，第一个顶点）
    vertex_index_to_select = v_i

    bm.verts[vertex_index_to_select].select = True

    # 更新选择状态
    bmesh.update_edit_mesh(obj.data)



def select_vertex_groups(obj,name):#为选中顶点创建顶点组
    # 创建一个新的顶点组
    bpy.ops.object.vertex_group_add()
    
    # 获取当前选定的顶点组
    vertex_group = obj.vertex_groups.active
    
    # 将选定的顶点分配到顶点组中
    bpy.ops.object.vertex_group_assign()
    # 切换回对象模式
    bpy.ops.object.mode_set(mode='OBJECT')    
    # 重命名顶点组
    vertex_group.name = name # 将顶点组重命名为您想要的名称
    # 进入编辑模式
    bpy.ops.object.mode_set(mode='EDIT')




# 检查对象类型是否为网格
if cube_obj and cube_obj.type == 'MESH':
    # 进入编辑模式
    bpy.ops.object.mode_set(mode='EDIT')
    
    # 选择所有顶点
    bpy.ops.mesh.select_all(action='SELECT')
    
    # 移动所有顶点
    bpy.ops.transform.translate(value=(cube_size, cube_size, cube_size))

    select_vertex(cube_obj,7)

    bpy.ops.mesh.delete(type='VERT')

    # 选择所有顶点
    bpy.ops.mesh.select_all(action='SELECT')
    
    # 缩放所有顶点，以世界原点为中心
    bpy.ops.transform.resize(value=(cube_size, cube_size, cube_size), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)))


    #指定顶点组
    select_vertex(cube_obj,0)
    select_vertex_groups(cube_obj,"p")

    select_vertex(cube_obj,4)
    select_vertex_groups(cube_obj,"x")

    select_vertex(cube_obj,2)
    select_vertex_groups(cube_obj,"y")

    select_vertex(cube_obj,1)
    select_vertex_groups(cube_obj,"z")



    # 切换回对象模式
    bpy.ops.object.mode_set(mode='OBJECT')   

else:
    print("创建骨架网格失败")

bone_names=[]

# 检查当前激活的对象是否是骨架类型
if bone_object and bone_object.type == 'ARMATURE':
    

    # 获取选中的骨骼
    selected_bones = [bone for bone in bone_object.data.bones if bone.select]
    
    # 遍历选中的骨骼
    for bone in selected_bones:

        bone_names.append(bone.name)

        #复制物体引用
        copy_cube_object = cube_obj.copy()

        # 复制物体数据
        copy_cube_object.data = cube_obj.data.copy()

        # 将复制物体添加到场景中
        bpy.context.collection.objects.link(copy_cube_object)
    
        # 将立方体的名称设置为骨骼的名称
        copy_cube_object.name = bone.name
        
        # 获取骨骼的变换矩阵并将其应用于立方体的变换
        copy_cube_object.matrix_world = bone_object.matrix_world @ bone.matrix_local

        # 添加骨架修改器到物体
        modifier = copy_cube_object.modifiers.new(name="Armature Modifier", type='ARMATURE')


        # 遍历物体的顶点组
        for vertex_group in copy_cube_object.vertex_groups:
        # 获取原始的顶点组名称
            original_name = vertex_group.name
        
        # 修改顶点组名称为物体名称加上原始的顶点组名称
            new_name = bone.name + "_" + original_name
            vertex_group.name = new_name


        # 设置骨架对象
        modifier.object = bone_object
        #新建顶点组名称为骨骼名称
        vertex_group = copy_cube_object.vertex_groups.new(name=bone.name)

        # 设置权重值
        weight_value = 1.0  # 设置为所需的权重值
        for vertex in copy_cube_object.data.vertices:
            vertex_group.add([vertex.index], weight_value, 'REPLACE')


        child_object = copy_cube_object
        parent_object = bone_object

        if child_object is not None and parent_object is not None:
            # 将子物体添加到父物体的子集中
            parent_object.select_set(True)  # 选中父物体
            bpy.context.view_layer.objects.active = parent_object
            bpy.ops.object.parent_set(type='OBJECT')  # 使用 'OBJECT' 类型的父子关系
            child_object.select_set(False)  # 取消选择子物体
            bpy.context.view_layer.update()

    print("骨骼名称列表:", bone_names)



    all_objects = bpy.context.scene.objects

    bpy.ops.object.select_all(action='DESELECT')  # 取消选择所有物体
    bpy.context.view_layer.objects.active = None  # 取消活动物体

    for bone_name in bone_names:
        for obj in all_objects:
            if obj.name==bone_name:
                obj.select_set(True)
                bpy.context.view_layer.objects.active = obj
                
    bpy.ops.object.join()#合并物体


    # 获取当前选中的物体列表
    selected_objects = bpy.context.selected_objects
    # 检查是否有物体被选中
    if selected_objects:
        # 获取第一个选中的物体
        selected_object = selected_objects[0]
        
        # 设置新的名称
        new_name = "骨骼坐标系"
        # 更改物体的名称
        selected_object.name = new_name

    else:
        print("没有选中的物体")
    bpy.data.objects.remove(cube_obj, do_unlink=True)


else:
    print("当前没有选中的骨架对象或者选中的不是骨骼对象")


