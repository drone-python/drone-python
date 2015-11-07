import sys
import copy
import json
import unittest

# noinspection PyProtectedMember
from drone.plugin.input import _get_input_from_argv


class ArgvInputTestCase(unittest.TestCase):

    def setUp(self):
        # We are going to be mucking with this. Back it up for
        # later restoration.
        self.original_argv = copy.copy(sys.argv)

    def tearDown(self):
        sys.argv = self.original_argv

    def test_empty_payload(self):
        """
        Call the plugin with no input at all.
        """
        # No payload was passed in. We can't do anything with this
        # aside from fail.
        sys.argv = ['some-plugin', '--']
        self.assertRaises(ValueError, _get_input_from_argv)

    def test_valid_payload(self):
        """
        Call the plugin with a properly formed payload.
        """
        test_dict = {'test': 'hello'}
        sys.argv = ['some-plugin', '--', json.dumps(test_dict)]
        parsed_dict = json.loads(_get_input_from_argv())
        # There should be no differences in the dicts.
        self.assertFalse(set(test_dict.keys()) ^ set(parsed_dict.keys()))
