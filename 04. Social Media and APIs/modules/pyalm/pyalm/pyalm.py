import requests
from utils import dictmapper, MappingRule as to
import cleanup
import config

BASE_HEADERS = {'Accept': 'application/json'}

MetricsBase = dictmapper('MetricsBase',
                         {'citations': to(['citations'],
                                          cleanup._parse_numbers_to_int),
                          'comments': to(['comments'],
                                         cleanup._parse_numbers_to_int),
                          'groups': to(['groups'],
                                       cleanup._parse_numbers_to_int),
                          'likes': to(['likes'],
                                      cleanup._parse_numbers_to_int),
                          'pdf': to(['pdf'],
                                    cleanup._parse_numbers_to_int),
                          'shares': to(['shares'],
                                       cleanup._parse_numbers_to_int),
                          'total': to(['total'],
                                      cleanup._parse_numbers_to_int)
                         }
)


class Metrics(MetricsBase):
    def __repr__(self):
        return """
<%s total:%s shares:%s citations:%s comments:%s>
""" % (type(self).__name__, self.total, self.shares, self.citations, self.comments)


SourceBase = dictmapper('SourceBase',
                        {'name': ['name'],
                         'display_name': ['display_name'],
                         'events_url': ['events_url'],
                         'update_date': to(['update_date'],
                                           cleanup._parse_dates_to_datetime),
                         'events': ['events'],
                         'metrics': to(['metrics'],
                                       lambda l: Metrics(l)
                                       if l is not None else None),
                         'histories': to(['histories'],
                                         cleanup._process_histories)
                        }
)


class Source(SourceBase):
    def __repr__(self):
        return "<%s %s:%s>" % (type(self).__name__, self.display_name, self.metrics.total)


ArticleALMBase = dictmapper('ArticleALMBase',
                            {
                                'doi': ['doi'],
                                'mendeley_id': ['mendeley'],
                                'pmcid': ['pmcid'],
                                'pmid': ['pmid'],
                                'publication_date': to(['publication_date'],
                                                       cleanup._parse_dates_to_datetime),
                                'update_date': to(['update_date'],
                                                  cleanup._parse_dates_to_datetime),
                                'url': ['url'],
                                'title': ['title'],
                                'citations': to(['citations'],
                                                cleanup._parse_numbers_to_int),
                                'bookmarks': to(['bookmarks'],
                                                cleanup._parse_numbers_to_int),
                                'shares': to(['shares'],
                                             cleanup._parse_numbers_to_int),
                                'views': to(['views'],
                                            cleanup._parse_numbers_to_int)
                            }
)


class ArticleALM(ArticleALMBase):
    _sources = {}
    _resp_json = None

    def _load_sources(self):
        for src in self._resp_json.get('sources', None):
            self._sources[src['name']] = Source(src)

    @property
    def sources(self):
        if self._sources == {}:
            self._load_sources()
        return self._sources

    def __repr__(self):
        return "<%s %s, DOI %s>" % (type(self).__name__, self.title, self.doi)


def get_alm(identifiers,
            id_type=None,
            info=None,
            source=None,
            days=None,
            months=None,
            years=None,
            instance='plos'):
    """
    Get summary level alms based on an identifier or identifiers
    """

    if type(identifiers) != str:
        identifiers = ','.join(identifiers)

    parameters = {'ids': identifiers,
                  'api_key': config.APIS.get(instance).get('key'),
                  'type': id_type,
                  'info': info,
                  'source': source,
                  'days': days,
                  'months': months,
                  'years': years
    }

    url = config.APIS.get(instance).get('url')
    if url:
        resp = requests.get(url,
                            params=parameters,
                            headers=BASE_HEADERS)

        resp.raise_for_status()

        articles = []
        for article_json in resp.json():
            articles.append(_process_json_to_article(article_json))

        return articles

    else:
        raise


def _process_json_to_article(article_json):
    article = ArticleALM(article_json)
    article._sources = {}
    article._resp_json = article_json
    return article
