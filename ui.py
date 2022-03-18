import bpy

from .operator_make_target_bones import MakeTargetBones


class MakeTargetBonePanel(bpy.types.Panel):
    """Makes panel in mesh edit context in the 3D view side panel"""
    bl_label = "Make Target Bone"
    bl_idname = "EDIT_PT_make_tgt_bone_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Edit'
    bl_context = "armature_edit"
    bl_options = {'DEFAULT_CLOSED'}
    
    @classmethod
    def poll(cls, context):
        return context.mode in ['EDIT_ARMATURE']

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator(MakeTargetBones.bl_idname, text="Generate Target Bones")


def register():
    bpy.utils.register_class(MakeTargetBonePanel)


def unregister():
    bpy.utils.unregister_class(MakeTargetBonePanel)
