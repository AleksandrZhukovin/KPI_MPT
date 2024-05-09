from .config import app
from .models import Post, db

from flask import render_template, request


class IndexView:
    def __init__(self, request_: request.__class__):
        self.request = request_
        self.POST = None

    def post(self, post_data: dict):
        self.POST = post_data

    def update_model(self):
        if self.POST.get('title'):
            post = Post(title=self.POST.get('title'))
            db.session.add(post)
            db.session.commit()
            return self.make_response()
        else:
            raise ValueError('No title')

    @staticmethod
    def read_model():
        return Post.query.all()

    @staticmethod
    def make_response():
        html = ''
        for post in Post.query.all():
            html += f"""<p><b>Post {post.id}:</b> {post.title}. 
                    <i>({post.created_at.strftime('%d.%m.%Y %H:%M:%S')})</i></p>"""
        return html


@app.route('/', methods=['GET', 'POST'])
def index():
    view = IndexView(request)
    if request.method == 'GET':
        return render_template('index.html', data=view.read_model())
    elif request.method == 'POST':
        view.post(request.form)
        return view.update_model()
