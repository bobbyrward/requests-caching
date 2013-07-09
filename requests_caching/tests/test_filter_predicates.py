import unittest

import mock

from requests_caching.filters import predicates


class TestMethodCanReadcache(unittest.TestCase):
    def _mock_request(self, method):
        request = mock.MagicMock()
        request.method = method
        return request

    def test_get(self):
        self.assertTrue(
            predicates.method_can_read_cache(self._mock_request('GET'))
        )

    def test_put(self):
        self.assertFalse(
            predicates.method_can_read_cache(self._mock_request('PUT'))
        )

    def test_post(self):
        self.assertFalse(
            predicates.method_can_read_cache(self._mock_request('POST'))
        )

    def test_delete(self):
        self.assertFalse(
            predicates.method_can_read_cache(self._mock_request('DELETE'))
        )

    def test_patch(self):
        self.assertFalse(
            predicates.method_can_read_cache(self._mock_request('PATCH'))
        )
