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


CrossrefBase = dictmapper('CrossrefBase',
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


class CrossRef(CrossrefBase):
    def __repr__(self):
        return '<%s %s:%s>' % (type(self).__name__, self.article_title, self.doi)

TweetBase = dictmapper('TweetBase',
                    {
                     'created_at' : to(['event', 'created_at'],
                           cleanup._parse_dates_to_datetime),
                     'id' : ['event', 'id'],
                     'user' : ['event', 'user'],
                     'user_name' : ['event', 'user_name'],
                     'user_profile_image' : ['event', 'user_profile_image'],
                     'text' : ['event', 'text'],
                     'url' : ['event_url'],
                     'time' : ['event_time'],
                     'event_csl' : ['event_csl']
                     }
                   )

class Tweet(TweetBase):
    def __repr__(self):
        return '<%s %s:%s>' % (type(self).__name__, self.user, self.text)

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

# MendeleyBase = dictmapper('MendeleyBase',
#                             {
#                                 'readers' : ['events', 'readers'],
#                                 'discipline' : ['events', 'discipline'],
#                                 'country' : ['events', 'country'],
#                                 'status' : ['events', 'status'],
#                                 'events_csl' : ['events_csl']
#                             }
#                           )

# class Mendeley(MendeleyBase):
#     def __repr__(self):
#         return '<%s Readers:%s>' % (type(self).__name__, self.readers)

def mendeley_events(object):
    out = object.events
    out['url'] = object.events_url
    out['events_csl'] = object.events_csl
    out['events_url'] = object.events_url
    return out

FacebookBase = dictmapper('FacebookBase',
                            {
                                'url' : ['url'],
                                'share_count' : ['share_count'],
                                'like_count' : ['like_count'],
                                'comment_count' : ['comment_count'],
                                'click_count' : ['click_count'],
                                'total_count' : ['total_count']
                            }
                          )

class Facebook(FacebookBase):
    def __repr__(self):
        return '<%s Total:%s>' % (type(self).__name__, self.total_count)

NatureBase = dictmapper('NatureBase',
                    {
                     'blog' : ['event', 'blog'],
                     'links_to_doi' : ['event', 'links_to_doi'],
                     'percent_complex_words' : ['event', 'percent_complex_words'],
                    'popularity' : ['event', 'popularity'],
                    'created_at' : ['event', 'created_at'],
                    'title' : ['event', 'title'],
                    'body' : ['event', 'body'],
                    'updated_at' : ['event', 'updated_at'],
                    'flesch' : ['event', 'flesch'],
                    'url' : ['event', 'url'],
                    'blog_id' : ['event', 'blog_id'],
                    'id' : ['event', 'id'],
                    'hashed_id' : ['event', 'hashed_id'],
                    'num_words' : ['event', 'num_words'],
                    'published_at' : ['event', 'published_at'],
                    'fog' : ['event', 'fog'],
                    'event_time' : ['event_time'],
                    'event_url' : ['event_url'],
                    'event_csl' : ['event_csl']
                     }
                   )

class Nature(NatureBase):
    def __repr__(self):
        return '<%s: %s>' % (type(self).__name__, self.title)


PubmedBase = dictmapper('PubmedBase',
                    {
                      'event' : ['event'],
                      'event_url' : ['event_url']
                     }
                   )

class Pubmed(PubmedBase):
    def __repr__(self):
        return '<%s: %s>' % (type(self).__name__, self.event)



ScopusBase = dictmapper('ScopusBase',
                    {
                        'fa' : [ '@_fa' ],
                        'link' : [ 'link' ],
                        'prism_url' : [ 'prism:url' ],
                        'dc_identifier' : [ 'dc:identifier' ],
                        'eid' : [ 'eid' ],
                        'dc_title' : [ 'dc:title' ],
                        'dc_creator' : [ 'dc:creator' ],
                        'prism_publicationName' : [ 'prism:publicationName' ],
                        'prism_issn' : [ 'prism:issn' ],
                        'prism_eIssn' : [ 'prism:eIssn' ],
                        'prism_volume' : [ 'prism:volume' ],
                        'prism_issueIdentifier' : [ 'prism:issueIdentifier' ],
                        'prism_coverDate' : [ 'prism:coverDate' ],
                        'prism_coverDisplayDate' : [ 'prism:coverDisplayDate' ],
                        'prism_doi' : [ 'prism:doi' ],
                        'citedby_count' : [ 'citedby-count' ],
                        'affiliation' : [ 'affiliation' ],
                        'pubmed_id' : [ 'pubmed-id' ],
                        'prism_aggregationType' : [ 'prism:aggregationType' ],
                        'subtype' : [ 'subtype' ],
                        'subtypeDescription' : [ 'subtypeDescription' ]
                     }
                   )

class Scopus(ScopusBase):
    def __repr__(self):
        return '<%s: %s>' % (type(self).__name__, self.citedby_count)


CounterBase = dictmapper('CounterBase',
                    {
                        'month' : [ 'month' ],
                        'year' : [ 'year' ],
                        'pdf_views' : [ 'pdf_views' ],
                        'xml_views' : [ 'xml_views' ],
                        'html_views' : [ 'html_views' ]
                     }
                   )

class Counter(CounterBase):
    def __repr__(self):
        return '<%s PDF:%s XML:%s HTML:%s>' % (type(self).__name__, self.pdf_views, self.xml_views, self.html_views)


ResearchBloggingBase = dictmapper('ResearchBloggingBase',
                    {
                        'post_title' : [ 'event', 'post_title' ],
                        'blog_name' : [ 'event', 'blog_name' ],
                        'blogger_name' : [ 'event', 'blogger_name' ],
                        'received_date' : [ 'event', 'received_date' ],
                        'published_date' : [ 'event', 'published_date' ],
                        'post_URL' : [ 'event', 'post_URL' ],
                        'citations' : to(['event','citations'],
                                        cleanup._parse_citations),
                        'id' : [ 'event', 'id' ],
                        'event_url' : [ 'event_url' ]
                     }
                   )

class ResearchBlogging(ResearchBloggingBase):
    def __repr__(self):
        return '<%s: %s>' % (type(self).__name__, self.post_title)


PMCBase = dictmapper('PMCBase',
                    {
                        'month' : [ 'month' ],
                        'year' : [ 'year' ],
                        'pdf' : [ 'pdf' ],
                        'unique_ip' : [ 'unique-ip' ],
                        'full_text' : [ 'full-text' ],
                        'abstract' : [ 'abstract' ],
                        'scanned_summary' : [ 'scanned-summary' ],
                        'scanned_page_browse' : [ 'scanned-page-browse' ],
                        'figure' : [ 'figure' ],
                        'supp_data' : [ 'supp-data' ],
                        'cited_by' : [ 'cited-by' ]
                     }
                   )

class PMC(PMCBase):
    def __repr__(self):
        return '<%s YR/MO:%s/%s PDF:%s>' % (type(self).__name__, self.year, self.month, self.pdf)


FigshareBase = dictmapper('FigshareBase',
                    {
                        'files' : [ 'month' ],
                        'pos_in_sequence' : [ 'pos_in_sequence' ],
                        'stats' : [ 'stats' ],
                        'users' : [ 'users' ],
                        'links' : [ 'links' ],
                        'tags' : [ 'tags' ],
                        'title' : [ 'figshare_url' ],
                        'figshare_url': [ 'figshare_url' ],
                        'defined_type' : [ 'defined_type' ],
                        'doi' : [ 'doi' ],
                        'published_date' : to(['published_date'],
                           cleanup._parse_dates_figshare),
                        'article_id' : [ 'article_id' ],
                        'categories' : [ 'categories' ],
                        'description' : [ 'description' ]
                     }
                   )

class Figshare(FigshareBase):
    def __repr__(self):
        return '<%s Downloads:%s Pageviews:%s Likes:%s>' % (type(self).__name__, self.stats['downloads'], self.stats['page_views'], self.stats['likes'])


PlosCommentsBase = dictmapper('PlosCommentsBase',
                    {
                        'originalTitle': [ 'event', 'originalTitle' ],
                        'title': [ 'event', 'title' ],
                        'body': [ 'event', 'body' ],
                        'originalBody': [ 'event', 'originalBody' ],
                        'truncatedBody': [ 'event', 'truncatedBody' ],
                        'bodyWithUrlLinkingNoPTags': [ 'event', 'bodyWithUrlLinkingNoPTags' ],
                        'truncatedBodyWithUrlLinkingNoPTags': [ 'event', 'truncatedBodyWithUrlLinkingNoPTags' ],
                        'bodyWithHighlightedText': [ 'event', 'bodyWithHighlightedText' ],
                        'competingInterestStatement': [ 'event', 'competingInterestStatement' ],
                        'truncatedCompetingInterestStatement': [ 'event', 'truncatedCompetingInterestStatement' ],
                        'annotationUri': [ 'event', 'annotationUri' ],
                        'creatorID': [ 'event', 'creatorID' ],
                        'creatorDisplayName': [ 'event', 'creatorDisplayName' ],
                        'creatorFormattedName': [ 'event', 'creatorFormattedName' ],
                        'articleID': [ 'event', 'articleID' ],
                        'articleDoi': [ 'event', 'articleDoi' ],
                        'articleTitle': [ 'event', 'articleTitle' ],
                        'created' : to(['event', 'created'],
                           cleanup._parse_dates_to_datetime),
                        'createdFormatted' : to(['event', 'createdFormatted'],
                           cleanup._parse_dates_to_datetime),
                        'type': [ 'event', 'type' ],
                        'replies': [ 'event', 'replies' ],
                        'lastReplyDate' : to(['event', 'lastReplyDate'],
                           cleanup._parse_dates_to_datetime),
                        'totalNumReplies': [ 'event' ,'totalNumReplies' ],
                        'event_time' : to(['event_time'],
                           cleanup._parse_dates_to_datetime),
                        'event_url' : [ 'event_url' ],
                        'event_csl' : [ 'event_csl' ]
                     }
                   )

class PlosComments(PlosCommentsBase):
    def __repr__(self):
        return '<%s: %s>' % (type(self).__name__, self.title)


ScienceseekerBase = dictmapper('ScienceseekerBase',
                    {
                        'title': [ 'event', 'title' ],
                        'id': [ 'event', 'id' ],
                        'link': [ 'event', 'link' ],
                        'updated' : to(['event', 'updated'],
                           cleanup._parse_dates_to_datetime),
                        'author': [ 'event', 'author' ],
                        'summary': [ 'event', 'summary' ],
                        'citations': [ 'event', 'citations' ],
                        'community': [ 'event', 'community' ],
                        'category': [ 'event', 'category' ],
                        'source': [ 'event', 'source' ],
                        'lang': [ 'event', 'lang' ],
                        'event_time' : to(['event_time'],
                           cleanup._parse_dates_to_datetime),
                        'event_url': [ 'event_url' ],
                        'event_csl': [ 'event_csl' ]
                     }
                   )

class Scienceseeker(ScienceseekerBase):
    def __repr__(self):
        return '<%s: %s>' % (type(self).__name__, self.title)



F1000Base = dictmapper('F1000Base',
                    {
                        'classifications': [ 'event', 'classifications' ],
                        'doi': [ 'event', 'doi' ],
                        'f1000_id': [ 'event', 'f1000_id' ],
                        'updated_at' : to(['event', 'updated_at'],
                           cleanup._parse_dates_to_datetime),
                        'year': [ 'event', 'year' ],
                        'month': [ 'event', 'month' ],
                        'score': [ 'event', 'score' ],
                        'url': [ 'event', 'url' ],
                        'event_url': [ 'event_url' ]
                     }
                   )

class F1000(F1000Base):
    def __repr__(self):
        return '<%s: %s>' % (type(self).__name__, self.doi)


WordpressBase = dictmapper('WordpressBase',
                    {
                        'title': [ 'event', 'title' ],
                        'author': [ 'event', 'author' ],
                        'link': [ 'event', 'link' ],
                        'epoch_time': [ 'event', 'epoch_time' ],
                        'guid': [ 'event', 'guid' ],
                        'content': [ 'event', 'content' ],
                        'event_time' : to(['event_time'],
                           cleanup._parse_dates_to_datetime),
                        'event_url': [ 'event_url' ],
                        'event_csl': [ 'event_csl' ]
                     }
                   )

class Wordpress(WordpressBase):
    def __repr__(self):
        return '<%s %s:%s>' % (type(self).__name__, self.author, self.title)



RedditBase = dictmapper('RedditBase',
                    {
                        'domain': [ 'event', 'domain' ],
                        'banned_by': [ 'event', 'banned_by' ],
                        'media_embed': [ 'event', 'media_embed' ],
                        'subreddit': [ 'event', 'subreddit' ],
                        'selftext_html': [ 'event', 'selftext_html' ],
                        'selftext': [ 'event', 'selftext' ],
                        'likes': [ 'event', 'likes' ],
                        'user_reports': [ 'event', 'user_reports' ],
                        'secure_media': [ 'event', 'secure_media' ],
                        'link_flair_text': [ 'event', 'link_flair_text' ],
                        'id': [ 'event', 'id' ],
                        'gilded': [ 'event', 'gilded' ],
                        'secure_media_embed': [ 'event', 'secure_media_embed' ],
                        'clicked': [ 'event', 'clicked' ],
                        'report_reasons': [ 'event', 'report_reasons' ],
                        'author': [ 'event', 'author' ],
                        'media': [ 'event', 'media' ],
                        'score': [ 'event', 'score' ],
                        'approved_by': [ 'event', 'approved_by' ],
                        'over_18': [ 'event', 'over_18' ],
                        'hidden': [ 'event', 'hidden' ],
                        'num_comments': [ 'event', 'num_comments' ],
                        'thumbnail': [ 'event', 'thumbnail' ],
                        'subreddit_id': [ 'event', 'subreddit_id' ],
                        'edited': to([ 'event', 'edited' ],
                            cleanup._parse_unix),
                        'link_flair_css_class': [ 'event', 'link_flair_css_class' ],
                        'author_flair_css_class': [ 'event', 'author_flair_css_class' ],
                        'downs': [ 'event', 'downs' ],
                        'saved': [ 'event', 'saved' ],
                        'stickied': [ 'event', 'stickied' ],
                        'is_self': [ 'event', 'is_self' ],
                        'permalink': [ 'event', 'permalink' ],
                        'name': [ 'event', 'name' ],
                        'created': to([ 'event', 'created' ],
                            cleanup._parse_unix),
                        'url': [ 'event', 'url' ],
                        'author_flair_text': [ 'event', 'author_flair_text' ],
                        'title': [ 'event', 'title' ],
                        'created_utc': to([ 'event', 'created_utc' ],
                            cleanup._parse_unix),
                        'distinguished': [ 'event', 'distinguished' ],
                        'mod_reports': [ 'event', 'mod_reports' ],
                        'visited': [ 'event', 'visited' ],
                        'num_reports': [ 'event', 'num_reports' ],
                        'ups': [ 'event', 'ups' ],
                        'event_time' : to(['event_time'],
                           cleanup._parse_dates_to_datetime),
                        'event_url': [ 'event_url' ],
                        'event_csl': [ 'event_csl' ]
                     }
                   )

class Reddit(RedditBase):
    def __repr__(self):
        return '<%s %s:%s>' % (type(self).__name__, self.author, self.title)



DataciteBase = dictmapper('DataciteBase',
                    {
                        'relatedIdentifier': [ 'event', 'relatedIdentifier' ],
                        'doi': [ 'event', 'doi' ],
                        'publicationYear': [ 'event', 'publicationYear' ],
                        'publisher': [ 'event', 'publisher' ],
                        'title': [ 'event', 'title' ],
                        'creator': [ 'event', 'creator' ],
                        'event_url': [ 'event_url' ]
                     }
                   )

class Datacite(DataciteBase):
    def __repr__(self):
        return '<%s: %s>' % (type(self).__name__, self.doi)


ArticlecoverageBase = dictmapper('ArticlecoverageBase',
                    {
                        'link_state': [ 'event', 'link_state' ],
                        'publication': [ 'event', 'publication' ],
                        'published_on' : to(['event', 'published_on'],
                           cleanup._parse_dates_to_datetime),
                        'referral': [ 'event', 'referral' ],
                        'title': [ 'event', 'title' ],
                        'type': [ 'event', 'type' ],
                        'language': [ 'event', 'language' ],
                        'event_url': [ 'event_url' ],
                        'event_time' : to(['event_time'],
                           cleanup._parse_dates_to_datetime)
                     }
                   )

class Articlecoverage(ArticlecoverageBase):
    def __repr__(self):
        return '<%s: %s>' % (type(self).__name__, self.title)

class ArticlecoverageCurated(ArticlecoverageBase):
    def __repr__(self):
        return '<%s: %s>' % (type(self).__name__, self.title)
