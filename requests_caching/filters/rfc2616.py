from requests_caching import filters
from requests_caching.filters import predicates


class ValidationFilter(filters.ValidationFilter):
    def __init__(self, cache):
        super(ValidationFilter, self).__init__(cache, predicates=[
            predicates.method_can_read_cache
        ])


class CacheabilityFilter(filters.ValidationFilter):
    def __init__(self, cache):
        super(CacheabilityFilter, self).__init__(cache)
