from drone import plugin
import copy
import io
import json
import sys
import unittest


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
        self.assertRaises(ValueError, plugin.get_input)

    def test_valid_payload(self):
        """
        Call the plugin with a properly formed payload.
        """
        test_dict = {'test': 'hello'}
        sys.argv = ['some-plugin', '--', json.dumps(test_dict)]
        parsed_dict = plugin.get_input()
        # There should be no differences in the dicts.
        self.assertFalse(set(test_dict.keys()) ^ set(parsed_dict.keys()))


class StdinInputTestCase(unittest.TestCase):

    def setUp(self):
        self.stdin = sys.stdin

    def tearDown(self):
        sys.stdin = self.stdin

    def test_empty_payload(self):
        """Call the plugin with no input at all.
        """
        sys.stdin = io.StringIO()
        self.assertRaises(ValueError, plugin.get_input)

    def test_valid_payload(self):
        """Call the plugin with a properly formed payload.
        """
        s = u'{"test": "hello"}'
        sys.stdin = io.StringIO(s)
        self.assertEqual(plugin.get_input(), json.loads(s))


if __name__ == '__main__':
    unittest.main()
