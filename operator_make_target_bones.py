import bpy
import re

from bpy.types import Operator


class MakeTargetBones(Operator):
    """Make Target Bones from Deformation Bones"""
    bl_idname = "armature.make_target_bones" 
    bl_label = "Make Target Bones from Deformation Bones"
    

    def execute(self, context):
        armature_obj = bpy.context.selected_objects[0] # Get armature object
        def_bones_edit = bpy.context.selected_bones
        def_bones_pose_dict = {def_bone_edit.name : armature_obj.pose.bones[def_bone_edit.name] for def_bone_edit in def_bones_edit} # Make dictionary of pose bones from selected edit bones, with name as key
        
        bpy.ops.armature.duplicate() # Duplicate rig to make target bones
        
        
        bpy.ops.object.posemode_toggle() # Enter pose mode
        
        tgt_bones_pose = bpy.context.selected_pose_bones
        
        for tgt_bone_pose in tgt_bones_pose:
            trimmed_tgt_bone_name = tgt_bone_pose.name[:-4]
            def_bone_pose = def_bones_pose_dict[trimmed_tgt_bone_name] # Get corresponding deformation bone
            
            # Rename bone
            bone_name = re.search("^[^-_]*(.*)", trimmed_tgt_bone_name) # Capture string ater first "-" or "_" character
            bone_name = "-" + trimmed_tgt_bone_name if bone_name.groups()[0] == '' else bone_name.groups()[0] # If no match found then just use current name
            tgt_bone_pose.name = 'TGT' + bone_name
            
            # Disable Deformation
            tgt_bone_pose.bone.use_deform = False
            
            # Add constraint
            cpy_transform = def_bone_pose.constraints.new(type='COPY_TRANSFORMS') # Add copy transform to pose deformation bone
            cpy_transform.target = armature_obj 
            cpy_transform.subtarget = tgt_bone_pose.name # Set target to the target bone
        
        bpy.ops.object.editmode_toggle() # Return to edit mode
        
        return {'FINISHED'}

def register():
    bpy.utils.register_class(MakeTargetBones)


def unregister():
    bpy.utils.unregister_class(MakeTargetBones)
