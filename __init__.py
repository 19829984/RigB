# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
from . import operator_make_target_bones
from . import ui
import bpy

bl_info = {
    "name": "Make Target Cones",
    "author": "Bowen Wu",
    "description": "Simple tool make target bones from your deformation bones with constraints made for you",
    "blender": (2, 80, 3),
    "version": (1, 0, 0),
    "location": "",
    "warning": "",
    "category": "Rigging"
}


def register():
    operator_make_target_bones.register()
    ui.register()


def unregister():
    operator_make_target_bones.unregister()
    ui.unregister()
