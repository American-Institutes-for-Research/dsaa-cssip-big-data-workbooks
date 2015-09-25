import unittest
import pyalm.utilities.plossearch as search
import datetime
import pprint
import json

class SetUp(unittest.TestCase):

    def setUp(self):
        self.query = {'author' : 'Neylon'}
        self.start_date = datetime.datetime(2007, 1, 1)
        self.end_date = datetime.datetime(2013, 12, 31, 12, 34, 01)
        self.fields = ['title', 'doi']
        self.test_query = search.Request(self.query, self.fields)

class TestRequests(SetUp):
    def testBasicQuery(self):
        test_response = self.test_query.get()
        self.assertEqual(self.test_query.response.status_code, 200)
        self.assertGreater(len(test_response['response']['docs']), 6)

    def testQueryWithYearInts(self):
        self.test_query.search_date(2013, 2014)
        test_response = self.test_query.get()
        self.assertEqual(self.test_query.response.status_code, 200)
        self.assertEqual(len(test_response['response']['docs']), 3)

    def testQueryWithYearDatetimes(self):
        self.test_query.search_date(self.start_date, self.end_date)
        test_response = self.test_query.get()
        self.assertEqual(self.test_query.response.status_code, 200)
        self.assertEqual(len(test_response['response']['docs']), 7)

    def testQueryWithPaging(self):
        test_response = self.test_query.get()
        self.assertEqual(self.test_query.response.status_code, 200)
        self.assertGreater(len(test_response['response']['docs']), 6)

class TestCollectDOIs(unittest.TestCase):
    def setUp(self):
        self.query = {'author' : 'Neylon'}
        self.start_date = datetime.datetime(2007, 1, 1)
        self.end_date = datetime.datetime(2013, 12, 31, 12, 34, 01)

    def testCollectDOIs(self):
        dois = search.collect_dois(self.query, (self.start_date, self.end_date))
        self.assertIsInstance(dois, list)
        self.assertEqual(len(dois), 7)

class TestFormattingFunctions(SetUp):
    def testSearchYear(self):
        self.test_query.search_year(2013)
        self.assertEqual(self.test_query.query['publication_date'],
                            '[2013-01-01T00:00:00Z TO 2013-12-31T23:59:59Z]')

if __name__ == "__main__":
    unittest.main()
