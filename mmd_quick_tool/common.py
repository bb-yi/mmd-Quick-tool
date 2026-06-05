# This module was split from the Serpens-generated mmd Quick tool source.

import bpy
import bpy.utils.previews
import os
from bpy_extras.io_utils import ImportHelper, ExportHelper
import mathutils
import math
from bpy.app.handlers import persistent
from datetime import datetime
addon_keymaps = {}
ikfix = {'sna_bone_obj': None, 'sna_base_obj': None, 'sna_bone': [], 'sna_constraint_obj': None, 'sna_abc': None, 'sna_bone_list': [], }
node_tree = {'sna_act_obj': None, 'sna_sna_new_variable': [], 'sna_sna_new_variable_001': 0, }
abc = {'sna_sna_new_variable': False, }
node_tree_001 = {'sna_old_light_shading': 'MATCAP', 'sna_old_color_type_shading': 'OBJECT', 'sna_old_show_wireframes': False, 'sna_old_show_bones': True, 'sna_old_active_objects': '', }
node_tree_004 = {'sna_is_other_color_space': False, 'sna_select_ver': [], 'sna_select_ver_pos': [], }
node_tree_005 = {'sna_act_obj': None, 'sna_base_obj': None, }
node_tree_005 = {'sna_sna_new_variable': None, 'sna_camera': None, 'sna_sna_new_variable_001': None, 'sna_sna_new_variable_002': None, 'sna_sna_new_variable_002': None, 'sna_sna_new_variable_003': None, }
node_tree_004 = {'sna_last_node': None, 'sna_bake_tex_size_x': 0, 'sna_bake_tex_size_y': 0, }
node_tree_008 = {'sna_select_obj': [], 'sna_num': 0, 'sna_bone_obj': None, 'sna_bone_weight_from': None, 'sna_bone_weight_to': [], }
node_tree_002 = {'sna_sna_new_variable': '', }
node_tree_005 = {'sna_light_obj': [], }
node_tree_002 = {'sna_old_render_size': [], }


class _IconPreviewStore:
    def __init__(self):
        self.collection = None

    def new(self):
        if self.collection is None:
            self.collection = bpy.utils.previews.new()
        return self.collection

    def remove(self):
        if self.collection is not None:
            bpy.utils.previews.remove(self.collection)
            self.collection = None

    def load(self, *args, **kwargs):
        if self.collection is None:
            self.new()
        return self.collection.load(*args, **kwargs)

    def __contains__(self, key):
        return self.collection is not None and key in self.collection

    def __getitem__(self, key):
        if self.collection is None:
            raise KeyError(key)
        return self.collection[key]


_icons = _IconPreviewStore()


def create_icons():
    _icons.new()


def remove_icons():
    _icons.remove()


def addon_module_names():
    names = []
    package_name = __package__
    if package_name:
        names.append(package_name)
    names.append('mmd_quick_tool')
    names.append('bl_ext.user_default.mmd_quick_tool')
    return tuple(dict.fromkeys(names))


def get_addon_preferences():
    addons = bpy.context.preferences.addons
    for module_name in addon_module_names():
        addon = addons.get(module_name)
        if addon is not None and addon.preferences is not None:
            return addon.preferences
    return None



def string_to_int(value):
    if value.isdigit():
        return int(value)
    return 0


def string_to_icon(value):
    if value in bpy.types.UILayout.bl_rna.functions["prop"].parameters["icon"].enum_items.keys():
        return bpy.types.UILayout.bl_rna.functions["prop"].parameters["icon"].enum_items[value].value
    return string_to_int(value)


