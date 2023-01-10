import bpy
import os
import shutil
import subprocess

from ...utils.addon import get_props

from bpy_extras.io_utils import ImportHelper

# TODO Do not allow duplicate link files
# TODO This relocate links operator should run recursively, so source link files with links should be changed too
# TODO Implement possibility to also relocate textures of source links, so everything will be in the same folder

class SAH_OP_RelocateLinks(bpy.types.Operator, ImportHelper):
    """Relocate Resources"""

    bl_idname = "sah.relocate_links"
    bl_label = "SAH Relocate Links"
    bl_options = {'REGISTER', 'UNDO'}
        
    deep_save_as : bpy.props.BoolProperty(name="Deep Save As", default=True, description = "Instead of just copying link source files, each source file will be opened and saved in the new location, automatically updating relative links") # type:ignore
    do_not_duplicate : bpy.props.BoolProperty(name = "Dot Not Create Duplicates", default = True, description="Do not create duplicate link files from same source link, when necessary, different data-block types with same reference will have only one link file created") # type:ignore
    
    directory : bpy.props.StringProperty() # type:ignore
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "deep_save_as")  
        layout.prop(self, "do_not_duplicate") 
    
    def save_simple_copy(self, old_path, new_path):
        '''Simply copy source file to another location'''
        
        shutil.copyfile(old_path, new_path)
    
    @staticmethod
    def save_deep_save_as(old_path, new_path):
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
                
        folder_link_directory = os.path.join(self.link_directory, data_block) 
        
        for data in getattr(bpy.data, data_block, []):
            
            if not data.library:
                continue
            
            old_path = data.library.filepath
            
            print(" Found link: " + data.name + " in " + old_path)
            
            if self.do_not_duplicate:
                if old_path.startswith(self.link_directory):
                    print("     Link already relocated, skipping...")
                    continue
            
            if not os.path.exists(folder_link_directory):
                os.makedirs(folder_link_directory)
            
            if not os.path.exists(data.library.filepath):
                print("     Source file does not exist: " + data.library.filepath)
                continue
            
            old_path = data.library.filepath
            new_path = os.path.join(folder_link_directory, os.path.basename(data.library.filepath))
            
            if self.deep_save_as:
                self.save_deep_save_as(old_path, new_path)
            else:
                self.save_simple_copy(old_path, new_path)
                
            data.library.filepath = new_path            
         
    def execute(self, context):
        
        props = get_props()
        self.link_directory = os.path.join(self.directory, "links")
        
        if not os.path.exists(self.directory):
            self.report({'ERROR'}, "Directory does not exist")
            return {'CANCELLED'}
        
        print("\nRelocating Links...\n")
        
        for data_block in props.data_blocks.__annotations__:
            if getattr(props.data_blocks, data_block) == False:
                continue
        
            self.relocate_links(data_block)
            
        return {'FINISHED'}

        
        

        
            

    

        