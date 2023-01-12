import bpy
import os
import shutil
import subprocess

from ...utils.addon import get_props
from ...utils.path import convert_to_absolute

from bpy_extras.io_utils import ImportHelper

# TODO For now, only absolute paths work

class SAH_OP_RelocateLinks(bpy.types.Operator, ImportHelper):
    """Relocate Resources"""

    bl_idname = "sah.relocate_links"
    bl_label = "SAH Relocate Links"
    bl_options = {'REGISTER', 'UNDO'}
        
    deep_save_as : bpy.props.BoolProperty(name="Deep Save As", default=True, description = "Instead of just copying link source files, each source file will be opened and saved in the new location, automatically updating relative links") # type:ignore
    do_not_duplicate : bpy.props.BoolProperty(name = "Dot Not Create Duplicates", default = True, description="Do not create duplicate link files from same source link, when necessary, different data-block types with same reference will have only one link file created") # type:ignore
    relocate_link_images : bpy.props.BoolProperty(name = "Relocate Link Images", default = True, description="Relocate images linked to the file") # type:ignore
    
    directory : bpy.props.StringProperty() # type:ignore
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "deep_save_as")  
        layout.prop(self, "do_not_duplicate") 
        layout.prop(self, "relocate_link_images")
    
    def save_simple_copy(self, old_path, new_path):
        '''Simply copy source file to another location'''
        
        shutil.copyfile(old_path, new_path)
    
    def save_deep_save_as(self, old_path, new_path):
        '''Open and save the file to the new location'''
        
        print("     Running deep save on: " + old_path)
        
        python_generator_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "generator_deep_save_as.py")
        
        cmd = [
            bpy.app.binary_path,
            "--background",
            "--factory-startup",
            "--python", python_generator_path,
            "--",
            "open_file:" + old_path,
            "save_path:" + new_path,
            "relocate_directory:" + self.directory,
            "relocate_images:" + str(self.relocate_link_images),
        ]
   
        p = subprocess.Popen(cmd, universal_newlines=True,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                                    
        for line in iter(p.stdout.readline,''): # type: ignore   
            #if line.startswith("Info: Saved"):
            #    print("     Saved: " + new_path)
            
            print(line, end='')
    
    def relocate_links(self, data_block):
        
        print("Searching for " + data_block + " links...")
                
        folder_link_directory = os.path.join(self.link_directory, data_block) 
        
        for data in getattr(bpy.data, data_block, []):
            
            if not data.library:
                continue
            
            original_path = convert_to_absolute(data.library.filepath)
            
            print(" Found link: " + data.name + " in " + original_path)
            
            if self.do_not_duplicate:
                if original_path.startswith(self.link_directory):
                    
                    print("     Link already relocated, skipping...")
                    print("     Link Directory: " + self.link_directory)
                    print("     Original Path: " + original_path)
                    
                    continue
            
            if not os.path.exists(folder_link_directory):
                os.makedirs(folder_link_directory)
            
            if not os.path.exists(original_path):
                print("     Source file does not exist: " + data.library.filepath)
                continue
            
            new_path = os.path.join(folder_link_directory, os.path.basename(original_path))
                        
            if self.deep_save_as:
                self.save_deep_save_as(original_path, new_path)
            else:
                self.save_simple_copy(original_path, new_path)
            
            # checking if convert to relative is necessary  
            if data.library.filepath.startswith("//"):
                new_path = bpy.path.relpath(new_path)
                            
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

        
        

        
            

    

        