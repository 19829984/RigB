import bpy

from .operator_make_target_bones import MakeTargetBones
from .space_switch import *
from .utils.registration import *


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

class SpaceSwitchPanel(bpy.types.Panel):
    """Make panel in pose mode context for space switching"""
    bl_label = "Space Switching"
    bl_idname = "POSE_PT_space_switch_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Animation'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.mode in ['POSE']

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator(SpaceSwitch.bl_idname, text="Make Space Switching Empties")
        row.operator(MakeSpaceSwitchConstraint.bl_idname, text="Make Constraints")
        row = layout.row()
        row.operator(OffsetAnimation.bl_idname, text="Shift Keyframes")

ui = [MakeTargetBonePanel, SpaceSwitchPanel]

def register():
    register_classes(ui)


def unregister():
    unregister_classes(ui)
