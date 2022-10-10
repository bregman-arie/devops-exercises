#!/usr/bin/env python
# coding=utf-8

import unittest

from app import main


class TestCase(unittest.TestCase):

    def setUp(self):
        self.app = main.app.test_client()

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_matrix(self):
        response = self.app.get('/matrix/123n459,789', follow_redirects=True)
        # Change when the matrix route is fixed and returning the actual matrix
        self.assertEqual(response.status_code, 500)


if __name__ == '__main__':
    unittest.main()
