

class BaseFilter(object):
    def __init__(self, cache, predicates=None):
        self.cache = cache

        if predicates is None:
            predicates = []

        self.predicates = list(predicates)

    def filter(self, *args):
        for predicate in self.predicates:
            if not predicate(*args):
                return False

        return True


class ValidationFilter(BaseFilter):
    pass


class CacheabilityFilter(BaseFilter):
    pass
