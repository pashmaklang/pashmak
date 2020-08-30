
from TestCore import TestCore

script_content = '''
mem 'first'; out ^;

return;

mem 'last'; out ^;
'''

script_content_b = '''
mem 'first'; out ^;

return 126;

mem 'last'; out ^;
'''

class test_return(TestCore):
    def run(self):
        program_data = self.run_script(script_content)

        self.assert_equals(program_data['output'] , 'first')
        self.assert_equals(program_data['exit_code'] , 0)

        # next script

        program_data = self.run_script(script_content_b)

        self.assert_equals(program_data['output'] , 'first')
        self.assert_equals(program_data['exit_code'] , 126)

