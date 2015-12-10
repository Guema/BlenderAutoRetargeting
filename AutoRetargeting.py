import bpy


def normlize_BVH(animation):
    """ this function make the bvh suitable for riggify"""

    print(animation)
    bpy.context.object.rotation_euler[2] = -0.785398
    return


def retarget(rig, animation):
    """ this function retarget context animation on rig"""
    # bpy.context.space_data.context = 'OBJECT'
    bpy.data.armature[animation.name]
    return

if len(bpy.context.selected_objects) == 1:
    BvhAnimation = bpy.context.selected_objects[0]
    Rig = bpy.ops.object.armature_human_metarig_add()

normlize_BVH(BvhAnimation)
retarget(Rig, BvhAnimation)
