import unittest

from requests_caching import adapter


class TestAdapter(unittest.TestCase):
    def test_creation(self):
        cache = adapter.CacheAdapter()  #flake8: noqa
