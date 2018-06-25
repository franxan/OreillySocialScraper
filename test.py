#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from core import AuthorProbe


class TestCore(unittest.TestCase):
    def test_one(self):
        a = AuthorProbe(query='', max_pages=1, delay=1)
        assert a.authors != {}


if __name__ == '__main__':
    unittest.main()
