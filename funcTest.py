import unittest
import myfunc

class myFuncTest(unittest.TestCase):
    
    def myTest(self):
        self.assertEqual(myfunc(1,1),2)
     
    