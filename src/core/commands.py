import sys

class Commands:
    def run_set(self , op):
        seted_vars = {}
        args = op['args_str'].split(' ')
        for arg in args:
            if len(arg) > 0:
                if arg[0] == '%':
                    varname = arg[1:]
                    self.variables[varname] = None
                else:
                    self.raise_error('SyntaxError' , 'unexpected "' + arg[0] + '"' , op)

    def run_free(self , op):
        args = op['args_str'].split(' ')
        for arg in args:
            if arg == '^':
                self.mem = None
            else:
                if len(arg) > 0:
                    if arg[0] == '%':
                        varname = arg[1:]
                        del self.variables[varname]
                    else:
                        self.raise_error('SyntaxError' , 'unexpected "' + arg[0] + '"' , op)

    def run_copy(self , op):
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

    def run_mem(self , op):
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

    def run_out(self , op):
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

    def run_read(self , op):
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

    def run_return(self , op):
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

    def run_alias(self , op):
        arg = op['args_str'].split(' ')

        if len(arg) <= 0:
            self.raise_error('SyntaxError' , 'alias command required alias name argument' , op)
    
        arg = arg[0]

        if arg != '':
            self.current_alias = arg
            self.aliases[self.current_alias] = []
        else:
            self.raise_error('SyntaxError' , 'alias command required alias name argument' , op)

    def run_endalias(self , op):
        try:
            del self.current_alias
        except:
            pass

    def run_call(self , op):
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

        '''
        import pprint
        print(self.current_step)
        tmp_i = 0
        for tmp_op in self.operations:
            print(str(tmp_i) + ':' + tmp_op)
            tmp_i += 1
        pprint.pprint(self.sections)
        sys.exit()
        '''


        


    def run_required(self , op):
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

    def run_typeof(self , op):
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

    def run_system(self , op):
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

    def run_include(self , op):
        args = op['args_str'].strip().split(' ')

        if len(args) <= 0:
            self.raise_error('SyntaxError' , 'include command gets a parameter' , op)

        arg = args[0]

        if arg != '':
            if arg == '^':
                path = self.get_mem()
            else:
                if arg[0] == '%':
                    try:
                        path = self.variables[arg[1:]]
                    except:
                        self.raise_error('VariableError' , 'undefined variable "' + arg + '"' , op)
                else:
                    self.raise_error('SyntaxError' , 'unexpected "' + arg[0] + '"' , op)
            
            try:
                content = open(path , 'r').read()
                operations = parser.parse(content)
                for operation in operations:
                    self.run(operation)
            except Exception as ex:
                self.raise_error('FileError' , str(ex) , op)
        else:
            self.raise_error('SyntaxError' , 'include command gets a parameter' , op)

    def run_goto(self , op):
        arg = op['args_str'].strip().split(' ')[0].strip()

        if arg == '':
            self.raise_error('SyntaxError' , 'goto command gets section name argument' , op)
        
        try:
            section_index = self.sections[arg]
        except:
            self.raise_error('SectionError' , 'undefined section "' + str(arg) + '"' , op)

        self.current_step = section_index-1

    def run_gotoif(self , op):
        arg = op['args_str'].strip().split(' ')[0].strip()

        if arg == '':
            self.raise_error('SyntaxError' , 'goto command gets section name argument' , op)
        
        try:
            section_index = self.sections[arg]
        except:
            self.raise_error('SectionError' , 'undefined section "' + str(arg) + '"' , op)

        if self.mem:
            self.current_step = section_index-1