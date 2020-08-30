import os

def run(self , op):
    args = op['args_str'].strip().split(' ')

    if len(args) <= 0:
        self.raise_error('SyntaxError' , 'system command gets a parameter' , op)

    arg = args[0]

    if arg != '':
        if arg == '^':
            cmd = self.get_mem()
        else:
            if arg[0] == '%':
                try:
                    cmd = self.variables[arg[1:]]
                except:
                    self.raise_error('VariableError' , 'undefined variable "' + arg + '"' , op)
            else:
                self.raise_error('SyntaxError' , 'unexpected "' + arg[0] + '"' , op)
            
        self.mem = os.system(cmd)
    else:
        self.raise_error('SyntaxError' , 'system command gets a parameter' , op)