def sna_update_sna_ik_fix_on_057DD(self, context):
    sna_updated_prop = self.sna_ik_fix_on
    if ((len(bpy.context.view_layer.objects.selected) == 1) and (bpy.context.view_layer.objects.active.type == 'ARMATURE')):
        for i_40A47 in range(len(bpy.context.view_layer.objects.active.data.bones)):
            for i_8327B in range(len(bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_40A47].name].constraints)-1,-1,-1):
                if ('Copy Location_P' in bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_40A47].name].constraints[i_8327B].name or 'Damped Track_X' in bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_40A47].name].constraints[i_8327B].name or 'Damped Track_Z' in bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_40A47].name].constraints[i_8327B].name):
                    if bpy.context.scene.sna_ik_fix_on:
                        if bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_40A47].name].constraints[i_8327B].enabled:
                            pass
                        else:
                            bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_40A47].name].constraints[i_8327B].enabled = True
                    else:
                        if bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_40A47].name].constraints[i_8327B].enabled:
                            bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_40A47].name].constraints[i_8327B].enabled = False
    else:
        self.report({'WARNING'}, message='没有选中骨骼')


def sna_update_sna_bili_31149(self, context):
    sna_updated_prop = self.sna_bili
    print(sna_updated_prop)
    if sna_updated_prop == "1:1":
        bpy.context.scene.render.resolution_x = bpy.context.scene.render.resolution_y
    elif sna_updated_prop == "3:2":
        bpy.context.scene.render.resolution_x = int(bpy.context.scene.render.resolution_y * float(3.0 / 2.0))
    elif sna_updated_prop == "4:3":
        bpy.context.scene.render.resolution_x = int(bpy.context.scene.render.resolution_y * float(4.0 / 3.0))
    elif sna_updated_prop == "16:9":
        bpy.context.scene.render.resolution_x = int(bpy.context.scene.render.resolution_y * float(16.0 / 9.0))
    elif sna_updated_prop == "14:9":
        bpy.context.scene.render.resolution_x = int(bpy.context.scene.render.resolution_y * float(14.0 / 9.0))
    elif sna_updated_prop == "1.85:1":
        bpy.context.scene.render.resolution_x = int(bpy.context.scene.render.resolution_y * float(1.850000023841858 / 1.0))
    elif sna_updated_prop == "2.39:1":
        bpy.context.scene.render.resolution_x = int(bpy.context.scene.render.resolution_y * float(2.390000104904175 / 1.0))
    else:
        pass


def sna_update_sna_view_tex_632AA(self, context):
    sna_updated_prop = self.sna_view_tex
    for i_16090 in range(len(bpy.context.screen.areas)):
        if (bpy.context.screen.areas[i_16090].type == 'VIEW_3D'):
            for i_BB728 in range(len(bpy.context.screen.areas[i_16090].spaces)):
                if (bpy.context.screen.areas[i_16090].spaces[i_BB728].type == 'VIEW_3D'):
                    if (((bpy.context.screen.areas[i_16090].spaces[i_BB728].shading.light == 'FLAT') and (bpy.context.screen.areas[i_16090].spaces[i_BB728].shading.color_type == 'TEXTURE')) and bpy.context.scene.sna_view_tex):
                        node_tree_001['sna_old_light_shading'] = 'MATCAP'
                        node_tree_001['sna_old_color_type_shading'] = 'OBJECT'
                        node_tree_001['sna_old_show_wireframes'] = False
                        node_tree_001['sna_old_show_bones'] = True
                        bpy.context.screen.areas[i_16090].spaces[i_BB728].shading.light = node_tree_001['sna_old_light_shading']
                        bpy.context.screen.areas[i_16090].spaces[i_BB728].shading.color_type = node_tree_001['sna_old_color_type_shading']
                        bpy.context.screen.areas[i_16090].spaces[i_BB728].overlay.show_wireframes = node_tree_001['sna_old_show_wireframes']
                        bpy.context.screen.areas[i_16090].spaces[i_BB728].overlay.show_bones = node_tree_001['sna_old_show_bones']
                    else:
                        if bpy.context.scene.sna_view_tex:
                            node_tree_001['sna_old_light_shading'] = bpy.context.screen.areas[i_16090].spaces[i_BB728].shading.light
                            node_tree_001['sna_old_color_type_shading'] = bpy.context.screen.areas[i_16090].spaces[i_BB728].shading.color_type
                            node_tree_001['sna_old_show_wireframes'] = bpy.context.screen.areas[i_16090].spaces[i_BB728].overlay.show_wireframes
                            node_tree_001['sna_old_show_bones'] = bpy.context.screen.areas[i_16090].spaces[i_BB728].overlay.show_bones
                            bpy.context.screen.areas[i_16090].spaces[i_BB728].shading.light = 'FLAT'
                            bpy.context.screen.areas[i_16090].spaces[i_BB728].shading.color_type = 'TEXTURE'
                            bpy.context.screen.areas[i_16090].spaces[i_BB728].overlay.show_wireframes = False
                            bpy.context.screen.areas[i_16090].spaces[i_BB728].overlay.show_bones = False
                        else:
                            bpy.context.screen.areas[i_16090].spaces[i_BB728].shading.light = node_tree_001['sna_old_light_shading']
                            bpy.context.screen.areas[i_16090].spaces[i_BB728].shading.color_type = node_tree_001['sna_old_color_type_shading']
                            bpy.context.screen.areas[i_16090].spaces[i_BB728].overlay.show_wireframes = node_tree_001['sna_old_show_wireframes']
                            bpy.context.screen.areas[i_16090].spaces[i_BB728].overlay.show_bones = node_tree_001['sna_old_show_bones']
                            node_tree_001['sna_old_light_shading'] = 'MATCAP'
                            node_tree_001['sna_old_color_type_shading'] = 'OBJECT'
                            node_tree_001['sna_old_show_wireframes'] = False
                            node_tree_001['sna_old_show_bones'] = True


