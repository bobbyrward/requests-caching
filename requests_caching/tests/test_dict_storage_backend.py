import unittest

from requests_caching.storage.backends.dict_backend import DictStorageBackend


class TestDictStorageBackend(unittest.TestCase):
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

    def test_get_missing_key_keyerror(self):
        backend = DictStorageBackend()

        with self.assertRaises(KeyError):
            backend.get('key')
