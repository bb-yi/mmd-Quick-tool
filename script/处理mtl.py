#import re

def extract_materials_from_mtl(mtl_file_path):
    materials = {}
    with open(mtl_file_path, 'r', encoding='gbk') as f:
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
    
    # Extract keys and values into separate lists
    keys = list(materials.keys())
    values = list(materials.values())
    
    return keys, values

# 指定MTL文件路径
#mtl_file_path = 'F:\\mmd_project\\純情スカート 甘雨\\wj\\alembic_file.mtl'
mtl_file_path=a
# 提取材质和贴图文件名称
obj_name, tex_name = extract_materials_from_mtl(mtl_file_path)
