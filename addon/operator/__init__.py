
from .save_duplicate.op_save_duplicate import SAH_OP_SaveAsDuplicate 
from .save_and_relocate.op_save_and_relocate import SAH_OP_SaveAndRelocate

from .relocate_links.op_relocate_links import SAH_OP_RelocateLinks
from .relocate_images.op_relocate_images import SAH_OP_RelocateImages


classes = (
    SAH_OP_SaveAsDuplicate, 
    SAH_OP_SaveAndRelocate,
    SAH_OP_RelocateLinks,
    SAH_OP_RelocateImages
)


def register_operators():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister_operators():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

    