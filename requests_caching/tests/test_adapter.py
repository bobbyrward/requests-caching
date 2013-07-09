import unittest

import mock

from requests_caching import adapter
from requests_caching.cache import Cache
from requests_caching.filters import rfc2616


class TestAdapter(unittest.TestCase):
    def test_creation(self):
        cache = adapter.CacheAdapter()
        self.assertIsInstance(cache.cache, Cache)
        self.assertIsInstance(cache.validation_filter, rfc2616.ValidationFilter)
        self.assertIsInstance(cache.cacheability_filter, rfc2616.CacheabilityFilter)

    def test_creation_provide_cache(self):
        mock_cache = mock.MagicMock()
        cache = adapter.CacheAdapter(cache=mock_cache)
        self.assertIs(cache.cache, mock_cache)

    def test_creation_provide_validation_filter(self):
        mock_filter = mock.MagicMock()
        cache = adapter.CacheAdapter(validation_filter=mock_filter)
        self.assertIs(cache.validation_filter, mock_filter)

    def test_creation_provide_cacheability_filter(self):
        mock_filter = mock.MagicMock()
        cache = adapter.CacheAdapter(cacheability_filter=mock_filter)
        self.assertIs(cache.cacheability_filter, mock_filter)

    def test_send_calls_base(self):
        request = mock.MagicMock()
        cache = adapter.CacheAdapter()

        with mock.patch('requests_caching.adapter.HTTPAdapter.send') as mocked_send:
            returned = cache.send(request)

        mocked_send.assert_called_once_with(request)
        self.assertEqual(returned, mocked_send.return_value)

    def test_build_response_calls_base(self):
        request = mock.MagicMock()
        response = mock.MagicMock()
        cache = adapter.CacheAdapter()

        with mock.patch('requests_caching.adapter.HTTPAdapter.build_response') as mocked_br:
            returned = cache.build_response(request, response)

        mocked_br.assert_called_once_with(request, response)
        self.assertEqual(returned, mocked_br.return_value)

    def test_can_read_cache(self):
        validation = mock.MagicMock()
        request = mock.MagicMock()
        cache = adapter.CacheAdapter(validation_filter=validation)
        self.assertIs(cache.can_read_cache(request), validation.filter.return_value)
        validation.filter.assert_called_once_with(request)

    def test_can_cache_response(self):
        cacheability = mock.MagicMock()
        request = mock.MagicMock()
        response = mock.MagicMock()
        cache = adapter.CacheAdapter(cacheability_filter=cacheability)
        self.assertIs(cache.can_cache_response(request, response), cacheability.filter.return_value)
        cacheability.filter.assert_called_once_with(request, response)
