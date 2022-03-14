import bpy

from .fastsavebackup import Fast_Save_Backup_SaveAsHelper 


classes = (
    Fast_Save_Backup_SaveAsHelper,
)


def register_operators():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

        


def unregister_operators():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

    