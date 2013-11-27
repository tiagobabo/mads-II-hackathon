import unittest

class MyTest(unittest.TestCase):

    def testMethod(self):
        self.assertEqual(2 + 2, 3, "1 + 2 not equal to 3")


if __name__ == '__main__':
        
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MyTest))
    unittest.TextTestRunner(verbosity=2).run(suite)


