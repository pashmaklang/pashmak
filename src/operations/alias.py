def run(self , op):
    arg = op['args_str'].split(' ')

    if len(arg) <= 0:
        self.raise_error('SyntaxError' , 'alias command required alias name argument' , op)
    
    arg = arg[0]

    if arg != '':
        self.current_alias = arg
        self.aliases[self.current_alias] = []
    else:
        self.raise_error('SyntaxError' , 'alias command required alias name argument' , op)
