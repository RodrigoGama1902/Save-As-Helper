#type:ignore

import bpy

class SAH_DataBlocks(bpy.types.PropertyGroup):
    
    worlds : bpy.props.BoolProperty(name="World", default=True) # type:ignore
    workspaces : bpy.props.BoolProperty(name="WorkSpace", default=True) # type:ignore
    textures : bpy.props.BoolProperty(name="Texture", default=True) # type:ignore
    images : bpy.props.BoolProperty(name="Image", default=True) # type:ignore
    scenes : bpy.props.BoolProperty(name="Scene", default=True) # type:ignore
    palettes : bpy.props.BoolProperty(name="Palette", default=True) # type:ignore
    objects : bpy.props.BoolProperty(name="Object", default=True) # type:ignore
    meshes : bpy.props.BoolProperty(name="Mesh", default=True) # type:ignore
    materials : bpy.props.BoolProperty(name="Material", default=True) # type:ignore
    collections : bpy.props.BoolProperty(name="Collection", default=True) # type:ignore
    cameras : bpy.props.BoolProperty(name="Camera", default=True) # type:ignore
    brushes : bpy.props.BoolProperty(name="Brush", default=True) # type:ignore
    armatures : bpy.props.BoolProperty(name="Armature", default=True) # type:ignore
    actions : bpy.props.BoolProperty(name="Action", default=True) # type:ignore

class SAH_AddonMainProps(bpy.types.PropertyGroup):
         
   data_blocks : bpy.props.PointerProperty(type=SAH_DataBlocks) # type:ignore