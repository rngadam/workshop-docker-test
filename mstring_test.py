# -----------------------------------------------------------------------------
# File Name: mstring_test.py
# Copyright: Jun 2019 Shanghai Mowen Technology Co., Ltd
# Author:    F. Wang
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

import unittest

import mstring


# -----------------------------------------------------------------------------
# Globals
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------


class TestString(unittest.TestCase):

    def test_execute(self):
      self.assertEqual(True, mstring.compareString('a', 'a'))

if __name__ == '__main__':
    unittest.main()