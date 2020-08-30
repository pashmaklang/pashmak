def run(self , op):
    arg = op['args_str'].split(' ')

    if len(arg) <= 0:
        self.raise_error('SyntaxError' , 'call command required alias name argument' , op)
    
    arg = arg[0]

    if arg != '':
        if arg[0] == '%':
            try:
                arg = self.variables[arg[1:]]
            except:
                self.raise_error('VariableError' , 'undefined variable "' + arg + '"' , op)
        try:
            alias_body = self.aliases[arg]
        except:
            self.raise_error('AliasError' , 'undefined alias "' + arg + '"' , op)
    else:
        self.raise_error('SyntaxError' , 'alias command required alias name argument' , op)

    i = int(self.current_step)
    for alias_op in alias_body:
        alias_op_parsed = self.parse_op(alias_op)
        if alias_op_parsed['command'] == 'section':
            section_name = alias_op_parsed['args_str'].strip().split(' ')[0].strip()
            self.sections[section_name] = i+1
        else:
            #print(str(i) + ':' + alias_op) ####
            self.operations.insert(i+1 , alias_op)
            i += 1
