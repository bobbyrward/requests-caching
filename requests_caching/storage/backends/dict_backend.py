from requests_caching.storage import StorageBackend


class DictStorageBackend(StorageBackend):
    def __init__(self, backing=None):
        if backing is None:
            backing = {}

        self.cache = backing

    def set(self, key, value):
        self.cache[key] = value

    def get(self, key):
        try:
            return self.cache[key]
        except KeyError:
            return None

    def delete(self, key):
        try:
            del self.cache[key]
        except KeyError:
            pass
