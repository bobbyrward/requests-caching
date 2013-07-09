import unittest

import mock

from requests_caching.cache import Cache
from requests_caching.storage.backends.dict_backend import DictStorageBackend


class TestCache(unittest.TestCase):
    def test_default_storage_backend(self):
        cache = Cache()
        self.assertIsInstance(cache.storage_backend, DictStorageBackend)

    def test_provide_storage_backend(self):
        storage_backend = mock.MagicMock()
        cache = Cache(storage_backend=storage_backend)
        self.assertIs(cache.storage_backend, storage_backend)
