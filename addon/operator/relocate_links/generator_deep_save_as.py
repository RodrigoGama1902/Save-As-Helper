import sys
import bpy

open_file = ""
save_path = ""
relocate_directory = ""
relocate_images = False

for arg in sys.argv:
    if arg.startswith("open_file:"):
        open_file = arg[10:]
    if arg.startswith("save_path:"):
        save_path = arg[10:]
    if arg.startswith("relocate_directory:"):
        relocate_directory = arg[19:]      
    if arg.startswith("relocate_images:"):
        relocate_images = arg[16:] == "True"
    
print()
print("     open_file: " + open_file)
print("     save_path: " + save_path)
print("     relocate_directory: " + relocate_directory)
print("     relocate_images: " + str(relocate_images))
print()
        
bpy.ops.wm.open_mainfile(filepath = open_file)
bpy.ops.wm.save_as_mainfile(filepath = save_path, copy=True)

bpy.ops.preferences.addon_enable(module="Save As Helper")

if relocate_images:
    bpy.ops.sah.relocate_images(directory = relocate_directory)

# Run relocate link operator inside the current source link file
bpy.ops.sah.relocate_links(directory = relocate_directory)



