import unittest
from urlmaker import UrlMaker

class WebTest(unittest.TestCase):

    def test_create_url(self):
        domain = 'jrrickerson'
        expected_url = 'www.jrrickerson.com'

        maker = UrlMaker()
        result = maker.make(domain)

        self.assertEquals(result, expected_url)

if __name__ == 'main':
    unittest.main()
