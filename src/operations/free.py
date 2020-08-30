def run(self , op):
    seted_vars = {}
    args = op['args_str'].split(' ')
    for arg in args:
        if len(arg) > 0:
            if arg[0] == '%':
                varname = arg[1:]
                self.variables[varname] = None
            else:
                self.raise_error('SyntaxError' , 'unexpected "' + arg[0] + '"' , op)
