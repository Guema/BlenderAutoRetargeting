import bpy

def normlize_BVH():
    """ this function make the bvh suitable for riggify"""

    bpy.ops.object.rotation_euler[2] = -0.785398
    bpy.context.space_data.context = 'OBJECT'
