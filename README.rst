********************************************************************************
requests-caching - A cache adapater for requests
********************************************************************************

requests-caching adds a caching layer using either date or etag conditional
requests and pluggable storage backends


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
