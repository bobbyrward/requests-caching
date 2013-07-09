from requests.adapters import HTTPAdapter


class CacheAdapter(HTTPAdapter):
    def __init__(self):
        super(CacheAdapter, self).__init__()
