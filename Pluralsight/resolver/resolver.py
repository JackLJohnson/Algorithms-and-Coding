import socket

class Resolver:

    def __init__(self):
        self._cache={}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host]=socket.gethostbyname(host)
            return self._cache[host]

    def clean(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache

obj = Resolver()
print(obj.has_host("google.com"))
print(obj('google.com'))
print(obj.__call__('google.com'))
print(obj._cache)
print(obj('pluralsight.com'))
print(obj._cache)
obj.clean()
print(obj.has_host("google.com"))

from timeit import timeit
