
from TestCore import TestCore

script_content = '''
mem 'this is \; semicolon'; out ^;
'''

script_content_b = '''
mem 'this is \\\; semicolon'; out ^;
'''

class test_backslash_semicolon(TestCore):
    def run(self):
        program_output = self.run_script(script_content)['output']
        self.assert_equals(program_output , 'this is ; semicolon')

        program_output = self.run_script(script_content_b)['output']
        self.assert_equals(program_output , 'this is \; semicolon')

