
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/src')

import tcolor

class TestRunner:
    def __init__(self):
        files = os.listdir('tests/items')
        self.tests = []
        for f in files:
            if f[len(f)-3:] == '.py':
                self.tests.append(f)

    def run_once(self , test):
        test_class_name = test[:len(test)-3]
        loaded_test = __import__('items.' + test_class_name)
        test_obj = eval('loaded_test.' + test_class_name + '.' + test_class_name + '()')
        test_obj.run()
        print(test_class_name.replace('_' , ' ') + ': ' + tcolor.OKGREEN + 'PASS' + tcolor.ENDC)

    def run(self):
        for test in self.tests:
            self.run_once(test)





test_runner = TestRunner()
test_runner.run()



