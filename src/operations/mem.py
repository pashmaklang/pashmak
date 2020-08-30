def run(self , op):
    args = op['args_str']

    code = '(' + args + ')'

    # replace variable names with value of them
    for k in self.variables:
        v = self.variables[k]
        if type(v) == str:
            v = '"' + v + '"'
        v = str(v)

        code = code.replace('%' + k , v)

    self.mem = eval(code)
