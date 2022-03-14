import email
from urllib import response
from flask import Flask
from website import create_app
import unittest
from website import create_app, db

app = create_app()

class FlaskTestCase(unittest.TestCase):
    def test_index_status(self):
        tester = app.test_client(self)
        response = tester.get('/login')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get('/login')
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    def test_signup_status(self):
        tester = app.test_client(self)
        response = tester.get('/sign-up')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_signup_content(self):
        tester = app.test_client(self)
        response = tester.get('/sign-up')
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    def test_about_status(self):
        tester = app.test_client(self)
        response = tester.get('/about')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_about_content(self): 
        tester = app.test_client(self)
        response = tester.get('/about')
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    def test_login_post(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(email='eliasashtonsaunders@gmail.com', password="Es7585**"), follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    def test_logout(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email='eliasashtonsaunders@gmail.com', password="Es7585**"), follow_redirects=True)
        response = tester.get('/logout', follow_redirects=True)
        print(response.status_code)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_signup_content(self):
        tester = app.test_client(self)
        response = tester.get('/sign-up')
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
    
    def test_signup_status(self):
        tester = app.test_client(self)
        response = tester.get('/sign-up')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    def test_signup_form(self):
        tester = app.test_client(self)
        response = tester.post('/sign-up', content_type="multipart/form-data", data=dict(email="weewoo@gmail.com", username="weewoo", passwordOne="weewoo2", passwordTwo="weewoo2"))
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_mainredirect(self):
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects=True)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

        

if __name__ == '__main__':
    unittest.main()