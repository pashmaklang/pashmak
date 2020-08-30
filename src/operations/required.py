def run(self , op):
    args = op['args_str'].split(' ')
    for arg in args:
        if len(arg) > 0:
            if arg[0] == '%':
                try:
                    tmp = self.variables[arg[1:]]
                except:
                    self.raise_error('RequireError' , 'undefined variable "' + arg + '"' , op)
            else:
                self.raise_error('SyntaxError' , 'unexpected "' + arg[0] + '"' , op)
