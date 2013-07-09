import unittest

from requests_caching.storage import StorageBackend


class TestStorageBackend(unittest.TestCase):
    def test_set_raises_not_implemented(self):
        backend = StorageBackend()

        with self.assertRaises(NotImplementedError):
            backend.set('key', 'value')

    def test_get_raises_not_implemented(self):
        backend = StorageBackend()

        with self.assertRaises(NotImplementedError):
            backend.get('key')

    def test_delete_raises_not_implemented(self):
        backend = StorageBackend()

        with self.assertRaises(NotImplementedError):
            backend.delete('key')
