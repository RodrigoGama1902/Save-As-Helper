import bpy
import os

def convert_to_absolute(filepath : str) -> str:
    
    if filepath.startswith('//'):
        filepath = (os.path.abspath(bpy.path.abspath(filepath)))
    
    return filepath

def convert_to_relative(filepath : str) -> str:
    
    if not filepath.startswith('//'):
        filepath = bpy.path.relpath(filepath)
    
    return filepath