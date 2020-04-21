import unittest
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import sys
from contextlib import contextmanager
from unittest.mock import patch
from unittest import mock
from unittest import TestCase

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

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

    def test_is_valid_dir_name(self):
        with captured_output() as (out, err):
            Validate.is_valid_dir_name('Test-Dir')
            output = out.getvalue().strip()
            self.assertEqual(output, '')

if __name__ == '__main__':
    unittest.main()