# Higher level interface for interacting with specific classes of events
import pyalm as alm
import cleanup
from utils import dictmapper, MappingRule as to

ContributorBase = dictmapper('ContributorBase',
                              {
                               'contributor_role' : ['contributor_role'],
                               'first_author': to(['first_author'],
                                                    cleanup._text_to_bool),
                               'given_name': ['given_name'],
                               'sequence': ['sequence'],
                               'surname': ['surname']
                              }
                            )

class Contributor(ContributorBase):
    def __repr__(self):
        return '<%s: %s%s>' % (type(self).__name__, self.given_name, self.surname)


CitationBase = dictmapper('CitationBase',
                            {
                             'article_title' : ['event','article_title'],
                             'doi' : ['event','doi'],
                             'fl_count' : to(['event','fl_count'],
                                        cleanup._parse_numbers_to_int),
                             'issn' : ['event','issn'],
                             'journal_abbreviation' : ['event','journal_abbreviation'],
                             'journal_title' : ['event','journal_title'],
                             'publication_type' : ['event','publication_type'],
                             'publication_year' : to(['event','year'],
                                        cleanup._parse_numbers_to_int),
                             'first_page' : to(['event', 'first_page'],
                                        cleanup._parse_numbers_to_int),
                             'issue' : to(['event', 'issue'],
                                        cleanup._parse_numbers_to_int),
                             'volume' : to(['event', 'volume'],
                                        cleanup._parse_numbers_to_int),
                             'contributors' : to(['event','contributors', 'contributor'],
                                                lambda l: map(Contributor, l)
                                                if l is not None else None)
                            }
                          )


class Citation(CitationBase):
    def __repr__(self):
        return '<%s %s:%s>' % (type(self).__name__, self.article_title, self.doi)

TweetBase = dictmapper('TweetBase',
                    {
                     'created_at' : to(['event', 'created_at'],
                                            cleanup._parse_dates_to_datetime),
                     'id' : ['event', 'id'],
                     'username' : ['event', 'user'],
                     'profile_image' : ['event', 'user_profile_image'],
                     'text' : ['event', 'text'],
                     'url' : ['event_url']
                     }
                   )

class Tweet(TweetBase):
    def __repr__(self):
        return '<%s %s:%s>' % (type(self).__name__, self.username, self.text)

WikiBase = dictmapper('WikiBase',
                        {
                            'ca': ['ca'],
                            'commons': ['commons'],
                            'cs': ['cs'],
                            'de': ['de'],
                            'en': ['en'],
                            'es': ['es'],
                            'fi': ['fi'],
                            'fr': ['fr'],
                            'hu': ['hu'],
                            'it': ['it'],
                            'ja': ['ja'],
                            'ko': ['ko'],
                            'nl': ['nl'],
                            'no': ['no'],
                            'pl': ['pl'],
                            'pt': ['pt'],
                            'ru': ['ru'],
                            'sv': ['sv'],
                            'total': ['total'],
                            'uk': ['uk'],
                            'vi': ['vi'],
                            'zh': ['zh']})

class WikiRef(WikiBase):
    def __repr__(self):
        return '<%s Citations:%s>' % (type(self).__name__, self.total)

MendeleyBase = dictmapper('MendeleyBase',
                            {
                                'reader_countries' : ['stats', 'country'],
                                'bookmarks' : ['stats', 'readers'],
                                'reader_status' : ['stats', 'status'],
                                'reader_disciplines' : ['stats', 'discipline'],
                                'uuid' : ['uuid'],
                                'mendeley_url' : ['mendeley_url'],
                                'related_articles' : ['related'],
                                'categories' : ['categories'],
                                'file_url' : ['file_url']
                            }
                          )

class Mendeley(MendeleyBase):
    def __repr__(self):
        return '<%s Bookmarks:%s>' % (type(self).__name__, self.bookmarks)

FacebookBase = dictmapper('FacebookBase',
                            {
                                'normalized_url' : ['normalized_url'],
                                'commentsbox_count' : ['commentsbox_count'],
                                'click_count' : ['click_count'],
                                'total_count' : ['total_count'],
                                'comment_count' : ['comment_count'],
                                'like_count' : ['like_count'],
                                'comments_fbid' : ['comments_fbid'],
                                'share_count' : ['share_count']
                            }
                          )
class Facebook(FacebookBase):
    def __repr__(self):
        return '<%s Total:%s>' % (type(self).__name__, self.total_count)