def sna_update_sna_new_property_003_B42B0(self, context):
    sna_updated_prop = self.sna_new_property_003
    if sna_updated_prop:
        bpy.context.preferences.view.language = 'zh_CN'
        bpy.context.preferences.view.use_translate_new_dataname = False
    else:
        bpy.context.preferences.view.language = 'en_US'
        bpy.context.preferences.view.use_translate_new_dataname = False


def property_exists(prop_path, glob, loc):
    try:
        eval(prop_path, glob, loc)
        return True
    except:
        return False


def sna_absin_C9F6D_724FA(Input):
    return (Input if (Input > 0) else float(Input * -1.0))


def sna_absin_C9F6D_188B6(Input):
    return (Input if (Input > 0) else float(Input * -1.0))


def sna_absin_C9F6D_CCBBB(Input):
    return (Input if (Input > 0) else float(Input * -1.0))


def sna_absin_C9F6D_880B5(Input):
    return (Input if (Input > 0) else float(Input * -1.0))


def sna_absin_C9F6D_46D54(Input):
    return (Input if (Input > 0) else float(Input * -1.0))


def sna_absin_C9F6D_E198F(Input):
    return (Input if (Input > 0) else float(Input * -1.0))


def display_collection_id(uid, vars):
    id = f"coll_{uid}"
    for var in vars.keys():
        if var.startswith("i_"):
            id += f"_{var}_{vars[var]}"
    return id


def sna_select_vertex_9E7EA(i):
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.context.view_layer.objects.active.data.vertices[i].select = True
    bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='EDIT')


def sna_select_vertex_groups_8448B(name):
    bpy.ops.object.vertex_group_assign_new('INVOKE_DEFAULT', )
    bpy.context.view_layer.objects.active.vertex_groups.active.name = name


def sna_switch_datain_C5A17(id, data0, data1, data2, data3, other):
    return (data0 if (id == 0) else (data1 if (id == 1) else (data2 if (id == 2) else (data3 if (id == 3) else other))))


def sna_in_79644(node_groups, node, Input, property_type, property_type_id, value):
    driver_2885E = node_groups.nodes[node].inputs[Input].driver_add('default_value', )
    driver_2885E.driver.type = 'SCRIPTED'
    var_50B28 = driver_2885E.driver.variables.new()
    var_50B28.name = 'var'
    var_50B28.type = 'SINGLE_PROP'
    var_50B28.targets[0].id_type = property_type
    var_50B28.targets[0].id = property_type_id
    var_50B28.targets[0].data_path = value
    driver_2885E.driver.expression = 'var'
    return [driver_2885E, var_50B28]


__all__ = [name for name in globals() if not name.startswith('__')]
