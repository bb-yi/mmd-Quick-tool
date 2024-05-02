import bpy
import re

# 脚本 by 三分仪

# 将alembic_file.mtl所在路径复制进去，贴图和alembic_file.mtl在同一文件夹下
#file_path = r'E:\mmd_project\深空之眼视频\赫拉荆棘花之梦CHUNGHA\wj\alembic_file.mtl'

materials = {}
with open(file_path, 'r', encoding='gbk') as f:
    current_material = None

    for line in f:
        if line.startswith("newmtl"):
            current_material = line.split()[1]
            materials[current_material] = {}
        elif line.startswith("map_Kd"):
            texture = line.split()[1:]
            texture_name = " ".join(texture)
            if current_material is not None:
                materials[current_material]["map_Kd"] = texture_name

new_materials_dict = {}
for i, (key, value) in enumerate(materials.items()):
    new_key = f'xform_0_material_{i}'
    new_materials_dict[new_key] = value

# Check if 'map_Kd' exists before trying to access it
materials = {k: v.get('map_Kd', '') for k, v in new_materials_dict.items()}

# Output the new dictionary
print(materials)

for key, value in materials.items():
    obj = bpy.data.objects[key]

    mat = bpy.data.materials.new(name=value)

    # 设置该材质使用节点
    mat.use_nodes = True

    # 创建一个新的Image纹理节点
    tex = mat.node_tree.nodes.new('ShaderNodeTexImage')
    tex.location = (-300, 300)

    new_name = value
    new_path = file_path.replace(file_path.split('\\')[-1], new_name)

    print(new_path)
    # 设置纹理图片路径
    tex.image = bpy.data.images.load(new_path)

    # 获取Diffuse BSDF节点
    bsdf = mat.node_tree.nodes.get('Principled BSDF')

    # 将Image纹理节点连接到Diffuse BSDF节点的Base Color输入
    mat.node_tree.links.new(tex.outputs['Color'], bsdf.inputs['Base Color'])
    mat.node_tree.links.new(tex.outputs['Alpha'], bsdf.inputs['Alpha'])

    # 赋予材质
    obj.data.materials.append(mat)
    # 遍历所有物体
    for obj in bpy.data.objects:
        # 判断物体名称中是否含有 xform_0_material
        if "xform_0_material" in obj.name:
            # 遍历该物体的材质
            for mat_slot in obj.material_slots:
                # 获取材质
                mat = mat_slot.material
                # 判断材质名称中是否含有序号
                if re.search(r"\.\d+", mat.name):
                    # 替换材质名称为没有序号的名称
                    new_name = re.sub(r"\.\d+", "", mat.name)
                    mat_slot.material = bpy.data.materials[new_name]
    # 清理未使用的数据块
    bpy.ops.outliner.orphans_purge()
