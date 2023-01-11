# "Save As Helper" Blender Addon.
# Copyright (C) 2022, Rodrigo Gama
#
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name": "Save As Helper",
    "description": "A simply way to save duplicate and backup files",
    "doc_url": "https://help.cgoutset.com/docs/save-as-helper/",
    "tracker_url": "https://help.cgoutset.com/bug-report/",
    "author": "Rodrigo Gama",
    "version": (1, 3, 1),
    "blender": (3, 3, 0),
    "location": "View3D",
    "category": "3D View"
    }


def register():
    from .addon.register import register_addon
    register_addon()


def unregister():
    from .addon.register import unregister_addon
    unregister_addon()