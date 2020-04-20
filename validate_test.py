import unittest
import sys
import os
sys.path.append("..")
from pprint import pprint
import os.path
#sys.path.append(
   # os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#sys.path.append("..")

from ..extra.validate import validate

class ValidateTest(unittest.TestCase):

    # Returns True or False.
    def test_dir_exists(self):
        # when dir exists
        exists = a.dir_exists(".")
        self.assertTrue(exists)

        # when dir doesn't exist
        exists = validate.dir_exists("~/IdontExist")
        self.assertFalse(exists)

    def test_is_valid_dir_name(self):
      return

if __name__ == '__main__':
    unittest.main()