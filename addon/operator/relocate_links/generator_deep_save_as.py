import sys
import bpy

open_file = ""
save_path = ""

for arg in sys.argv:
    if arg.startswith('open_file:'):
        open_file = arg[10:]
    if arg.startswith('save_path:'):
        save_path = arg[10:]
        
bpy.ops.wm.open_mainfile(filepath = open_file)
bpy.ops.wm.save_as_mainfile(filepath = save_path, copy=True)


