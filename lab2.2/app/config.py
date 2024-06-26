from flask import Flask


app = Flask(__name__)

app.config['SECRET_KEY'] = '<KEY>'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
