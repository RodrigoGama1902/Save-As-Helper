import bpy
import os
from ..addon_prefs.utility import addon_name, get_prefs

class Fast_Save_Backup_SaveAsHelper(bpy.types.Operator):
    """Create a new file in the same directory with a number added in the end of the file name"""

    bl_idname = "sah.fastsavebackup"
    bl_label = "Save As Duplicate File"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):

        if not bpy.data.is_saved:
            self.report({'WARNING'},
                                "Save This File first")
            return {'CANCELLED'} 

        prefs = get_prefs()
        props = bpy.context.scene.sahelper
        mytool = prefs.addon_prefs

        #File Path of the blend file (With Blend File Name)
        filepath = bpy.data.filepath
        #File Path without Name
        directory = os.path.dirname(filepath)
        #Blend File Name
        name = bpy.path.basename(bpy.context.blend_data.filepath)
        new_name = name[0:-6]

        if mytool.save_method == 's1':  

            to_check = new_name[-1] 

            if to_check.isdigit():

                num_final = []

                for n in reversed(new_name):
                    if not n.isdigit():
                        break
                    else:
                        num_final.append(n)
                
                num_final = ''.join(num_final)[::-1]

                # Name without Digit            
                n_index = len(new_name) - len(num_final)      
                name_nd = new_name[:n_index]

                # New Num

                num_final = int(num_final)
                new_num = num_final + 1

                # New Name

                if mytool.add_separator:

                    if name_nd:                
                        if name_nd[-1] != '_':
                            name_nd = name_nd + '_'

                new_name = name_nd + str(new_num)     
                directory = directory + f'\{new_name}' + ".blend"

                #Save the file with the new name                       
                bpy.ops.wm.save_as_mainfile(filepath=directory) 
                
            else:

                if mytool.add_separator:
                    if new_name:                
                        if new_name[-1] != '_':
                            new_name = new_name + '_'
                
                new_name = new_name + "1"         
                directory = directory + f'\{new_name}' + ".blend"         
                bpy.ops.wm.save_as_mainfile(filepath=directory)

        if mytool.save_method == 's2':

            if mytool.add_filename:
                folder_name = mytool.duplicate_folder + ' - ' + new_name
            else:
                folder_name = mytool.duplicate_folder
            
            folder_path = os.path.join(bpy.path.abspath("//"),folder_name)

            if not os.path.exists(folder_path):
                props.current_index = 1
                os.mkdir(folder_path)

                if mytool.add_separator:
                    new_name = new_name + '_'
                
                name = new_name + str(props.current_index)

                bpy.ops.wm.save_as_mainfile(filepath=os.path.join(folder_path,name + ".blend"),copy=True)              
                bpy.ops.wm.save_as_mainfile()
                props.current_index += 1

            else:

                if mytool.add_separator:
                    new_name = new_name + '_'
                
                name = new_name + str(props.current_index)

                bpy.ops.wm.save_as_mainfile(filepath=os.path.join(folder_path,name + ".blend"),copy=True)
                bpy.ops.wm.save_as_mainfile()
                props.current_index += 1
        
        if mytool.save_method == 's3':
            
            folder_name = os.path.splitext(bpy.data.filepath)[0] # Get Blend Path without extension
            folder_name = bpy.path.basename(folder_name) # Get Blend File Name
            
            folder_path = os.path.join(mytool.external_directory,folder_name)
            
            if not os.path.exists(folder_path):
                
                props.current_index = 1
                os.mkdir(folder_path)

            if mytool.add_separator:
                new_name = new_name + '_'
            
            name = new_name + str(props.current_index)

            bpy.ops.wm.save_as_mainfile(filepath=os.path.join(folder_path, name + ".blend"),copy=True)
            bpy.ops.wm.save_as_mainfile()
            props.current_index += 1
        
        self.report({'INFO'},
                                "Duplicate file saved")
        return {'FINISHED'}
    

        