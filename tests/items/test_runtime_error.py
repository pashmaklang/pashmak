
from TestCore import TestCore

script_content = '''
# this line has error
mem 'hello world; out ^;
'''

class test_runtime_error(TestCore):
    def run(self):
        program_data = self.run_script(script_content)

        self.assert_not_equals(program_data['runtime_error'] , None)

