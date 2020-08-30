def run(self , op):
    arg = op['args_str'].split(' ')[0]

    if len(arg) <= 0:
        self.raise_error('SyntaxError' , 'out command required argument' , op)

    out = None
    if arg == '^':
        out = self.get_mem()
    else:
        if arg[0] == '%':
            try:
                out = self.variables[arg[1:]]
            except:
                self.raise_error('VariableError' , 'undefined variable "' + arg + '"' , op)
        else:
            self.raise_error('SyntaxError' , 'unexpected "' + arg[0] + '"' , op)
        
    print(out , end='')
