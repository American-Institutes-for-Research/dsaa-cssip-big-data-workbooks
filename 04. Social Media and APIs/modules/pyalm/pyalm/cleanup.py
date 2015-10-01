import email.utils
import datetime
import requests

def _text_to_bool(response):
    if (type(response) == str) or (type(response) == unicode):
        return response == 'true'

    else:
        return response

def _parse_dates_to_datetime(response):
    return _time_parse_helper(response, '%Y-%m-%dT%H:%M:%SZ')

def _parse_dates_figshare(response):
    return _time_parse_helper(response, '%Y-%m-%d %H:%M:%S')

def _time_parse_helper(response, format):
    if (type(response) == str) or (type(response) == unicode):
        try:
            return datetime.datetime.strptime(response, format)
        except ValueError:
            tup = email.utils.parsedate_tz(response)[0:6]
            return datetime.datetime(*tup)

    else:
        return response

def _parse_unix(unix):
    return datetime.datetime.utcfromtimestamp(unix)

def _parse_issued(issued):
    return datetime.datetime.strptime('-'.join([str(x) for x in issued['date-parts'][0]]), '%Y-%m-%d')

def _parse_numbers_to_int(response):
    if (type(response) == str) or (type(response) == unicode):
        return int(response)
    else:
        return response

def _process_histories(history):
    timepoints= []
    for timepoint in history:
        timepoints.append([_parse_dates_to_datetime(timepoint.get('update_date')),
                           _parse_numbers_to_int(timepoint.get('total'))])

    timepoints.sort(key=lambda l: l[0])
    return timepoints

def _parse_day(datedict):
    for d in datedict:
        date = '-'.join([ str(d['year']), str(d['month']), str(d['day']) ])
        d['date'] = datetime.datetime.strptime(date, '%Y-%m-%d')
    return datedict

def _parse_month(datedict):
    for d in datedict:
        date='-'.join([ str(d['year']), str(d['month']) ])
        d['date'] = datetime.datetime.strptime(date, '%Y-%m')
    return datedict

def _parse_year(datedict):
    for d in datedict:
        d['date'] = datetime.datetime.strptime(str(d['year']), '%Y')
    return datedict

def _parse_citations(citations):
    citations_ = []
    for d in citations['citation']:
        d['full_citation'] = _crossref_cn(d['doi'])
        citations_.append(d)
    return citations_

def _crossref_cn(doi):
    '''
    _crossref_cn("10.1126/science.1157784")
    '''
    res = requests.get("http://dx.doi.org/" + doi,
                        headers={'Accept' : 'text/x-bibliography; style=apa; locale=en-US'},
                        allow_redirects=True)
    if res.status_code == 200:
        return res.text
    else:
        return None
