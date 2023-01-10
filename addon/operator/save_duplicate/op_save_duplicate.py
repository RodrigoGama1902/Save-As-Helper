import bpy
import os

from ...addon_prefs.utility import get_prefs

class SAH_OP_SaveAsDuplicate(bpy.types.Operator):
    """Save a Duplicate File"""

    bl_idname = "sah.saveduplicatefile"
    bl_label = "Save As Duplicate File"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):

        if not bpy.data.is_saved:
            self.report({'WARNING'},
                                "Save This File first")
            return {'CANCELLED'} 

        prefs = get_prefs().addon_prefs

        if prefs.save_method == 's1':  
              
            bpy.ops.wm.save_as_mainfile(filepath = self._simple_save_duplicate(context))

        if prefs.save_method == 's2':
 
            bpy.ops.wm.save_as_mainfile(filepath = self._save_on_duplicate_folder(context), copy=True)
            bpy.ops.wm.save_as_mainfile()

        if prefs.save_method == 's3':
            
            save_directory = self._save_on_external_folder(context)
            
            if not save_directory:
                return {'CANCELLED'}
            
            bpy.ops.wm.save_as_mainfile(filepath = save_directory, copy=True)
            bpy.ops.wm.save_as_mainfile()
 
        self.report({'INFO'},
                                "Duplicate file saved")
        return {'FINISHED'}


    def _simple_save_duplicate(self, context):
        
        directory = os.path.dirname(bpy.data.filepath)
        
        filename = self._get_blend_file_name(context)
              
        prefs = get_prefs().addon_prefs
        
        to_check = filename[-1] 

        if to_check.isdigit():
            
            num_final = self._get_duplicate_number(filename)
         
            n_index = len(filename) - len(num_final)      
            name_nd = filename[:n_index]

            new_num = int(num_final)+ 1
            
            if prefs.add_separator:
                if name_nd:                
                    if name_nd[-1] != '_':
                        name_nd = name_nd + '_'

            filename = name_nd + str(new_num)                
            
        else:           
            if prefs.add_separator:
                if filename:                
                    if filename[-1] != '_':
                        filename = filename + '_'
            
            filename = filename + "1" 
                              
        return os.path.join(directory,filename + ".blend" )     
    
    
    def _save_on_duplicate_folder(self, context):
        
        props = context.scene.sahelper
        prefs = get_prefs().addon_prefs
        
        filename = self._get_blend_file_name(context)
   
        if prefs.add_filename:
                folder_name = prefs.duplicate_folder + ' - ' + filename
        else:
            folder_name = prefs.duplicate_folder
        
        folder_path = os.path.join(bpy.path.abspath("//"),folder_name)

        if not os.path.exists(folder_path):
            props.current_index = 1
            os.mkdir(folder_path)

            if prefs.add_separator:
                filename = filename + '_'
            
            name = filename + str(props.current_index)

        else:

            if prefs.add_separator:
                filename = filename + '_'
            
            name = filename + str(props.current_index)

        props.current_index += 1
        
        return os.path.join(folder_path,name + ".blend")
    
    
    def _save_on_external_folder(self, context):
        
        props = context.scene.sahelper
        prefs = get_prefs().addon_prefs
        
        filename = self._get_blend_file_name(context)
        
        folder_name = os.path.splitext(bpy.data.filepath)[0] # Get Blend Path without extension
        folder_name = bpy.path.basename(folder_name) # Get Blend File Name
        
        folder_path = os.path.join(prefs.external_directory,folder_name)
        
        if os.path.exists(folder_path) and props.current_index == 0:
            self.report({'ERROR'},"Duplicate Folder Already Exists, Change This File Name To Save It")
            return None
                
        if not os.path.exists(folder_path):
              
            props.current_index = 0
            os.mkdir(folder_path)

        if prefs.add_separator:
            
            filename = filename + '_'
        
        name = filename + str(props.current_index)
        
        props.current_index += 1
        
        save_directory = os.path.join(folder_path, name + ".blend")
        
        if os.path.exists(save_directory):
            self.report({'ERROR'},"Duplicate File Already Exists, Change This File Name To Save It")
            return None

        return os.path.join(folder_path, name + ".blend")
        
    @staticmethod
    def _get_duplicate_number(filename):
        
        filenumber = ""

        for n in reversed(filename):
            if not n.isdigit():
                break
            else:
                filenumber += n
        
        return filenumber
    
    @staticmethod
    def _get_blend_file_name(context):
        
        name = bpy.path.basename(context.blend_data.filepath)
        
        if name.endswith(".blend"):   
            return name[0:-6]
        if name.endswith(".blend1"):   
            return name[0:-7]
        
        return name
            

    

        