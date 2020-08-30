def run(self , op):
    args = op['args_str'].strip().split(' ')

    if len(args) <= 0:
        self.raise_error('ArgumentError' , 'copy command gets two arguments' , op)
        
    if len(args[0]) == 0:
        self.raise_error('SyntaxError' , 'one or more arguments are empty' , op)

    first_var = args[0]

    if len(args) == 1:
        mem = self.get_mem()
        try:
            self.variables[first_var[1:]] = mem
            return
        except:
            self.raise_error('VariableError' , 'undefined variable "' + first_var + '"' , op)

    if len(args[1]) == 0:
        self.raise_error('SyntaxError' , 'one or more arguments are empty' , op)

    second_var = args[1]

    try:
        if first_var == '^':
            first_var_value = self.get_mem()
        else:
            first_var_value = self.variables[first_var[1:]]
    except:
        self.raise_error('VariableError' , 'undefined variable "' + first_var + '"' , op)

    try:
        if second_var == '^':
            self.mem = first_var_value
        else:
            self.variables[second_var[1:]] = first_var_value
    except:
        self.raise_error('VariableError' , 'undefined variable "' + second_var + '"' , op)
