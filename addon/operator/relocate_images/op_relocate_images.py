import bpy
import os
import shutil

from bpy_extras.io_utils import ImportHelper

class SAH_OP_RelocateImages(bpy.types.Operator, ImportHelper):
    """Relocate Resources"""

    bl_idname = "sah.relocate_images"
    bl_label = "SAH Relocate Images"
    bl_options = {'REGISTER', 'UNDO'}
    
    directory : bpy.props.StringProperty() # type:ignore
    ignore_packed_textures : bpy.props.BoolProperty(default = False) # type:ignore
     
    def execute(self, context):
        
        textures_directory = os.path.join(self.directory, "textures")
        
        if not os.path.exists(self.directory):
            self.report({'ERROR'}, "Directory does not exist")
            return {'CANCELLED'}
        
        print("\nRelocating Images...\n")
        
        for image in bpy.data.images:
                        
            if image.packed_file:
                if not self.ignore_packed_textures:
                    image.unpack()
                else:
                    print("Ignoring packed image: " + image.name)
                continue
            
            original_path = image.filepath_from_user()
            
            new_path = os.path.join(textures_directory, os.path.basename(original_path))
   
            if not os.path.exists(original_path):
                print("Image Not Found: " + original_path)
                continue

            print("Image found: " + original_path)
            print(" Relocating to: " + new_path)
            
            if not os.path.exists(textures_directory):
                os.makedirs(textures_directory)
            
            try:            
                shutil.copyfile(original_path, new_path)
            except Exception as e:
                print("Error: " + str(e))
                continue
            
            image.filepath = new_path

        return {'FINISHED'}

        
        

        
            

    

        