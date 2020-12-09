#
# commands.py
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

''' Only some aliases for operations '''

# operations imports
from operations import set as op_set
from operations import free as op_free
from operations import copy as op_copy
from operations import out as op_out
from operations import read as op_read
from operations import returnop as op_return
from operations import func as op_func
from operations import endfunc as op_endfunc
from operations import required as op_required
from operations import typeof as op_typeof
from operations import system as op_system
from operations import include as op_include
from operations import goto as op_goto
from operations import gotoif as op_gotoif
from operations import fread as op_fread
from operations import fwrite as op_fwrite
from operations import chdir as op_chdir
from operations import cwd as op_cwd
from operations import isset as op_isset
from operations import tryop as op_try
from operations import endtry as op_endtry
from operations import eval as op_eval
from operations import arraypush as op_arraypush
from operations import arraypop as op_arraypop
from operations import python as op_python
from operations import namespace as op_namespace
from operations import endnamespace as op_endnamespace
from operations import use as op_use
from operations import struct as op_struct
from operations import endstruct as op_endstruct
from operations import new as op_new

class Commands:
    ''' Only some aliases for operations '''

    def run_set(self, op: dict):
        ''' run set '''
        op_set.run(self, op)

    def run_free(self, op: dict):
        ''' run free '''
        op_free.run(self, op)

    def run_copy(self, op: dict):
        ''' run copy '''
        op_copy.run(self, op)

    def run_out(self, op: dict):
        ''' run out '''
        op_out.run(self, op)

    def run_read(self, op: dict):
        ''' run read '''
        op_read.run(self, op)

    def run_return(self, op: dict):
        ''' run return '''
        op_return.run(self, op)

    def run_func(self, op: dict):
        ''' run func '''
        op_func.run(self, op)

    def run_endfunc(self, op: dict):
        ''' run endfunc '''
        op_endfunc.run(self, op)

    def run_required(self, op: dict):
        ''' run required '''
        op_required.run(self, op)

    def run_typeof(self, op: dict):
        ''' run typeof '''
        op_typeof.run(self, op)

    def run_system(self, op: dict):
        ''' run system '''
        op_system.run(self, op)

    def run_include(self, op: dict):
        ''' run include '''
        op_include.run(self, op)

    def run_goto(self, op: dict):
        ''' run goto '''
        op_goto.run(self, op)

    def run_gotoif(self, op: dict):
        ''' run gotoif '''
        op_gotoif.run(self, op)

    def run_fread(self, op: dict):
        ''' run fread '''
        op_fread.run(self, op)

    def run_fwrite(self, op: dict):
        ''' run fwrite '''
        op_fwrite.run(self, op)

    def run_chdir(self, op: dict):
        ''' run chdir '''
        op_chdir.run(self, op)

    def run_cwd(self, op: dict):
        ''' run cwd '''
        op_cwd.run(self, op)

    def run_isset(self, op: dict):
        ''' run isset '''
        op_isset.run(self, op)

    def run_try(self, op: dict):
        ''' run try '''
        op_try.run(self, op)

    def run_endtry(self, op: dict):
        ''' run endtry '''
        op_endtry.run(self, op)

    def run_eval(self, op: dict):
        ''' run eval '''
        op_eval.run(self, op)

    def run_arraypush(self, op: dict):
        ''' run arraypush '''
        op_arraypush.run(self, op)

    def run_arraypop(self, op: dict):
        ''' run arraypop '''
        op_arraypop.run(self, op)

    def run_python(self, op: dict):
        ''' run python '''
        op_python.run(self, op)

    def run_namespace(self, op: dict):
        ''' run namespace '''
        op_namespace.run(self, op)

    def run_endnamespace(self, op: dict):
        ''' run endnamespace '''
        op_endnamespace.run(self, op)

    def run_use(self, op: dict):
        ''' run use '''
        op_use.run(self, op)

    def run_struct(self, op: dict):
        ''' run struct '''
        op_struct.run(self, op)

    def run_endstruct(self, op: dict):
        ''' run endstruct '''
        op_endstruct.run(self, op)

    def run_new(self, op: dict):
        ''' run new '''
        op_new.run(self, op)
