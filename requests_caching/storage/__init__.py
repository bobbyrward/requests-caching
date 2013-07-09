

class StorageBackend(object):
    """Interface for storage backends"""

    def set(self, key, value):
        raise NotImplementedError()

    def get(self, key):
        raise NotImplementedError()

    def delete(self, key):
        raise NotImplementedError()
