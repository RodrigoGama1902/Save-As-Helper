import bpy

from .save_duplicate import SAH_OP_SaveAsDuplicate 


classes = (
    SAH_OP_SaveAsDuplicate,
)


def register_operators():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister_operators():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

    