import unittest

from validate import Validate

class ValidateTest(unittest.TestCase):

    # Returns True or False.
    def test_dir_exists(self):
        # when dir exists
        try:
            Validate.dir_exists(".")
            self.assertTrue(False)
        except:
            self.assertTrue(True)

        # when dir doesn't exist
        exists = Validate.dir_exists("~/IdontExist")
        self.assertFalse(exists)

if __name__ == '__main__':
    unittest.main()