from flask import render_template, request
from models import Books

def register_routes(app, db):

  @app.route('/')
  def index():
    people = Books.query.all()
    return str(people)