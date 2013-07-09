

def method_can_read_cache(request):
    return request.method in ('GET',)
