import bpy

from bpy.props import PointerProperty

from .utility import addon_name, get_prefs

from .preferences_prop import SAH_Preferences_Props

from bpy.props import (IntProperty,)



class SAH_Prefs(bpy.types.AddonPreferences):    
    bl_idname = addon_name

    # Property Groups
    addon_prefs: PointerProperty(type=SAH_Preferences_Props)
    
    def draw(self, context):

        prefs = get_prefs()
        mytool = prefs.addon_prefs
        layout = self.layout

        box = layout.box()
        box.label(text='Settings:')
        box.prop(mytool, 'add_separator')
        box.prop(mytool, 'save_method')

        if mytool.save_method == 's2':
            box_s = box.box()
            box_s.prop(mytool, 'duplicate_folder')
            box_s.prop(mytool, 'add_filename')
            if mytool.add_filename:
                row_box = box_s.row()
                
                split = row_box.split(factor=0.25)
                split.label(text='Folder Name Example:')
                box = split.box()
                box.label(text=f'"{mytool.duplicate_folder} - FileName"')
        
        if mytool.save_method == 's3':
            
            box_s = box.box()
            box_s.prop(mytool, 'external_directory')

class SAH_Addon_Props(bpy.types.PropertyGroup):
    
    current_index: IntProperty(default=0)






     

 