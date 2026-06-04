# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "mmd Quick tool",
    "author" : "SFY", 
    "description" : "",
    "blender" : (3, 0, 0),
    "version" : (1, 1, 7),
    "location" : "",
    "warning" : "",
    "doc_url": "https://github.com/bb-yi/mmd-Quick-tool", 
    "tracker_url": "", 
    "category" : "3D View" 
}


import bpy
import bpy.utils.previews
import os
from bpy_extras.io_utils import ImportHelper, ExportHelper
import mathutils
import math
from bpy.app.handlers import persistent
from datetime import datetime




def string_to_int(value):
    if value.isdigit():
        return int(value)
    return 0


def string_to_icon(value):
    if value in bpy.types.UILayout.bl_rna.functions["prop"].parameters["icon"].enum_items.keys():
        return bpy.types.UILayout.bl_rna.functions["prop"].parameters["icon"].enum_items[value].value
    return string_to_int(value)


addon_keymaps = {}
_icons = None
ikfix = {'sna_bone_obj': None, 'sna_base_obj': None, 'sna_bone': [], 'sna_constraint_obj': None, 'sna_abc': None, 'sna_bone_list': [], }
node_tree = {'sna_act_obj': None, 'sna_sna_new_variable': [], 'sna_sna_new_variable_001': 0, }
abc = {'sna_sna_new_variable': False, }
node_tree_001 = {'sna_old_light_shading': 'MATCAP', 'sna_old_color_type_shading': 'OBJECT', 'sna_old_show_wireframes': False, 'sna_old_show_bones': True, 'sna_old_active_objects': '', }
node_tree_004 = {'sna_is_other_color_space': False, 'sna_select_ver': [], 'sna_select_ver_pos': [], }
node_tree_005 = {'sna_act_obj': None, 'sna_base_obj': None, }
node_tree_001 = {'sna_render_start_time': 0.0, 'sna_render_end_time': 0.0, 'sna_sna_new_variable': [], 'sna_sub_render_time': 0.0, 'sna_avg_render_time': 0.0, 'sna_sub_frame': 0, 'sna_default_camera': '', 'sna_default_frame_start': 0, 'sna_default_frame_end': 0, 'sna_default_output_directory': '', }
node_tree_005 = {'sna_sna_new_variable': None, 'sna_camera': None, 'sna_sna_new_variable_001': None, 'sna_sna_new_variable_002': None, 'sna_sna_new_variable_002': None, 'sna_sna_new_variable_003': None, }
node_tree_004 = {'sna_last_node': None, 'sna_bake_tex_size_x': 0, 'sna_bake_tex_size_y': 0, }
node_tree_008 = {'sna_select_obj': [], 'sna_num': 0, 'sna_bone_obj': None, 'sna_bone_weight_from': None, 'sna_bone_weight_to': [], }
node_tree_002 = {'sna_sna_new_variable': '', }
node_tree_005 = {'sna_light_obj': [], }
node_tree_002 = {'sna_old_render_size': [], }


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


def sna_update_render_camera_28727(self, context):
    sna_updated_prop = self.render_camera
    for i_18B62 in range(len(bpy.context.scene.sna_render_list)):
        if (bpy.context.scene.sna_render_list[i_18B62].render_camera == None):
            pass
        else:
            if ((bpy.context.scene.sna_render_list[i_18B62].render_camera != None) and bpy.context.scene.sna_render_list[i_18B62].render_camera.type == 'CAMERA'):
                pass
            else:
                bpy.context.scene.sna_render_list[i_18B62].render_camera = None


def display_collection_id(uid, vars):
    id = f"coll_{uid}"
    for var in vars.keys():
        if var.startswith("i_"):
            id += f"_{var}_{vars[var]}"
    return id


class SNA_UL_display_collection_list_B793B(bpy.types.UIList):

    def draw_item(self, context, layout, data, item_B793B, icon, active_data, active_propname, index_B793B):
        row = layout
        layout.prop(item_B793B, 'on', text='', icon_value=(string_to_icon('HIDE_OFF') if item_B793B.on else string_to_icon('HIDE_ON')), emboss=item_B793B.on)
        layout.prop(item_B793B, 'name', text='', icon_value=0, emboss=False)
        layout.prop(item_B793B, 'start_frame', text='开始', icon_value=0, emboss=item_B793B.on)
        layout.prop(item_B793B, 'end_frame', text='结束', icon_value=0, emboss=item_B793B.on)
        layout.prop(item_B793B, 'render_camera', text='', icon_value=string_to_icon('CAMERA_DATA'), emboss=item_B793B.on)
        layout.prop(item_B793B, 'output_directory', text='', icon_value=0, emboss=item_B793B.on)

    def filter_items(self, context, data, propname):
        flt_flags = []
        for item in getattr(data, propname):
            if not self.filter_name or self.filter_name.lower() in item.name.lower():
                if True:
                    flt_flags.append(self.bitflag_filter_item)
                else:
                    flt_flags.append(0)
            else:
                flt_flags.append(0)
        return flt_flags, []


def sna_select_vertex_9E7EA(i):
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.context.view_layer.objects.active.data.vertices[i].select = True
    bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='EDIT')


def sna_select_vertex_groups_8448B(name):
    bpy.ops.object.vertex_group_assign_new('INVOKE_DEFAULT', )
    bpy.context.view_layer.objects.active.vertex_groups.active.name = name


class SNA_OT_My_Generic_Operator_C8494(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_c8494"
    bl_label = "生成骨骼约束"
    bl_description = "选中骨架和abc(会自动识别顶点组包含的骨骼)"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (len(bpy.context.view_layer.objects.selected) == 2):
            for i_9F071 in range(len(bpy.context.view_layer.objects.selected)):
                if (bpy.context.view_layer.objects.selected[i_9F071].type == 'ARMATURE'):
                    ikfix['sna_constraint_obj'] = bpy.context.view_layer.objects.selected[i_9F071]
                else:
                    ikfix['sna_abc'] = bpy.context.view_layer.objects.selected[i_9F071]
            for i_78390 in range(len(ikfix['sna_abc'].vertex_groups)):
                if '_x' in ikfix['sna_abc'].vertex_groups[i_78390].name:
                    ikfix['sna_bone_list'].append(ikfix['sna_abc'].vertex_groups[i_78390].name[:int(len(ikfix['sna_abc'].vertex_groups[i_78390].name) - 2.0)])
            bpy.context.view_layer.objects.active = ikfix['sna_constraint_obj']
            bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='POSE')
            for i_293E9 in range(len(ikfix['sna_constraint_obj'].data.bones)):
                if ikfix['sna_constraint_obj'].data.bones[i_293E9].name in ikfix['sna_bone_list']:
                    ikfix['sna_constraint_obj'].data.bones.active = ikfix['sna_constraint_obj'].data.bones[i_293E9]
                    constraint_52BAD = ikfix['sna_constraint_obj'].pose.bones[ikfix['sna_constraint_obj'].data.bones.active.name].constraints.new(type='COPY_LOCATION', )
                    constraint_52BAD.name = 'Copy Location_P'
                    constraint_52BAD.target = ikfix['sna_abc']
                    constraint_52BAD.subtarget = ikfix['sna_constraint_obj'].data.bones[i_293E9].name + '_p'
                    constraint_BBB91 = ikfix['sna_constraint_obj'].pose.bones[ikfix['sna_constraint_obj'].data.bones.active.name].constraints.new(type='DAMPED_TRACK', )
                    constraint_BBB91.name = 'Damped Track_X'
                    constraint_BBB91.target = ikfix['sna_abc']
                    constraint_BBB91.subtarget = ikfix['sna_constraint_obj'].data.bones[i_293E9].name + '_x'
                    constraint_BBB91.track_axis = 'TRACK_X'
                    constraint_FA476 = ikfix['sna_constraint_obj'].pose.bones[ikfix['sna_constraint_obj'].data.bones.active.name].constraints.new(type='DAMPED_TRACK', )
                    constraint_FA476.name = 'Damped Track_Z'
                    constraint_FA476.target = ikfix['sna_abc']
                    constraint_FA476.subtarget = ikfix['sna_constraint_obj'].data.bones[i_293E9].name + '_z'
                    constraint_FA476.track_axis = 'TRACK_Z'
                    self.report({'INFO'}, message='添加约束完成')
        else:
            self.report({'WARNING'}, message='没有选中两个物体')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Ik_B204A(bpy.types.Operator):
    bl_idname = "sna.ik_b204a"
    bl_label = "切换ik"
    bl_description = "关闭/打开IK"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if ((len(bpy.context.view_layer.objects.selected) == 1) and (bpy.context.view_layer.objects.active.type == 'ARMATURE')):
            for i_74BC2 in range(len(bpy.context.view_layer.objects.active.data.bones)):
                for i_DC99E in range(len(bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_74BC2].name].constraints)-1,-1,-1):
                    if 'IK' in bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_74BC2].name].constraints[i_DC99E].name:
                        bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_74BC2].name].constraints[i_DC99E].enabled =  not bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_74BC2].name].constraints[i_DC99E].enabled
                        self.report({'INFO'}, message=('已打开ik' if bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_74BC2].name].constraints[i_DC99E].enabled else '已关闭ik'))
        else:
            self.report({'WARNING'}, message='没有选中骨骼')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_My_Generic_Operator_C3269(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_c3269"
    bl_label = "添加骨骼物体"
    bl_description = "选中需要添加骨骼物体的骨架"
    bl_options = {"REGISTER", "UNDO"}
    sna_new_property: bpy.props.BoolProperty(name='自定义骨骼物体', description='', default=False)

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (len(bpy.context.view_layer.objects.selected) == 1):
            if (bpy.context.view_layer.objects.active.type == 'ARMATURE'):
                ikfix['sna_bone'] = []
                for i_6AD46 in range(len(bpy.context.view_layer.objects.active.data.bones)):
                    if bpy.context.view_layer.objects.active.data.bones[i_6AD46].select:
                        ikfix['sna_bone'].append(bpy.context.view_layer.objects.active.data.bones[i_6AD46].name)
                if self.sna_new_property:
                    for i_CAD53 in range(len(bpy.context.view_layer.objects.active.data.bones)):
                        if bpy.context.view_layer.objects.active.data.bones[i_CAD53].name in ikfix['sna_bone']:
                            bpy.context.view_layer.objects.active.data.bones[i_CAD53].select = True
                else:
                    bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='POSE')
                    bpy.ops.pose.select_all('INVOKE_DEFAULT', action='DESELECT')
                    for i_F4341 in range(len(['足.L', 'ひざ.L', '足首.L', '足先EX.L', '足.R', 'ひざ.R', '足首.R', '足先EX.R'])):
                        bpy.ops.object.select_pattern(pattern=['足.L', 'ひざ.L', '足首.L', '足先EX.L', '足.R', 'ひざ.R', '足首.R', '足先EX.R'][i_F4341])
                if (self.sna_new_property and (len(ikfix['sna_bone']) == 0)):
                    self.report({'WARNING'}, message='没有选中骨骼')
                else:
                    ikfix['sna_bone_obj'] = bpy.context.view_layer.objects.active
                    if (ikfix['sna_bone_obj'].type == 'ARMATURE'):
                        bpy.ops.mesh.primitive_cube_add('INVOKE_DEFAULT', )
                        bpy.context.view_layer.objects.active.name = '骨骼坐标系'
                        ikfix['sna_base_obj'] = bpy.context.view_layer.objects.active
                        bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='EDIT')
                        bpy.ops.mesh.select_all(action='SELECT')
                        bpy.ops.transform.transform(value=(0.05000000074505806, 0.05000000074505806, 0.05000000074505806, 0.0))
                        bpy.ops.transform.resize(value=(0.05000000074505806, 0.05000000074505806, 0.05000000074505806), orient_type='GLOBAL')
                        bpy.ops.mesh.select_all(action='DESELECT')
                        bpy.ops.object.mode_set(mode='OBJECT')
                        bpy.context.view_layer.objects.active.data.vertices[7].select = True
                        bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='EDIT')
                        bpy.ops.mesh.delete(type='VERT')
                        sna_select_vertex_9E7EA(0)
                        sna_select_vertex_groups_8448B('p')
                        sna_select_vertex_9E7EA(4)
                        sna_select_vertex_groups_8448B('x')
                        sna_select_vertex_9E7EA(2)
                        sna_select_vertex_groups_8448B('y')
                        sna_select_vertex_9E7EA(1)
                        sna_select_vertex_groups_8448B('z')
                        bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='OBJECT')
                        bpy.context.view_layer.objects.active = ikfix['sna_bone_obj']
                        bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='POSE')
                        for i_7D9BF in range(len(ikfix['sna_bone_obj'].data.bones)):
                            if ikfix['sna_bone_obj'].data.bones[i_7D9BF].select:
                                id_C2AF2 = ikfix['sna_base_obj'].copy()
                                id_1CE8E = id_C2AF2.data.copy()
                                id_C2AF2.data = id_1CE8E
                                bpy.context.collection.objects.link(object=id_C2AF2, )
                                id_C2AF2.name = ikfix['sna_bone_obj'].data.bones[i_7D9BF].name
                                id_C2AF2.matrix_world = ikfix['sna_bone_obj'].data.bones[i_7D9BF].matrix_local
                                for i_A9C43 in range(len(id_C2AF2.vertex_groups)):
                                    id_C2AF2.vertex_groups[i_A9C43].name = ikfix['sna_bone_obj'].data.bones[i_7D9BF].name + '_' + id_C2AF2.vertex_groups[i_A9C43].name
                                group_01804 = id_C2AF2.vertex_groups.new(name=ikfix['sna_bone_obj'].data.bones[i_7D9BF].name, )
                                for i_37E11 in range(len(id_C2AF2.data.vertices)):
                                    group_01804.add(index=(id_C2AF2.data.vertices[i_37E11].index, 0, 0), weight=1.0, type='REPLACE', )
                                modifier_130DA = id_C2AF2.modifiers.new(name='Armature Modifier', type='ARMATURE', )
                                modifier_130DA.object = ikfix['sna_bone_obj']
                                bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='OBJECT')
                                bpy.ops.object.parent_set('INVOKE_DEFAULT', type='OBJECT')
                        bpy.data.objects.remove(object=ikfix['sna_base_obj'], )
                        bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.selected[int(len(bpy.context.view_layer.objects.selected) - 1.0)]
                        for i_D9642 in range(len(bpy.context.screen.areas)):
                            if (bpy.context.screen.areas[i_D9642].type == 'VIEW_3D'):
                                for i_09F37 in range(len(bpy.context.screen.areas[i_D9642].regions)):
                                    if (bpy.context.screen.areas[i_D9642].regions[i_09F37].type == 'WINDOW'):
                                        area_5AE5A = bpy.context.screen.areas[i_D9642]
                                        region_5AE5A = bpy.context.screen.areas[i_D9642].regions[i_09F37]
                                        with bpy.context.temp_override(area=area_5AE5A, region=region_5AE5A, ):
                                            if (None == bpy.context.view_layer.objects.active):
                                                self.report({'WARNING'}, message='未生成骨骼物体')
                                            else:
                                                if (bpy.context.view_layer.objects.active.type == 'MESH'):
                                                    bpy.ops.object.join('INVOKE_DEFAULT', )
                                                    bpy.context.scene.cursor.location = (0.0, 0.0, 0.0)
                                                    bpy.ops.object.origin_set('INVOKE_DEFAULT', type='ORIGIN_CURSOR')
                    else:
                        self.report({'WARNING'}, message='所选物体不是骨骼')
            else:
                self.report({'WARNING'}, message='没有选中骨骼')
        else:
            self.report({'WARNING'}, message='没有选中骨骼')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_My_Generic_Operator_Cc136(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_cc136"
    bl_label = "传递顶点组"
    bl_description = "选中abc和骨骼物体"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (len(bpy.context.view_layer.objects.selected) == 2):
            if (len(bpy.context.view_layer.objects.active.vertex_groups) == 0):
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
            else:
                self.report({'WARNING'}, message='活动物体含有顶点组')
        else:
            self.report({'WARNING'}, message='没有选中两个物体')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_My_Generic_Operator_89058(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_89058"
    bl_label = "清除骨骼约束"
    bl_description = "选中骨骼，将清除生成的骨骼约束"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if ((len(bpy.context.view_layer.objects.selected) == 1) and (bpy.context.view_layer.objects.active.type == 'ARMATURE')):
            for i_751D8 in range(len(bpy.context.view_layer.objects.active.data.bones)):
                for i_70648 in range(len(bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_751D8].name].constraints)-1,-1,-1):
                    if ('Copy Location_P' in bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_751D8].name].constraints[i_70648].name or 'Damped Track_X' in bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_751D8].name].constraints[i_70648].name or 'Damped Track_Z' in bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_751D8].name].constraints[i_70648].name):
                        bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_751D8].name].constraints.remove(constraint=bpy.context.view_layer.objects.active.pose.bones[bpy.context.view_layer.objects.active.data.bones[i_751D8].name].constraints[i_70648], )
                        self.report({'INFO'}, message='已移除约束')
        else:
            self.report({'WARNING'}, message='没有选中骨骼')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_My_Generic_Operator_C034B(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_c034b"
    bl_label = "烘焙约束"
    bl_description = "将ik约束烘焙为关键帧"
    bl_options = {"REGISTER", "UNDO"}
    sna_new_property: bpy.props.IntProperty(name='起始帧', description='', default=0, subtype='NONE', min=0)
    sna_new_property_001: bpy.props.IntProperty(name='结束帧', description='', default=250, subtype='NONE', min=0)

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (bpy.context.view_layer.objects.active.type == 'ARMATURE'):
            bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='POSE')
            bpy.ops.sna.my_generic_operator_400a9('INVOKE_DEFAULT', sna_new_property='腿ik骨')
            bpy.ops.nla.bake(frame_start=self.sna_new_property, frame_end=self.sna_new_property_001, only_selected=True, visual_keying=True, clear_constraints=True, use_current_action=True, bake_types={'POSE'})
            self.report({'INFO'}, message='烘焙完成')
        else:
            self.report({'WARNING'}, message='活动物体不是骨骼')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Uv_94B57(bpy.types.Operator):
    bl_idname = "sna.uv_94b57"
    bl_label = "移除位置uv"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_EE5B8 in range(len(bpy.context.view_layer.objects.selected)):
            bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.selected[i_EE5B8]
            bpy.context.view_layer.objects.active.data.uv_layers.active = bpy.context.view_layer.objects.active.data.uv_layers[int(len(bpy.context.view_layer.objects.active.data.uv_layers) - 1.0)]
            if 'pos' in bpy.context.view_layer.objects.active.data.uv_layers.active.name:
                bpy.ops.mesh.uv_texture_remove('INVOKE_DEFAULT', )
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Uv_9201E(bpy.types.Operator):
    bl_idname = "sna.uv_9201e"
    bl_label = "生成视图uv"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    def sna_new_property_enum_items(self, context):
        return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]
    sna_new_property: bpy.props.EnumProperty(name='视图方向', description='', items=[('FRONT', 'FRONT', '', 0, 0), ('LEFT', 'LEFT', '', 0, 1), ('TOP', 'TOP', '', 0, 2)])

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_7227A in range(len(bpy.context.view_layer.objects.selected)):
            bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.selected[i_7227A]
            bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='EDIT')
            bpy.ops.view3d.view_axis('INVOKE_DEFAULT', type=self.sna_new_property)
            bpy.ops.mesh.select_all('INVOKE_DEFAULT', action='SELECT')
            bpy.ops.mesh.uv_texture_add('INVOKE_DEFAULT', )
            bpy.context.view_layer.objects.active.data.uv_layers[int(len(bpy.context.view_layer.objects.active.data.uv_layers) - 1.0)].name = 'pos_' + self.sna_new_property
            bpy.context.view_layer.objects.active.data.uv_layers.active = bpy.context.view_layer.objects.active.data.uv_layers[int(len(bpy.context.view_layer.objects.active.data.uv_layers) - 1.0)]
        for i_F23AC in range(len(bpy.context.screen.areas)):
            if (bpy.context.screen.areas[i_F23AC].type == 'VIEW_3D'):
                for i_94977 in range(len(bpy.context.screen.areas[i_F23AC].regions)):
                    if (bpy.context.screen.areas[i_F23AC].regions[i_94977].type == 'WINDOW'):
                        area_9235B = bpy.context.screen.areas[i_F23AC]
                        region_9235B = bpy.context.screen.areas[i_F23AC].regions[i_94977]
                        with bpy.context.temp_override(area=area_9235B, region=region_9235B, ):
                            bpy.ops.uv.project_from_view('INVOKE_DEFAULT', )
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_My_Generic_Operator_Bedaf(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_bedaf"
    bl_label = "材质到物体"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_73298 in range(len(bpy.context.view_layer.objects.selected)):
            if (property_exists("bpy.context.view_layer.objects.selected[i_73298].data.materials", globals(), locals()) and len(bpy.context.view_layer.objects.selected[i_73298].data.materials) > 0):
                bpy.context.view_layer.objects.selected[i_73298].name = bpy.context.view_layer.objects.selected[i_73298].data.materials[0].name
            else:
                self.report({'INFO'}, message=bpy.context.view_layer.objects.selected[i_73298].name + '没有材质')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_My_Generic_Operator_04Cf5(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_04cf5"
    bl_label = "物体到材质"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_E1144 in range(len(bpy.context.view_layer.objects.selected)):
            if (property_exists("bpy.context.view_layer.objects.selected[i_E1144].data.materials", globals(), locals()) and len(bpy.context.view_layer.objects.selected[i_E1144].data.materials) > 0):
                bpy.context.view_layer.objects.selected[i_E1144].data.materials[0].name = bpy.context.view_layer.objects.selected[i_E1144].name
            else:
                self.report({'INFO'}, message=bpy.context.view_layer.objects.selected[i_E1144].name + '没有材质')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_My_Generic_Operator_60634(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_60634"
    bl_label = "贴图到材质"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_F171C in range(len(bpy.context.view_layer.objects.selected)):
            if (property_exists("bpy.context.view_layer.objects.selected[i_F171C].data.materials", globals(), locals()) and len(bpy.context.view_layer.objects.selected[i_F171C].data.materials) > 0):
                for i_000DB in range(len(bpy.context.view_layer.objects.selected[i_F171C].data.materials[0].node_tree.nodes)):
                    if (bpy.context.view_layer.objects.selected[i_F171C].data.materials[0].node_tree.nodes[i_000DB].type == 'TEX_IMAGE'):
                        for i_E8F57 in range(len(bpy.context.view_layer.objects.selected[i_F171C].data.materials[0].node_tree.nodes[i_000DB].id_data.links)):
                            for i_85594 in range(len(['Color', 'Base Color', 'Diffuse Color', 'Albedo', 'Base Tex'])):
                                if ((bpy.context.view_layer.objects.selected[i_F171C].data.materials[0].node_tree.nodes[i_000DB].id_data.links[i_E8F57].to_socket.name == ['Color', 'Base Color', 'Diffuse Color', 'Albedo', 'Base Tex'][i_85594]) and (bpy.context.view_layer.objects.selected[i_F171C].data.materials[0].node_tree.nodes[i_000DB].id_data.links[i_E8F57].from_node == bpy.context.view_layer.objects.selected[i_F171C].data.materials[0].node_tree.nodes[i_000DB])):
                                    bpy.context.view_layer.objects.selected[i_F171C].name = bpy.context.view_layer.objects.selected[i_F171C].data.materials[0].node_tree.nodes[i_000DB].image.name
            else:
                self.report({'INFO'}, message=bpy.context.view_layer.objects.selected[i_F171C].name + '没有材质')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_switch_datain_C5A17(id, data0, data1, data2, data3, other):
    return (data0 if (id == 0) else (data1 if (id == 1) else (data2 if (id == 2) else (data3 if (id == 3) else other))))


class SNA_OT_My_Generic_Operator_Dd728(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_dd728"
    bl_label = "分离临时合并"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        node_tree['sna_sna_new_variable_001'] = 0
        node_tree['sna_sna_new_variable'] = []
        for i_F242D in range(len(bpy.context.view_layer.objects.active.vertex_groups)-1,-1,-1):
            if '_临时合并' in bpy.context.view_layer.objects.active.vertex_groups[i_F242D].name:
                node_tree['sna_sna_new_variable'].append(bpy.context.view_layer.objects.active.vertex_groups[i_F242D].name)
        if (len(node_tree['sna_sna_new_variable']) == 0):
            self.report({'WARNING'}, message='不存在临时合并顶点组数据')
        else:
            node_tree['sna_sna_new_variable_001'] = len(node_tree['sna_sna_new_variable'])
            node_tree['sna_sna_new_variable'] = []
            for i_583AB in range(len(bpy.context.view_layer.objects.active.data.attributes)-1,-1,-1):
                if '_临时合并' in bpy.context.view_layer.objects.active.data.attributes[i_583AB].name:
                    node_tree['sna_sna_new_variable'].append(None)
            if (len(node_tree['sna_sna_new_variable']) == 0):
                self.report({'WARNING'}, message='不存在临时合并属性数据')
            else:
                if (len(node_tree['sna_sna_new_variable']) == int(node_tree['sna_sna_new_variable_001'] * 3.0)):
                    for i_5CA6A in range(len(bpy.context.view_layer.objects.active.vertex_groups)-1,-1,-1):
                        if '_临时合并' in bpy.context.view_layer.objects.active.vertex_groups[i_5CA6A].name:
                            bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='EDIT')
                            bpy.ops.mesh.select_all('INVOKE_DEFAULT', action='DESELECT')
                            bpy.context.view_layer.objects.active.vertex_groups.active = bpy.context.view_layer.objects.active.vertex_groups[i_5CA6A]
                            bpy.ops.object.vertex_group_select('INVOKE_DEFAULT', )
                            if (i_5CA6A == 0):
                                pass
                            else:
                                bpy.ops.mesh.separate('INVOKE_DEFAULT', type='SELECTED')
                            bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='OBJECT')
                            node_tree['sna_act_obj'] = None
                            node_tree['sna_act_obj'] = bpy.context.view_layer.objects.active
                            bpy.context.view_layer.objects.active = ((bpy.context.view_layer.objects.active if (len(bpy.context.view_layer.objects.selected) == 1) else bpy.context.view_layer.objects.selected[1]) if (bpy.context.view_layer.objects.active == bpy.context.view_layer.objects.selected[0]) else bpy.context.view_layer.objects.selected[0])
                            bpy.context.view_layer.objects.active.name = bpy.context.view_layer.objects.active.vertex_groups.active.name.replace('_临时合并', '')
                            bpy.context.scene.tool_settings.use_transform_data_origin = True
                            print(str(tuple(bpy.context.view_layer.objects.active.data.attributes[bpy.context.view_layer.objects.active.name + '_临时合并_locatiion'].data[0].vector)), str(tuple(bpy.context.view_layer.objects.active.data.attributes[bpy.context.view_layer.objects.active.name + '_临时合并_rotation'].data[0].vector)), str(tuple(bpy.context.view_layer.objects.active.data.attributes[bpy.context.view_layer.objects.active.name + '_临时合并_scale'].data[0].vector)))
                            bpy.context.scene.cursor.location = bpy.context.view_layer.objects.active.data.attributes[bpy.context.view_layer.objects.active.name + '_临时合并_locatiion'].data[0].vector
                            bpy.context.scene.cursor.rotation_mode = 'XYZ'
                            bpy.context.scene.cursor.rotation_euler = bpy.context.view_layer.objects.active.data.attributes[bpy.context.view_layer.objects.active.name + '_临时合并_rotation'].data[0].vector
                            for i_2835C in range(len(bpy.context.screen.areas)):
                                if (bpy.context.screen.areas[i_2835C].type == 'VIEW_3D'):
                                    for i_8CD55 in range(len(bpy.context.screen.areas[i_2835C].regions)):
                                        if (bpy.context.screen.areas[i_2835C].regions[i_8CD55].type == 'WINDOW'):
                                            area_A79EE = bpy.context.screen.areas[i_2835C]
                                            region_A79EE = bpy.context.screen.areas[i_2835C].regions[i_8CD55]
                                            with bpy.context.temp_override(area=area_A79EE, region=region_A79EE, ):
                                                bpy.ops.transform.transform(mode='ALIGN', orient_type='CURSOR')
                                                bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
                                                bpy.ops.transform.resize(value=(float(bpy.context.view_layer.objects.active.data.attributes[bpy.context.view_layer.objects.active.name + '_临时合并_scale'].data[0].vector[0] / bpy.context.view_layer.objects.active.scale[0]), float(bpy.context.view_layer.objects.active.data.attributes[bpy.context.view_layer.objects.active.name + '_临时合并_scale'].data[0].vector[1] / bpy.context.view_layer.objects.active.scale[1]), float(bpy.context.view_layer.objects.active.data.attributes[bpy.context.view_layer.objects.active.name + '_临时合并_scale'].data[0].vector[2] / bpy.context.view_layer.objects.active.scale[2])), orient_type='LOCAL')
                                                bpy.context.scene.tool_settings.use_transform_data_origin = False
                                                for i_A23D9 in range(len(bpy.context.view_layer.objects.active.vertex_groups)-1,-1,-1):
                                                    if '_临时合并' in bpy.context.view_layer.objects.active.vertex_groups[i_A23D9].name:
                                                        bpy.context.view_layer.objects.active.vertex_groups.remove(group=bpy.context.view_layer.objects.active.vertex_groups[i_A23D9], )
                                                for i_DAB1C in range(len(bpy.context.view_layer.objects.active.data.attributes)-1,-1,-1):
                                                    if '_临时合并' in bpy.context.view_layer.objects.active.data.attributes[i_DAB1C].name:
                                                        bpy.context.view_layer.objects.active.data.attributes.remove(attribute=bpy.context.view_layer.objects.active.data.attributes[i_DAB1C], )
                                                bpy.context.view_layer.objects.active.select = False
                                                bpy.context.view_layer.objects.active = node_tree['sna_act_obj']
                    bpy.context.scene.cursor.location = (1.0, 1.0, 1.0)
                    self.report({'INFO'}, message='已分离临时合并')
                else:
                    self.report({'WARNING'}, message='顶点组数据与属性数据不匹配')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_My_Generic_Operator_Fb95F(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_fb95f"
    bl_label = "临时合并.001"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_7420F in range(len(bpy.context.view_layer.objects.selected)):
            bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.selected[i_7420F]
            group_AFFA2 = bpy.context.view_layer.objects.selected[i_7420F].vertex_groups.new(name=bpy.context.view_layer.objects.selected[i_7420F].name + '_' + '临时合并', )
            bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='EDIT')
            bpy.ops.mesh.select_all('INVOKE_DEFAULT', action='SELECT')
            bpy.ops.object.vertex_group_assign('INVOKE_DEFAULT', )
            bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='OBJECT')
            for i_A100E in range(3):
                output_data_0_ab157 = sna_switch_datain_C5A17(i_A100E, 'locatiion', 'rotation', 'scale', None, None)
                output_data_0_88913 = sna_switch_datain_C5A17(i_A100E, bpy.context.view_layer.objects.selected[i_7420F].location, bpy.context.view_layer.objects.selected[i_7420F].rotation_euler, bpy.context.view_layer.objects.selected[i_7420F].scale, None, None)
                bpy.ops.geometry.attribute_add(name=bpy.context.view_layer.objects.selected[i_7420F].name + '_' + '临时合并' + '_' + output_data_0_ab157, domain='POINT', data_type='FLOAT_VECTOR')
                for i_0948D in range(len(bpy.context.view_layer.objects.selected[i_7420F].data.attributes[bpy.context.view_layer.objects.selected[i_7420F].name + '_' + '临时合并' + '_' + output_data_0_ab157].data)):
                    bpy.context.view_layer.objects.selected[i_7420F].data.attributes[bpy.context.view_layer.objects.selected[i_7420F].name + '_' + '临时合并' + '_' + output_data_0_ab157].data[i_0948D].vector = output_data_0_88913
        bpy.ops.object.join('INVOKE_DEFAULT', )
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Abc_B0Bf3(bpy.types.Operator, ImportHelper):
    bl_idname = "sna.abc_b0bf3"
    bl_label = "为abc添加材质"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}
    filter_glob: bpy.props.StringProperty( default='*.mtl', options={'HIDDEN'} )

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if os.path.exists(self.filepath):
            if (os.path.splitext(self.filepath)[1] == '.mtl'):
                a = self.filepath
                mtl_file_path = None
                tex_name = None
                obj_name = None
                for i_00339 in range(len(tex_name)):
                    abc['sna_sna_new_variable'] = False
                    for i_910C4 in range(len(bpy.data.materials)):
                        if (bpy.data.materials[i_910C4].name == tex_name[i_00339]):
                            abc['sna_sna_new_variable'] = True
                            break
                    if abc['sna_sna_new_variable']:
                        bpy.context.view_layer.objects['xform_0_material_' + str(i_00339)].data.materials.append(material=bpy.data.materials[tex_name[i_00339]], )
                    else:
                        if (len(bpy.context.view_layer.objects['xform_0_material_' + str(i_00339)].material_slots) == 0):
                            material_2593F = bpy.data.materials.new(name=tex_name[i_00339], )
                            material_2593F.use_nodes = True
                            if (os.path.exists(os.path.join(os.path.dirname(self.filepath),tex_name[i_00339])) and ('' != tex_name[i_00339])):
                                node_E38B9 = material_2593F.node_tree.nodes.new(type='ShaderNodeTexImage', )
                                node_E38B9.location = (-300.0, 300.0)
                            if (os.path.exists(os.path.join(os.path.dirname(self.filepath),tex_name[i_00339])) and ('' != tex_name[i_00339])):
                                image_7D5F6 = bpy.data.images.load(filepath=os.path.join(os.path.dirname(self.filepath),tex_name[i_00339]), check_existing=True, )
                                node_E38B9.image = image_7D5F6
                                link_92E7A = material_2593F.node_tree.links.new(input=material_2593F.node_tree.nodes[('原理化BSDF' if bpy.context.preferences.view.use_translate_new_dataname else 'Principled BSDF')].inputs['Base Color'], output=node_E38B9.outputs['Color'], )
                                link_72978 = material_2593F.node_tree.links.new(input=material_2593F.node_tree.nodes[('原理化BSDF' if bpy.context.preferences.view.use_translate_new_dataname else 'Principled BSDF')].inputs['Alpha'], output=node_E38B9.outputs['Alpha'], )
                            else:
                                self.report({'WARNING'}, message='贴图' + tex_name[i_00339] + '不存在')
                            bpy.context.view_layer.objects['xform_0_material_' + str(i_00339)].data.materials.append(material=material_2593F, )
                        else:
                            self.report({'WARNING'}, message=bpy.context.view_layer.objects['xform_0_material_' + str(i_00339)].name + '已存在材质')
                self.report({'INFO'}, message='成功添加材质')
            else:
                self.report({'WARNING'}, message='选中文件不是mtl')
        else:
            self.report({'WARNING'}, message='输入路径为空')
        return {"FINISHED"}


