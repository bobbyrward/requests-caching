from requests.adapters import HTTPAdapter

from requests_caching.cache import Cache
from requests_caching.filters import rfc2616


class CacheAdapter(HTTPAdapter):
    def __init__(self, cache=None, validation_filter=None, cacheability_filter=None):
        super(CacheAdapter, self).__init__()

        if cache is None:
            cache = Cache()

        self.cache = cache

        if validation_filter is None:
            validation_filter = rfc2616.ValidationFilter(cache=self.cache)

        self.validation_filter = validation_filter

        if cacheability_filter is None:
            cacheability_filter = rfc2616.CacheabilityFilter(cache=self.cache)

        self.cacheability_filter = cacheability_filter

    def send(self, request, **kwargs):
        return super(CacheAdapter, self).send(request, **kwargs)

    def build_response(self, request, response):
        return super(CacheAdapter, self).build_response(request, response)

    def can_read_cache(self, request):
        return self.validation_filter.filter(request)

    def can_cache_response(self, request, response):
        return self.cacheability_filter.filter(request, response)
