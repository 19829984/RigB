# RigB
Collection of rigging tools and macros made by me. 

# How to use
## Make Target Bone
UI located in Edit mode for an armature as a side panel button (Edit -> Make Target Bone)

This script will make a target bone for all selected bones and rename it by:
* Replacing everything before the first '-' or '_' character with 'tgt'
* If neither character are present, add 'tgt-' as a prefix

**MAKE SURE** that all bones have unique names without blender's default '.00x' suffix, this will break the script. 
