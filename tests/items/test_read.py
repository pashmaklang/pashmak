
from TestCore import TestCore

script_content = '''
set %input;
read %input;
out %input;
'''

script_content_b = '''
set %input;
read %input;
out %input;

set %input_1;
read %input_1;
out %input_1;
'''

class test_read(TestCore):
    def run(self):
        program_data = self.run_script(script_content , ['pashmak'])
        self.assert_equals(program_data['output'] , 'pashmak')
        self.assert_equals(program_data['vars'] , {'input': 'pashmak'})

        program_data = self.run_script(script_content_b , ['pashmak' , 'parsa'])
        self.assert_equals(program_data['output'] , 'pashmakparsa')
        self.assert_equals(program_data['vars'] , {'input': 'pashmak' , 'input_1': 'parsa'})

