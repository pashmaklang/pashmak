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
from operations import call as op_call
from operations import required as op_required
from operations import typeof as op_typeof
from operations import system as op_system
from operations import include as op_include
from operations import goto as op_goto
from operations import gotoif as op_gotoif

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

    def run_call(self , op):
        op_call.run(self , op)

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
