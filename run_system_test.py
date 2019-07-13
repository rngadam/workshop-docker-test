import unittest

import subprocess

class TestRun(unittest.TestCase):

    def test_execute(self):
      out = subprocess.check_output(["./run.py", "1"]) 
      self.assertEqual('2', out.strip().decode("utf-8") )

if __name__ == '__main__':
    unittest.main()