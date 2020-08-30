import sys

def run(self , op):
    arg = op['args_str'].strip().split(' ')[0].strip()

    exit_code = 0
    tmp = None

    if arg != '':
        if arg[0] == '%':
            try:
                tmp = self.variables[arg[1:]]

                try:
                    tmp = int(tmp)
                    exit_code = tmp
                except:
                    self.raise_error('TypeError' , 'return command gets integer value' , op)
            except:
                self.raise_error('VariableError' , 'undefined variable "' + arg + '"' , op)
        else:
            try:
                exit_code = int(arg)
            except:
                self.raise_error('TypeError' , 'return command gets integer value' , op)

    sys.exit(exit_code)
