import unittest
import myfunc

class myFuncTest(unittest.TestCase):
    
    def myTest(self):
        self.assertEqual(myfunc(1,1),2)
     

if __name__ == '__main__':
    unittest.main()