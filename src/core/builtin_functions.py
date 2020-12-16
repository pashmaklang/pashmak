#
# builtin_functions.py
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

""" Pashmak Builtin functions """

from operations import free as op_free
from operations import read as op_read
from operations import func as op_func
from operations import goto as op_goto
from operations import gotoif as op_gotoif
from operations import isset as op_isset
from operations import tryop as op_try
from operations import namespace as op_namespace
from operations import use as op_use
from operations import classop as op_class
from operations import new as op_new

class BuiltinFunctions:
    """ Builtin functions """
    def run_free(self, op: dict):
        """ run free """
        op_free.run(self, op)

    def run_read(self, op: dict):
        """ run read """
        op_read.run(self, op)

    def run_func(self, op: dict):
        """ run func """
        op_func.run(self, op)

    def run_endfunc(self, op: dict):
        """ Closes the functon declaration block """
        try:
            del self.current_func
        except AttributeError:
            pass

    def run_goto(self, op: dict):
        """ run goto """
        op_goto.run(self, op)

    def run_gotoif(self, op: dict):
        """ run gotoif """
        op_gotoif.run(self, op)

    def run_isset(self, op: dict):
        """ run isset """
        op_isset.run(self, op)

    def run_try(self, op: dict):
        """ run try """
        op_try.run(self, op)

    def run_endtry(self, op: dict):
        """ Closes the try-endtry block """
        if self.try_endtry:
            self.try_endtry.pop()

    def run_namespace(self, op: dict):
        """ run namespace """
        op_namespace.run(self, op)

    def run_endnamespace(self, op: dict):
        """ Closes the namespace block """
        if self.namespaces_tree:
            self.namespaces_tree.pop()

    def run_use(self, op: dict):
        """ run use """
        op_use.run(self, op)

    def run_class(self, op: dict):
        """ run class """
        op_class.run(self, op)

    def run_endclass(self, op: dict):
        """ Closes the class declaration block """
        try:
            del self.current_class
        except AttributeError:
            pass

    def run_new(self, op: dict):
        """ run new """
        op_new.run(self, op)
