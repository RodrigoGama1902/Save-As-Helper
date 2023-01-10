# type:ignore

import bpy

class SAH_Preferences_Props(bpy.types.PropertyGroup):

    # Save as Properties
    add_separator : bpy.props.BoolProperty(name=" Add Separator Before Numbers", default = True, description = "Add a separator before numbers in the duplicaded file name") 

    save_method : bpy.props.EnumProperty(
        name= 'Save Method',
        description = 'Select a Save Method',
        default = 's3',
        items = [
            ('s3','Save in External Folder', ''),
            ('s2','Save in Duplicates Folder', ''),
            ('s1','Simple Duplicate', ''),
        ]        
    )
    
    use_external_directory : bpy.props.BoolProperty(name=" Use External Directory", default = False, description = "Use other directory to save duplicates") 
    external_directory : bpy.props.StringProperty(subtype = 'DIR_PATH', name="External Directory", default = "D:\\Studio R Borges\\Save As Helper Duplicates\\")
    duplicate_folder : bpy.props.StringProperty(name='Folder Name', description='The name of duplicate folder',default='Previous Blend Files')
    add_filename : bpy.props.BoolProperty(name=" Add file name", default = True, description = "Add original file name in duplicates folder name") 