class SNA_OT_My_Generic_Operator_Abaaa(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_abaaa"
    bl_label = "移除选中物体所有材质"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_F4DCC in range(len(bpy.context.view_layer.objects.selected)):
            bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.selected[i_F4DCC]
            for i_356FC in range(len(bpy.context.view_layer.objects.selected[i_F4DCC].material_slots)):
                bpy.ops.object.material_slot_remove('INVOKE_DEFAULT', )
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator015_0Ebb1(bpy.types.Operator):
    bl_idname = "sna.operator015_0ebb1"
    bl_label = "Operator.015"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    def sna_new_property_enum_items(self, context):
        return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]
    sna_new_property: bpy.props.EnumProperty(name='位姿', description='', items=[('位置', '位置', '', 0, 0), ('旋转', '旋转', '', 0, 1), ('缩放', '缩放', '', 0, 2)])
    sna_x: bpy.props.BoolProperty(name='x', description='', default=True)
    sna_y: bpy.props.BoolProperty(name='y', description='', default=True)
    sna_z: bpy.props.BoolProperty(name='z', description='', default=True)

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_37CB5 in range(len(bpy.context.selected_objects)):
            if (self.sna_new_property == '位置'):
                if property_exists("bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].location", globals(), locals()):
                    bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].location = tuple(mathutils.Vector((bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].location if (self.sna_new_property == '位置') else (bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].rotation_euler if (self.sna_new_property == '旋转') else None))) * mathutils.Vector(((0 if self.sna_x else 1), (0 if self.sna_y else 1), (0 if self.sna_z else 1))))
            else:
                if (self.sna_new_property == '旋转'):
                    if property_exists("bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].rotation_euler", globals(), locals()):
                        bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].rotation_euler = tuple(mathutils.Vector((bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].location if (self.sna_new_property == '位置') else (bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].rotation_euler if (self.sna_new_property == '旋转') else None))) * mathutils.Vector(((0 if self.sna_x else 1), (0 if self.sna_y else 1), (0 if self.sna_z else 1))))
                else:
                    if (self.sna_new_property == '缩放'):
                        if property_exists("bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].scale", globals(), locals()):
                            bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].scale = ((1.0 if self.sna_x else bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].scale[0]), (1.0 if self.sna_y else bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].scale[1]), (1.0 if self.sna_z else bpy.context.view_layer.objects.selected[bpy.context.selected_objects[i_37CB5].name].scale[2]))
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_add_to_dopesheet_ht_header_E775E(self, context):
    if not (False):
        layout = self.layout
        row_85DC3 = layout.row(heading='', align=True)
        row_85DC3.alert = False
        row_85DC3.enabled = True
        row_85DC3.active = True
        row_85DC3.use_property_split = False
        row_85DC3.use_property_decorate = False
        row_85DC3.scale_x = 1.0
        row_85DC3.scale_y = 1.0
        row_85DC3.alignment = 'Expand'.upper()
        row_85DC3.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_85DC3.operator('sna.operator023_dc120', text='', icon_value=string_to_icon('TRIA_LEFT'), emboss=True, depress=False)
        op = row_85DC3.operator('sna.operator024_d37ce', text='', icon_value=string_to_icon('TRIA_RIGHT'), emboss=True, depress=False)


