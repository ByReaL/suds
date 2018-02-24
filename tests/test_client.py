#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division

import unittest

from suds import reader


class TestReader(unittest.TestCase):

    def test_mangle(self):
        self.assertEqual(reader.mangle('asdasd', '123'), '4841200568723399630-123')


if __name__ == '__main__':
    unittest.main()
