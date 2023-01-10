import bpy

from .addon_props import SAH_AddonMainProps, SAH_DataBlocks


classes = (
    SAH_DataBlocks,
    SAH_AddonMainProps, 
)

def register_props():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
        
    bpy.types.Scene.save_as_helper = bpy.props.PointerProperty(type = SAH_AddonMainProps)
    
def unregister_props():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    
    del bpy.types.Scene.save_as_helper