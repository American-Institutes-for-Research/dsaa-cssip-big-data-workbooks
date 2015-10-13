import unittest
import pyalm.pyalm as pyalm
import pyalm.events as events
import datetime
import pprint
import json
from test_pyalm import TestOffline as TestOffline

class TestSourcesEvents(TestOffline):
    def testTwitterEvents(self):
        tweets = []
        for tweet in self.mock_resp.sources['twitter'].events:
            tweets.append(events.Tweet(tweet))

        self.assertEqual(tweets[0].username, 'opdebult')
        self.assertEqual(tweets[0].created_at, datetime.datetime(2012, 8, 19, 7, 26, 6))
        self.assertEqual(tweets[0].id, '237088032224849920')
        self.assertEqual(tweets[0].profile_image,
            'http://a0.twimg.com/profile_images/1741153180/Tidan_normal.jpg')
        self.assertEqual(tweets[0].text,
            "#PLOS: Ecological Guild Evolution and the Discovery of the World's Smallest Vertebrate http://t.co/yEGLyWTf")
        self.assertEqual(tweets[0].url,
            "http://twitter.com/opdebult/status/237088032224849920")
        self.assertEqual(tweets[8].username, 'didicikit')
        self.assertEqual(tweets[8].text, "Ecological Guild Evolution and the Discovery of the World's Smallest Vertebrate http://t.co/2G6fQJvFhq")
        self.assertEqual(tweets[8].url, "http://twitter.com/didicikit/status/313850610174799873")


    def testCrossrefEvents(self):
        cites = []
        for cite in self.mock_resp.sources['crossref'].events:
            cites.append(events.Citation(cite))

        #Testing against first entry
        self.assertEqual(cites[0].article_title,
                    'New insights into the systematics and molecular phylogeny of the Malagasy snake genus Liopholidophis suggest at least one rapid reversal of extreme sexual dimorphism in tail length')
        self.assertEqual(cites[0].doi, '10.1007/s13127-013-0152-4')
        self.assertEqual(cites[0].fl_count, 0)
        self.assertEqual(cites[0].issn, [u'1439-6092', u'1618-1077'])
        self.assertEqual(cites[0].journal_abbreviation,
            'Org Divers Evol')
        self.assertEqual(cites[0].journal_title,
            'Organisms Diversity & Evolution')
        self.assertEqual(cites[0].publication_type, 'full_text')
        self.assertEqual(cites[0].publication_year, 2013)
        self.assertEqual(cites[0].issue, None)
        self.assertEqual(cites[0].volume, None)
        self.assertEqual(cites[0].first_page, None)

        #Testing against last entry
        self.assertEqual(cites[6].article_title,
                    'Are diminutive turtles miniaturized? The ontogeny of plastron shape in emydine turtles')
        self.assertEqual(cites[6].doi, '10.1111/bij.12010')
        self.assertEqual(cites[6].fl_count, 0)
        self.assertEqual(cites[6].issn, '00244066')
        self.assertEqual(cites[6].journal_abbreviation,
            'Biol J Linn Soc Lond')
        self.assertEqual(cites[6].journal_title,
            'Biological Journal of the Linnean Society')
        self.assertEqual(cites[6].publication_type, 'full_text')
        self.assertEqual(cites[6].publication_year, 2013)
        self.assertEqual(cites[6].issue, 4)
        self.assertEqual(cites[6].volume, 108)
        self.assertEqual(cites[6].first_page, 727)

        #Contributors
        self.assertEqual(len(cites[0].contributors), 5)
        self.assertEqual(cites[0].contributors[0].contributor_role, 'author')
        self.assertEqual(cites[0].contributors[0].first_author, True)
        self.assertEqual(cites[0].contributors[0].given_name, 'Frank')
        self.assertEqual(cites[0].contributors[0].surname, 'Glaw')
        self.assertEqual(cites[0].contributors[0].sequence, 'first')
        self.assertEqual(cites[6].contributors[1].contributor_role, 'author')
        self.assertEqual(cites[6].contributors[1].first_author, False)
        self.assertEqual(cites[6].contributors[1].given_name, 'Chris R.')
        self.assertEqual(cites[6].contributors[1].surname, 'Feldman')
        self.assertEqual(cites[6].contributors[1].sequence, 'additional')

    def testWikipedia(self):
        wiki = events.WikiRef(self.mock_resp.sources['wikipedia'].events)
        self.assertEqual(wiki.ca, 2)
        self.assertEqual(wiki.commons, 0)
        self.assertEqual(wiki.cs, 0)
        self.assertEqual(wiki.en, 10)
        self.assertEqual(wiki.es, 2)
        self.assertEqual(wiki.fi, 1)
        self.assertEqual(wiki.fr, 3)
        self.assertEqual(wiki.hu, 0)
        self.assertEqual(wiki.it, 2)
        self.assertEqual(wiki.ja, 1)
        self.assertEqual(wiki.ko, 1)
        self.assertEqual(wiki.nl, 2)
        self.assertEqual(wiki.no, 2)
        self.assertEqual(wiki.pl, 7)
        self.assertEqual(wiki.pt, 2)
        self.assertEqual(wiki.ru, 3)
        self.assertEqual(wiki.sv, 1)
        self.assertEqual(wiki.total, 49)
        self.assertEqual(wiki.uk, 1)
        self.assertEqual(wiki.vi, 2)
        self.assertEqual(wiki.zh, 2)

    def testMendeley(self):
        mend = events.Mendeley(self.mock_resp.sources['mendeley'].events)
        self.assertEqual(mend.categories, [35, 48, 52, 43, 40, 44, 210])
        self.assertEqual(mend.bookmarks, 50)
        self.assertEqual(mend.reader_countries,
                            [
                                {u'name': u'United States', u'value': 18},
                                {u'name': u'Portugal', u'value': 8},
                                {u'name': u'Brazil', u'value': 8}
                            ]
                        )
        self.assertEqual(mend.uuid, '476c0910-3e94-11e1-a0e9-0024e8453de6')
        self.assertEqual(mend.mendeley_url,
          'http://www.mendeley.com/research/ecological-guild-evolution-discovery-worlds-smallest-vertebrate/')
        self.assertEqual(mend.file_url,
          'https://api.mendeley.com/oapi/documents/file/476c0910-3e94-11e1-a0e9-0024e8453de6/164889e703e0cd991f1a6a5a77b469f74a546f9d/')

    def testFacebook(self):
        facebook = events.Facebook(self.mock_resp.sources['facebook'].events)
        self.assertEqual(facebook.commentsbox_count, 0)
        self.assertEqual(facebook.normalized_url,
                           'http://dx.doi.org/10.1371/journal.pone.0029797')
        self.assertEqual(facebook.click_count, 0)
        self.assertEqual(facebook.total_count, 228)
        self.assertEqual(facebook.comment_count, 22)
        self.assertEqual(facebook.like_count, 59)
        self.assertEqual(facebook.comments_fbid, None)
        self.assertEqual(facebook.share_count, 147)


if __name__ == "__main__":
    unittest.main()