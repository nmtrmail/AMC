""" Run a regresion test on a precharge array. """

import unittest
from testutils import header,AMC_test
import sys,os
sys.path.append(os.path.join(sys.path[0],".."))
import globals
from globals import OPTS
import debug

class precharge_test(AMC_test):

    def runTest(self):
        globals.init_AMC("config_20_{0}".format(OPTS.tech_name))
        
        global calibre
        import calibre
        OPTS.check_lvsdrc = False

        import precharge_array

        debug.info(2, "Checking 3 column precharge")
        pc = precharge_array.precharge_array(columns=3)
        self.local_check(pc)

        # return it back to it's normal state
        OPTS.check_lvsdrc = True
        globals.end_AMC()
        

# instantiate a copy of the class to actually run the test
if __name__ == "__main__":
    (OPTS, args) = globals.parse_args()
    del sys.argv[1:]
    header(__file__, OPTS.tech_name)
    unittest.main()