import bpy
import re
from typing import List
from .utils.registration import *

from bpy.types import Operator

COLLECTION_NAME = "Space Switch Empties"
EMPTY_SUFFIX = "_space_switch"

#TODO: Get rid of operators
def make_space_switch_empties(bones: List[bpy.types.PoseBone]):
    '''
    Given a list of bones, make an empty for each and add a constraint to them to copy the respective bone's rotation
    '''
    bpy.ops.object.posemode_toggle() # Enter Object Mode
    armature_obj = bpy.context.selected_objects[0] # Get armature object
    empties=set()
    for bone in bones:
        bone_name = bone.name
        bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        new_empty = bpy.context.selected_objects[0]
        new_empty.name = f"{bone_name}{EMPTY_SUFFIX}"
        empties.add(new_empty)
        constraint = new_empty.constraints.new(type="COPY_ROTATION")
        constraint.target=armature_obj
        constraint.subtarget=bone_name
    bpy.ops.object.select_all(action='DESELECT')
    if COLLECTION_NAME not in bpy.data.collections:
        collection = bpy.data.collections.new(COLLECTION_NAME)
        bpy.context.scene.collection.children.link(collection)
    collection = bpy.data.collections[COLLECTION_NAME]
    for emp in empties:
        collection.objects.link(emp)
        bpy.context.scene.collection.objects.unlink(emp)
        emp.select_set(True)
    bpy.ops.object.posemode_toggle() # Enter Object Mode
    

class SpaceSwitch(Operator):
    """Generate Space Switching Empties"""
    bl_idname = "armature.make_space_switch"
    bl_label = "Generate Space Switching Empties"
    bl_options = {'UNDO'}

    def execute(self, context):
        bones= bpy.context.selected_pose_bones
        make_space_switch_empties(bones)

        return {'FINISHED'}

class MakeSpaceSwitchConstraint(Operator):
    bl_idname = "armature.finish_space_switch"
    bl_label = "Generate Space Switching Empties"
    bl_options = {'UNDO'}

    def execute(self, context):
        for bone in bpy.context.selected_pose_bones:
            bone_name = bone.name
            empty_name = bone_name+EMPTY_SUFFIX
            if empty_name in bpy.data.objects:
                constraint = bone.constraints.new(type="COPY_ROTATION")
                constraint.target = bpy.data.objects[empty_name]

        return {'FINISHED'}

class OffsetAnimation(Operator):
    bl_idname = "animation.offset_animation"
    bl_label = "Offset animations by n keyframes"
    bl_options = {'UNDO'}



    def execute(self, context):
        
        def _offset_keyframes(offset, bone):
            bone_name = bone.name
            empty_name = bone_name+EMPTY_SUFFIX
            if empty_name in bpy.data.objects:
                empty = bpy.data.objects[empty_name]
                anim_action = empty.animation_data.action
                if anim_action:
                    for fcurve in anim_action.fcurves:
                        for keyframe in fcurve.keyframe_points:
                            keyframe.co[0] += offset
            for child in bone.children:
                _offset_keyframes(offset + 1, child)

        offset = 1
        root_bone = bpy.context.selected_pose_bones[0]
        _offset_keyframes(0, root_bone)

        return {'FINISHED'}


classes = [SpaceSwitch, MakeSpaceSwitchConstraint, OffsetAnimation]

def register():
    register_classes(classes)


def unregister():
    unregister_classes(classes)
