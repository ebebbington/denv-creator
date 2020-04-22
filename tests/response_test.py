from response import Response
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

class ResponseTest(unittest.TestCase):

    # Returns True or False.
    @patch('builtins.input', lambda *args: 'Hello')
    def test_ask_for_input(self):
        #mocked_input.side_effect = ['Albert Einstein', '42.81', 'done']
        result = Response.ask_for_input('hi')
        self.assertEqual(result, 'Hello')

    def test_show_info(self):
        with captured_output() as (out, err):
            Response.show_info('Test Info')
            output = out.getvalue().strip()
            self.assertEqual(output, '\x1b[92mTest Info\x1b[0m')

    def test_show_log(self):
        with captured_output() as (out, err):
            Response.show_log('Test Info')
            output = out.getvalue().strip()
            self.assertEqual(output, 'Test Info')

if __name__ == '__main__':
    unittest.main()