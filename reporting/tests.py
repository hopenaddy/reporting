from django.test import TestCase, Client
import unittest
#
#
class IndexPageTest(TestCase):
#
    def test_indexpage_available(self):
        c = Client()
        response = c.get('http://127.0.0.1:8000/', follow=True) 
        self.assertEquals(response.status_code,200)
      


if __name__ == '__main__':
	
	unittest.main()

# Create your tests here.