class SNA_OT_Operator024_D37Ce(bpy.types.Operator):
    bl_idname = "sna.operator024_d37ce"
    bl_label = "Operator.024"
    bl_description = "将当前帧设置为结束帧"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.frame_end = bpy.context.scene.frame_current
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator023_Dc120(bpy.types.Operator):
    bl_idname = "sna.operator023_dc120"
    bl_label = "Operator.023"
    bl_description = "将当前帧设置为起始帧"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.frame_start = bpy.context.scene.frame_current
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator021_0D655(bpy.types.Operator):
    bl_idname = "sna.operator021_0d655"
    bl_label = "Operator.021"
    bl_description = "删除装配产生的材质变形节点组"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        # 获取当前选中的对象
        selected_objects = bpy.context.selected_objects
        for obj in selected_objects:
            # 检查对象是否有材质
            if obj.material_slots:
                for slot in obj.material_slots:
                    # 检查材质是否有节点
                    if slot.material.use_nodes:
                        # 初始化要删除的节点列表
                        nodes_to_remove = []
                        # 初始化贴图节点变量
                        base1_rgb_texture_node = None
                        # 遍历节点，收集所有MMDMorphAdd和MMDMorphMul节点，并找到初始的贴图节点
                        for node in slot.material.node_tree.nodes:
                            if node.type == 'GROUP' and ('MMDMorphAdd' in node.node_tree.name or 'MMDMorphMul' in node.node_tree.name):
                                # 如果是第一个MMDMorph节点组，获取它的贴图
                                if base1_rgb_texture_node is None:
                                    for link in node.inputs['Base1 RGB'].links:
                                        if link.from_node.type == 'TEX_IMAGE':
                                            base1_rgb_texture_node = link.from_node
                                            break
                                # 添加节点到待删除列表
                                nodes_to_remove.append(node)
                        # 删除所有MMDMorphAdd和MMDMorphMul节点
                        for node in nodes_to_remove:
                            slot.material.node_tree.nodes.remove(node)
                        # 如果找到贴图节点，连接到MMDShaderDev的Base Tex输入
                        if base1_rgb_texture_node:
                            # 找到MMDShaderDev节点组
                            target_node_group = next((node for node in slot.material.node_tree.nodes if node.type == 'GROUP' and 'MMDShaderDev' in node.node_tree.name), None)
                            # 连接贴图节点到MMDShaderDev的Base Tex
                            if target_node_group:
                                slot.material.node_tree.links.new(target_node_group.inputs['Base Tex'], base1_rgb_texture_node.outputs['Color'])
        # 更新场景，以反映节点更改
        bpy.context.view_layer.update()
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator005_9368B(bpy.types.Operator):
    bl_idname = "sna.operator005_9368b"
    bl_label = "Operator.005"
    bl_description = "将替换mmd自带节点组为原理化节点组"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        # 获取当前选中的物体
        selected_objects = bpy.context.selected_objects
        # 遍历选中的物体
        for obj in selected_objects:
            # 遍历物体的所有材质槽
            for material_slot in obj.material_slots:
                material = material_slot.material
                # 遍历材质的所有节点
                for node in material.node_tree.nodes:
                    # 检查节点的类型和名称
                    if node.type == 'GROUP' and node.node_tree.name == 'MMDShaderDev':  # 替换为你的节点组名称
                        # 获取节点组的输入
                        base_tex_input = node.inputs.get('Base Tex')
                        base_alpha_input = node.inputs.get('Base Alpha')
                        # 如果找到对应的输入，继续处理
                        if base_tex_input and base_alpha_input:
                            # 获取连接到 Base Tex 和 Base Alpha 的连接
                            base_tex_link = base_tex_input.links[0] if base_tex_input.links else None
                            base_alpha_link = base_alpha_input.links[0] if base_alpha_input.links else None
                            # 创建新的原理化节点
                            principled_node = material.node_tree.nodes.new(type='ShaderNodeBsdfPrincipled')
                            principled_node.location = node.location
                            # 连接 Base Tex
                            if base_tex_link:
                                material.node_tree.links.new(principled_node.inputs['Base Color'], base_tex_link.from_socket)
                            # 连接 Base Alpha
                            if base_alpha_link:
                                material.node_tree.links.new(principled_node.inputs['Alpha'], base_alpha_link.from_socket)
                            # 连接新原理化节点到材质输出
                            material_output_node = material.node_tree.nodes.get("Material Output")
                            if material_output_node:
                                material.node_tree.links.new(material_output_node.inputs['Surface'], principled_node.outputs['BSDF'])
                            # 删除旧的节点
                            material.node_tree.nodes.remove(node)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator004_Fa32A(bpy.types.Operator):
    bl_idname = "sna.operator004_fa32a"
    bl_label = "Operator.004"
    bl_description = "合并使用同一基础色贴图的材质"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        # 存储贴图的字典
        texture_dict = {}
        color_input_name=["Color", "Base Color", "Diffuse Color", "Albedo","Base Tex"]
        # 获取所选物体列表
        selected_objects = bpy.context.selected_objects
        # 循环遍历所选物体
        for obj in selected_objects:
            # 检查物体是否为网格对象
            if isinstance(obj.data, bpy.types.Mesh):
                # 遍历物体的材质列表
                for material in obj.data.materials:
                    # 获取材质的节点树
                    tree = material.node_tree
                    # 遍历节点树中的所有节点
                    for node in tree.nodes:
                        # 检查节点类型是否为ShaderNodeTexImage（贴图节点）
                        if node.type == 'TEX_IMAGE':
                            # 检查节点的输出连接是否存在
                            if node.outputs['Color'].is_linked:
                                # 遍历节点的输出连接
                                for link in node.outputs['Color'].links:
                                    # 检查连接的输入端口名称是否为"基础颜色"
                                    for input_name in color_input_name:
                                        if link.to_socket.name == input_name:
                                            # 检查贴图是否已经在字典中
                                            if node.image.name not in texture_dict:
                                                # 将贴图节点添加到字典
                                                texture_dict[node.image.name] = material
                                                print('贴图已经在字典中', node.image.name)
                                            else:
                                                # 替换材质为字典中的材质
                                                new_material = texture_dict[node.image.name]
                                                # 将物体的材质更改为新的材质
                                                obj.data.materials[0] = new_material
                                                print('贴图不在字典中', node.image.name, '替换材质:', new_material.name)
                                    else:
                                        print('连接端口的贴图没找到')
                        else:
                            print("没有找到贴图")
            else:
                print('没有找到网格对象')
        #清理未使用数据块
        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
        # 设置材质的名称为贴图名称
        for tex_name, material in texture_dict.items():
            material.name = tex_name
        # 打印贴图字典
        print(texture_dict)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator025_4038C(bpy.types.Operator):
    bl_idname = "sna.operator025_4038c"
    bl_label = "Operator.025"
    bl_description = "为选中物体添加表情(需要安装mmd插件)"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_0D15C in range(len(bpy.context.view_layer.objects.selected)):
            bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.selected[i_0D15C]
            bpy.ops.mmd_tools.import_vmd('INVOKE_DEFAULT', )
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator001_64C4A(bpy.types.Operator):
    bl_idname = "sna.operator001_64c4a"
    bl_label = "Operator.001"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.render.resolution_x = 2560
        bpy.context.scene.render.resolution_y = 1440
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator_B46A6(bpy.types.Operator):
    bl_idname = "sna.operator_b46a6"
    bl_label = "Operator"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.render.resolution_x = 1920
        bpy.context.scene.render.resolution_y = 1080
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator007_85779(bpy.types.Operator):
    bl_idname = "sna.operator007_85779"
    bl_label = "Operator.007"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}
    sna_ax: bpy.props.IntProperty(name='ax', description='', default=0, subtype='NONE')

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        self.sna_ax = bpy.context.scene.render.resolution_x
        bpy.context.scene.render.resolution_x = bpy.context.scene.render.resolution_y
        bpy.context.scene.render.resolution_y = self.sna_ax
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator008_F7B4C(bpy.types.Operator):
    bl_idname = "sna.operator008_f7b4c"
    bl_label = "Operator.008"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.render.resolution_x = int(bpy.context.scene.render.resolution_x / 2.0)
        bpy.context.scene.render.resolution_y = int(bpy.context.scene.render.resolution_y / 2.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator002_7Dbd9(bpy.types.Operator):
    bl_idname = "sna.operator002_7dbd9"
    bl_label = "Operator.002"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.render.resolution_x = 3840
        bpy.context.scene.render.resolution_y = 2160
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator014_47F89(bpy.types.Operator):
    bl_idname = "sna.operator014_47f89"
    bl_label = "Operator.014"
    bl_description = "方形"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.render.resolution_x = 1920
        bpy.context.scene.render.resolution_y = 1920
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_add_to_render_pt_format_54259(self, context):
    if not ( not bpy.context.preferences.addons['mmd_quick_tool'].preferences.sna_new_property):
        layout = self.layout
        row_96091 = layout.row(heading='', align=False)
        row_96091.alert = False
        row_96091.enabled = True
        row_96091.active = True
        row_96091.use_property_split = False
        row_96091.use_property_decorate = False
        row_96091.scale_x = 1.0
        row_96091.scale_y = 1.0
        row_96091.alignment = 'Center'.upper()
        row_96091.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_96091.prop(bpy.context.scene.render, 'film_transparent', text='透明', icon_value=0, emboss=True)
        row_96091.prop(bpy.context.scene.render, 'use_persistent_data', text='持久数据', icon_value=0, emboss=True)
        row_96091.prop(bpy.context.scene.cycles, 'use_auto_tile', text='使用平铺', icon_value=0, emboss=True)
        row_96091.prop(bpy.context.scene.cycles, 'tile_size', text='平铺尺寸', icon_value=0, emboss=True)


class SNA_OT_Operator009_F9Bf5(bpy.types.Operator):
    bl_idname = "sna.operator009_f9bf5"
    bl_label = "Operator.009"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.render.resolution_x = int(bpy.context.scene.render.resolution_x * 2.0)
        bpy.context.scene.render.resolution_y = int(bpy.context.scene.render.resolution_y * 2.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_PT_MMD_0B0AC(bpy.types.Panel):
    bl_label = 'mmd快速工具'
    bl_idname = 'SNA_PT_MMD_0B0AC'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'MMD'
    bl_order = 0
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout


class SNA_OT_Operator003_Da1Be(bpy.types.Operator):
    bl_idname = "sna.operator003_da1be"
    bl_label = "Operator.003"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.render.resolution_x = int(bpy.context.scene.render.resolution_x * float(1.5 + 0.0))
        bpy.context.scene.render.resolution_y = int(bpy.context.scene.render.resolution_y * float(1.5 + 0.0))
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator010_18497(bpy.types.Operator):
    bl_idname = "sna.operator010_18497"
    bl_label = "Operator.010"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.render.resolution_x = int(bpy.context.scene.render.resolution_x * float(0.75 + 0.0))
        bpy.context.scene.render.resolution_y = int(bpy.context.scene.render.resolution_y * float(0.75 + 0.0))
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_add_to_time_mt_editor_menus_A1C9F(self, context):
    if not ((not bpy.context.preferences.addons['mmd_quick_tool'].preferences.sna_display_time)):
        layout = self.layout
        box_0652E = layout.box()
        box_0652E.alert = False
        box_0652E.enabled = True
        box_0652E.active = True
        box_0652E.use_property_split = False
        box_0652E.use_property_decorate = False
        box_0652E.alignment = 'Expand'.upper()
        box_0652E.scale_x = 1.0
        box_0652E.scale_y = 1.0
        if not True: box_0652E.operator_context = "EXEC_DEFAULT"
        row_89995 = box_0652E.row(heading='', align=False)
        row_89995.alert = False
        row_89995.enabled = True
        row_89995.active = True
        row_89995.use_property_split = False
        row_89995.use_property_decorate = False
        row_89995.scale_x = 1.0
        row_89995.scale_y = 1.0
        row_89995.alignment = 'Expand'.upper()
        row_89995.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_89995.label(text=str(('0' + str(int(int(bpy.context.scene.frame_current / bpy.context.scene.render.fps) / 60.0)) if (int(int(bpy.context.scene.frame_current / bpy.context.scene.render.fps) / 60.0) < 10) else int(int(bpy.context.scene.frame_current / bpy.context.scene.render.fps) / 60.0))) + ':' + str(('0' + str(int(bpy.context.scene.frame_current / bpy.context.scene.render.fps)) if (int(bpy.context.scene.frame_current / bpy.context.scene.render.fps) < 10) else int(bpy.context.scene.frame_current / bpy.context.scene.render.fps))) + ':' + str(('0' + str(int(float(int(bpy.context.scene.frame_current - int(int(bpy.context.scene.frame_current / bpy.context.scene.render.fps) * bpy.context.scene.render.fps)) * 100.0) / bpy.context.scene.render.fps)) if (int(float(int(bpy.context.scene.frame_current - int(int(bpy.context.scene.frame_current / bpy.context.scene.render.fps) * bpy.context.scene.render.fps)) * 100.0) / bpy.context.scene.render.fps) < 10) else int(float(int(bpy.context.scene.frame_current - int(int(bpy.context.scene.frame_current / bpy.context.scene.render.fps) * bpy.context.scene.render.fps)) * 100.0) / bpy.context.scene.render.fps))) + '+' + str(('0' + str(int(bpy.context.scene.frame_current - int(int(bpy.context.scene.frame_current / bpy.context.scene.render.fps) * bpy.context.scene.render.fps))) if (int(bpy.context.scene.frame_current - int(int(bpy.context.scene.frame_current / bpy.context.scene.render.fps) * bpy.context.scene.render.fps)) < 10) else int(bpy.context.scene.frame_current - int(int(bpy.context.scene.frame_current / bpy.context.scene.render.fps) * bpy.context.scene.render.fps)))), icon_value=string_to_icon('TIME'))
        op = row_89995.operator('sna.my_generic_operator_83d28', text='', icon_value=string_to_icon('KEY_RETURN'), emboss=True, depress=False)
        op.sna_new_property = 0
        op.sna_new_property_001 = 0


class SNA_OT_My_Generic_Operator_83D28(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_83d28"
    bl_label = "跳转到指定时间"
    bl_description = "跳转到指定时间"
    bl_options = {"REGISTER", "UNDO"}
    sna_new_property: bpy.props.IntProperty(name='分', description='', default=0, subtype='NONE', min=0)
    sna_new_property_001: bpy.props.IntProperty(name='秒', description='', default=0, subtype='NONE', min=0, max=60)

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.frame_current = int(int(self.sna_new_property_001 + int(self.sna_new_property * 60.0)) * bpy.context.scene.render.fps)
        self.report({'INFO'}, message='跳转到' + str(int(int(self.sna_new_property_001 + int(self.sna_new_property * 60.0)) * bpy.context.scene.render.fps)) + '帧')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_PT_MMD_5DD0C(bpy.types.Panel):
    bl_label = 'MMD工具'
    bl_idname = 'SNA_PT_MMD_5DD0C'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 2
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'SNA_PT_MMD_0B0AC'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout


class SNA_OT_Operator020_173C4(bpy.types.Operator):
    bl_idname = "sna.operator020_173c4"
    bl_label = "Operator.020"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_DBE3D in range(len(bpy.context.view_layer.objects.selected)):
            bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.selected[i_DBE3D]
            bpy.ops.mesh.customdata_custom_splitnormals_clear('INVOKE_DEFAULT', )
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator022_D211D(bpy.types.Operator):
    bl_idname = "sna.operator022_d211d"
    bl_label = "Operator.022"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_687B4 in range(len(bpy.context.view_layer.objects.selected)-1,-1,-1):
            bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.selected[i_687B4]
            for i_3F2FD in range(len(bpy.context.active_object.data.shape_keys.animation_data.action.fcurves)-1,-1,-1):
                if (len(bpy.context.object.data.shape_keys.animation_data.action.fcurves[i_3F2FD].keyframe_points) == 1):
                    bpy.context.object.data.shape_keys.animation_data.action.fcurves.remove(fcurve=bpy.context.active_object.data.shape_keys.animation_data.action.fcurves[i_3F2FD], )
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator023_9E188(bpy.types.Operator):
    bl_idname = "sna.operator023_9e188"
    bl_label = "Operator.023"
    bl_description = "清理形态键上的驱动器"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
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
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator024_1Bdb7(bpy.types.Operator):
    bl_idname = "sna.operator024_1bdb7"
    bl_label = "Operator.024"
    bl_description = "清除选中物体材质中未使用的节点"
    bl_options = {"REGISTER", "UNDO"}
    sna_new_property: bpy.props.IntProperty(name='深度', description='', default=1, subtype='NONE', min=1)

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        x = self.sna_new_property

        def delete_unconnected_nodes(material):
            # 遍历材质中的所有节点
            for node in material.node_tree.nodes:
                # 跳过材质输出节点
                if node.type == 'OUTPUT_MATERIAL':
                    continue
                # 检查节点的每个输出是否连接到其他节点
                if all(output.is_linked == False for output in node.outputs):
                    # 删除未连接的节点
                    material.node_tree.nodes.remove(node)

        def main():
            # 确保有物体被选中
            if bpy.context.selected_objects:
                for obj in bpy.context.selected_objects:
                    # 确保物体有材质
                    if obj.data.materials:
                        for mat in obj.data.materials:
                            # 如果材质存在节点，则调用函数
                            if mat and mat.node_tree:
                                delete_unconnected_nodes(mat)
        # 调用主函数
        #x = 3 #删除深度
        for i in range(x):
            main()
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator025_C68F6(bpy.types.Operator):
    bl_idname = "sna.operator025_c68f6"
    bl_label = "Operator.025"
    bl_description = "清除选中物体的骨骼修改器"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_A9AE5 in range(len(bpy.context.view_layer.objects.selected)):
            if (bpy.context.view_layer.objects.selected[i_A9AE5].type == 'MESH'):
                for i_02857 in range(len(bpy.context.view_layer.objects.selected[i_A9AE5].modifiers)):
                    print(bpy.context.view_layer.objects.selected[i_A9AE5].modifiers[i_02857].type)
                    if (bpy.context.view_layer.objects.selected[i_A9AE5].modifiers[i_02857].type == 'ARMATURE'):
                        bpy.context.view_layer.objects.selected[i_A9AE5].modifiers.remove(modifier=bpy.context.view_layer.objects.selected[i_A9AE5].modifiers[i_02857], )
                        break
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator002_Ac0A6(bpy.types.Operator):
    bl_idname = "sna.operator002_ac0a6"
    bl_label = "Operator.002"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.sna_view_tex = (not bpy.context.scene.sna_view_tex)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_add_to_view3d_ht_tool_header_80556(self, context):
    if not (False):
        layout = self.layout
        row_1F802 = layout.row(heading='', align=False)
        row_1F802.alert = False
        row_1F802.enabled = True
        row_1F802.active = True
        row_1F802.use_property_split = False
        row_1F802.use_property_decorate = False
        row_1F802.scale_x = 1.0
        row_1F802.scale_y = 1.0
        row_1F802.alignment = 'Center'.upper()
        row_1F802.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_1F802.prop(bpy.context.scene, 'sna_new_property_003', text=('中' if bpy.context.scene.sna_new_property_003 else '英'), icon_value=(string_to_icon('EVENT_C') if bpy.context.scene.sna_new_property_003 else string_to_icon('EVENT_E')), emboss=True)
        row_1F802.prop(bpy.context.scene, 'sna_view_tex', text='', icon_value=string_to_icon('TEXTURE'), emboss=True)
        op = row_1F802.operator('sna.my_generic_operator_4a59f', text='清理数据', icon_value=string_to_icon('ORPHAN_DATA'), emboss=True, depress=False)


class SNA_OT_Operator001_1136E(bpy.types.Operator):
    bl_idname = "sna.operator001_1136e"
    bl_label = "Operator.001"
    bl_description = "选中相同材质的物体"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        # 获取当前场景
        scene = bpy.context.scene
        # 获取当前选中的物体
        active_obj = bpy.context.active_object
        # 检查是否有选中物体和它是否有材质
        if active_obj and active_obj.material_slots:
            # 获取选中物体的所有材质
            active_materials = set(slot.material for slot in active_obj.material_slots if slot.material)
            # 遍历场景中的所有物体
            for obj in scene.objects:
                # 只对网格物体进行操作
                if obj.type == 'MESH':
                    # 遍历物体的所有材质插槽
                    for slot in obj.material_slots:
                        # 如果物体使用了与选中物体相同的材质之一
                        if slot.material in active_materials:
                            # 选择物体
                            obj.select_set(True)
                            # 一旦找到匹配的材质，无需检查其余材质
                            break
        else:
            print("No active mesh object with materials selected.")
        # 更新视图层以反映物体的选择变化
        bpy.context.view_layer.update()
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator_5Ed64(bpy.types.Operator):
    bl_idname = "sna.operator_5ed64"
    bl_label = "Operator"
    bl_description = "在材质编辑器中选择一个贴图节点，就选中相同使用了这张贴图的物体"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        import bpy
        # 此函数用于在Blender中显示提示信息

        def show_message_box(message = "", title = "Message Box", icon = 'INFO'):

            def draw(self, context):
                self.layout.label(text=message)
            bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)
        # 使用示例
        show_message_box("未选中纹理节点", "提示", 'ERROR')
        # 初始化变量
        selected_image = None
        node_editor = None
        # 尝试获取当前节点编辑器的上下文
        for area in bpy.context.screen.areas:
            if area.type == 'NODE_EDITOR':
                node_editor = area.spaces.active
                break
        # 如果找到节点编辑器
        if node_editor and node_editor.tree_type == 'ShaderNodeTree' and node_editor.edit_tree:
            # 获取选中的节点
            selected_nodes = [node for node in node_editor.edit_tree.nodes if node.select and node.type == 'TEX_IMAGE']
            # 如果选中了纹理节点，获取它的图像数据
            if selected_nodes:
                selected_image = selected_nodes[0].image
            else:
                show_message_box("未选中纹理节点", "提示", 'ERROR')
        # 如果有选中的纹理
        if selected_image:
            # 遍历所有物体
            for obj in bpy.data.objects:
                # 只检查具有材质的网格物体
                if obj.type == 'MESH' and obj.material_slots:
                    # 遍历所有材质插槽
                    for slot in obj.material_slots:
                        if slot.material and slot.material.use_nodes:
                            # 遍历所有材质节点
                            for node in slot.material.node_tree.nodes:
                                if node.type == 'TEX_IMAGE' and node.image == selected_image:
                                    # 如果该材质使用了选中的纹理，选中物体
                                    obj.select_set(True)
                                    break  # 跳出节点循环
        else:
            print("No texture node selected in the active Node Editor.")
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_My_Generic_Operator_400A9(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_400a9"
    bl_label = "选中骨架"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    def sna_new_property_enum_items(self, context):
        return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]
    sna_new_property: bpy.props.EnumProperty(name='选择', description='', items=[('腿ik骨', '腿ik骨', '', 0, 0), ('全部身体骨', '全部身体骨', '', 0, 1), ('身体骨', '身体骨', '', 0, 2), ('手骨', '手骨', '', 0, 3), ('调整骨', '调整骨', '', 0, 4), ('d骨', 'd骨', '', 0, 5), ('捩骨', '捩骨', '', 0, 6)])

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if self.sna_new_property == "全部身体骨":
            for i_30AF0 in range(len(['足.L', 'ひざ.L', '足首.L', '足先EX.L', '足.R', 'ひざ.R', '足首.R', '足先EX.R'])):
                bpy.ops.object.select_pattern(pattern=['足.L', 'ひざ.L', '足首.L', '足先EX.L', '足.R', 'ひざ.R', '足首.R', '足先EX.R'][i_30AF0])
            for i_FCA08 in range(len(['下半身', '上半身2', '上半身', '上半身3', '首', '頭', '肩.R', '肩.L', '腕.R', '腕.L', 'ひじ.R', 'ひじ.L', '手首.R', '手首.L'])):
                bpy.ops.object.select_pattern(pattern=['下半身', '上半身2', '上半身', '上半身3', '首', '頭', '肩.R', '肩.L', '腕.R', '腕.L', 'ひじ.R', 'ひじ.L', '手首.R', '手首.L'][i_FCA08])
            for i_AA1B7 in range(len(['親指０.R', '親指１.R', '親指２.R', '人指０.R', '人指１.R', '人指２.R', '人指３.R', '中指０.R', '中指１.R', '中指２.R', '中指３.R', '薬指０.R', '薬指１.R', '薬指２.R', '薬指３.R', '小指０.R', '小指１.R', '小指２.R', '小指３.R'])):
                bpy.ops.object.select_pattern(pattern=['親指０.R', '親指１.R', '親指２.R', '人指０.R', '人指１.R', '人指２.R', '人指３.R', '中指０.R', '中指１.R', '中指２.R', '中指３.R', '薬指０.R', '薬指１.R', '薬指２.R', '薬指３.R', '小指０.R', '小指１.R', '小指２.R', '小指３.R'][i_AA1B7])
            for i_844DC in range(len(['親指０.L', '親指１.L', '親指２.L', '人指０.L', '人指１.L', '人指２.L', '人指３.L', '中指０.L', '中指１.L', '中指２.L', '中指３.L', '薬指０.L', '薬指１.L', '薬指２.L', '薬指３.L', '小指０.L', '小指１.L', '小指２.L', '小指３.L'])):
                bpy.ops.object.select_pattern(pattern=['親指０.L', '親指１.L', '親指２.L', '人指０.L', '人指１.L', '人指２.L', '人指３.L', '中指０.L', '中指１.L', '中指２.L', '中指３.L', '薬指０.L', '薬指１.L', '薬指２.L', '薬指３.L', '小指０.L', '小指１.L', '小指２.L', '小指３.L'][i_844DC])
        elif self.sna_new_property == "身体骨":
            for i_1B62D in range(len(['足.L', 'ひざ.L', '足首.L', '足先EX.L', '足.R', 'ひざ.R', '足首.R', '足先EX.R'])):
                bpy.ops.object.select_pattern(pattern=['足.L', 'ひざ.L', '足首.L', '足先EX.L', '足.R', 'ひざ.R', '足首.R', '足先EX.R'][i_1B62D])
            for i_EFC29 in range(len(['下半身', '上半身2', '上半身', '上半身3', '首', '頭', '肩.R', '肩.L', '腕.R', '腕.L', 'ひじ.R', 'ひじ.L', '手首.R', '手首.L'])):
                bpy.ops.object.select_pattern(pattern=['下半身', '上半身2', '上半身', '上半身3', '首', '頭', '肩.R', '肩.L', '腕.R', '腕.L', 'ひじ.R', 'ひじ.L', '手首.R', '手首.L'][i_EFC29])
        elif self.sna_new_property == "腿ik骨":
            for i_FA29C in range(len(['足.L', 'ひざ.L', '足首.L', '足先EX.L', '足.R', 'ひざ.R', '足首.R', '足先EX.R'])):
                bpy.ops.object.select_pattern(pattern=['足.L', 'ひざ.L', '足首.L', '足先EX.L', '足.R', 'ひざ.R', '足首.R', '足先EX.R'][i_FA29C])
        elif self.sna_new_property == "手骨":
            for i_256E3 in range(len(['親指０.R', '親指１.R', '親指２.R', '人指０.R', '人指１.R', '人指２.R', '人指３.R', '中指０.R', '中指１.R', '中指２.R', '中指３.R', '薬指０.R', '薬指１.R', '薬指２.R', '薬指３.R', '小指０.R', '小指１.R', '小指２.R', '小指３.R'])):
                bpy.ops.object.select_pattern(pattern=['親指０.R', '親指１.R', '親指２.R', '人指０.R', '人指１.R', '人指２.R', '人指３.R', '中指０.R', '中指１.R', '中指２.R', '中指３.R', '薬指０.R', '薬指１.R', '薬指２.R', '薬指３.R', '小指０.R', '小指１.R', '小指２.R', '小指３.R'][i_256E3])
            for i_6EC5E in range(len(['親指０.L', '親指１.L', '親指２.L', '人指０.L', '人指１.L', '人指２.L', '人指３.L', '中指０.L', '中指１.L', '中指２.L', '中指３.L', '薬指０.L', '薬指１.L', '薬指２.L', '薬指３.L', '小指０.L', '小指１.L', '小指２.L', '小指３.L'])):
                bpy.ops.object.select_pattern(pattern=['親指０.L', '親指１.L', '親指２.L', '人指０.L', '人指１.L', '人指２.L', '人指３.L', '中指０.L', '中指１.L', '中指２.L', '中指３.L', '薬指０.L', '薬指１.L', '薬指２.L', '薬指３.L', '小指０.L', '小指１.L', '小指２.L', '小指３.L'][i_6EC5E])
        elif self.sna_new_property == "调整骨":
            bpy.ops.object.select_pattern(pattern='*調整*', extend=True)
        elif self.sna_new_property == "d骨":
            for i_A62E2 in range(len(['足D.L', 'ひざD.L', '足首D.L', '足D.R', 'ひざD.R', '足首D.R'])):
                bpy.ops.object.select_pattern(pattern=['足D.L', 'ひざD.L', '足首D.L', '足D.R', 'ひざD.R', '足首D.R'][i_A62E2])
        elif self.sna_new_property == "捩骨":
            bpy.ops.object.select_pattern(pattern='*捩*', extend=True)
        else:
            pass
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_My_Generic_Operator_E6Bd2(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_e6bd2"
    bl_label = "添加顶点色属性"
    bl_description = "为选中的物体添加顶点色"
    bl_options = {"REGISTER", "UNDO"}
    sna_new_property: bpy.props.StringProperty(name='顶点色名称', description='', default='顶点色', subtype='NONE', maxlen=0)

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        node_tree_001['sna_old_active_objects'] = bpy.context.view_layer.objects.active.name
        for i_58412 in range(len(bpy.context.view_layer.objects.selected)):
            bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.selected[i_58412]
            bpy.ops.geometry.color_attribute_add(name=self.sna_new_property, domain='POINT', data_type='FLOAT_COLOR', color=(0.0, 0.0, 0.0, 1.0))
            bpy.context.view_layer.objects.active = bpy.context.view_layer.objects[node_tree_001['sna_old_active_objects']]
            self.report({'INFO'}, message='已添加顶点色')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_My_Generic_Operator_E9B48(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_e9b48"
    bl_label = "移除顶点色属性"
    bl_description = "移除选中物体指定名称的顶点色，如果为空则移除最后一个"
    bl_options = {"REGISTER", "UNDO"}
    sna_new_property: bpy.props.StringProperty(name='删除名称', description='', default='', subtype='NONE', maxlen=0)

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        node_tree_001['sna_old_active_objects'] = bpy.context.view_layer.objects.active.name
        for i_76711 in range(len(bpy.context.view_layer.objects.selected)):
            bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.selected[i_76711]
            if (len(bpy.context.view_layer.objects.active.data.color_attributes) != 0):
                for i_9755E in range(len(bpy.context.view_layer.objects.active.data.color_attributes)-1,-1,-1):
                    if (self.sna_new_property == bpy.context.view_layer.objects.active.data.color_attributes[i_9755E].name):
                        bpy.context.view_layer.objects.active.data.color_attributes.active_color = bpy.context.view_layer.objects.active.data.color_attributes[i_9755E]
                        bpy.ops.geometry.color_attribute_remove('INVOKE_DEFAULT', )
                        bpy.context.view_layer.objects.active = bpy.context.view_layer.objects[node_tree_001['sna_old_active_objects']]
                        self.report({'INFO'}, message='已移除指定名称顶点色')
                if (self.sna_new_property == ''):
                    bpy.context.view_layer.objects.active.data.color_attributes.active_color = bpy.context.view_layer.objects.active.data.color_attributes[int(len(bpy.context.view_layer.objects.active.data.color_attributes) - 1.0)]
                    bpy.ops.geometry.color_attribute_remove('INVOKE_DEFAULT', )
                    bpy.context.view_layer.objects.active = bpy.context.view_layer.objects[node_tree_001['sna_old_active_objects']]
                    self.report({'INFO'}, message='已移除最后一个顶点色')
            else:
                bpy.context.view_layer.objects.active = bpy.context.view_layer.objects[node_tree_001['sna_old_active_objects']]
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_My_Generic_Operator_0C8D6(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_0c8d6"
    bl_label = "快捷键切换中英文"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.sna_new_property_003 = (not bpy.context.scene.sna_new_property_003)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_My_Generic_Operator_4A59F(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_4a59f"
    bl_label = "清理数据"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
        self.report({'INFO'}, message='已清理未使用数据')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_add_to_view3d_mt_select_edit_mesh_C0326(self, context):
    if not (False):
        layout = self.layout
        col_61C3C = layout.column(heading='', align=False)
        col_61C3C.alert = False
        col_61C3C.enabled = True
        col_61C3C.active = True
        col_61C3C.use_property_split = False
        col_61C3C.use_property_decorate = False
        col_61C3C.scale_x = 1.0
        col_61C3C.scale_y = 1.0
        col_61C3C.alignment = 'Expand'.upper()
        col_61C3C.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = col_61C3C.operator('sna.my_generic_operator_acbd7', text='按位置选择顶点', icon_value=0, emboss=True, depress=False)
        op.sna_new_property_002 = 0.0
        op = col_61C3C.operator('sna.my_generic_operator_4bd78', text='按编号选择顶点', icon_value=0, emboss=True, depress=False)
        op.sna_new_property = 0


class SNA_OT_My_Generic_Operator_Acbd7(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_acbd7"
    bl_label = "按位置选择顶点"
    bl_description = "编辑模式中选择顶点"
    bl_options = {"REGISTER", "UNDO"}

    def sna_new_property_enum_items(self, context):
        return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]
    sna_new_property: bpy.props.EnumProperty(name='轴向', description='', items=[('X', 'X', '', 0, 0), ('Y', 'Y', '', 0, 1), ('Z', 'Z', '', 0, 2)])

    def sna_new_property_001_enum_items(self, context):
        return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]
    sna_new_property_001: bpy.props.EnumProperty(name='条件', description='', items=[('大于', '大于', '', 0, 0), ('等于', '等于', '', 0, 1), ('小于', '小于', '', 0, 2)])
    sna_new_property_002: bpy.props.FloatProperty(name='分界', description='', default=0.0, subtype='NONE', unit='NONE', step=3, precision=2)

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (bpy.context.object.mode == 'EDIT'):
            if (bpy.context.active_object.type == 'MESH'):
                bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='OBJECT')
                for i_75CC7 in range(len(bpy.context.active_object.data.vertices)):
                    if (((bpy.context.active_object.data.vertices[i_75CC7].co[0] if (self.sna_new_property == 'X') else (bpy.context.active_object.data.vertices[i_75CC7].co[1] if ('Y' == self.sna_new_property) else (bpy.context.active_object.data.vertices[i_75CC7].co[2] if (self.sna_new_property == 'Z') else None))) > self.sna_new_property_002) if (self.sna_new_property_001 == '大于') else (((bpy.context.active_object.data.vertices[i_75CC7].co[0] if (self.sna_new_property == 'X') else (bpy.context.active_object.data.vertices[i_75CC7].co[1] if ('Y' == self.sna_new_property) else (bpy.context.active_object.data.vertices[i_75CC7].co[2] if (self.sna_new_property == 'Z') else None))) == self.sna_new_property_002) if ('等于' == self.sna_new_property_001) else (((bpy.context.active_object.data.vertices[i_75CC7].co[0] if (self.sna_new_property == 'X') else (bpy.context.active_object.data.vertices[i_75CC7].co[1] if ('Y' == self.sna_new_property) else (bpy.context.active_object.data.vertices[i_75CC7].co[2] if (self.sna_new_property == 'Z') else None))) < self.sna_new_property_002) if (self.sna_new_property_001 == '小于') else None))):
                        bpy.context.active_object.data.vertices[i_75CC7].select = True
                result_1E786 = bpy.context.active_object.update_from_editmode()
                bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='EDIT')
            else:
                self.report({'INFO'}, message='所选不是网格')
        else:
            self.report({'INFO'}, message='不在编辑模式')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_My_Generic_Operator_4Bd78(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_4bd78"
    bl_label = "按编号选择顶点"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}
    sna_new_property: bpy.props.IntProperty(name='编号', description='', default=0, subtype='NONE', min=0)

    def sna_new_property_001_enum_items(self, context):
        return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]
    sna_new_property_001: bpy.props.EnumProperty(name='条件', description='', items=[('等于', '等于', '', 0, 0), ('大于', '大于', '', 0, 1), ('小于', '小于', '', 0, 2)])

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (bpy.context.object.mode == 'EDIT'):
            if (bpy.context.active_object.type == 'MESH'):
                bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='OBJECT')
                for i_863A2 in range(len(bpy.context.active_object.data.vertices)):
                    if ((i_863A2 == self.sna_new_property) if (self.sna_new_property_001 == '等于') else ((i_863A2 > self.sna_new_property) if ('大于' == self.sna_new_property_001) else ((i_863A2 < self.sna_new_property) if ('小于' == self.sna_new_property_001) else None))):
                        bpy.context.active_object.data.vertices[i_863A2].select = True
                result_05FA6 = bpy.context.active_object.update_from_editmode()
                bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='EDIT')
            else:
                self.report({'INFO'}, message='所选不是网格')
        else:
            self.report({'INFO'}, message='不在编辑模式')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_add_to_view3d_mt_edit_mesh_context_menu_48850(self, context):
    if not (False):
        layout = self.layout
        op = layout.operator('sna.my_generic_operator_c68a2', text='原点到选中项', icon_value=0, emboss=True, depress=False)


