from requests_caching.storage.backends.dict_backend import DictStorageBackend


class Cache(object):
    def __init__(self, storage_backend=None):
        if storage_backend is None:
            storage_backend = DictStorageBackend()

        self.storage_backend = storage_backend
