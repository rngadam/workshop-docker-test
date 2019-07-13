import unittest

import run

class TestRun(unittest.TestCase):

    def test_execute(self):
      self.assertEqual(2, run.execute(1))

    def test_execute_10(self):
      self.assertEqual(11, run.execute(10))

    def test_execute_minus(self):
      self.assertEqual(0, run.execute(-1))


    def test_execute_invalid_parameter(self):
        with self.assertRaises(run.RunExceptionInvalidParameter):
            run.execute('')

if __name__ == '__main__':
    unittest.main()