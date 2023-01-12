import bpy

from bpy_extras.io_utils import ImportHelper

class SAH_OP_SaveAndRelocate(bpy.types.Operator, ImportHelper):
    """Save And Relocate"""

    bl_idname = "sah.save_and_relocate"
    bl_label = "SAH Save And Relocate"
    bl_options = {'REGISTER', 'UNDO'}
    
    filepath : bpy.props.StringProperty() # type:ignore
    directory : bpy.props.StringProperty() # type:ignore
    
    relocate_images : bpy.props.BoolProperty(name = "Relocate Images", default = True) # type:ignore
    relocate_links : bpy.props.BoolProperty(name = "Relocate Links", default = True) # type:ignore
    convert_to_relative : bpy.props.BoolProperty(name = "Convert To Relative", description = "Convert all paths to relative after finishing", default = True) # type:ignore
     
    def execute(self, context):
                
        if self.relocate_images:
            bpy.ops.sah.relocate_images(directory = self.directory)
        if self.relocate_links:
            bpy.ops.sah.relocate_links(directory = self.directory)
                
        if self.convert_to_relative:
            try:
                bpy.ops.file.make_paths_relative()
            except:
                pass
        
        bpy.ops.wm.save_as_mainfile(filepath = self.filepath)
        bpy.ops.wm.revert_mainfile()
        
        return {'FINISHED'}

        
        

        
            

    

        