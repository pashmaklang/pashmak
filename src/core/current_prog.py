#
# current_prog.py
#
# The Pashmak Project
# Copyright 2020-2021 parsa shahmaleki <parsampsh@gmail.com>
#
# This file is part of Pashmak.
#
# Pashmak is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pashmak is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pashmak.  If not, see <https://www.gnu.org/licenses/>.
#########################################################################

""" This file only have a variable to keep current program object

Actually, The current running program object should be accessbile in everywhere,
Because of that, when a new Program object is initialized,
Puts pointer of he's/she's self in here.
then, other functions and classes in interpreter core can access to this:
    from . import current_prog
    current_prog.current_prog.<something>

The `current_prog.current_prog` Should be a object from class `program.Program`
"""

current_prog = None
""" The current program object(program.Program) """
