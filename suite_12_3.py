import unittest
import  tests_12_3



torST = unittest.TestSuite()
torST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TestTournament))
torST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))


runner =unittest.TextTestRunner(verbosity=2)
runner.run(torST)
