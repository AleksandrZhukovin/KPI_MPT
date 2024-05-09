from unittest import TestCase

from .config import app
from .models import Post, db
from .views import IndexView


class AppTest(TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_post_create(self):
        view = IndexView(None)
        view.post({'title': 'Test'})
        view.update_model()
        assert Post.query.get(1).title == 'Test'
        assert Post.query.count() == 1

    def test_make_response(self):
        view = IndexView(None)
        html = view.make_response()
        assert '<p><b>Post {post.id}:</b> {post.title}.' in html
