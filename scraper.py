from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def extract(url):
    """Attempt to get the content at 'url' by making an HTTP Get request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None."""
    try:
        # closing helps with network timeouts errors
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error during reqest to {0} : {1}'.format(url, str(e)))

def is_good_response(resp):
    """Returns True if the response seems to be HTML, False otherwise"""
    content_type = resp.headers['Content-Type'].lower()
    return(resp.status_code==200
            and content_type is not None
            and content_type.find('html') > -1)


raw_html = extract('https://www.novelupdates.com/reading-list/')
obj = open("test.html","w")
obj.write(raw_html.decode("utf-8"))
obj.close()
