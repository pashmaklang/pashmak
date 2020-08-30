
import time, os

from TestCore import TestCore

script_content = '''
mem 'start\\n'; out ^;

mem 'end\\n'; out ^;

mem 'touch /tmp/pashmak-test-created-file-<rand>'; system ^;
'''

class test_system(TestCore):
    def run(self):
        rand = time.time()
        program_data = self.run_script(script_content.replace('<rand>' , str(rand)))

        self.assert_equals(program_data['output'] , 'start\nend\n')

        self.assert_equals(program_data['mem'] , 0)

        self.assert_true(os.path.isfile('/tmp/pashmak-test-created-file-' + str(rand)))
        os.remove('/tmp/pashmak-test-created-file-' + str(rand))




