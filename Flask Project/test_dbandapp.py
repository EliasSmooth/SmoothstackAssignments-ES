import email
import os
os.environ['DATABASE_URL'] = 'sqlite://'

import unittest
from flask import current_app
from website import create_app, db
from website.models import User


class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.appctx = self.app.app_context()
        self.appctx.push()
        db.create_all()
        self.populate_db()
        self.client = self.app.test_client

    def tearDown(self):
        db.drop_all()
        self.appctx.pop()
        self.app = None
        self.appctx = None

    def test_app(self):
        assert self.app is not None
        assert current_app == self.app

    def populate_db(self):
        user = User(username='tester', email='tester@gmail.com', password='tester1')
        db.session.add(user)
        db.session.commit()