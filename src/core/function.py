#
# function.py
#
# The Pashmak Project
# Copyright 2020 parsa shahmaleki <parsampsh@gmail.com>
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

class Function:
    """ the pashmak function object """
    def __init__(self, name, prog):
        self.name = name
        self.body = []
        self.prog = prog

    def __call__(self, *args, **kwargs):
        self.prog.mem = args
        if len(self.prog.mem) == 1:
            self.prog.mem = self.prog.mem[0]
        default_vars = {}
        try:
            self.parent_object
            default_vars['this'] = self.parent_object
        except:
            pass
        self.prog.exec_func(self.body, True, default_vars)
        return self.prog.get_mem()
