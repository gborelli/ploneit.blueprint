import urllib
from xmlrpclib import Binary


def get_file(base_url, path):
    url = '/'.join((base_url, path))
    response = urllib.urlopen(url)
    return Binary(response.read())
