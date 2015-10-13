# try:
#     from api_key import *

# except ImportError: # This will happen when external integration platforms try to get key
#     API_KEY = {}
#     API_KEY['plos'] = 'FAKE-TEST-KEY'

# APIS = { 'plos'       : {
#                           'url': "http://alm.plos.org/api/v5/articles",
#                           'key': API_KEY.get('plos')
#                         },
#          'ojs'        : {
#                           'url': None,
#                           'key': API_KEY.get('ojs')
#                         },
#          'copernicus' : {
#                           'url': None,
#                           'key': API_KEY.get('copernicus')
#                         }}


API_KEY = None

PYALM_LOCATION = "~/.pyalm"
"""
This is the location of the api keys and url stored on the filesystem. Currently,
it uses a file directly under a tilde, so that windows users don't have to feel
as much pain when using the API. Usually this is something like
``~/.pyalm``
"""

PLOS_KEY_ENVVAR = "PLOS_API_KEY"
ELIFE_KEY_ENVVAR = "ELIFE_API_KEY"
CROSSREF_KEY_ENVVAR = "CROSSREF_API_KEY"
PKP_KEY_ENVVAR = "PKP_API_KEY"
COPERNICUS_KEY_ENVVAR = "COPERNICUS_API_KEY"
PENSOFT_KEY_ENVVAR = "PENSOFT_API_KEY"
"""
These are the names of the ``os.environ`` keys to look for.
"""

PLOS_URL_ENVVAR = "PLOS_URL"
ELIFE_URL_ENVVAR = "ELIFE_URL"
CROSSREF_URL_ENVVAR = "CROSSREF_URL"
PKP_URL_ENVVAR = "PKP_URL"
COPERNICUS_URL_ENVVAR = "COPERNICUS_URL"
PENSOFT_URL_ENVVAR = "PENSOFT_URL"
"""
These are the names of the ``os.environ`` urls to look for.
"""
