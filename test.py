#!/usr/bin/python

import unittest
import api


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_search(self):
        # [{"guid": "3030-19578","name": "Scapeghost"}]
        result = api.search('Scapeghost')
        result = result[0]
        self.assertEqual(result['guid'], "3030-19578")
        self.assertEqual(result['name'], "Scapeghost")

    def test_inspect(self):
        result = api.inspect('3030-19578')
        self.assertEqual(result['name'], "Scapeghost")
        self.assertEqual(result['deck'], None)
        self.assertEqual(result['description'], None)


if __name__ == '__main__':
    unittest.main()
