import bpy
import os
import shutil
import subprocess

from ...utils.addon import get_props

from bpy_extras.io_utils import ImportHelper

class SAH_OP_RelocateLinks(bpy.types.Operator, ImportHelper):
    """Relocate Resources"""

    bl_idname = "sah.relocate_links"
    bl_label = "SAH Relocate Links"
    bl_options = {'REGISTER', 'UNDO'}
    
    textures : bpy.props.BoolProperty(name="Textures", default=True) # type:ignore
    links : bpy.props.BoolProperty(name="Links", default=True) # type:ignore
    
    copy : bpy.props.BoolProperty(name="Copy", default=True) # type:ignore
    deep_save_as : bpy.props.BoolProperty(name="Deep Save As", default=True) # type:ignore
    
    directory : bpy.props.StringProperty() # type:ignore 
    
    def save_simple_copy(self, old_path, new_path):
        '''Simply copy source file to another location'''
                                
        if self.copy:
            shutil.copyfile(old_path, new_path)
            
    def save_deep_save_as(self, old_path, new_path):
        '''Open and save the file to the new location'''
        
        python_generator_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "generator_deep_save_as.py")
        
        cmd = [
            bpy.app.binary_path,
            "--background",
            "--factory-startup",
            "--python", python_generator_path,
            "--",
            "open_file:" + old_path,
            "save_path:" + new_path,
        ]
   
        p = subprocess.Popen(cmd, universal_newlines=True,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                                    
        for line in iter(p.stdout.readline,''): # type: ignore   
            if line.startswith("Info: Saved"):
                print("     Saved: " + new_path)
    
    def relocate_links(self, data_block):
        
        print("Searching for " + data_block + " links...")
                
        folder_link_directory = os.path.join(self.directory, "links", data_block) 
        data_collection = getattr(bpy.data, data_block, None)

        if not data_collection:
            return False
        
        for data in data_collection:
            
            if data.library:
                
                print(" Found link: " + data.name + " in " + data.library.filepath)
                
                if not os.path.exists(folder_link_directory):
                    os.makedirs(folder_link_directory)
                
                if not os.path.exists(data.library.filepath):
                    continue
                
                new_path = os.path.join(folder_link_directory, os.path.basename(data.library.filepath))
                old_path = data.library.filepath
                
                if self.deep_save_as:
                    self.save_deep_save_as(old_path, new_path)
                else:
                    self.save_simple_copy(old_path, new_path)
                    
                data.library.filepath = new_path
         
    def execute(self, context):
        
        props = get_props()
        
        if not os.path.exists(self.directory):
            self.report({'ERROR'}, "Directory does not exist")
            return {'CANCELLED'}
        
        print("\nRelocating Links...\n")
        
        for data_block in props.data_blocks.__annotations__:
            if getattr(props.data_blocks, data_block) == False:
                continue
        
            self.relocate_links(data_block)
            
        return {'FINISHED'}

        
        

        
            

    

        