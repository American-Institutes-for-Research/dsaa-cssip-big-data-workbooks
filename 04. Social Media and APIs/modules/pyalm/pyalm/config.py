try:
    from api_key import *

except ImportError: # This will happen when external integration platforms try to get key
    API_KEY = {}
    API_KEY['plos'] = 'FAKE-TEST-KEY'

APIS = { 'plos'       : {
                          'url': "http://alm.plos.org/api/v3/articles",
                          'key': API_KEY.get('plos')
                        },
         'ojs'        : {
                          'url': None,
                          'key': API_KEY.get('ojs')
                        },
         'copernicus' : {
                          'url': None,
                          'key': API_KEY.get('copernicus')
                        }}