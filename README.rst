********************************************************************************
requests-caching - A cache adapater for requests
********************************************************************************

requests-caching adds a caching layer using either date or etag conditional
requests and pluggable storage backends

While this package should work for general HTTP, it's focus is on consuming a
caching-aware REST api.  To this end,  the logic around determining cachability
and cache validation is extensible through the use of filters.

Filters receive either a response or a request/response pair for validation
and cachability checks respectively and return a boolean value.  The default
filters can be extended through adding callables to the chain or overridden
completely.

Two sets of filters are provided.  One set conforms to RFC 2616[#]_ and the
other conforms to the current httpbis draft[#]_.

.. [#] http://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html#sec13.9
.. [#] http://datatracker.ietf.org/doc/draft-ietf-httpbis-p6-cache



================================================================================
Installation
================================================================================

pip install requests-caching

================================================================================
Usage
================================================================================


.. code-block:: python

    import requests
    import requests_caching

    session = requests.session()
    cache_adapter = requests_caching.CacheAdapter()
    session.mount('http://', cache_adapter)


.. TODO::
    Name me
