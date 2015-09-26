import datetime
import time
import requests
import pyalm.config


BASE_HEADERS = {'Accept':'application/json'}


SEARCH_URL = 'http://api.plos.org/search?q='

'''
   _JMap - map a journal name to a url.
'''
_JMap = {
        'PLoS Biology'               : 'http://www.plosbiology.org',
        'PLoS Genetics'              : 'http://www.plosgenetics.org',
        'PLoS Computational Biology' : 'http://www.ploscompbiol.org',
        'PLoS Medicine'              : 'http://www.plosmedicine.org',
        'PLoS ONE'                   : 'http://www.plosone.org',
        'PLoS Neglected Tropical Diseases' : 'http://www.plosntds.org',
        'PLoS Clinical Trials'       : 'http://clinicaltrials.ploshubs.org',
        'PLoS Pathogens'             : 'http://www.plospathogens.org'
        }
'''
   _JIds - map a 4 character journal id to quoted journal name.
'''
_JIds = {
        'pbio' : '"PLoS Biology"',
        'pgen' : '"PLoS Genetics"',
        'pcbi' : '"PLoS Computational Biology"',
        'pmed' : '"PLoS Medicine"',
        'pone' : '"PLoS ONE"',
        'pntd' : '"PLoS Neglected Tropical Diseases"',
        'pctr' : '"PLoS Clinical Trials"',
        'ppat' : '"PLoS Pathogens"'
    }

def articleUrl(doi,jid):
    '''
        articleUrl- return a valid link to the article page given the journal
                    4 character identifier and the article doi.
    '''
    return _JMap[jid] + '/article/' + quote('info:doi/' + doi)

def articleXML(doi,jid):
    '''
        articleXML - return a valid link to the article XML give the journal
                     4 character identifier and the article doi.
    '''
    return _JMap[jid] + '/article/fetchObjectAttachment.action?uri=' + quote('info:doi/' + doi) +\
           '&representation=XML'


class Request:
    """
    Base class for a PLOS Search API Request Object
    """

    def __init__(self, query = {}, fields = ['doi'], instance = 'plos',
                start=0, limit=99, maxRows=100, verbose=False, delay = 0.5):
        self.start = start
        self.limit = limit
        self.maxrows = limit if limit < maxRows else maxRows
        self.delay = delay
        self.query = query
        self.fields = fields
        self.instance = instance
        self.api_key = pyalm.config.APIS.get(self.instance).get('key')
        self._query_text = ''
        self._api_url = SEARCH_URL
        self._headers = BASE_HEADERS
        self._params = {
                    'start': str(self.start),
                    'rows': str(self.maxrows),
                    'fq': 'doc_type:full AND !article_type_facet:"Issue Image"',
                    'wt': 'json',
                    'api_key' : self.api_key
                    }



    def add_query_term(self, term, query):
        self.query[term] = query


    def search_date(self, start, end=None):
        """
        Add date limits to the query

        The function accepts datetime objects, year integers, year strings, or
        YYYY-mm strings. If end is not set then assumes the current date. Single
        years will default to first of January so to search for 2012 articles
        start=2012 and end=2013
        """

        start_date = self._process_dates(start)
        if end:
            end_date = self._process_dates(end)
        else:
            end_date = datetime.datetime.now().isoformat()

        self.query['publication_date'] = '[%sZ TO %sZ]' % (start_date, end_date)

    def search_year(self, year):
        """
        Add date limits to the query for a single year

        The function accepts either strings or ints that can be parsed to the year
        element of datetime objects.
        """

        start_date = datetime.datetime(int(year), 1, 1, 0, 0, 0)
        end_date = datetime.datetime(int(year), 12, 31, 23, 59, 59)
        self.search_date(start_date, end_date)

    def _process_dates(self, date):
        """
        Utility method for handling dates as date, datetime, or strings
        """

        try:
            string = date.isoformat()
            return string

        except AttributeError: # If date is not a datetime object
            year = int(str(date).split('-')[0])
            try:
                month = int(str(date).split('-')[1])
                try:
                    day = int(str(date).split('-')[2])
                except IndexError:
                    day = 1
            except IndexError: # No month in the string
                month = 1
                day = 1


            return datetime.datetime(year, month, day, 0,0,0).isoformat()


    def add_field(self, field):
        self.fields.append(field)

    def set_query_text(self, text):
        self._query_text = text


    def _format_query(self):
        try:
            _query_text = ''
            _query_text = ' AND '.join(['%s:%s' % (k,v) for k,v in self.query.iteritems()])
            self._query_text = _query_text
            return _query_text
        except AttributeError:
            assert type(self.query) == str
            self._query_text = self.query
            return self._query_text
            


    def _format_query_url(self):
        query_url = self._api_url + self._format_query()
        return query_url

    def _finalize_params(self):
        self._params['fl'] = ','.join(self.fields)
        return self._params


    def get(self):
        query_url = self._format_query_url()
        params = self._finalize_params()
        headers = self._headers
        response = requests.get(query_url,
                                params = params,
                                headers = headers
                                )
        response.raise_for_status()

        return_json = response.json()
        self.response = response
        numFound = response.json().get('response').get('numFound')
        start = self.start + self.maxrows
        while len(return_json.get('response').get('docs')) < numFound:
            self._params['start'] = start
            params = self._finalize_params()
            paged_response = requests.get(query_url,
                                params = params,
                                headers = headers
                                )
            response.raise_for_status()
            return_json.get('response').get('docs').extend(paged_response.json().get('response').get('docs'))
            time.sleep(self.delay)
            start += self.maxrows
        return return_json


def collect_dois(query, dates=None):
    request = Request(query)
    if dates:
        try:
            request.search_date(dates[0],dates[1])
        except TypeError:
            request.search_date(dates)
    resp = request.get()
    dois = [article.get('doi')[0] for article in resp.get('response').get('docs')]
    return dois



