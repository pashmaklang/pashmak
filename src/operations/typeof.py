def run(self , op):
    args = op['args_str'].split(' ')
    for arg in args:
        if len(arg) > 0:
            if arg[0] == '%':
                try:
                    var = self.variables[arg[1:]]
                    var_type = str(type(var))
                    var_type = var_type[8:]
                    var_type = var_type[:len(var_type)-2]
                    self.mem = var_type
                except:
                    self.raise_error('RequireError' , 'undefined variable "' + arg + '"' , op)
            else:
                self.raise_error('SyntaxError' , 'unexpected "' + arg[0] + '"' , op)