class SNA_OT_My_Generic_Operator_C68A2(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_c68a2"
    bl_label = "原点到选中项"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected('INVOKE_DEFAULT', )
        bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='OBJECT')
        bpy.ops.object.origin_set('INVOKE_DEFAULT', type='ORIGIN_CURSOR')
        bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='EDIT')
        bpy.ops.view3d.snap_cursor_to_center('INVOKE_DEFAULT', )
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_add_to_view3d_mt_edit_mesh_vertices_D20F4(self, context):
    if not (False):
        layout = self.layout
        op = layout.operator('sna.my_generic_operator_32f6a', text='对称两个顶点', icon_value=0, emboss=True, depress=False)
        op.sna_new_property = 'X'
        op.sna_new_property_001 = '第一个顶点'


class SNA_OT_My_Generic_Operator_32F6A(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_32f6a"
    bl_label = "对称两个顶点"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    def sna_new_property_enum_items(self, context):
        return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]
    sna_new_property: bpy.props.EnumProperty(name='轴向', description='', items=[('X', 'X', '', 0, 0), ('Y', 'Y', '', 0, 1), ('Z', 'Z', '', 0, 2)])

    def sna_new_property_001_enum_items(self, context):
        return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]
    sna_new_property_001: bpy.props.EnumProperty(name='方式', description='', items=[('第一个顶点', '第一个顶点', '', 0, 0), ('第二个顶点', '第二个顶点', '', 0, 1), ('平均', '平均', '', 0, 2)])

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        node_tree_004['sna_select_ver'] = []
        node_tree_004['sna_select_ver_pos'] = []
        if (bpy.context.object.mode == 'EDIT'):
            if (bpy.context.active_object.type == 'MESH'):
                bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='OBJECT')
                for i_581AD in range(len(bpy.context.active_object.data.vertices)):
                    if bpy.context.active_object.data.vertices[i_581AD].select:
                        node_tree_004['sna_select_ver'].append(i_581AD)
                    if (len(node_tree_004['sna_select_ver']) > 2):
                        self.report({'WARNING'}, message='没有选中两个顶点')
                        break
                if (len(node_tree_004['sna_select_ver']) == 2):
                    node_tree_004['sna_select_ver_pos'].append(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co)
                    node_tree_004['sna_select_ver_pos'].append(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][1]].co)
                    if property_exists("bpy.context.active_object.data.shape_keys.key_blocks[0]", globals(), locals()):
                        if self.sna_new_property_001 == "平均":
                            bpy.context.active_object.data.shape_keys.key_blocks[0].data[node_tree_004['sna_select_ver'][0]].co = (((eval("(sna_absin_C9F6D_46D54(node_tree_004['sna_select_ver_pos'][0][0]) + sna_absin_C9F6D_E198F(node_tree_004['sna_select_ver_pos'][1][0]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'X') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(sna_absin_C9F6D_CCBBB(node_tree_004['sna_select_ver_pos'][0][1]) + sna_absin_C9F6D_880B5(node_tree_004['sna_select_ver_pos'][1][1]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'Y') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(sna_absin_C9F6D_724FA(node_tree_004['sna_select_ver_pos'][0][2]) + sna_absin_C9F6D_188B6(node_tree_004['sna_select_ver_pos'][1][2]))/2")) if (self.sna_new_property == 'Z') else None))) if ((node_tree_004['sna_select_ver_pos'][0][0] > node_tree_004['sna_select_ver_pos'][1][0]) if (self.sna_new_property == 'X') else ((node_tree_004['sna_select_ver_pos'][0][1] > node_tree_004['sna_select_ver_pos'][1][1]) if (self.sna_new_property == 'Y') else ((node_tree_004['sna_select_ver_pos'][0][2] > node_tree_004['sna_select_ver_pos'][1][2]) if (self.sna_new_property == 'Z') else None))) else (tuple(mathutils.Vector(((eval("(sna_absin_C9F6D_46D54(node_tree_004['sna_select_ver_pos'][0][0]) + sna_absin_C9F6D_E198F(node_tree_004['sna_select_ver_pos'][1][0]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'X') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(sna_absin_C9F6D_CCBBB(node_tree_004['sna_select_ver_pos'][0][1]) + sna_absin_C9F6D_880B5(node_tree_004['sna_select_ver_pos'][1][1]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'Y') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(sna_absin_C9F6D_724FA(node_tree_004['sna_select_ver_pos'][0][2]) + sna_absin_C9F6D_188B6(node_tree_004['sna_select_ver_pos'][1][2]))/2")) if (self.sna_new_property == 'Z') else None)))) * mathutils.Vector((-1.0, 1.0, 1.0))) if (self.sna_new_property == 'X') else (tuple(mathutils.Vector(((eval("(sna_absin_C9F6D_46D54(node_tree_004['sna_select_ver_pos'][0][0]) + sna_absin_C9F6D_E198F(node_tree_004['sna_select_ver_pos'][1][0]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'X') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(sna_absin_C9F6D_CCBBB(node_tree_004['sna_select_ver_pos'][0][1]) + sna_absin_C9F6D_880B5(node_tree_004['sna_select_ver_pos'][1][1]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'Y') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(sna_absin_C9F6D_724FA(node_tree_004['sna_select_ver_pos'][0][2]) + sna_absin_C9F6D_188B6(node_tree_004['sna_select_ver_pos'][1][2]))/2")) if (self.sna_new_property == 'Z') else None)))) * mathutils.Vector((1.0, -1.0, 1.0))) if (self.sna_new_property == 'Y') else (tuple(mathutils.Vector(((eval("(sna_absin_C9F6D_46D54(node_tree_004['sna_select_ver_pos'][0][0]) + sna_absin_C9F6D_E198F(node_tree_004['sna_select_ver_pos'][1][0]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'X') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(sna_absin_C9F6D_CCBBB(node_tree_004['sna_select_ver_pos'][0][1]) + sna_absin_C9F6D_880B5(node_tree_004['sna_select_ver_pos'][1][1]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'Y') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(sna_absin_C9F6D_724FA(node_tree_004['sna_select_ver_pos'][0][2]) + sna_absin_C9F6D_188B6(node_tree_004['sna_select_ver_pos'][1][2]))/2")) if (self.sna_new_property == 'Z') else None)))) * mathutils.Vector((1.0, 1.0, -1.0))) if (self.sna_new_property == 'Z') else None))))
                            bpy.context.active_object.data.shape_keys.key_blocks[0].data[node_tree_004['sna_select_ver'][1]].co = (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co) * mathutils.Vector((-1.0, 1.0, 1.0))) if (self.sna_new_property == 'X') else (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co) * mathutils.Vector((1.0, -1.0, 1.0))) if (self.sna_new_property == 'Y') else (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co) * mathutils.Vector((1.0, 1.0, -1.0))) if (self.sna_new_property == 'Z') else None)))
                        elif self.sna_new_property_001 == "第一个顶点":
                            bpy.context.active_object.data.shape_keys.key_blocks[0].data[node_tree_004['sna_select_ver'][1]].co = (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co) * mathutils.Vector((-1.0, 1.0, 1.0))) if (self.sna_new_property == 'X') else (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co) * mathutils.Vector((1.0, -1.0, 1.0))) if (self.sna_new_property == 'Y') else (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co) * mathutils.Vector((1.0, 1.0, -1.0))) if (self.sna_new_property == 'Z') else None)))
                        elif self.sna_new_property_001 == "第二个顶点":
                            bpy.context.active_object.data.shape_keys.key_blocks[0].data[node_tree_004['sna_select_ver'][0]].co = (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][1]].co) * mathutils.Vector((-1.0, 1.0, 1.0))) if (self.sna_new_property == 'X') else (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][1]].co) * mathutils.Vector((1.0, -1.0, 1.0))) if (self.sna_new_property == 'Y') else (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][1]].co) * mathutils.Vector((1.0, 1.0, -1.0))) if (self.sna_new_property == 'Z') else None)))
                        else:
                            pass
                    else:
                        if self.sna_new_property_001 == "平均":
                            bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co = (((eval("(sna_absin_C9F6D_46D54(node_tree_004['sna_select_ver_pos'][0][0]) + sna_absin_C9F6D_E198F(node_tree_004['sna_select_ver_pos'][1][0]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'X') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(sna_absin_C9F6D_CCBBB(node_tree_004['sna_select_ver_pos'][0][1]) + sna_absin_C9F6D_880B5(node_tree_004['sna_select_ver_pos'][1][1]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'Y') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(sna_absin_C9F6D_724FA(node_tree_004['sna_select_ver_pos'][0][2]) + sna_absin_C9F6D_188B6(node_tree_004['sna_select_ver_pos'][1][2]))/2")) if (self.sna_new_property == 'Z') else None))) if ((node_tree_004['sna_select_ver_pos'][0][0] > node_tree_004['sna_select_ver_pos'][1][0]) if (self.sna_new_property == 'X') else ((node_tree_004['sna_select_ver_pos'][0][1] > node_tree_004['sna_select_ver_pos'][1][1]) if (self.sna_new_property == 'Y') else ((node_tree_004['sna_select_ver_pos'][0][2] > node_tree_004['sna_select_ver_pos'][1][2]) if (self.sna_new_property == 'Z') else None))) else (tuple(mathutils.Vector(((eval("(sna_absin_C9F6D_46D54(node_tree_004['sna_select_ver_pos'][0][0]) + sna_absin_C9F6D_E198F(node_tree_004['sna_select_ver_pos'][1][0]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'X') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(sna_absin_C9F6D_CCBBB(node_tree_004['sna_select_ver_pos'][0][1]) + sna_absin_C9F6D_880B5(node_tree_004['sna_select_ver_pos'][1][1]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'Y') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(sna_absin_C9F6D_724FA(node_tree_004['sna_select_ver_pos'][0][2]) + sna_absin_C9F6D_188B6(node_tree_004['sna_select_ver_pos'][1][2]))/2")) if (self.sna_new_property == 'Z') else None)))) * mathutils.Vector((-1.0, 1.0, 1.0))) if (self.sna_new_property == 'X') else (tuple(mathutils.Vector(((eval("(sna_absin_C9F6D_46D54(node_tree_004['sna_select_ver_pos'][0][0]) + sna_absin_C9F6D_E198F(node_tree_004['sna_select_ver_pos'][1][0]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'X') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(sna_absin_C9F6D_CCBBB(node_tree_004['sna_select_ver_pos'][0][1]) + sna_absin_C9F6D_880B5(node_tree_004['sna_select_ver_pos'][1][1]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'Y') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(sna_absin_C9F6D_724FA(node_tree_004['sna_select_ver_pos'][0][2]) + sna_absin_C9F6D_188B6(node_tree_004['sna_select_ver_pos'][1][2]))/2")) if (self.sna_new_property == 'Z') else None)))) * mathutils.Vector((1.0, -1.0, 1.0))) if (self.sna_new_property == 'Y') else (tuple(mathutils.Vector(((eval("(sna_absin_C9F6D_46D54(node_tree_004['sna_select_ver_pos'][0][0]) + sna_absin_C9F6D_E198F(node_tree_004['sna_select_ver_pos'][1][0]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'X') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(sna_absin_C9F6D_CCBBB(node_tree_004['sna_select_ver_pos'][0][1]) + sna_absin_C9F6D_880B5(node_tree_004['sna_select_ver_pos'][1][1]))/2"), eval("(node_tree_004['sna_select_ver_pos'][0][2] + node_tree_004['sna_select_ver_pos'][1][2])/2")) if (self.sna_new_property == 'Y') else ((eval("(node_tree_004['sna_select_ver_pos'][0][0] + node_tree_004['sna_select_ver_pos'][1][0])/2"), eval("(node_tree_004['sna_select_ver_pos'][0][1] + node_tree_004['sna_select_ver_pos'][1][1])/2"), eval("(sna_absin_C9F6D_724FA(node_tree_004['sna_select_ver_pos'][0][2]) + sna_absin_C9F6D_188B6(node_tree_004['sna_select_ver_pos'][1][2]))/2")) if (self.sna_new_property == 'Z') else None)))) * mathutils.Vector((1.0, 1.0, -1.0))) if (self.sna_new_property == 'Z') else None))))
                            bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][1]].co = (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co) * mathutils.Vector((-1.0, 1.0, 1.0))) if (self.sna_new_property == 'X') else (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co) * mathutils.Vector((1.0, -1.0, 1.0))) if (self.sna_new_property == 'Y') else (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co) * mathutils.Vector((1.0, 1.0, -1.0))) if (self.sna_new_property == 'Z') else None)))
                        elif self.sna_new_property_001 == "第一个顶点":
                            bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][1]].co = (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co) * mathutils.Vector((-1.0, 1.0, 1.0))) if (self.sna_new_property == 'X') else (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co) * mathutils.Vector((1.0, -1.0, 1.0))) if (self.sna_new_property == 'Y') else (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co) * mathutils.Vector((1.0, 1.0, -1.0))) if (self.sna_new_property == 'Z') else None)))
                        elif self.sna_new_property_001 == "第二个顶点":
                            bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][0]].co = (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][1]].co) * mathutils.Vector((-1.0, 1.0, 1.0))) if (self.sna_new_property == 'X') else (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][1]].co) * mathutils.Vector((1.0, -1.0, 1.0))) if (self.sna_new_property == 'Y') else (tuple(mathutils.Vector(bpy.context.active_object.data.vertices[node_tree_004['sna_select_ver'][1]].co) * mathutils.Vector((1.0, 1.0, -1.0))) if (self.sna_new_property == 'Z') else None)))
                        else:
                            pass
                else:
                    self.report({'WARNING'}, message='没有选中两个顶点')
                bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='EDIT')
            else:
                self.report({'INFO'}, message='所选不是网格')
        else:
            self.report({'INFO'}, message='不在编辑模式')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_My_Generic_Operator_16Cb7(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_16cb7"
    bl_label = "对齐物体"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}
    sna_new_property: bpy.props.BoolProperty(name='位置', description='', default=False)
    sna_new_property_001: bpy.props.BoolProperty(name='旋转', description='', default=False)
    sna_new_property_002: bpy.props.BoolProperty(name='缩放', description='', default=False)

    def sna_new_property_003_enum_items(self, context):
        return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]
    sna_new_property_003: bpy.props.EnumProperty(name='轴向', description='', items=[('全部', '全部', '', 0, 0), ('X', 'X', '', 0, 1), ('Y', 'Y', '', 0, 2), ('Z', 'Z', '', 0, 3), ('YZ', 'YZ', '', 0, 4), ('XZ', 'XZ', '', 0, 5), ('XY', 'XY', '', 0, 6)])

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_D0D1D in range(len(bpy.context.selected_objects)):
            if (bpy.context.selected_objects[i_D0D1D].name != bpy.context.active_object.name):
                if self.sna_new_property:
                    bpy.context.selected_objects[i_D0D1D].location = ((bpy.context.active_object.location[0], bpy.context.active_object.location[1], bpy.context.active_object.location[2]) if (self.sna_new_property_003 == '全部') else ((bpy.context.active_object.location[0], 0.0, 0.0) if (self.sna_new_property_003 == 'X') else ((0.0, bpy.context.active_object.location[1], 0.0) if (self.sna_new_property_003 == 'Y') else ((0.0, 0.0, bpy.context.active_object.location[2]) if (self.sna_new_property_003 == 'Z') else ((0.0, bpy.context.active_object.location[1], bpy.context.active_object.location[2]) if (self.sna_new_property_003 == 'YZ') else ((bpy.context.active_object.location[0], 0.0, bpy.context.active_object.location[2]) if (self.sna_new_property_003 == 'XZ') else ((bpy.context.active_object.location[0], bpy.context.active_object.location[1], 0.0) if (self.sna_new_property_003 == 'XY') else None)))))))
                if self.sna_new_property_001:
                    bpy.context.selected_objects[i_D0D1D].rotation_euler = ((bpy.context.active_object.rotation_euler[0], bpy.context.active_object.rotation_euler[1], bpy.context.active_object.rotation_euler[2]) if (self.sna_new_property_003 == '全部') else ((bpy.context.active_object.rotation_euler[0], 0.0, 0.0) if (self.sna_new_property_003 == 'X') else ((0.0, bpy.context.active_object.rotation_euler[1], 0.0) if (self.sna_new_property_003 == 'Y') else ((0.0, 0.0, bpy.context.active_object.rotation_euler[2]) if (self.sna_new_property_003 == 'Z') else ((0.0, bpy.context.active_object.rotation_euler[1], bpy.context.active_object.rotation_euler[2]) if (self.sna_new_property_003 == 'YZ') else ((bpy.context.active_object.rotation_euler[0], 0.0, bpy.context.active_object.rotation_euler[2]) if (self.sna_new_property_003 == 'XZ') else ((bpy.context.active_object.rotation_euler[0], bpy.context.active_object.rotation_euler[1], 0.0) if (self.sna_new_property_003 == 'XY') else None)))))))
                if self.sna_new_property_002:
                    bpy.context.selected_objects[i_D0D1D].scale = ((bpy.context.active_object.scale[0], bpy.context.active_object.scale[1], bpy.context.active_object.scale[2]) if (self.sna_new_property_003 == '全部') else ((bpy.context.active_object.scale[0], 0.0, 0.0) if (self.sna_new_property_003 == 'X') else ((0.0, bpy.context.active_object.scale[1], 0.0) if (self.sna_new_property_003 == 'Y') else ((0.0, 0.0, bpy.context.active_object.scale[2]) if (self.sna_new_property_003 == 'Z') else ((0.0, bpy.context.active_object.scale[1], bpy.context.active_object.scale[2]) if (self.sna_new_property_003 == 'YZ') else ((bpy.context.active_object.scale[0], 0.0, bpy.context.active_object.scale[2]) if (self.sna_new_property_003 == 'XZ') else ((bpy.context.active_object.scale[0], bpy.context.active_object.scale[1], 0.0) if (self.sna_new_property_003 == 'XY') else None)))))))
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_add_to_view3d_mt_transform_object_E49E0(self, context):
    if not (False):
        layout = self.layout
        op = layout.operator('sna.my_generic_operator_16cb7', text='对齐物体到活动项', icon_value=0, emboss=True, depress=False)
        op.sna_new_property = True
        op.sna_new_property_001 = False
        op.sna_new_property_002 = False


