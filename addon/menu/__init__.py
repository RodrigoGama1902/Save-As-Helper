import bpy

def sah_unpack_draw(self, context):
    
    # menu separator
    
    self.layout.separator()
    
    self.layout.operator("sah.relocate_links")

def register_menus():
    bpy.types.TOPBAR_MT_file_external_data.append(sah_unpack_draw)
    
def unregister_menus():
    bpy.types.TOPBAR_MT_file_external_data.remove(sah_unpack_draw)