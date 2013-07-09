import unittest

from requests_caching.storage.backends.dict_backend import DictStorageBackend


class TestDictStorageBackend(unittest.TestCase):
    def test_backing_default(self):
        backend = DictStorageBackend()
        self.assertIsInstance(backend.cache, dict)

    def test_backing_provided(self):
        backing = {}
        backend = DictStorageBackend(backing)
        self.assertIs(backend.cache, backing)

    def test_set_new_key(self):
        backend = DictStorageBackend()
        backend.set('key', 'value')

    def test_set_overwrite_key(self):
        backend = DictStorageBackend()
        backend.set('key', 'first value')
        backend.set('key', 'second value')
        self.assertEqual(backend.get('key'), 'second value')

    def test_set_deleted_key(self):
        backend = DictStorageBackend()
        backend.set('key', 'first value')
        backend.delete('key')
        backend.set('key', 'second value')
        self.assertEqual(backend.get('key'), 'second value')

    def test_delete_missing_key_no_keyerror(self):
        backend = DictStorageBackend()
        backend.delete('key')

    def test_get_missing_returns_none(self):
        backend = DictStorageBackend()
        returned = backend.get('key')
        self.assertIsNone(returned)
