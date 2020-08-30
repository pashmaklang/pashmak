def run(self , op):
    arg = op['args_str'].split(' ')[0]

    if len(arg) <= 0:
        self.raise_error('SyntaxError' , 'read command required variable argument' , op)

    out = None
    if arg == '^':
        pass
    else:
        if arg[0] == '%':
            try:
                tmp = self.variables[arg[1:]]
                del tmp
            except:
                self.raise_error('VariableError' , 'undefined variable "' + arg + '"' , op)
        else:
            self.raise_error('SyntaxError' , 'unexpected "' + arg[0] + '"' , op)
        
    readed_data = input()

    if out == '^':
        self.mem = readed_data
    else:
        self.variables[arg[1:]] = readed_data
