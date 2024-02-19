import uniitest

from main import app
import os

class TestToPerform(uniitest.TestCase):
    def setup(self):
        self.app = app.test_client()

    def tearDown():
        pass

    def test_age(self):
        response = self.app.get('/',follow_redirects = True)
        print(response)
        self.assertEqual(response.status_code, 200)

if __name__=='__main__':
    uniitest.main()
