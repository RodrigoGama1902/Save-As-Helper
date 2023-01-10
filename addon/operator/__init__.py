
from .save_duplicate.op_save_duplicate import SAH_OP_SaveAsDuplicate 
from .relocate_links.op_relocate_links import SAH_OP_RelocateLinks

classes = (
    SAH_OP_SaveAsDuplicate, SAH_OP_RelocateLinks
)


def register_operators():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister_operators():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

    