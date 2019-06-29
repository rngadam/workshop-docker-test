# -----------------------------------------------------------------------------
# File Name: string_test.py
# Copyright: Jun 2019 Shanghai Mowen Technology Co., Ltd
# Author:    F. Wang
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

import unittest

import string


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
      self.assertEqual(True, string.compareString(1))

if __name__ == '__main__':
    unittest.main()