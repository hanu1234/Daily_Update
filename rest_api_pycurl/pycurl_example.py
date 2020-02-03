import pycurl
from io import BytesIO


class Rest:
    def __init__(self):
        pass

    def pycurl_request(self, url):
        """
        pycurl request provides a simple way to conduct the http GET, PUT, POST and DELETE the HTTP requests
        """
        b = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEDAT, b)

