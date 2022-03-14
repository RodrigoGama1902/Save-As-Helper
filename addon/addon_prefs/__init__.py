import bpy

from .addon import SAH_Prefs, SAH_Addon_Props
from .preferences_prop import SAH_Preferences_Props

classes = (
    SAH_Addon_Props, SAH_Preferences_Props, SAH_Prefs
)

def register_properties():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    
    bpy.types.Scene.sahelper = bpy.props.PointerProperty(type=SAH_Addon_Props)

        

def unregister_properties():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    
    del bpy.types.Scene.sahelper

       