class SNA_OT_My_Generic_Operator_A5A90(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_a5a90"
    bl_label = "批量传递形态键"
    bl_description = "将形态键复制到激活物体(按编号传递位置)"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        node_tree_005['sna_act_obj'] = None
        node_tree_005['sna_base_obj'] = None
        for i_192DE in range(len(bpy.context.selected_objects)):
            if (bpy.context.selected_objects[i_192DE].name == bpy.context.active_object.name):
                node_tree_005['sna_act_obj'] = bpy.context.selected_objects[i_192DE]
            else:
                node_tree_005['sna_base_obj'] = bpy.context.selected_objects[i_192DE]
        if (node_tree_005['sna_act_obj'] != None):
            if (node_tree_005['sna_base_obj'] != None):
                if (node_tree_005['sna_act_obj'].data.shape_keys == None):
                    bpy.ops.object.shape_key_add('INVOKE_DEFAULT', )
                for i_35552 in range(len(node_tree_005['sna_base_obj'].data.shape_keys.key_blocks)):
                    node_tree_005['sna_base_obj'].active_shape_key_index = i_35552
                    if (i_35552 != 0):
                        print(node_tree_005['sna_base_obj'].active_shape_key.name)
                        bpy.ops.object.shape_key_transfer('INVOKE_DEFAULT', )
                        node_tree_005['sna_act_obj'].show_only_shape_key = False
            else:
                self.report({'INFO'}, message='形态键来源物体为空')
        else:
            self.report({'INFO'}, message='活动物体为空')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_add_to_mesh_mt_shape_key_context_menu_B7E3D(self, context):
    if not (False):
        layout = self.layout
        op = layout.operator('sna.my_generic_operator_a5a90', text='传递所有形态键', icon_value=string_to_icon('CHECKMARK'), emboss=True, depress=False)


def sna_add_to_data_pt_modifiers_55FB3(self, context):
    if not (False):
        layout = self.layout
        box_34AAE = layout.box()
        box_34AAE.alert = False
        box_34AAE.enabled = True
        box_34AAE.active = True
        box_34AAE.use_property_split = False
        box_34AAE.use_property_decorate = False
        box_34AAE.alignment = 'Expand'.upper()
        box_34AAE.scale_x = 1.0
        box_34AAE.scale_y = 1.0
        if not True: box_34AAE.operator_context = "EXEC_DEFAULT"
        col_6D143 = box_34AAE.column(heading='', align=False)
        col_6D143.alert = False
        col_6D143.enabled = True
        col_6D143.active = True
        col_6D143.use_property_split = False
        col_6D143.use_property_decorate = False
        col_6D143.scale_x = 1.0
        col_6D143.scale_y = 1.0
        col_6D143.alignment = 'Expand'.upper()
        col_6D143.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_15203 = col_6D143.row(heading='', align=False)
        row_15203.alert = False
        row_15203.enabled = True
        row_15203.active = True
        row_15203.use_property_split = False
        row_15203.use_property_decorate = False
        row_15203.scale_x = 1.0
        row_15203.scale_y = 1.0
        row_15203.alignment = 'Expand'.upper()
        row_15203.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_15203.operator('object.modifier_add', text='几何节点', icon_value=string_to_icon('GEOMETRY_NODES'), emboss=True, depress=False)
        op.type = 'NODES'
        op = row_15203.operator('object.modifier_add', text='遮罩', icon_value=string_to_icon('MOD_MASK'), emboss=True, depress=False)
        op.type = 'MASK'
        op = row_15203.operator('object.modifier_add', text='镜像', icon_value=string_to_icon('MOD_MIRROR'), emboss=True, depress=False)
        op.type = 'MIRROR'
        op = row_15203.operator('object.modifier_add', text='细分', icon_value=string_to_icon('MOD_SUBSURF'), emboss=True, depress=False)
        op.type = 'SUBSURF'
        row_49F3B = col_6D143.row(heading='', align=False)
        row_49F3B.alert = False
        row_49F3B.enabled = True
        row_49F3B.active = True
        row_49F3B.use_property_split = False
        row_49F3B.use_property_decorate = False
        row_49F3B.scale_x = 1.0
        row_49F3B.scale_y = 1.0
        row_49F3B.alignment = 'Expand'.upper()
        row_49F3B.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_49F3B.operator('object.modifier_add', text='实体化', icon_value=string_to_icon('MOD_SOLIDIFY'), emboss=True, depress=False)
        op.type = 'SOLIDIFY'
        op = row_49F3B.operator('object.modifier_add', text='焊接', icon_value=string_to_icon('AUTOMERGE_OFF'), emboss=True, depress=False)
        op.type = 'WELD'
        op = row_49F3B.operator('object.modifier_add', text='骨架', icon_value=string_to_icon('MOD_ARMATURE'), emboss=True, depress=False)
        op.type = 'ARMATURE'
        op = row_49F3B.operator('object.modifier_add', text='矫正平滑', icon_value=string_to_icon('MOD_SMOOTH'), emboss=True, depress=False)
        op.type = 'CORRECTIVE_SMOOTH'
        row_4E969 = col_6D143.row(heading='', align=False)
        row_4E969.alert = False
        row_4E969.enabled = True
        row_4E969.active = True
        row_4E969.use_property_split = False
        row_4E969.use_property_decorate = False
        row_4E969.scale_x = 1.0
        row_4E969.scale_y = 1.0
        row_4E969.alignment = 'Expand'.upper()
        row_4E969.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_4E969.operator('object.modifier_add', text='数据传递', icon_value=string_to_icon('MESH_DATA'), emboss=True, depress=False)
        op.type = 'DATA_TRANSFER'
        op = row_4E969.operator('object.modifier_add', text='精简', icon_value=string_to_icon('MOD_DECIM'), emboss=True, depress=False)
        op.type = 'DECIMATE'
        op = row_4E969.operator('object.modifier_add', text='倒角', icon_value=string_to_icon('MOD_BEVEL'), emboss=True, depress=False)
        op.type = 'BEVEL'
        op = row_4E969.operator('object.modifier_add', text='缩裹', icon_value=string_to_icon('MOD_SHRINKWRAP'), emboss=True, depress=False)
        op.type = 'SHRINKWRAP'


class SNA_OT_Down_25Ee0(bpy.types.Operator):
    bl_idname = "sna.down_25ee0"
    bl_label = "down"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (float(len(bpy.context.scene.sna_render_list) - 1.0) == bpy.context.scene.sna_render_list_id):
            pass
        else:
            bpy.context.scene.sna_render_list.move(bpy.context.scene.sna_render_list_id, int(bpy.context.scene.sna_render_list_id + 1.0))
            item_CA05D = bpy.context.scene.sna_render_list[int(bpy.context.scene.sna_render_list_id + 1.0)]
            bpy.context.scene.sna_render_list_id = int(bpy.context.scene.sna_render_list_id + 1.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Up_B66Ca(bpy.types.Operator):
    bl_idname = "sna.up_b66ca"
    bl_label = "up"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (bpy.context.scene.sna_render_list_id == 0):
            pass
        else:
            bpy.context.scene.sna_render_list.move(bpy.context.scene.sna_render_list_id, int(bpy.context.scene.sna_render_list_id - 1.0))
            item_BA94F = bpy.context.scene.sna_render_list[int(bpy.context.scene.sna_render_list_id - 1.0)]
            bpy.context.scene.sna_render_list_id = int(bpy.context.scene.sna_render_list_id - 1.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Add_Render_List_84292(bpy.types.Operator):
    bl_idname = "sna.add_render_list_84292"
    bl_label = "add_render_list"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        item_D5070 = bpy.context.scene.sna_render_list.add()
        item_D5070.name = '渲染任务' + str(len(bpy.context.scene.sna_render_list))
        item_D5070.start_frame = bpy.context.scene.frame_start
        item_D5070.end_frame = bpy.context.scene.frame_end
        bpy.context.scene.sna_render_list_id = int(len(bpy.context.scene.sna_render_list) - 1.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Remove_Render_List_E8059(bpy.types.Operator):
    bl_idname = "sna.remove_render_list_e8059"
    bl_label = "remove_render_list"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (int(len(bpy.context.scene.sna_render_list) - 1.0) == bpy.context.scene.sna_render_list_id):
            if len(bpy.context.scene.sna_render_list) > bpy.context.scene.sna_render_list_id:
                bpy.context.scene.sna_render_list.remove(bpy.context.scene.sna_render_list_id)
            bpy.context.scene.sna_render_list_id = int(len(bpy.context.scene.sna_render_list) - 1.0)
        else:
            if len(bpy.context.scene.sna_render_list) > bpy.context.scene.sna_render_list_id:
                bpy.context.scene.sna_render_list.remove(bpy.context.scene.sna_render_list_id)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_My_Generic_Operator_5874F(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_5874f"
    bl_label = "渲染"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.ops.sna.my_generic_operator_33f13('INVOKE_DEFAULT', )
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


@persistent
def render_complete_handler_825EB(dummy):
    if bpy.context.preferences.addons['mmd_quick_tool'].preferences.sna_new_property_004:
        if bpy.context.scene.sna_is_render:
            bpy.context.scene.sna_render_list_id = int(bpy.context.scene.sna_render_list_id + 1.0)
            for i_D5DFF in range(len(bpy.context.scene.sna_render_list)):
                if (bpy.context.scene.sna_render_list[i_D5DFF].on and (i_D5DFF >= bpy.context.scene.sna_render_list_id)):
                    bpy.context.scene.sna_render_list_id = i_D5DFF
                    break

            def delayed_3D3B7():
                bpy.context.scene.sna_is_render = False
                if bpy.context.scene.sna_render_list[bpy.context.scene.sna_render_list_id].on:
                    bpy.context.scene.frame_start = bpy.context.scene.sna_render_list[bpy.context.scene.sna_render_list_id].start_frame
                    bpy.context.scene.frame_end = bpy.context.scene.sna_render_list[bpy.context.scene.sna_render_list_id].end_frame
                    bpy.context.scene.camera = (bpy.data.objects[node_tree_001['sna_default_camera']] if (bpy.context.scene.sna_render_list[bpy.context.scene.sna_render_list_id].render_camera == None) else bpy.context.scene.sna_render_list[bpy.context.scene.sna_render_list_id].render_camera)
                    bpy.context.scene.render.filepath = (node_tree_001['sna_default_output_directory'] if (bpy.context.scene.sna_render_list[bpy.context.scene.sna_render_list_id].output_directory == '') else bpy.context.scene.sna_render_list[bpy.context.scene.sna_render_list_id].output_directory)
                    bpy.context.scene.sna_is_render = True
                    bpy.ops.render.render('INVOKE_DEFAULT', animation=True, use_viewport=True)
                else:

                    def delayed_C1A0C():
                        bpy.context.scene.frame_start = node_tree_001['sna_default_frame_start']
                        bpy.context.scene.frame_end = node_tree_001['sna_default_frame_end']
                        bpy.context.scene.camera = bpy.context.view_layer.objects[node_tree_001['sna_default_camera']]

                        def delayed_F65CF():
                            bpy.context.scene.render.filepath = node_tree_001['sna_default_output_directory']
                            bpy.context.scene.sna_is_render = False
                        bpy.app.timers.register(delayed_F65CF, first_interval=0.5)
                    bpy.app.timers.register(delayed_C1A0C, first_interval=1.0)
            bpy.app.timers.register(delayed_3D3B7, first_interval=0.30000001192092896)


@persistent
def render_complete_handler_C420C(dummy):
    pass


class SNA_OT_My_Generic_Operator_33F13(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_33f13"
    bl_label = "开始渲染"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        node_tree_001['sna_default_frame_start'] = bpy.context.scene.frame_start
        node_tree_001['sna_default_frame_end'] = bpy.context.scene.frame_end
        node_tree_001['sna_default_camera'] = bpy.context.scene.camera.name
        node_tree_001['sna_default_output_directory'] = bpy.context.scene.render.filepath
        for i_ACDF3 in range(len(bpy.context.scene.sna_render_list)):
            if bpy.context.scene.sna_render_list[i_ACDF3].on:
                print(str(i_ACDF3))
                bpy.context.scene.sna_render_list_id = i_ACDF3
                break
        bpy.context.scene.frame_start = bpy.context.scene.sna_render_list[bpy.context.scene.sna_render_list_id].start_frame
        bpy.context.scene.frame_end = bpy.context.scene.sna_render_list[bpy.context.scene.sna_render_list_id].end_frame
        bpy.context.scene.camera = (bpy.context.scene.camera if (bpy.context.scene.sna_render_list[bpy.context.scene.sna_render_list_id].render_camera == None) else bpy.context.scene.sna_render_list[bpy.context.scene.sna_render_list_id].render_camera)
        bpy.context.scene.render.filepath = (node_tree_001['sna_default_output_directory'] if (bpy.context.scene.sna_render_list[bpy.context.scene.sna_render_list_id].output_directory == '') else bpy.context.scene.sna_render_list[bpy.context.scene.sna_render_list_id].output_directory)
        bpy.context.scene.sna_is_render = True
        bpy.ops.render.render('INVOKE_DEFAULT', animation=True, use_viewport=True)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


@persistent
def render_cancel_handler_58683(dummy):
    if bpy.context.preferences.addons['mmd_quick_tool'].preferences.sna_new_property_004:
        bpy.context.scene.sna_is_render = False


# @persistent
# def render_post_handler_4E079(dummy):
#     if bpy.context.preferences.addons['mmd_quick_tool'].preferences.sna_new_property_004:
#         render_list = bpy.context.scene.sna_render_list
#         if not render_list:
#             return
#         if render_list[-1].end_frame == bpy.context.scene.frame_current:
#             bpy.context.scene.sna_is_render = False
@persistent
def render_post_handler_4E079(dummy):
    # 检查插件偏好设置是否启用该功能
    if not bpy.context.preferences.addons['mmd_quick_tool'].preferences.sna_new_property_004:
        return

    render_list = bpy.context.scene.sna_render_list
    # 如果渲染列表为空，直接退出
    if not render_list:
        return

    # 安全获取最后一个任务
    last_task = render_list[-1]
    if last_task.end_frame == bpy.context.scene.frame_current:
        bpy.context.scene.sna_is_render = False



class SNA_OT_My_Generic_Operator_2032A(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_2032a"
    bl_label = "设置时间段"
    bl_description = "设置开始和结束帧为任务帧"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.frame_start = bpy.context.scene.sna_render_list[bpy.context.scene.sna_render_list_id].start_frame
        bpy.context.scene.frame_end = bpy.context.scene.sna_render_list[bpy.context.scene.sna_render_list_id].end_frame
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_get_now_timein_D4FB8():
    return [float(int(datetime.now().time().hour * 3600.0) + int(datetime.now().time().minute * 60.0) + datetime.now().time().second + float(datetime.now().time().microsecond//1000 / 1000.0)), int(int(datetime.now().time().hour * 3600.0) + int(datetime.now().time().minute * 60.0) + datetime.now().time().second + float(datetime.now().time().microsecond//1000 / 1000.0))]


@persistent
def render_pre_handler_7F068(dummy):
    if bpy.context.preferences.addons['mmd_quick_tool'].preferences.sna_new_property_004:
        if bpy.context.scene.sna_is_render:
            float_0_7aafa, int_1_7aafa = sna_get_now_timein_D4FB8()
            node_tree_001['sna_render_start_time'] = float_0_7aafa


@persistent
def render_post_handler_53081(dummy):
    if bpy.context.preferences.addons['mmd_quick_tool'].preferences.sna_new_property_004:
        if bpy.context.scene.sna_is_render:
            float_0_8a9fd, int_1_8a9fd = sna_get_now_timein_D4FB8()
            node_tree_001['sna_render_end_time'] = float_0_8a9fd
            node_tree_001['sna_sna_new_variable'].append(round(float(node_tree_001['sna_render_end_time'] - node_tree_001['sna_render_start_time']), abs(2)))
            node_tree_001['sna_sub_render_time'] = 0.0
            node_tree_001['sna_avg_render_time'] = 0.0
            if (len(node_tree_001['sna_sna_new_variable']) > 5):
                node_tree_001['sna_sna_new_variable'].pop(0)
            for i_073C1 in range(len(node_tree_001['sna_sna_new_variable'])):
                node_tree_001['sna_sub_render_time'] = round(float(node_tree_001['sna_sna_new_variable'][i_073C1] + node_tree_001['sna_sub_render_time']), abs(2))
            node_tree_001['sna_avg_render_time'] = round(float(node_tree_001['sna_sub_render_time'] / 5), abs(2))
            node_tree_001['sna_sub_frame'] = 0
            for i_78937 in range(len(bpy.context.scene.sna_render_list)):
                if (bpy.context.scene.sna_render_list[i_78937].on and (i_78937 > bpy.context.scene.sna_render_list_id)):
                    node_tree_001['sna_sub_frame'] = int(int(bpy.context.scene.sna_render_list[i_78937].end_frame - bpy.context.scene.sna_render_list[i_78937].start_frame) + node_tree_001['sna_sub_frame'])
            node_tree_001['sna_sub_frame'] = int(int(bpy.context.scene.sna_render_list[bpy.context.scene.sna_render_list_id].end_frame - bpy.data.scenes['Scene'].frame_current) + node_tree_001['sna_sub_frame'])


def sna_add_to_object_pt_constraints_16F76(self, context):
    if not ((not bpy.context.preferences.addons['mmd_quick_tool'].preferences.sna_new_property_002)):
        layout = self.layout
        col_24E34 = layout.column(heading='', align=False)
        col_24E34.alert = False
        col_24E34.enabled = True
        col_24E34.active = True
        col_24E34.use_property_split = False
        col_24E34.use_property_decorate = False
        col_24E34.scale_x = 1.0
        col_24E34.scale_y = 1.0
        col_24E34.alignment = 'Expand'.upper()
        col_24E34.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_D8E68 = col_24E34.row(heading='', align=True)
        row_D8E68.alert = bpy.context.scene.sna_remove_transform_constraint
        row_D8E68.enabled = True
        row_D8E68.active = True
        row_D8E68.use_property_split = False
        row_D8E68.use_property_decorate = False
        row_D8E68.scale_x = 1.0
        row_D8E68.scale_y = 1.0
        row_D8E68.alignment = 'Expand'.upper()
        row_D8E68.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_D8E68.prop(bpy.context.scene, 'sna_remove_transform_constraint', text='', icon_value=21, emboss=True)
        op = row_D8E68.operator('sna.my_generic_operator_cde4f', text='位置变换约束', icon_value=string_to_icon('CON_LOCLIKE'), emboss=True, depress=False)
        op = row_D8E68.operator('sna.my_generic_operator_2b24e', text='旋转变换约束', icon_value=string_to_icon('CON_ROTLIKE'), emboss=True, depress=False)


class SNA_OT_My_Generic_Operator_Cde4F(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_cde4f"
    bl_label = "添加位置变换约束"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if bpy.context.scene.sna_remove_transform_constraint:
            if (len(bpy.context.view_layer.objects.selected) == 0):
                self.report({'INFO'}, message='没有选中物体')
            else:
                for i_11CEA in range(len(bpy.context.view_layer.objects.selected)):
                    if (len(bpy.context.view_layer.objects.selected[i_11CEA].constraints) == 0):
                        self.report({'INFO'}, message='没有找到约束')
                    else:
                        for i_9C95C in range(len(bpy.context.view_layer.objects.selected[i_11CEA].constraints)):
                            if '变换位置' in bpy.context.view_layer.objects.selected[i_11CEA].constraints[i_9C95C].name:
                                bpy.context.view_layer.objects.selected[i_11CEA].constraints.remove(constraint=bpy.context.view_layer.objects.selected[i_11CEA].constraints[i_9C95C], )
                                self.report({'INFO'}, message='移除了一个位置变换约束')
                                break
                            else:
                                self.report({'INFO'}, message='没有找到位置变换约束')
        else:
            if (len(bpy.context.view_layer.objects.selected) == 0):
                self.report({'INFO'}, message='没有选中物体')
            else:
                for i_73428 in range(len(bpy.context.view_layer.objects.selected)):
                    constraint_5341E = bpy.context.view_layer.objects.selected[i_73428].constraints.new(type='TRANSFORM', )
                    constraint_5341E.name = '变换位置'
                    constraint_5341E.from_max_x = 100.0
                    constraint_5341E.from_min_x = float(100.0 * -1.0)
                    constraint_5341E.from_max_y = 100.0
                    constraint_5341E.from_min_y = float(100.0 * -1.0)
                    constraint_5341E.from_max_z = 100.0
                    constraint_5341E.from_min_z = float(100.0 * -1.0)
                    constraint_5341E.to_max_x = 100.0
                    constraint_5341E.to_min_x = float(100.0 * -1.0)
                    constraint_5341E.to_max_y = 100.0
                    constraint_5341E.to_min_y = float(100.0 * -1.0)
                    constraint_5341E.to_max_z = 100.0
                    constraint_5341E.to_min_z = float(100.0 * -1.0)
                    self.report({'INFO'}, message='已添加位置变换约束')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_My_Generic_Operator_2B24E(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_2b24e"
    bl_label = "添加旋转变换约束"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if bpy.context.scene.sna_remove_transform_constraint:
            if (len(bpy.context.view_layer.objects.selected) == 0):
                self.report({'INFO'}, message='没有选中物体')
            else:
                for i_37FC5 in range(len(bpy.context.view_layer.objects.selected)):
                    if (len(bpy.context.view_layer.objects.selected[i_37FC5].constraints) == 0):
                        self.report({'INFO'}, message='没有找到约束')
                    else:
                        for i_6D01C in range(len(bpy.context.view_layer.objects.selected[i_37FC5].constraints)):
                            if '变换旋转' in bpy.context.view_layer.objects.selected[i_37FC5].constraints[i_6D01C].name:
                                bpy.context.view_layer.objects.selected[i_37FC5].constraints.remove(constraint=bpy.context.view_layer.objects.selected[i_37FC5].constraints[i_6D01C], )
                                self.report({'INFO'}, message='移除了一个旋转变换约束')
                                break
                            else:
                                self.report({'INFO'}, message='没有找到旋转变换约束')
        else:
            if (len(bpy.context.view_layer.objects.selected) == 0):
                self.report({'INFO'}, message='没有选中物体')
            else:
                for i_00AAE in range(len(bpy.context.view_layer.objects.selected)):
                    constraint_C50CC = bpy.context.view_layer.objects.selected[i_00AAE].constraints.new(type='TRANSFORM', )
                    constraint_C50CC.name = '变换旋转'
                    constraint_C50CC.map_from = 'ROTATION'
                    constraint_C50CC.map_to = 'ROTATION'
                    constraint_C50CC.from_max_x_rot = 3.1415927410125732
                    constraint_C50CC.from_min_x_rot = float(3.1415927410125732 * -1.0)
                    constraint_C50CC.from_max_y_rot = 3.1415927410125732
                    constraint_C50CC.from_min_y_rot = float(3.1415927410125732 * -1.0)
                    constraint_C50CC.from_max_z_rot = 3.1415927410125732
                    constraint_C50CC.from_min_z_rot = float(3.1415927410125732 * -1.0)
                    constraint_C50CC.to_max_x_rot = 3.1415927410125732
                    constraint_C50CC.to_min_x_rot = float(3.1415927410125732 * -1.0)
                    constraint_C50CC.to_max_y_rot = 3.1415927410125732
                    constraint_C50CC.to_min_y_rot = float(3.1415927410125732 * -1.0)
                    constraint_C50CC.to_max_z_rot = 3.1415927410125732
                    constraint_C50CC.to_min_z_rot = float(3.1415927410125732 * -1.0)
                    self.report({'INFO'}, message='已添加旋转变换约束')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_My_Generic_Operator_39Ebf(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_39ebf"
    bl_label = "独立显示曲线"
    bl_description = "独立显示选中曲线"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_E7E99 in range(len(bpy.context.selected_objects)):
            if property_exists("bpy.context.selected_objects[i_E7E99].animation_data.action.fcurves[0]", globals(), locals()):
                for i_D4794 in range(len(bpy.context.selected_objects[i_E7E99].animation_data.action.fcurves)):
                    if bpy.context.selected_objects[i_E7E99].animation_data.action.fcurves[i_D4794].select:
                        bpy.context.selected_objects[i_E7E99].animation_data.action.fcurves[i_D4794].hide = False
                    else:
                        bpy.context.selected_objects[i_E7E99].animation_data.action.fcurves[i_D4794].hide = True
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_add_to_graph_mt_editor_menus_9BAD1(self, context):
    if not (False):
        layout = self.layout
        op = layout.operator('sna.my_generic_operator_39ebf', text='', icon_value=string_to_icon('HIDE_OFF'), emboss=True, depress=False)


class SNA_OT_Operator_F1B3D(bpy.types.Operator):
    bl_idname = "sna.operator_f1b3d"
    bl_label = "Operator"
    bl_description = "选中一个相机，为这个相机配置自动对焦和光圈系统"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        node_tree_005['sna_camera'] = None
        node_tree_005['sna_sna_new_variable_001'] = None
        node_tree_005['sna_sna_new_variable'] = None
        node_tree_005['sna_sna_new_variable_002'] = None
        node_tree_005['sna_sna_new_variable_003'] = None
        node_tree_005['sna_sna_new_variable_002'] = None
        node_tree_005['sna_camera'] = bpy.context.view_layer.objects.active
        if os.path.exists(os.path.join(os.path.dirname(__file__), 'assets', '光圈焦点.blend')):
            if (len(bpy.context.view_layer.objects.selected) == 1):
                if (bpy.context.view_layer.objects.active.type == 'CAMERA'):
                    before_data = list(bpy.data.collections)
                    bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', '光圈焦点.blend') + r'\Collection', filename='光圈焦点', link=False)
                    new_data = list(filter(lambda d: not d in before_data, list(bpy.data.collections)))
                    appended_474EA = None if not new_data else new_data[0]
                    print(appended_474EA.name)
                    for i_54FD0 in range(len(appended_474EA.objects)):
                        if '焦点烘焙' in appended_474EA.objects[i_54FD0].name:
                            node_tree_005['sna_sna_new_variable_002'] = appended_474EA.objects[i_54FD0]
                        if '焦点物体' in appended_474EA.objects[i_54FD0].name:
                            node_tree_005['sna_sna_new_variable'] = appended_474EA.objects[i_54FD0]
                        if '光圈物体' in appended_474EA.objects[i_54FD0].name:
                            node_tree_005['sna_sna_new_variable_001'] = appended_474EA.objects[i_54FD0]
                        if ('焦点' in appended_474EA.objects[i_54FD0].name and ('EMPTY' == appended_474EA.objects[i_54FD0].type)):
                            node_tree_005['sna_sna_new_variable_002'] = appended_474EA.objects[i_54FD0]
                        if ('光圈' in appended_474EA.objects[i_54FD0].name and ('EMPTY' == appended_474EA.objects[i_54FD0].type)):
                            node_tree_005['sna_sna_new_variable_003'] = appended_474EA.objects[i_54FD0]
                    print(node_tree_005['sna_sna_new_variable'].name, node_tree_005['sna_sna_new_variable_001'].name, node_tree_005['sna_sna_new_variable_002'].name, node_tree_005['sna_sna_new_variable_003'].name, node_tree_005['sna_camera'].name, node_tree_005['sna_sna_new_variable_002'].name)
                    node_tree_005['sna_sna_new_variable'].modifiers['GeometryNodes'].node_group.nodes['对焦物体'].inputs[2].default_value = node_tree_005['sna_camera']
                    driver_0_eeb89, var_1_eeb89 = sna_in_79644(node_tree_005['sna_sna_new_variable'].modifiers['GeometryNodes'].node_group, '对焦物体', '分辨率X', 'SCENE', bpy.context.scene, 'render.resolution_x')
                    driver_0_2ed19, var_1_2ed19 = sna_in_79644(node_tree_005['sna_sna_new_variable'].modifiers['GeometryNodes'].node_group, '对焦物体', '分辨率Y', 'SCENE', bpy.context.scene, 'render.resolution_y')
                    driver_0_74dc9, var_1_74dc9 = sna_in_79644(node_tree_005['sna_sna_new_variable'].modifiers['GeometryNodes'].node_group, '对焦物体', '焦距', 'CAMERA', node_tree_005['sna_camera'].data, 'lens')
                    node_tree_005['sna_sna_new_variable_001'].modifiers['GeometryNodes'].node_group.nodes['光圈'].inputs[1].default_value = node_tree_005['sna_camera']
                    node_tree_005['sna_sna_new_variable_001'].modifiers['GeometryNodes'].node_group.nodes['光圈'].inputs[2].default_value = node_tree_005['sna_sna_new_variable_002']
                    driver_0_f9206, var_1_f9206 = sna_in_79644(node_tree_005['sna_sna_new_variable_001'].modifiers['GeometryNodes'].node_group, '光圈', '焦距', 'CAMERA', node_tree_005['sna_camera'].data, 'lens')
                    node_tree_005['sna_camera'].data.dof.use_dof = True
                    node_tree_005['sna_camera'].data.dof.focus_object = node_tree_005['sna_sna_new_variable_002']
                    success_7BE7A = node_tree_005['sna_camera'].data.driver_remove('dof.aperture_fstop', )
                    driver_BDF65 = node_tree_005['sna_camera'].data.driver_add('dof.aperture_fstop', )
                    driver_BDF65.driver.type = 'SCRIPTED'
                    var_C8F2F = driver_BDF65.driver.variables.new()
                    var_C8F2F.name = 'var'
                    var_C8F2F.type = 'TRANSFORMS'
                    var_C8F2F.targets[0].id = node_tree_005['sna_sna_new_variable_003']
                    var_C8F2F.targets[0].transform_type = 'LOC_Z'
                    driver_BDF65.driver.expression = 'var'
                    node_tree_005['sna_sna_new_variable_001'].hide_render = True
                    node_tree_005['sna_sna_new_variable'].hide_render = True
                    self.report({'INFO'}, message='配置完成')
                    self.report({'INFO'}, message='记得去几何节点里设置对焦物体（没有报错）')
                else:
                    self.report({'WARNING'}, message='所选物体不是相机')
            else:
                self.report({'WARNING'}, message='选中一个相机')
        else:
            self.report({'ERROR'}, message='光圈焦点资产不存在')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


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


class SNA_PT_MMD_QUICK_TOOL_MATERIAL_67F0C(bpy.types.Panel):
    bl_label = 'mmd Quick tool Material'
    bl_idname = 'SNA_PT_MMD_QUICK_TOOL_MATERIAL_67F0C'
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'QT MMD'
    bl_order = 0
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (((not ((eval('bpy.context.space_data.type') == 'NODE_EDITOR') and (eval('bpy.context.space_data.tree_type') == 'ShaderNodeTree'))) or (not bpy.context.preferences.addons['mmd_quick_tool'].preferences.sna_new_property_003)))

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout


class SNA_OT_Bake_Tex_F278F(bpy.types.Operator):
    bl_idname = "sna.bake_tex_f278f"
    bl_label = "bake_tex"
    bl_description = "bake"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (bpy.context.area.type == 'NODE_EDITOR'):
            if bpy.context.scene.sna_use_choose_tex:
                if (('TEX_IMAGE' == bpy.context.active_object.active_material.node_tree.nodes.active.type) and (bpy.context.active_object.active_material.node_tree.nodes.active.select == True)):
                    bpy.ops.object.bake('INVOKE_DEFAULT', type='EMIT', margin=16, margin_type='ADJACENT_FACES', target='IMAGE_TEXTURES', use_clear=True)
                    self.report({'INFO'}, message='烘焙完成')
                else:
                    self.report({'INFO'}, message='没有选中图像节点')
            else:
                for i_E93E1 in range(len(bpy.context.active_object.active_material.node_tree.links)):
                    if (('材质输出' == bpy.context.active_object.active_material.node_tree.links[i_E93E1].to_node.name) or (bpy.context.active_object.active_material.node_tree.links[i_E93E1].to_node.name == 'Material Output')):
                        node_tree_004['sna_last_node'] = bpy.context.active_object.active_material.node_tree.links[i_E93E1].from_node
                        print(bpy.context.active_object.active_material.node_tree.links[i_E93E1].to_node.name)
                node_73893 = bpy.context.active_object.active_material.node_tree.nodes.new(type='ShaderNodeTexImage', )
                node_73893.location = tuple(mathutils.Vector(node_tree_004['sna_last_node'].location) + mathutils.Vector((0.0, 250.0)))
                image_E6981 = bpy.data.images.new(name='bake_tex', width=bpy.context.scene.sna_bake_tex_size_x, height=bpy.context.scene.sna_bake_tex_size_y, alpha=True, )
                node_73893.image = image_E6981
                for i_3E53F in range(len(bpy.context.active_object.active_material.node_tree.nodes)):
                    bpy.context.active_object.active_material.node_tree.nodes[i_3E53F].select = False
                node_73893.select = True
                bpy.context.active_object.active_material.node_tree.nodes.active = node_73893
                bpy.ops.object.bake('INVOKE_DEFAULT', type='EMIT', margin=16, margin_type='ADJACENT_FACES', target='IMAGE_TEXTURES', use_clear=True)
                self.report({'INFO'}, message='烘焙完成')
        else:
            self.report({'INFO'}, message='活动区域不在节点编辑器')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_My_Generic_Operator_7A93E(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_7a93e"
    bl_label = "复制活动骨骼权重到选中骨骼"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}
    sna_new_property: bpy.props.BoolProperty(name='保留目标骨骼的权重', description='', default=False)
    sna_new_property_001: bpy.props.BoolProperty(name='移除源骨骼权重', description='', default=False)

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        node_tree_008['sna_select_obj'] = []
        node_tree_008['sna_bone_obj'] = None
        node_tree_008['sna_bone_weight_from'] = None
        node_tree_008['sna_bone_weight_to'] = []
        node_tree_008['sna_num'] = 0
        for i_7D72D in range(len(bpy.context.selected_objects)):
            if (bpy.context.selected_objects[i_7D72D].type == 'MESH'):
                node_tree_008['sna_select_obj'].append(bpy.context.selected_objects[i_7D72D])
            if (bpy.context.selected_objects[i_7D72D].type == 'ARMATURE'):
                node_tree_008['sna_bone_obj'] = bpy.context.selected_objects[i_7D72D]
                node_tree_008['sna_num'] = int(node_tree_008['sna_num'] + 1.0)
        if (node_tree_008['sna_num'] == 1):
            node_tree_008['sna_num'] = 0
            node_tree_008['sna_bone_weight_from'] = node_tree_008['sna_bone_obj'].data.bones.active
            for i_E5D6B in range(len(node_tree_008['sna_bone_obj'].data.bones)):
                if node_tree_008['sna_bone_obj'].data.bones[i_E5D6B].select:
                    node_tree_008['sna_bone_weight_to'].append(node_tree_008['sna_bone_obj'].data.bones[i_E5D6B])
            print(str(node_tree_008['sna_select_obj']), node_tree_008['sna_bone_obj'].name, node_tree_008['sna_bone_weight_from'].name, str(node_tree_008['sna_bone_weight_to']))
            for i_D8AF4 in range(len(node_tree_008['sna_select_obj'])):
                for i_A491A in range(len(node_tree_008['sna_bone_weight_to'])):
                    if (node_tree_008['sna_bone_weight_from'].name == node_tree_008['sna_bone_weight_to'][i_A491A].name):
                        pass
                    else:
                        if (property_exists("node_tree_008['sna_select_obj'][i_D8AF4].vertex_groups", globals(), locals()) and node_tree_008['sna_bone_weight_to'][i_A491A].name in node_tree_008['sna_select_obj'][i_D8AF4].vertex_groups):
                            if self.sna_new_property:
                                pass
                            else:
                                node_tree_008['sna_select_obj'][i_D8AF4].vertex_groups.remove(group=node_tree_008['sna_select_obj'][i_D8AF4].vertex_groups[node_tree_008['sna_bone_weight_to'][i_A491A].name], )
                                group_A4275 = node_tree_008['sna_select_obj'][i_D8AF4].vertex_groups.new(name=node_tree_008['sna_bone_weight_to'][i_A491A].name, )
                        else:
                            group_6A270 = node_tree_008['sna_select_obj'][i_D8AF4].vertex_groups.new(name=node_tree_008['sna_bone_weight_to'][i_A491A].name, )
                for i_00775 in range(len(node_tree_008['sna_select_obj'][i_D8AF4].data.vertices)):
                    for i_E114B in range(len(node_tree_008['sna_select_obj'][i_D8AF4].data.vertices[i_00775].groups)):
                        if (node_tree_008['sna_select_obj'][i_D8AF4].vertex_groups[node_tree_008['sna_select_obj'][i_D8AF4].data.vertices[i_00775].groups[i_E114B].group].name == node_tree_008['sna_bone_weight_from'].name):
                            for i_2F3E8 in range(len(node_tree_008['sna_bone_weight_to'])):
                                if (node_tree_008['sna_bone_weight_from'].name == node_tree_008['sna_bone_weight_to'][i_2F3E8].name):
                                    pass
                                else:
                                    if self.sna_new_property:
                                        node_tree_008['sna_select_obj'][i_D8AF4].vertex_groups[node_tree_008['sna_bone_weight_to'][i_2F3E8].name].add(index=(i_00775, i_00775, i_00775), weight=node_tree_008['sna_select_obj'][i_D8AF4].data.vertices[i_00775].groups[i_E114B].weight, type='ADD', )
                                    else:
                                        node_tree_008['sna_select_obj'][i_D8AF4].vertex_groups[node_tree_008['sna_bone_weight_to'][i_2F3E8].name].add(index=(i_00775, i_00775, i_00775), weight=node_tree_008['sna_select_obj'][i_D8AF4].data.vertices[i_00775].groups[i_E114B].weight, type='REPLACE', )
                if self.sna_new_property_001:
                    node_tree_008['sna_select_obj'][i_D8AF4].vertex_groups.remove(group=node_tree_008['sna_select_obj'][i_D8AF4].vertex_groups[node_tree_008['sna_bone_weight_from'].name], )
                    group_6C7C6 = node_tree_008['sna_select_obj'][i_D8AF4].vertex_groups.new(name=node_tree_008['sna_bone_weight_from'].name, )
                    self.report({'INFO'}, message='完成')
        else:
            self.report({'WARNING'}, message='选择的骨架超过一个')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_add_to_view3d_mt_paint_weight_1FE39(self, context):
    if not (False):
        layout = self.layout
        op = layout.operator('sna.my_generic_operator_7a93e', text='复制激活骨骼权重到选中骨骼', icon_value=0, emboss=True, depress=False)
        op.sna_new_property = False
        op.sna_new_property_001 = False


def sna_add_to_view3d_ht_tool_header_CFA13(self, context):
    if not ( not 'PAINT_VERTEX'==bpy.context.mode):
        layout = self.layout
        row_9B98E = layout.row(heading='', align=True)
        row_9B98E.alert = False
        row_9B98E.enabled = True
        row_9B98E.active = True
        row_9B98E.use_property_split = False
        row_9B98E.use_property_decorate = False
        row_9B98E.scale_x = 1.0
        row_9B98E.scale_y = 1.0
        row_9B98E.alignment = 'Left'.upper()
        row_9B98E.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_9B98E.operator('sna.operator_6aa4f', text='', icon_value=string_to_icon('BRUSHES_ALL'), emboss=True, depress=False)
        op = row_9B98E.operator('sna.operator001_05281', text='', icon_value=_icons['white.png'].icon_id, emboss=True, depress=False)
        op = row_9B98E.operator('sna.operator002_2a623', text='', icon_value=_icons['black.png'].icon_id, emboss=True, depress=False)
        op = row_9B98E.operator('sna.operator003_d462c', text='', icon_value=_icons['red.png'].icon_id, emboss=True, depress=False)
        op = row_9B98E.operator('sna.operator004_d6bee', text='', icon_value=_icons['green.png'].icon_id, emboss=True, depress=False)
        op = row_9B98E.operator('sna.operator005_2a676', text='', icon_value=_icons['blue.png'].icon_id, emboss=True, depress=False)
        op = row_9B98E.operator('sna.operator006_dda67', text='', icon_value=_icons['yellow.png'].icon_id, emboss=True, depress=False)
        op = row_9B98E.operator('sna.operator007_17ad2', text='', icon_value=_icons['purple.png'].icon_id, emboss=True, depress=False)
        op = row_9B98E.operator('sna.operator008_a3fb7', text='', icon_value=_icons['cyan.png'].icon_id, emboss=True, depress=False)


class SNA_OT_Operator001_05281(bpy.types.Operator):
    bl_idname = "sna.operator001_05281"
    bl_label = "Operator.001"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        brush = getattr(bpy.context.tool_settings.vertex_paint, 'brush', None)
        if brush is None:
            self.report({'WARNING'}, message='No active vertex paint brush')
            return {"CANCELLED"}
        brush.color = (1.0, 1.0, 1.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator003_D462C(bpy.types.Operator):
    bl_idname = "sna.operator003_d462c"
    bl_label = "Operator.003"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.tool_settings.vertex_paint.brush.color = (1.0, 0.0, 0.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator004_D6Bee(bpy.types.Operator):
    bl_idname = "sna.operator004_d6bee"
    bl_label = "Operator.004"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.tool_settings.vertex_paint.brush.color = (0.0, 1.0, 0.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator005_2A676(bpy.types.Operator):
    bl_idname = "sna.operator005_2a676"
    bl_label = "Operator.005"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.tool_settings.vertex_paint.brush.color = (0.0, 0.0, 1.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator006_Dda67(bpy.types.Operator):
    bl_idname = "sna.operator006_dda67"
    bl_label = "Operator.006"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.tool_settings.vertex_paint.brush.color = (1.0, 1.0, 0.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator007_17Ad2(bpy.types.Operator):
    bl_idname = "sna.operator007_17ad2"
    bl_label = "Operator.007"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.tool_settings.vertex_paint.brush.color = (1.0, 0.0, 1.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator008_A3Fb7(bpy.types.Operator):
    bl_idname = "sna.operator008_a3fb7"
    bl_label = "Operator.008"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.tool_settings.vertex_paint.brush.color = (0.0, 1.0, 1.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator002_2A623(bpy.types.Operator):
    bl_idname = "sna.operator002_2a623"
    bl_label = "Operator.002"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.tool_settings.vertex_paint.brush.color = (0.0, 0.0, 0.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Operator_6Aa4F(bpy.types.Operator):
    bl_idname = "sna.operator_6aa4f"
    bl_label = "Operator"
    bl_description = "设置选中物体的顶点色为画笔颜色"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        node_tree_002['sna_sna_new_variable'] = bpy.context.view_layer.objects.active.name
        bpy.ops.paint.vertex_color_set('INVOKE_DEFAULT', )
        bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='OBJECT')
        for i_44E9C in range(len(bpy.context.view_layer.objects.selected)):
            bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.selected[i_44E9C]
            bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='VERTEX_PAINT')
            bpy.ops.paint.vertex_color_set('INVOKE_DEFAULT', )
            bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='OBJECT')
            if (i_44E9C == int(len(bpy.context.view_layer.objects.selected) - 1.0)):
                bpy.context.view_layer.objects.active = bpy.context.view_layer.objects[node_tree_002['sna_sna_new_variable']]
                bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='VERTEX_PAINT')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_My_Generic_Operator_48003(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_48003"
    bl_label = "标注工具"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if ((bpy.context.area.type == 'NODE_EDITOR') or (bpy.context.area.type == 'IMAGE_EDITOR') or (bpy.context.area.type == 'VIEW_3D')):
            bpy.ops.wm.call_menu_pie(name="SNA_MT_3BB6D")
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_MT_3BB6D(bpy.types.Menu):
    bl_idname = "SNA_MT_3BB6D"
    bl_label = ""

    @classmethod
    def poll(cls, context):
        return not ((not bpy.context.preferences.addons['mmd_quick_tool'].preferences.sna_new_property_005))

    def draw(self, context):
        layout = self.layout.menu_pie()
        op = layout.operator('wm.tool_set_by_id', text='标注', icon_value=string_to_icon('GREASEPENCIL'), emboss=True, depress=False)
        op.name = 'builtin.annotate'
        op = layout.operator('wm.tool_set_by_id', text='框选', icon_value=string_to_icon('CHECKBOX_DEHLT'), emboss=True, depress=False)
        op.name = 'builtin.select_box'
        op = layout.operator('view3d.localview', text='独立显示', icon_value=0, emboss=True, depress=False)
        op = layout.operator('wm.tool_set_by_id', text='标注橡皮擦', icon_value=string_to_icon('SNAP_FACE'), emboss=True, depress=False)
        op.name = 'builtin.annotate_eraser'
        op = layout.operator('gpencil.layer_annotation_remove', text='清除标注层', icon_value=0, emboss=True, depress=False)
        op = layout.operator('sna.my_generic_operator_8ad72', text='添加预览灯光', icon_value=0, emboss=True, depress=False)
        if ((bpy.context.area.type == 'VIEW_3D') and 'EDIT_MESH'==bpy.context.mode):
            op = layout.operator('sna.my_generic_operator_a52b1', text='合并所选顶点', icon_value=0, emboss=True, depress=False)
            op.sna_new_property = 'CENTER'


class SNA_OT_My_Generic_Operator_8Ad72(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_8ad72"
    bl_label = "添加预览灯光"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        node_tree_005['sna_light_obj'] = []
        bpy.ops.object.light_add('INVOKE_DEFAULT', type='AREA', radius=1.0, location=(-1.7913199663162231, -1.0733000040054321, 1.4290000200271606), rotation=(1.3820528984069824, 0.0, -1.0796327590942383), scale=(1.0, 1.0, 1.0))
        bpy.context.view_layer.objects.active.scale = (1.9769999980926514, 1.9769999980926514, 1.9769999980926514)
        bpy.context.view_layer.objects.active.name = '副光'
        bpy.context.view_layer.objects.active.data.name = '副光'
        bpy.context.view_layer.objects.active.data.energy = 15.0
        node_tree_005['sna_light_obj'].append(bpy.context.view_layer.objects.active)
        bpy.ops.object.light_add('INVOKE_DEFAULT', type='AREA', radius=1.0, location=(0.2778179943561554, 1.6447900533676147, 2.0871999263763428), rotation=(1.3820528984069824, 0.0, -3.2447938919067383), scale=(1.0, 1.0, 1.0))
        bpy.context.view_layer.objects.active.scale = (5.754690170288086, 2.634190082550049, 1.9773199558258057)
        bpy.context.view_layer.objects.active.name = '背光'
        bpy.context.view_layer.objects.active.data.name = '背光'
        bpy.context.view_layer.objects.active.data.energy = 240.0
        node_tree_005['sna_light_obj'].append(bpy.context.view_layer.objects.active)
        bpy.ops.object.light_add('INVOKE_DEFAULT', type='AREA', radius=1.0, location=(2.334399938583374, -0.8916320204734802, 1.4290000200271606), rotation=(1.492418885231018, 0.0, 1.2703763246536255), scale=(1.0, 1.0, 1.0))
        bpy.context.view_layer.objects.active.scale = (1.9773199558258057, 1.9773199558258057, 1.9773199558258057)
        bpy.context.view_layer.objects.active.name = '主光'
        bpy.context.view_layer.objects.active.data.name = '主光'
        bpy.context.view_layer.objects.active.data.energy = 60.0
        bpy.context.view_layer.objects.active.data.spread = 2.094395160675049
        node_tree_005['sna_light_obj'].append(bpy.context.view_layer.objects.active)
        bpy.ops.object.empty_add('INVOKE_DEFAULT', type='PLAIN_AXES', radius=1.0, align='WORLD', location=(0.0, 0.0, 0.0))
        bpy.context.view_layer.objects.active.name = '快速灯光'
        for i_CAE75 in range(len(node_tree_005['sna_light_obj'])):
            node_tree_005['sna_light_obj'][i_CAE75].select = True
        bpy.ops.object.parent_set('INVOKE_DEFAULT', type='OBJECT', keep_transform=True)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_My_Generic_Operator_A52B1(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_a52b1"
    bl_label = "合并所选顶点"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    def sna_new_property_enum_items(self, context):
        return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]
    sna_new_property: bpy.props.EnumProperty(name='类型', description='', items=[('CENTER', 'CENTER', '', 0, 0), ('CURSOR', 'CURSOR', '', 0, 1), ('COLLAPSE', 'COLLAPSE', '', 0, 2), ('FIRST', 'FIRST', '', 0, 3), ('LAST', 'LAST', '', 0, 4)])

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.ops.mesh.merge('INVOKE_DEFAULT', type=self.sna_new_property)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_AddonPreferences_C113E(bpy.types.AddonPreferences):
    bl_idname = 'mmd_quick_tool'
    sna_display_time: bpy.props.BoolProperty(name='display_time', description='', default=True)
    sna_new_property: bpy.props.BoolProperty(name='快速设置分辨率界面', description='', default=True)
    sna_new_property_001: bpy.props.BoolProperty(name='顶点色工具', description='', default=True)
    sna_new_property_002: bpy.props.BoolProperty(name='添加变换约束工具', description='', default=True)
    sna_new_property_003: bpy.props.BoolProperty(name='着色器贴图烘焙', description='', default=True)
    sna_new_property_004: bpy.props.BoolProperty(name='分段渲染', description='', default=True)
    sna_new_property_005: bpy.props.BoolProperty(name='使用快速饼菜单', description='', default=True)

    def draw(self, context):
        if not (False):
            layout = self.layout 
            box_BBD0E = layout.box()
            box_BBD0E.alert = False
            box_BBD0E.enabled = True
            box_BBD0E.active = True
            box_BBD0E.use_property_split = False
            box_BBD0E.use_property_decorate = False
            box_BBD0E.alignment = 'Expand'.upper()
            box_BBD0E.scale_x = 1.0
            box_BBD0E.scale_y = 1.0
            if not True: box_BBD0E.operator_context = "EXEC_DEFAULT"
            box_BBD0E.label(text='显示设置', icon_value=0)
            row_D5B1E = box_BBD0E.row(heading='', align=False)
            row_D5B1E.alert = False
            row_D5B1E.enabled = True
            row_D5B1E.active = True
            row_D5B1E.use_property_split = False
            row_D5B1E.use_property_decorate = False
            row_D5B1E.scale_x = 1.0
            row_D5B1E.scale_y = 1.0
            row_D5B1E.alignment = 'Expand'.upper()
            row_D5B1E.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            row_D5B1E.prop(bpy.context.preferences.addons['mmd_quick_tool'].preferences, 'sna_display_time', text='显示分秒', icon_value=0, emboss=True)
            row_D5B1E.prop(bpy.context.preferences.addons['mmd_quick_tool'].preferences, 'sna_new_property', text='快速设置分辨率界面', icon_value=0, emboss=True)
            row_D5B1E.prop(bpy.context.preferences.addons['mmd_quick_tool'].preferences, 'sna_new_property_001', text='顶点色工具', icon_value=0, emboss=True)
            row_D5B1E.prop(bpy.context.preferences.addons['mmd_quick_tool'].preferences, 'sna_new_property_002', text='约束工具', icon_value=0, emboss=True)
            row_D5B1E.prop(bpy.context.preferences.addons['mmd_quick_tool'].preferences, 'sna_new_property_003', text='着色器贴图烘焙', icon_value=0, emboss=True)
            row_F8ACB = box_BBD0E.row(heading='', align=False)
            row_F8ACB.alert = False
            row_F8ACB.enabled = True
            row_F8ACB.active = True
            row_F8ACB.use_property_split = False
            row_F8ACB.use_property_decorate = False
            row_F8ACB.scale_x = 1.0
            row_F8ACB.scale_y = 1.0
            row_F8ACB.alignment = 'Expand'.upper()
            row_F8ACB.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            row_F8ACB.prop(bpy.context.preferences.addons['mmd_quick_tool'].preferences, 'sna_new_property_004', text='分段渲染', icon_value=0, emboss=True)
            row_F8ACB.prop(bpy.context.preferences.addons['mmd_quick_tool'].preferences, 'sna_new_property_005', text='使用快速饼菜单', icon_value=0, emboss=True)
            row_1F4FE = layout.row(heading='', align=False)
            row_1F4FE.alert = False
            row_1F4FE.enabled = True
            row_1F4FE.active = True
            row_1F4FE.use_property_split = False
            row_1F4FE.use_property_decorate = False
            row_1F4FE.scale_x = 1.0
            row_1F4FE.scale_y = 1.0
            row_1F4FE.alignment = 'Expand'.upper()
            row_1F4FE.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            op = row_1F4FE.operator('sna.my_generic_operator_763af', text='查看更新日志', icon_value=string_to_icon('TEXT'), emboss=True, depress=False)
            row_472B7 = layout.row(heading='', align=False)
            row_472B7.alert = False
            row_472B7.enabled = True
            row_472B7.active = True
            row_472B7.use_property_split = False
            row_472B7.use_property_decorate = False
            row_472B7.scale_x = 1.0
            row_472B7.scale_y = 1.0
            row_472B7.alignment = 'Expand'.upper()
            row_472B7.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            op = row_472B7.operator('wm.url_open', text='打开github首页获取帮助', icon_value=string_to_icon('HELP'), emboss=True, depress=False)
            op.url = 'https://github.com/bb-yi/mmd-Quick-tool'
            row_99DC0 = layout.row(heading='', align=False)
            row_99DC0.alert = False
            row_99DC0.enabled = True
            row_99DC0.active = True
            row_99DC0.use_property_split = False
            row_99DC0.use_property_decorate = False
            row_99DC0.scale_x = 1.0
            row_99DC0.scale_y = 1.0
            row_99DC0.alignment = 'Center'.upper()
            row_99DC0.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            row_99DC0.label(text='mmd Quick tool', icon_value=0)
            row_99DC0.label(text='插件版本' + str(tuple((1, 1, 5))), icon_value=0)
            row_99DC0.label(text='by  ' + 'SFY', icon_value=string_to_icon('FUND'))
            row_99DC0.label(text='感谢使用', icon_value=0)


class SNA_OT_My_Generic_Operator_763Af(bpy.types.Operator):
    bl_idname = "sna.my_generic_operator_763af"
    bl_label = "查看更新日志"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        exec('import webbrowser')
        exec("webbrowser.open('https://github.com/bb-yi/mmd-Quick-tool/blob/main/%E6%9B%B4%E6%96%B0%E6%97%A5%E5%BF%97.txt')")
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_PT_IK_CC508(bpy.types.Panel):
    bl_label = 'ik修复'
    bl_idname = 'SNA_PT_IK_CC508'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 0
    bl_parent_id = 'SNA_PT_MMD_0B0AC'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        col_79ECE = layout.column(heading='', align=False)
        col_79ECE.alert = False
        col_79ECE.enabled = True
        col_79ECE.active = True
        col_79ECE.use_property_split = False
        col_79ECE.use_property_decorate = False
        col_79ECE.scale_x = 1.0
        col_79ECE.scale_y = 1.0
        col_79ECE.alignment = 'Expand'.upper()
        col_79ECE.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = col_79ECE.operator('sna.my_generic_operator_c3269', text='添加骨骼物体', icon_value=string_to_icon('BONE_DATA'), emboss=True, depress=False)
        op.sna_new_property = True
        op = col_79ECE.operator('sna.my_generic_operator_cc136', text='传递顶点组', icon_value=string_to_icon('MESH_DATA'), emboss=True, depress=False)
        op = col_79ECE.operator('sna.my_generic_operator_c8494', text='生成骨骼约束', icon_value=string_to_icon('CONSTRAINT_BONE'), emboss=True, depress=False)
        row_4175F = col_79ECE.row(heading='', align=False)
        row_4175F.alert = False
        row_4175F.enabled = True
        row_4175F.active = True
        row_4175F.use_property_split = False
        row_4175F.use_property_decorate = False
        row_4175F.scale_x = 1.0
        row_4175F.scale_y = 1.0
        row_4175F.alignment = 'Expand'.upper()
        row_4175F.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_4175F.prop(bpy.context.scene, 'sna_ik_fix_on', text=('开启' if bpy.context.scene.sna_ik_fix_on else '关闭'), icon_value=(string_to_icon('HIDE_OFF') if bpy.context.scene.sna_ik_fix_on else string_to_icon('HIDE_ON')), emboss=True)
        op = row_4175F.operator('sna.my_generic_operator_89058', text='清除骨骼约束', icon_value=string_to_icon('DECORATE_OVERRIDE'), emboss=True, depress=False)
        op = col_79ECE.operator('sna.ik_b204a', text='关闭/打开IK', icon_value=string_to_icon('CON_SPLINEIK'), emboss=True, depress=False)
        op = col_79ECE.operator('sna.my_generic_operator_c034b', text='烘焙约束', icon_value=string_to_icon('KEYTYPE_KEYFRAME_VEC'), emboss=True, depress=False)
        op.sna_new_property = bpy.context.scene.frame_start
        op.sna_new_property_001 = bpy.context.scene.frame_end


class SNA_PT_UV_5331C(bpy.types.Panel):
    bl_label = 'UV'
    bl_idname = 'SNA_PT_UV_5331C'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 2
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'SNA_PT_MMD_5DD0C'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        col_8BB61 = layout.column(heading='', align=False)
        col_8BB61.alert = False
        col_8BB61.enabled = True
        col_8BB61.active = True
        col_8BB61.use_property_split = False
        col_8BB61.use_property_decorate = False
        col_8BB61.scale_x = 1.0
        col_8BB61.scale_y = 1.0
        col_8BB61.alignment = 'Expand'.upper()
        col_8BB61.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_4EF87 = col_8BB61.row(heading='', align=False)
        row_4EF87.alert = False
        row_4EF87.enabled = True
        row_4EF87.active = True
        row_4EF87.use_property_split = False
        row_4EF87.use_property_decorate = False
        row_4EF87.scale_x = 1.0
        row_4EF87.scale_y = 1.0
        row_4EF87.alignment = 'Expand'.upper()
        row_4EF87.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_4EF87.operator('sna.uv_9201e', text='生成位置uv', icon_value=0, emboss=True, depress=False)
        op.sna_new_property = 'FRONT'
        op = row_4EF87.operator('sna.uv_94b57', text='移除位置uv', icon_value=0, emboss=True, depress=False)


class SNA_PT__35D62(bpy.types.Panel):
    bl_label = '名称编辑'
    bl_idname = 'SNA_PT__35D62'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'SNA_PT_MMD_5DD0C'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        row_02724 = layout.row(heading='', align=False)
        row_02724.alert = False
        row_02724.enabled = True
        row_02724.active = True
        row_02724.use_property_split = False
        row_02724.use_property_decorate = False
        row_02724.scale_x = 1.0
        row_02724.scale_y = 1.0
        row_02724.alignment = 'Expand'.upper()
        row_02724.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_02724.operator('sna.my_generic_operator_bedaf', text='材质到物体', icon_value=0, emboss=True, depress=False)
        op = row_02724.operator('sna.my_generic_operator_04cf5', text='物体到材质', icon_value=0, emboss=True, depress=False)
        op = row_02724.operator('sna.my_generic_operator_60634', text='贴图到材质', icon_value=0, emboss=True, depress=False)


class SNA_PT__E26FF(bpy.types.Panel):
    bl_label = '物体操作'
    bl_idname = 'SNA_PT__E26FF'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'SNA_PT_MMD_0B0AC'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        op = layout.operator('sna.operator015_0ebb1', text='位姿归零', icon_value=0, emboss=True, depress=False)
        op.sna_x = True
        op.sna_y = True
        op.sna_z = True


class SNA_PT__668A7(bpy.types.Panel):
    bl_label = '临时合并'
    bl_idname = 'SNA_PT__668A7'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'SNA_PT__E26FF'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        col_3CAA1 = layout.column(heading='', align=False)
        col_3CAA1.alert = False
        col_3CAA1.enabled = True
        col_3CAA1.active = True
        col_3CAA1.use_property_split = False
        col_3CAA1.use_property_decorate = False
        col_3CAA1.scale_x = 1.0
        col_3CAA1.scale_y = 1.0
        col_3CAA1.alignment = 'Expand'.upper()
        col_3CAA1.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_7247F = col_3CAA1.row(heading='', align=False)
        row_7247F.alert = False
        row_7247F.enabled = True
        row_7247F.active = True
        row_7247F.use_property_split = False
        row_7247F.use_property_decorate = False
        row_7247F.scale_x = 1.0
        row_7247F.scale_y = 1.0
        row_7247F.alignment = 'Expand'.upper()
        row_7247F.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_7247F.operator('sna.my_generic_operator_fb95f', text='临时合并', icon_value=0, emboss=True, depress=False)
        op = row_7247F.operator('sna.my_generic_operator_dd728', text='分离临时合并', icon_value=0, emboss=True, depress=False)


class SNA_PT__023F8(bpy.types.Panel):
    bl_label = '分辨率调整'
    bl_idname = 'SNA_PT__023F8'
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'output'
    bl_order = 0
    bl_parent_id = 'RENDER_PT_format'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        row_9A4A1 = layout.row(heading='', align=False)
        row_9A4A1.alert = False
        row_9A4A1.enabled = True
        row_9A4A1.active = True
        row_9A4A1.use_property_split = False
        row_9A4A1.use_property_decorate = False
        row_9A4A1.scale_x = 1.0
        row_9A4A1.scale_y = 1.0
        row_9A4A1.alignment = 'Left'.upper()
        row_9A4A1.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_9A4A1.operator('sna.operator_b46a6', text='1080p', icon_value=0, emboss=True, depress=False)
        op = row_9A4A1.operator('sna.operator001_64c4a', text='2k', icon_value=0, emboss=True, depress=False)
        op = row_9A4A1.operator('sna.operator002_7dbd9', text='4k', icon_value=0, emboss=True, depress=False)
        op = row_9A4A1.operator('sna.operator007_85779', text='交换', icon_value=string_to_icon('FILE_REFRESH'), emboss=True, depress=False)
        op.sna_ax = 7
        op = row_9A4A1.operator('sna.operator008_f7b4c', text='*0.5', icon_value=0, emboss=True, depress=False)
        op = row_9A4A1.operator('sna.operator010_18497', text='*0.75', icon_value=0, emboss=True, depress=False)
        op = row_9A4A1.operator('sna.operator003_da1be', text='*1.5', icon_value=0, emboss=True, depress=False)
        op = row_9A4A1.operator('sna.operator009_f9bf5', text='*2', icon_value=0, emboss=True, depress=False)
        row_3E7EE = layout.row(heading='', align=False)
        row_3E7EE.alert = False
        row_3E7EE.enabled = True
        row_3E7EE.active = True
        row_3E7EE.use_property_split = False
        row_3E7EE.use_property_decorate = False
        row_3E7EE.scale_x = 1.0
        row_3E7EE.scale_y = 1.0
        row_3E7EE.alignment = 'Left'.upper()
        row_3E7EE.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_3E7EE.prop(bpy.context.scene, 'sna_bili', text='比例', icon_value=0, emboss=True, expand=True)


class SNA_PT__6062D(bpy.types.Panel):
    bl_label = '相机设置'
    bl_idname = 'SNA_PT__6062D'
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'output'
    bl_order = 0
    bl_parent_id = 'RENDER_PT_format'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not ((not property_exists("bpy.context.scene.camera.data", globals(), locals())))

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        row_854C3 = layout.row(heading='', align=False)
        row_854C3.alert = False
        row_854C3.enabled = True
        row_854C3.active = True
        row_854C3.use_property_split = False
        row_854C3.use_property_decorate = False
        row_854C3.scale_x = 1.0
        row_854C3.scale_y = 1.0
        row_854C3.alignment = 'Left'.upper()
        row_854C3.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_854C3.prop(bpy.context.scene.camera.data, 'lens', text='焦距', icon_value=0, emboss=True)
        row_854C3.prop(bpy.context.scene.camera.data.dof, 'aperture_fstop', text='光圈', icon_value=0, emboss=True)


class SNA_PT_MMD_B11D3(bpy.types.Panel):
    bl_label = 'MMD流程'
    bl_idname = 'SNA_PT_MMD_B11D3'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 1
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'SNA_PT_MMD_5DD0C'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        col_85326 = layout.column(heading='', align=False)
        col_85326.alert = False
        col_85326.enabled = True
        col_85326.active = True
        col_85326.use_property_split = False
        col_85326.use_property_decorate = False
        col_85326.scale_x = 1.0
        col_85326.scale_y = 1.0
        col_85326.alignment = 'Expand'.upper()
        col_85326.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = col_85326.operator('sna.operator021_0d655', text='删除材质变形节点组', icon_value=0, emboss=True, depress=False)
        op = col_85326.operator('sna.operator004_fa32a', text='合并相同贴图的材质', icon_value=0, emboss=True, depress=False)
        op = col_85326.operator('sna.operator005_9368b', text='替换mmd材质节点组', icon_value=0, emboss=True, depress=False)
        op = col_85326.operator('sna.abc_b0bf3', text='为abc添加材质', icon_value=0, emboss=True, depress=False)
        op = col_85326.operator('sna.my_generic_operator_abaaa', text='移除选中物体所有材质', icon_value=0, emboss=True, depress=False)
        op = col_85326.operator('sna.operator025_4038c', text='为选中物体导入表情', icon_value=0, emboss=True, depress=False)
        row_F2AD3 = col_85326.row(heading='', align=True)
        row_F2AD3.alert = False
        row_F2AD3.enabled = True
        row_F2AD3.active = True
        row_F2AD3.use_property_split = False
        row_F2AD3.use_property_decorate = False
        row_F2AD3.scale_x = 1.0
        row_F2AD3.scale_y = 2.190999984741211
        row_F2AD3.alignment = 'Expand'.upper()
        row_F2AD3.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_F2AD3.operator('sna.operator_f1b3d', text='添加自动光圈焦点', icon_value=string_to_icon('CON_CAMERASOLVER'), emboss=True, depress=False)


class SNA_PT__30162(bpy.types.Panel):
    bl_label = '清理'
    bl_idname = 'SNA_PT__30162'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 1
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'SNA_PT_MMD_5DD0C'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        col_E927A = layout.column(heading='', align=False)
        col_E927A.alert = False
        col_E927A.enabled = True
        col_E927A.active = True
        col_E927A.use_property_split = False
        col_E927A.use_property_decorate = False
        col_E927A.scale_x = 1.0
        col_E927A.scale_y = 1.0
        col_E927A.alignment = 'Expand'.upper()
        col_E927A.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = col_E927A.operator('sna.operator020_173c4', text='清理自定义几何数据', icon_value=0, emboss=True, depress=False)
        op = col_E927A.operator('sna.operator022_d211d', text='清理空形态键关键帧', icon_value=0, emboss=True, depress=False)
        op = col_E927A.operator('sna.operator023_9e188', text='清除形态键上的驱动器', icon_value=0, emboss=True, depress=False)
        op = col_E927A.operator('sna.operator024_1bdb7', text='清除无用材质节点', icon_value=0, emboss=True, depress=False)
        op.sna_new_property = 0
        op = col_E927A.operator('sna.operator025_c68f6', text='清除骨骼修改器', icon_value=0, emboss=True, depress=False)


class SNA_PT__D880A(bpy.types.Panel):
    bl_label = '选择'
    bl_idname = 'SNA_PT__D880A'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 1
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'SNA_PT_MMD_5DD0C'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_7FD55 = layout.box()
        box_7FD55.alert = False
        box_7FD55.enabled = True
        box_7FD55.active = True
        box_7FD55.use_property_split = False
        box_7FD55.use_property_decorate = False
        box_7FD55.alignment = 'Expand'.upper()
        box_7FD55.scale_x = 1.0
        box_7FD55.scale_y = 1.0
        if not True: box_7FD55.operator_context = "EXEC_DEFAULT"
        col_BA6C8 = box_7FD55.column(heading='', align=False)
        col_BA6C8.alert = False
        col_BA6C8.enabled = True
        col_BA6C8.active = True
        col_BA6C8.use_property_split = False
        col_BA6C8.use_property_decorate = False
        col_BA6C8.scale_x = 1.0
        col_BA6C8.scale_y = 1.0
        col_BA6C8.alignment = 'Expand'.upper()
        col_BA6C8.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_4AFCF = col_BA6C8.row(heading='', align=False)
        row_4AFCF.alert = False
        row_4AFCF.enabled = True
        row_4AFCF.active = True
        row_4AFCF.use_property_split = False
        row_4AFCF.use_property_decorate = False
        row_4AFCF.scale_x = 1.0
        row_4AFCF.scale_y = 1.0
        row_4AFCF.alignment = 'Expand'.upper()
        row_4AFCF.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_4AFCF.operator('sna.operator_5ed64', text='根据贴图选择物体', icon_value=0, emboss=True, depress=False)
        op = row_4AFCF.operator('sna.operator001_1136e', text='选中相同材质的物体', icon_value=0, emboss=True, depress=False)
        row_0DF0B = col_BA6C8.row(heading='', align=False)
        row_0DF0B.alert = False
        row_0DF0B.enabled = True
        row_0DF0B.active = True
        row_0DF0B.use_property_split = False
        row_0DF0B.use_property_decorate = False
        row_0DF0B.scale_x = 1.0
        row_0DF0B.scale_y = 1.0
        row_0DF0B.alignment = 'Expand'.upper()
        row_0DF0B.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_0DF0B.operator('sna.my_generic_operator_400a9', text='选中骨架', icon_value=0, emboss=True, depress=False)
        op.sna_new_property = '腿ik骨'
        row_778C2 = col_BA6C8.row(heading='', align=False)
        row_778C2.alert = False
        row_778C2.enabled = (bpy.context.object.mode == 'EDIT')
        row_778C2.active = True
        row_778C2.use_property_split = False
        row_778C2.use_property_decorate = False
        row_778C2.scale_x = 1.0
        row_778C2.scale_y = 1.0
        row_778C2.alignment = 'Expand'.upper()
        row_778C2.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_778C2.operator('sna.my_generic_operator_acbd7', text='按位置选择顶点', icon_value=0, emboss=True, depress=False)
        op.sna_new_property_002 = 0.0
        op = row_778C2.operator('sna.my_generic_operator_4bd78', text='按编号选择顶点', icon_value=0, emboss=True, depress=False)
        op.sna_new_property = 0


class SNA_PT__92512(bpy.types.Panel):
    bl_label = '顶点色'
    bl_idname = 'SNA_PT__92512'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 3
    bl_parent_id = 'SNA_PT_MMD_5DD0C'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not ((not bpy.context.preferences.addons['mmd_quick_tool'].preferences.sna_new_property_001))

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        col_222AF = layout.column(heading='', align=False)
        col_222AF.alert = False
        col_222AF.enabled = True
        col_222AF.active = True
        col_222AF.use_property_split = False
        col_222AF.use_property_decorate = False
        col_222AF.scale_x = 1.0
        col_222AF.scale_y = 1.0
        col_222AF.alignment = 'Expand'.upper()
        col_222AF.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_BFA66 = col_222AF.row(heading='', align=False)
        row_BFA66.alert = False
        row_BFA66.enabled = True
        row_BFA66.active = True
        row_BFA66.use_property_split = False
        row_BFA66.use_property_decorate = False
        row_BFA66.scale_x = 1.0
        row_BFA66.scale_y = 1.0
        row_BFA66.alignment = 'Expand'.upper()
        row_BFA66.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_BFA66.operator('sna.my_generic_operator_e6bd2', text='添加顶点色属性', icon_value=0, emboss=True, depress=False)
        op.sna_new_property = '顶点色'
        op = row_BFA66.operator('sna.my_generic_operator_e9b48', text='移除顶点色属性', icon_value=0, emboss=True, depress=False)
        op.sna_new_property = ''


class SNA_PT_panel_D171F(bpy.types.Panel):
    bl_label = '分段渲染'
    bl_idname = 'SNA_PT_panel_D171F'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 2
    bl_parent_id = 'SNA_PT_MMD_0B0AC'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not ((not bpy.context.preferences.addons['mmd_quick_tool'].preferences.sna_new_property_004))

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        row_9BC54 = layout.row(heading='', align=False)
        row_9BC54.alert = False
        row_9BC54.enabled = True
        row_9BC54.active = True
        row_9BC54.use_property_split = False
        row_9BC54.use_property_decorate = False
        row_9BC54.scale_x = 1.0
        row_9BC54.scale_y = 1.0
        row_9BC54.alignment = 'Expand'.upper()
        row_9BC54.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        coll_id = display_collection_id('B793B', locals())
        row_9BC54.template_list('SNA_UL_display_collection_list_B793B', coll_id, bpy.context.scene, 'sna_render_list', bpy.context.scene, 'sna_render_list_id', rows=0)
        col_B28B3 = row_9BC54.column(heading='', align=True)
        col_B28B3.alert = False
        col_B28B3.enabled = True
        col_B28B3.active = True
        col_B28B3.use_property_split = False
        col_B28B3.use_property_decorate = False
        col_B28B3.scale_x = 1.0
        col_B28B3.scale_y = 1.0
        col_B28B3.alignment = 'Expand'.upper()
        col_B28B3.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = col_B28B3.operator('sna.add_render_list_84292', text='', icon_value=string_to_icon('ADD'), emboss=True, depress=False)
        op = col_B28B3.operator('sna.remove_render_list_e8059', text='', icon_value=string_to_icon('REMOVE'), emboss=True, depress=False)
        col_B28B3.separator(factor=1.6389999389648438)
        op = col_B28B3.operator('sna.up_b66ca', text='', icon_value=string_to_icon('TRIA_UP'), emboss=True, depress=False)
        op = col_B28B3.operator('sna.down_25ee0', text='', icon_value=string_to_icon('TRIA_DOWN'), emboss=True, depress=False)
        col_B28B3.separator(factor=1.4469999074935913)
        col_716D2 = col_B28B3.column(heading='', align=False)
        col_716D2.alert = False
        col_716D2.enabled = True
        col_716D2.active = True
        col_716D2.use_property_split = False
        col_716D2.use_property_decorate = False
        col_716D2.scale_x = 1.0
        col_716D2.scale_y = 1.0
        col_716D2.alignment = 'Expand'.upper()
        col_716D2.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = col_716D2.operator('sna.my_generic_operator_2032a', text='', icon_value=string_to_icon('CHECKMARK'), emboss=True, depress=False)
        col_34299 = layout.column(heading='', align=False)
        col_34299.alert = False
        col_34299.enabled = True
        col_34299.active = True
        col_34299.use_property_split = False
        col_34299.use_property_decorate = False
        col_34299.scale_x = 1.0
        col_34299.scale_y = 1.0
        col_34299.alignment = 'Expand'.upper()
        col_34299.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_9779E = col_34299.row(heading='', align=False)
        row_9779E.alert = bpy.context.scene.sna_is_render
        row_9779E.enabled = True
        row_9779E.active = True
        row_9779E.use_property_split = False
        row_9779E.use_property_decorate = False
        row_9779E.scale_x = 1.0
        row_9779E.scale_y = 1.0
        row_9779E.alignment = 'Expand'.upper()
        row_9779E.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_9779E.operator('sna.my_generic_operator_5874f', text=('正在渲染' if bpy.context.scene.sna_is_render else '开始渲染'), icon_value=0, emboss=True, depress=False)
        if bpy.context.scene.sna_is_render:
            row_42916 = col_34299.row(heading='', align=False)
            row_42916.alert = True
            row_42916.enabled = True
            row_42916.active = True
            row_42916.use_property_split = False
            row_42916.use_property_decorate = False
            row_42916.scale_x = 1.0
            row_42916.scale_y = 1.0
            row_42916.alignment = 'Center'.upper()
            row_42916.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            row_42916.label(text='正在进行    ' + bpy.context.scene.sna_render_list[bpy.context.scene.sna_render_list_id].name, icon_value=0)
            row_42916.label(text='第' + str(bpy.context.scene.frame_current) + '帧', icon_value=0)
        row_71992 = col_34299.row(heading='', align=False)
        row_71992.alert = False
        row_71992.enabled = True
        row_71992.active = True
        row_71992.use_property_split = False
        row_71992.use_property_decorate = False
        row_71992.scale_x = 1.0
        row_71992.scale_y = 1.0
        row_71992.alignment = 'Center'.upper()
        row_71992.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_71992.label(text='平均渲染时间(五次)  ' + str(node_tree_001['sna_avg_render_time']), icon_value=0)
        row_71992.label(text='还剩' + str(node_tree_001['sna_sub_frame']) + '帧', icon_value=0)
        row_71992.label(text='预计剩余' + str(round(float(node_tree_001['sna_avg_render_time'] * node_tree_001['sna_sub_frame']), abs(2))) + '秒', icon_value=0)


class SNA_PT_bake_tex_0E9C6(bpy.types.Panel):
    bl_label = '烘焙贴图'
    bl_idname = 'SNA_PT_bake_tex_0E9C6'
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 0
    bl_parent_id = 'SNA_PT_MMD_QUICK_TOOL_MATERIAL_67F0C'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        op = layout.operator('sna.bake_tex_f278f', text='烘焙当前预览', icon_value=0, emboss=True, depress=False)
        col_2ED0C = layout.column(heading='', align=True)
        col_2ED0C.alert = False
        col_2ED0C.enabled = True
        col_2ED0C.active = True
        col_2ED0C.use_property_split = False
        col_2ED0C.use_property_decorate = False
        col_2ED0C.scale_x = 1.0
        col_2ED0C.scale_y = 1.0
        col_2ED0C.alignment = 'Expand'.upper()
        col_2ED0C.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_2ED0C.prop(bpy.context.scene, 'sna_bake_tex_size_x', text='X', icon_value=0, emboss=True)
        col_2ED0C.prop(bpy.context.scene, 'sna_bake_tex_size_y', text='Y', icon_value=0, emboss=True)
        layout.prop(bpy.context.scene, 'sna_use_choose_tex', text='使用当前选中图像节点', icon_value=0, emboss=True)


class SNA_GROUP_sna_render_list_property(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(name='name', description='渲染任务名', default='', subtype='NONE', maxlen=0)
    start_frame: bpy.props.IntProperty(name='start_frame', description='', default=0, subtype='NONE')
    end_frame: bpy.props.IntProperty(name='end_frame', description='', default=0, subtype='NONE')
    render_camera: bpy.props.PointerProperty(name='render_camera', description='渲染队列使用的相机，空则使用场景活动相机', type=bpy.types.Object, update=sna_update_render_camera_28727)
    output_directory: bpy.props.StringProperty(name='output_directory', description='输出路径，空则使用输出中指定的路径', default='', subtype='FILE_PATH', maxlen=0)
    on: bpy.props.BoolProperty(name='on', description='是否使用队列', default=True)


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.utils.register_class(SNA_GROUP_sna_render_list_property)
    bpy.types.Scene.sna_bili = bpy.props.EnumProperty(name='bili', description='', items=[('自定义', '自定义', '', 0, 0), ('1:1', '1:1', '', 0, 1), ('3:2', '3:2', '', 0, 2), ('4:3', '4:3', '', 0, 3), ('16:9', '16:9', '', 0, 4), ('14:9', '14:9', '', 0, 5), ('1.85:1', '1.85:1', '', 0, 6), ('2.39:1', '2.39:1', '', 0, 7)], update=sna_update_sna_bili_31149)
    bpy.types.Scene.sna_new_property_003 = bpy.props.BoolProperty(name='切换中英文', description='切换中英文，快捷键ctrl+shift+e', default=True, update=sna_update_sna_new_property_003_B42B0)
    bpy.types.Scene.sna_render_list_id = bpy.props.IntProperty(name='render_list_id', description='渲染队列的id', default=0, subtype='NONE')
    bpy.types.Scene.sna_render_list = bpy.props.CollectionProperty(name='render_list', description='渲染队列集合', type=SNA_GROUP_sna_render_list_property)
    bpy.types.Scene.sna_is_render = bpy.props.BoolProperty(name='is_render', description='是否渲染', default=False)
    bpy.types.Scene.sna_time_show_is_change = bpy.props.BoolProperty(name='time_show_is_change', description='', default=True)
    bpy.types.Scene.sna_view_tex = bpy.props.BoolProperty(name='view_tex', description='贴图预览模式，快捷键ctrl+shift+t', default=False, update=sna_update_sna_view_tex_632AA)
    bpy.types.Scene.sna_remove_transform_constraint = bpy.props.BoolProperty(name='Remove_transform_constraint', description='', default=False)
    bpy.types.Scene.sna_bake_tex_size_x = bpy.props.IntProperty(name='bake_tex_size_x', description='', default=1024, subtype='NONE')
    bpy.types.Scene.sna_bake_tex_size_y = bpy.props.IntProperty(name='bake_tex_size_y', description='', default=1024, subtype='NONE')
    bpy.types.Scene.sna_use_choose_tex = bpy.props.BoolProperty(name='use_choose_tex', description='', default=False)
    bpy.types.Scene.sna_ik_fix_on = bpy.props.BoolProperty(name='ik_fix_on', description='', default=True, update=sna_update_sna_ik_fix_on_057DD)
    bpy.types.Scene.sna_display_time = bpy.props.BoolProperty(name='display_time', description='打开分秒显示', default=True)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_C8494)
    bpy.utils.register_class(SNA_OT_Ik_B204A)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_C3269)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_Cc136)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_89058)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_C034B)
    bpy.utils.register_class(SNA_OT_Uv_94B57)
    bpy.utils.register_class(SNA_OT_Uv_9201E)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_Bedaf)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_04Cf5)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_60634)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_Dd728)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_Fb95F)
    bpy.utils.register_class(SNA_OT_Abc_B0Bf3)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_Abaaa)
    bpy.utils.register_class(SNA_OT_Operator015_0Ebb1)
    bpy.types.DOPESHEET_HT_header.append(sna_add_to_dopesheet_ht_header_E775E)
    bpy.utils.register_class(SNA_OT_Operator024_D37Ce)
    bpy.utils.register_class(SNA_OT_Operator023_Dc120)
    bpy.utils.register_class(SNA_OT_Operator021_0D655)
    bpy.utils.register_class(SNA_OT_Operator005_9368B)
    bpy.utils.register_class(SNA_OT_Operator004_Fa32A)
    bpy.utils.register_class(SNA_OT_Operator025_4038C)
    bpy.utils.register_class(SNA_OT_Operator001_64C4A)
    bpy.utils.register_class(SNA_OT_Operator_B46A6)
    bpy.utils.register_class(SNA_OT_Operator007_85779)
    bpy.utils.register_class(SNA_OT_Operator008_F7B4C)
    bpy.utils.register_class(SNA_OT_Operator002_7Dbd9)
    bpy.utils.register_class(SNA_OT_Operator014_47F89)
    bpy.types.RENDER_PT_format.append(sna_add_to_render_pt_format_54259)
    bpy.utils.register_class(SNA_OT_Operator009_F9Bf5)
    bpy.utils.register_class(SNA_PT_MMD_0B0AC)
    bpy.utils.register_class(SNA_OT_Operator003_Da1Be)
    bpy.utils.register_class(SNA_OT_Operator010_18497)
    # bpy.types.TIME_MT_editor_menus.append(sna_add_to_time_mt_editor_menus_A1C9F)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_83D28)
    bpy.utils.register_class(SNA_PT_MMD_5DD0C)
    bpy.utils.register_class(SNA_OT_Operator020_173C4)
    bpy.utils.register_class(SNA_OT_Operator022_D211D)
    bpy.utils.register_class(SNA_OT_Operator023_9E188)
    bpy.utils.register_class(SNA_OT_Operator024_1Bdb7)
    bpy.utils.register_class(SNA_OT_Operator025_C68F6)
    bpy.utils.register_class(SNA_OT_Operator002_Ac0A6)
    bpy.types.VIEW3D_HT_tool_header.append(sna_add_to_view3d_ht_tool_header_80556)
    bpy.utils.register_class(SNA_OT_Operator001_1136E)
    bpy.utils.register_class(SNA_OT_Operator_5Ed64)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_400A9)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_E6Bd2)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_E9B48)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_0C8D6)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_4A59F)
    bpy.types.VIEW3D_MT_select_edit_mesh.append(sna_add_to_view3d_mt_select_edit_mesh_C0326)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_Acbd7)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_4Bd78)
    bpy.types.VIEW3D_MT_edit_mesh_context_menu.append(sna_add_to_view3d_mt_edit_mesh_context_menu_48850)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_C68A2)
    bpy.types.VIEW3D_MT_edit_mesh_vertices.append(sna_add_to_view3d_mt_edit_mesh_vertices_D20F4)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_32F6A)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_16Cb7)
    bpy.types.VIEW3D_MT_transform_object.append(sna_add_to_view3d_mt_transform_object_E49E0)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_A5A90)
    bpy.types.MESH_MT_shape_key_context_menu.append(sna_add_to_mesh_mt_shape_key_context_menu_B7E3D)
    bpy.types.DATA_PT_modifiers.prepend(sna_add_to_data_pt_modifiers_55FB3)
    bpy.utils.register_class(SNA_OT_Down_25Ee0)
    bpy.utils.register_class(SNA_OT_Up_B66Ca)
    bpy.utils.register_class(SNA_OT_Add_Render_List_84292)
    bpy.utils.register_class(SNA_OT_Remove_Render_List_E8059)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_5874F)
    bpy.app.handlers.render_complete.append(render_complete_handler_825EB)
    bpy.app.handlers.render_complete.append(render_complete_handler_C420C)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_33F13)
    bpy.app.handlers.render_cancel.append(render_cancel_handler_58683)
    bpy.app.handlers.render_post.append(render_post_handler_4E079)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_2032A)
    bpy.app.handlers.render_pre.append(render_pre_handler_7F068)
    bpy.app.handlers.render_post.append(render_post_handler_53081)
    bpy.types.OBJECT_PT_constraints.prepend(sna_add_to_object_pt_constraints_16F76)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_Cde4F)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_2B24E)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_39Ebf)
    bpy.types.GRAPH_MT_editor_menus.append(sna_add_to_graph_mt_editor_menus_9BAD1)
    bpy.utils.register_class(SNA_OT_Operator_F1B3D)
    bpy.utils.register_class(SNA_PT_MMD_QUICK_TOOL_MATERIAL_67F0C)
    bpy.utils.register_class(SNA_OT_Bake_Tex_F278F)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_7A93E)
    bpy.types.VIEW3D_MT_paint_weight.append(sna_add_to_view3d_mt_paint_weight_1FE39)
    bpy.types.VIEW3D_HT_tool_header.prepend(sna_add_to_view3d_ht_tool_header_CFA13)
    if not 'white.png' in _icons: _icons.load('white.png', os.path.join(os.path.dirname(__file__), 'icons', 'white.png'), "IMAGE")
    if not 'black.png' in _icons: _icons.load('black.png', os.path.join(os.path.dirname(__file__), 'icons', 'black.png'), "IMAGE")
    if not 'red.png' in _icons: _icons.load('red.png', os.path.join(os.path.dirname(__file__), 'icons', 'red.png'), "IMAGE")
    if not 'green.png' in _icons: _icons.load('green.png', os.path.join(os.path.dirname(__file__), 'icons', 'green.png'), "IMAGE")
    if not 'blue.png' in _icons: _icons.load('blue.png', os.path.join(os.path.dirname(__file__), 'icons', 'blue.png'), "IMAGE")
    if not 'yellow.png' in _icons: _icons.load('yellow.png', os.path.join(os.path.dirname(__file__), 'icons', 'yellow.png'), "IMAGE")
    if not 'purple.png' in _icons: _icons.load('purple.png', os.path.join(os.path.dirname(__file__), 'icons', 'purple.png'), "IMAGE")
    if not 'cyan.png' in _icons: _icons.load('cyan.png', os.path.join(os.path.dirname(__file__), 'icons', 'cyan.png'), "IMAGE")
    bpy.utils.register_class(SNA_OT_Operator001_05281)
    bpy.utils.register_class(SNA_OT_Operator003_D462C)
    bpy.utils.register_class(SNA_OT_Operator004_D6Bee)
    bpy.utils.register_class(SNA_OT_Operator005_2A676)
    bpy.utils.register_class(SNA_OT_Operator006_Dda67)
    bpy.utils.register_class(SNA_OT_Operator007_17Ad2)
    bpy.utils.register_class(SNA_OT_Operator008_A3Fb7)
    bpy.utils.register_class(SNA_OT_Operator002_2A623)
    bpy.utils.register_class(SNA_OT_Operator_6Aa4F)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_48003)
    bpy.utils.register_class(SNA_MT_3BB6D)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_8Ad72)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_A52B1)
    bpy.utils.register_class(SNA_AddonPreferences_C113E)
    bpy.utils.register_class(SNA_OT_My_Generic_Operator_763Af)
    bpy.utils.register_class(SNA_PT_IK_CC508)
    bpy.utils.register_class(SNA_PT_UV_5331C)
    bpy.utils.register_class(SNA_PT__35D62)
    bpy.utils.register_class(SNA_PT__E26FF)
    bpy.utils.register_class(SNA_PT__668A7)
    bpy.utils.register_class(SNA_PT__023F8)
    bpy.utils.register_class(SNA_PT__6062D)
    bpy.utils.register_class(SNA_PT_MMD_B11D3)
    bpy.utils.register_class(SNA_PT__30162)
    bpy.utils.register_class(SNA_PT__D880A)
    bpy.utils.register_class(SNA_PT__92512)
    bpy.utils.register_class(SNA_PT_panel_D171F)
    bpy.utils.register_class(SNA_UL_display_collection_list_B793B)
    bpy.utils.register_class(SNA_PT_bake_tex_0E9C6)
    kc = bpy.context.window_manager.keyconfigs.addon
    km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
    kmi = km.keymap_items.new('sna.operator002_ac0a6', 'T', 'PRESS',
        ctrl=True, alt=False, shift=True, repeat=False)
    addon_keymaps['21D05'] = (km, kmi)
    kc = bpy.context.window_manager.keyconfigs.addon
    km = kc.keymaps.new(name='Window', space_type='EMPTY')
    kmi = km.keymap_items.new('sna.my_generic_operator_0c8d6', 'E', 'PRESS',
        ctrl=True, alt=False, shift=True, repeat=False)
    addon_keymaps['3C33E'] = (km, kmi)
    kc = bpy.context.window_manager.keyconfigs.addon
    km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
    kmi = km.keymap_items.new('sna.operator_6aa4f', 'NUMPAD_1', 'PRESS',
        ctrl=False, alt=True, shift=False, repeat=False)
    addon_keymaps['FCCB2'] = (km, kmi)
    kc = bpy.context.window_manager.keyconfigs.addon
    km = kc.keymaps.new(name='Window', space_type='EMPTY')
    kmi = km.keymap_items.new('sna.my_generic_operator_48003', 'Q', 'PRESS',
        ctrl=True, alt=False, shift=True, repeat=False)
    addon_keymaps['D7D72'] = (km, kmi)


