import unittest
from unittest.mock import MagicMock

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

    def test_read_config(self):
      f = MagicMock()
      f.readline.return_value = '   5\n'
      r = run.read_config(f)
      self.assertEqual(5, r)

if __name__ == '__main__':
    unittest.main()