
from TestCore import TestCore

script_content = '''
set %somevar %v1;
set %hoho;

free %v1 %hoho;
'''

class test_free(TestCore):
    def run(self):
        program_vars = self.run_script(script_content)['vars']

        try:
            tmp = program_vars['somevar']
        except:
            self.assert_true(False)

        try:
            tmp = program_vars['v1']
            tmp = program_vars['hoho']
            self.assert_true(False)
        except:
            pass

