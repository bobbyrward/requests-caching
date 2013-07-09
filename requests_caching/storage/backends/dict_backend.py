from requests_caching.storage import StorageBackend


class DictStorageBackend(StorageBackend):
    def __init__(self):
        self.cache = {}

    def set(self, key, value):
        self.cache[key] = value

    def get(self, key):
        return self.cache[key]

    def delete(self, key):
        try:
            del self.cache[key]
        except KeyError:
            pass
