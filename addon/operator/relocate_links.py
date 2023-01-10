import bpy
import os
import shutil

from ..utils.addon import get_props

from bpy_extras.io_utils import ImportHelper

class SAH_OP_RelocateLinks(bpy.types.Operator, ImportHelper):
    """Relocate Resources"""

    bl_idname = "sah.relocate_links"
    bl_label = "SAH Relocate Links"
    bl_options = {'REGISTER', 'UNDO'}
    
    textures : bpy.props.BoolProperty(name="Textures", default=True) # type:ignore
    links : bpy.props.BoolProperty(name="Links", default=True) # type:ignore
    
    copy : bpy.props.BoolProperty(name="Copy", default=True) # type:ignore
    
    directory : bpy.props.StringProperty() # type:ignore 
    
    def relocate_links(self, data_block):
        
        # TODO For now, the new file links are just copying the original link file to location, should have an option
        # to open and save the file to this new location.
        
        folder_link_directory = os.path.join(self.directory, "links", data_block) 
        data_collection = getattr(bpy.data, data_block, None)

        if not data_collection:
            return False
        
        for data in data_collection:
            if data.library:
                
                if not os.path.exists(folder_link_directory):
                    os.makedirs(folder_link_directory)
                
                if not os.path.exists(data.library.filepath):
                    continue
                
                new_filepath = os.path.join(folder_link_directory, os.path.basename(data.library.filepath))
                
                if self.copy:
                    shutil.copyfile(data.library.filepath, new_filepath)
                    
                data.library.filepath = new_filepath
         
    def execute(self, context):
        
        props = get_props()
        
        if not os.path.exists(self.directory):
            self.report({'ERROR'}, "Directory does not exist")
            return {'CANCELLED'}
        
        for data_block in props.data_blocks.__annotations__:
            if getattr(props.data_blocks, data_block) == False:
                continue
            
            print(">" + data_block)
            
            self.relocate_links(data_block)
            
        return {'FINISHED'}

        
        

        
            

    

        