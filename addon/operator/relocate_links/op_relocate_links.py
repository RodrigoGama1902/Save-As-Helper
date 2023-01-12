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
        
    do_not_duplicate : bpy.props.BoolProperty(name = "Dot Not Create Duplicates", default = True, description="Do not create duplicate link files from same source link, when necessary, different data-block types with same reference will have only one link file created") # type:ignore
    relocate_link_images : bpy.props.BoolProperty(name = "Relocate Link Images", default = True, description="Relocate images linked to the file") # type:ignore
    
    directory : bpy.props.StringProperty() # type:ignore
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "do_not_duplicate") 
        layout.prop(self, "relocate_link_images")
        
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
            #print(line, end='')             
            if line.startswith("Info: Saved"):
                print("     Saved: " + new_path)   
                
    
    def relocate_library(self, librarie):
        
        print(f"\nRelocating {librarie.name}\n")
                
        if not librarie:
            return False
        
        if not os.path.exists(self.link_directory):
            os.mkdir(self.link_directory)
        
        original_path = convert_to_absolute(librarie.filepath)
        
        print(" Found link: " + librarie.name + " in " + original_path)
        
        if self.do_not_duplicate:
            if original_path.startswith(self.link_directory):  
                print("     Link already relocated, skipping...")                    
                return False
                    
        if not os.path.exists(original_path):
            print("     Source file does not exist: " + librarie.filepath)
            return False
        
        new_path = os.path.join(self.link_directory, os.path.basename(original_path))

        self.save_deep_save_as(original_path, new_path)

        if librarie.filepath.startswith("//"):
            new_path = bpy.path.relpath(new_path)
                        
        librarie.filepath = new_path    
        
        return True        
         
    def execute(self, context):
        
        self.link_directory = os.path.join(self.directory, "links")
        
        if not os.path.exists(self.directory):
            self.report({'ERROR'}, "Directory does not exist")
            return {'CANCELLED'}
        
        for librarie in bpy.data.libraries:       
            self.relocate_library(librarie)
            
        return {'FINISHED'}

        
        

        
            

    

        