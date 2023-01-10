import bpy

def sah_relocate_menu_draw(self, context):
    
    self.layout.separator()
    self.layout.operator("sah.relocate_links")
    self.layout.operator("sah.relocate_images")

def sah_save_menu_draw(self, context):
    
    self.layout.separator()
    self.layout.operator("sah.save_and_relocate")  

def register_menus():
    bpy.types.TOPBAR_MT_file_external_data.append(sah_relocate_menu_draw)
    bpy.types.TOPBAR_MT_file.append(sah_save_menu_draw)
    
def unregister_menus():
    bpy.types.TOPBAR_MT_file_external_data.remove(sah_relocate_menu_draw)
    bpy.types.TOPBAR_MT_file.remove(sah_save_menu_draw)