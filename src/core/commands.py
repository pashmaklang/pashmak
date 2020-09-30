#
# commands.py
#
# the pashmak project
# Copyright 2020 parsa mpsh <parsampsh@gmail.com>
#
# This file is part of pashmak.
#
# pashmak is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pashmak is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pashmak.  If not, see <https://www.gnu.org/licenses/>.
##################################################

# operations imports
from operations import set as op_set
from operations import free as op_free
from operations import copy as op_copy
from operations import mem as op_mem
from operations import out as op_out
from operations import read as op_read
from operations import returnop as op_return
from operations import alias as op_alias
from operations import endalias as op_endalias
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

class Commands:
    def run_set(self , op):
        op_set.run(self , op)

    def run_free(self , op):
        op_free.run(self , op)

    def run_copy(self , op):
        op_copy.run(self , op)

    def run_mem(self , op):
        op_mem.run(self , op)

    def run_out(self , op):
        op_out.run(self , op)

    def run_read(self , op):
        op_read.run(self , op)

    def run_return(self , op):
        op_return.run(self , op)

    def run_alias(self , op):
        op_alias.run(self , op)

    def run_endalias(self , op):
        op_endalias.run(self , op)

    def run_required(self , op):
        op_required.run(self , op)

    def run_typeof(self , op):
        op_typeof.run(self , op)

    def run_system(self , op):
        op_system.run(self , op)

    def run_include(self , op):
        op_include.run(self , op)

    def run_goto(self , op):
        op_goto.run(self , op)

    def run_gotoif(self , op):
        op_gotoif.run(self , op)

    def run_fread(self , op):
        op_fread.run(self , op)

    def run_fwrite(self , op):
        op_fwrite.run(self , op)

    def run_chdir(self , op):
        op_chdir.run(self , op)

    def run_cwd(self , op):
        op_cwd.run(self , op)

    def run_isset(self , op):
        op_isset.run(self , op)

    def run_try(self , op):
        op_try.run(self , op)

    def run_endtry(self , op):
        op_endtry.run(self , op)

    def run_eval(self , op):
        op_eval.run(self , op)

    def run_arraypush(self , op):
        op_arraypush.run(self , op)

    def run_arraypop(self , op):
        op_arraypop.run(self , op)

    def run_python(self , op):
        op_python.run(self , op)
