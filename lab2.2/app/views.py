from .config import app
from .models import Post, Model

from flask import render_template, request


class ViewModel:
    def __init__(self, request_, view_class, template_name):
        self.request = request_
        self.view = view_class(template_name)
        self.model = Model(Post)

    def process(self):
        if self.request.method == 'GET':
            return self.get()
        elif self.request.method == 'POST':
            return self.post()

    def get(self):
        return render_template(self.view.template_name, data=self.model.get_table_data())

    def post(self):
        self.model.insert_table_data(self.request.form)
        return self.view.make_post_template_response(self.model.get_table_data())


class IndexView:
    def __init__(self, template_name):
        self.template_name = template_name

    @staticmethod
    def make_post_template_response(post_data: list):
        html = ''
        for post in post_data:
            html += f"""<p><b>Post {post.id}:</b> {post.title}. 
                    <i>({post.created_at.strftime('%d.%m.%Y %H:%M:%S')})</i></p>"""
        return html


@app.route('/', methods=['GET', 'POST'])
def index():
    view_model = ViewModel(request, IndexView, 'index.html')
    response = view_model.process()
    return response
