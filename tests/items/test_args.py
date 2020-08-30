
from TestCore import TestCore

script_content = '''
out %argv_0;
out %argv_1;
out %argc;
'''

class test_args(TestCore):
    def run(self):
        program_data = self.run_script(script_content , [] , ['hi' , 'bye'])
        self.assert_equals(program_data['vars']['argv_0'] , 'hi')
        self.assert_equals(program_data['vars']['argv_1'] , 'bye')
        self.assert_equals(program_data['output'] , 'hibye2')

