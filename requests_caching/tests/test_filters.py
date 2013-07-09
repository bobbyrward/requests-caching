import unittest

import mock

from requests_caching import filters


class TestBaseFilter(unittest.TestCase):
    def _filter(self, cache=None, predicates=None):
        cache = mock.MagicMock() if cache is None else cache
        return filters.BaseFilter(cache, predicates)

    def test_no_predicates_returns_true(self):
        filter = self._filter()
        self.assertTrue(filter.filter())

    def test_accepts_variable_arguments(self):
        filter = self._filter()
        self.assertTrue(filter.filter(1))
        self.assertTrue(filter.filter(1, 2))
        self.assertTrue(filter.filter(1, 2, 3))

        with self.assertRaises(TypeError):
            filter.filter(1, 2, 3, keyword=4)

    def test_sets_cache(self):
        cache = mock.MagicMock()
        filter = self._filter(cache=cache)
        self.assertIs(filter.cache, cache)

    def test_predicates(self):
        predicate1 = mock.MagicMock(return_value=True)
        predicate2 = mock.MagicMock(return_value=False)
        filter = self._filter(predicates=[predicate1, predicate2])
        self.assertFalse(filter.filter(1, 2, 3))
        predicate1.assert_called_once_with(1, 2, 3)
        predicate2.assert_called_once_with(1, 2, 3)

    def test_predicates_is_list(self):
        predicate1 = mock.MagicMock(return_value=True)
        predicate2 = mock.MagicMock(return_value=False)
        filter = self._filter(predicates=(predicate1, predicate2))
        self.assertIsInstance(filter.predicates, list)


class TestValidationFilter(unittest.TestCase):
    def test_is_filter(self):
        cache = mock.MagicMock()
        filter = filters.ValidationFilter(cache=cache)
        self.assertIsInstance(filter, filters.BaseFilter)


class TestCacheabilityFilter(unittest.TestCase):
    def test_is_filter(self):
        cache = mock.MagicMock()
        filter = filters.CacheabilityFilter(cache=cache)
        self.assertIsInstance(filter, filters.BaseFilter)
