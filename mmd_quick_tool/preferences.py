# This module was split from the Serpens-generated mmd Quick tool source.


from .common import *


class SNA_AddonPreferences_C113E(bpy.types.AddonPreferences):
    bl_idname = __package__
    sna_display_time: bpy.props.BoolProperty(name='display_time', description='', default=True)
    sna_new_property: bpy.props.BoolProperty(name='快速设置分辨率界面', description='', default=True)
    sna_new_property_001: bpy.props.BoolProperty(name='顶点色工具', description='', default=True)
    sna_new_property_002: bpy.props.BoolProperty(name='添加变换约束工具', description='', default=True)
    sna_new_property_003: bpy.props.BoolProperty(name='着色器贴图烘焙', description='', default=True)
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
            row_D5B1E.prop(get_addon_preferences(), 'sna_display_time', text='显示分秒', icon_value=0, emboss=True)
            row_D5B1E.prop(get_addon_preferences(), 'sna_new_property', text='快速设置分辨率界面', icon_value=0, emboss=True)
            row_D5B1E.prop(get_addon_preferences(), 'sna_new_property_001', text='顶点色工具', icon_value=0, emboss=True)
            row_D5B1E.prop(get_addon_preferences(), 'sna_new_property_002', text='约束工具', icon_value=0, emboss=True)
            row_D5B1E.prop(get_addon_preferences(), 'sna_new_property_003', text='着色器贴图烘焙', icon_value=0, emboss=True)
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
            row_F8ACB.prop(get_addon_preferences(), 'sna_new_property_005', text='使用快速饼菜单', icon_value=0, emboss=True)
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
