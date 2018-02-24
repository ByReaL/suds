#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division

import unittest




class TestReader(unittest.TestCase):
    def setUp(self):
        from suds.reader import Reader
        from suds.options import Options
        options = Options()
        self.r = Reader(options)

    def tearDown(self):
        self.r = None

    def test_mangle(self):
        self.assertEqual(self.r.mangle('asdasd', '123'), '2033017806-123')


if __name__ == '__main__':
    unittest.main()
