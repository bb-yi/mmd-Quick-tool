# This module was split from the Serpens-generated mmd Quick tool source.


from .common import *


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
