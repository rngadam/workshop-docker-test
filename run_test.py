import unittest

import run

class TestRun(unittest.TestCase):

    def test_execute(self):
      self.assertEqual(2, run.execute(1))

    def test_foo(self):
      self.assertEqual(4, run.foo(2))

if __name__ == '__main__':
    unittest.main()