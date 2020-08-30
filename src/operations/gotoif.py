def run(self , op):
    arg = op['args_str'].strip().split(' ')[0].strip()

    if arg == '':
        self.raise_error('SyntaxError' , 'goto command gets section name argument' , op)
        
    try:
        section_index = self.sections[arg]
    except:
        self.raise_error('SectionError' , 'undefined section "' + str(arg) + '"' , op)

    if self.mem:
        self.current_step = section_index-1