def unregister():
    global _icons
    if _icons is not None:
        bpy.utils.previews.remove(_icons)
        _icons = None
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        try:
            km.keymap_items.remove(kmi)
        except Exception:
            pass
    addon_keymaps.clear()
    del bpy.types.Scene.sna_display_time
    del bpy.types.Scene.sna_ik_fix_on
    del bpy.types.Scene.sna_use_choose_tex
    del bpy.types.Scene.sna_bake_tex_size_y
    del bpy.types.Scene.sna_bake_tex_size_x
    del bpy.types.Scene.sna_remove_transform_constraint
    del bpy.types.Scene.sna_view_tex
    del bpy.types.Scene.sna_time_show_is_change
    del bpy.types.Scene.sna_is_render
    del bpy.types.Scene.sna_render_list
    del bpy.types.Scene.sna_render_list_id
    del bpy.types.Scene.sna_new_property_003
    del bpy.types.Scene.sna_bili
    bpy.utils.unregister_class(SNA_GROUP_sna_render_list_property)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_C8494)
    bpy.utils.unregister_class(SNA_OT_Ik_B204A)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_C3269)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_Cc136)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_89058)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_C034B)
    bpy.utils.unregister_class(SNA_OT_Uv_94B57)
    bpy.utils.unregister_class(SNA_OT_Uv_9201E)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_Bedaf)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_04Cf5)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_60634)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_Dd728)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_Fb95F)
    bpy.utils.unregister_class(SNA_OT_Abc_B0Bf3)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_Abaaa)
    bpy.utils.unregister_class(SNA_OT_Operator015_0Ebb1)
    bpy.types.DOPESHEET_HT_header.remove(sna_add_to_dopesheet_ht_header_E775E)
    bpy.utils.unregister_class(SNA_OT_Operator024_D37Ce)
    bpy.utils.unregister_class(SNA_OT_Operator023_Dc120)
    bpy.utils.unregister_class(SNA_OT_Operator021_0D655)
    bpy.utils.unregister_class(SNA_OT_Operator005_9368B)
    bpy.utils.unregister_class(SNA_OT_Operator004_Fa32A)
    bpy.utils.unregister_class(SNA_OT_Operator025_4038C)
    bpy.utils.unregister_class(SNA_OT_Operator001_64C4A)
    bpy.utils.unregister_class(SNA_OT_Operator_B46A6)
    bpy.utils.unregister_class(SNA_OT_Operator007_85779)
    bpy.utils.unregister_class(SNA_OT_Operator008_F7B4C)
    bpy.utils.unregister_class(SNA_OT_Operator002_7Dbd9)
    bpy.utils.unregister_class(SNA_OT_Operator014_47F89)
    bpy.types.RENDER_PT_format.remove(sna_add_to_render_pt_format_54259)
    bpy.utils.unregister_class(SNA_OT_Operator009_F9Bf5)
    bpy.utils.unregister_class(SNA_PT_MMD_0B0AC)
    bpy.utils.unregister_class(SNA_OT_Operator003_Da1Be)
    bpy.utils.unregister_class(SNA_OT_Operator010_18497)
    # bpy.types.TIME_MT_editor_menus.remove(sna_add_to_time_mt_editor_menus_A1C9F)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_83D28)
    bpy.utils.unregister_class(SNA_PT_MMD_5DD0C)
    bpy.utils.unregister_class(SNA_OT_Operator020_173C4)
    bpy.utils.unregister_class(SNA_OT_Operator022_D211D)
    bpy.utils.unregister_class(SNA_OT_Operator023_9E188)
    bpy.utils.unregister_class(SNA_OT_Operator024_1Bdb7)
    bpy.utils.unregister_class(SNA_OT_Operator025_C68F6)
    bpy.utils.unregister_class(SNA_OT_Operator002_Ac0A6)
    bpy.types.VIEW3D_HT_tool_header.remove(sna_add_to_view3d_ht_tool_header_80556)
    bpy.utils.unregister_class(SNA_OT_Operator001_1136E)
    bpy.utils.unregister_class(SNA_OT_Operator_5Ed64)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_400A9)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_E6Bd2)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_E9B48)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_0C8D6)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_4A59F)
    bpy.types.VIEW3D_MT_select_edit_mesh.remove(sna_add_to_view3d_mt_select_edit_mesh_C0326)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_Acbd7)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_4Bd78)
    bpy.types.VIEW3D_MT_edit_mesh_context_menu.remove(sna_add_to_view3d_mt_edit_mesh_context_menu_48850)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_C68A2)
    bpy.types.VIEW3D_MT_edit_mesh_vertices.remove(sna_add_to_view3d_mt_edit_mesh_vertices_D20F4)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_32F6A)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_16Cb7)
    bpy.types.VIEW3D_MT_transform_object.remove(sna_add_to_view3d_mt_transform_object_E49E0)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_A5A90)
    bpy.types.MESH_MT_shape_key_context_menu.remove(sna_add_to_mesh_mt_shape_key_context_menu_B7E3D)
    bpy.types.DATA_PT_modifiers.remove(sna_add_to_data_pt_modifiers_55FB3)
    bpy.utils.unregister_class(SNA_OT_Down_25Ee0)
    bpy.utils.unregister_class(SNA_OT_Up_B66Ca)
    bpy.utils.unregister_class(SNA_OT_Add_Render_List_84292)
    bpy.utils.unregister_class(SNA_OT_Remove_Render_List_E8059)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_5874F)
    bpy.app.handlers.render_complete.remove(render_complete_handler_825EB)
    bpy.app.handlers.render_complete.remove(render_complete_handler_C420C)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_33F13)
    bpy.app.handlers.render_cancel.remove(render_cancel_handler_58683)
    bpy.app.handlers.render_post.remove(render_post_handler_4E079)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_2032A)
    bpy.app.handlers.render_pre.remove(render_pre_handler_7F068)
    bpy.app.handlers.render_post.remove(render_post_handler_53081)
    bpy.types.OBJECT_PT_constraints.remove(sna_add_to_object_pt_constraints_16F76)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_Cde4F)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_2B24E)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_39Ebf)
    bpy.types.GRAPH_MT_editor_menus.remove(sna_add_to_graph_mt_editor_menus_9BAD1)
    bpy.utils.unregister_class(SNA_OT_Operator_F1B3D)
    bpy.utils.unregister_class(SNA_PT_MMD_QUICK_TOOL_MATERIAL_67F0C)
    bpy.utils.unregister_class(SNA_OT_Bake_Tex_F278F)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_7A93E)
    bpy.types.VIEW3D_MT_paint_weight.remove(sna_add_to_view3d_mt_paint_weight_1FE39)
    bpy.types.VIEW3D_HT_tool_header.remove(sna_add_to_view3d_ht_tool_header_CFA13)
    bpy.utils.unregister_class(SNA_OT_Operator001_05281)
    bpy.utils.unregister_class(SNA_OT_Operator003_D462C)
    bpy.utils.unregister_class(SNA_OT_Operator004_D6Bee)
    bpy.utils.unregister_class(SNA_OT_Operator005_2A676)
    bpy.utils.unregister_class(SNA_OT_Operator006_Dda67)
    bpy.utils.unregister_class(SNA_OT_Operator007_17Ad2)
    bpy.utils.unregister_class(SNA_OT_Operator008_A3Fb7)
    bpy.utils.unregister_class(SNA_OT_Operator002_2A623)
    bpy.utils.unregister_class(SNA_OT_Operator_6Aa4F)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_48003)
    bpy.utils.unregister_class(SNA_MT_3BB6D)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_8Ad72)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_A52B1)
    bpy.utils.unregister_class(SNA_AddonPreferences_C113E)
    bpy.utils.unregister_class(SNA_OT_My_Generic_Operator_763Af)
    bpy.utils.unregister_class(SNA_PT_IK_CC508)
    bpy.utils.unregister_class(SNA_PT_UV_5331C)
    bpy.utils.unregister_class(SNA_PT__35D62)
    bpy.utils.unregister_class(SNA_PT__E26FF)
    bpy.utils.unregister_class(SNA_PT__668A7)
    bpy.utils.unregister_class(SNA_PT__023F8)
    bpy.utils.unregister_class(SNA_PT__6062D)
    bpy.utils.unregister_class(SNA_PT_MMD_B11D3)
    bpy.utils.unregister_class(SNA_PT__30162)
    bpy.utils.unregister_class(SNA_PT__D880A)
    bpy.utils.unregister_class(SNA_PT__92512)
    bpy.utils.unregister_class(SNA_PT_panel_D171F)
    bpy.utils.unregister_class(SNA_UL_display_collection_list_B793B)
    bpy.utils.unregister_class(SNA_PT_bake_tex_0E9C6)
