from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy import Integer, String, Float
from sqlalchemy import create_engine


class Base(DeclarativeBase):
 pass


db = SQLAlchemy(model_class=Base)  # app instead fo Base


# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./new-books-collection.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning

# initialize the app with the extension
db.init_app(app)


# class Books(db.Model):
#   __tablename__ = "books"
#   id = db.Column(db.Integer, primary_key=True)
#   title = db.Column(db.String(200), nullable=False)
#   email = db.Column(db.String(120), nullable=False)


# app = create_app()


class Books(db.Model):
    __tablename__ = 'Books'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    author: Mapped[str]
    review: Mapped[str]


engine = create_engine('sqlite:///./new-books-collection.db', echo = True)
Session = sessionmaker(bind = engine)
session = Session()


# book = Books(id=3, title='Harry Potter',
#                        author='J.K. Rowling',
#                        review='9.3')


with app.app_context():
    db.create_all()
    # db.session.add(book)
    db.session.commit()


# # Read A Particular Record By Query
with app.app_context():
    book = db.session.execute(db.select(Books).where(Books.title == "Harry Potter")).scalars()
# To get a single element we can use scalar() instead of scalars().
print(book)


# # Update A Particular Record By Query
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Books).where(Books.title == "Harry Potter")).scalar()
#     book_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit() 


# # Update A Record By PRIMARY KEY
# book_id = 1
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
#     # or book_to_update = db.get_or_404(Book, book_id)
#     book_to_update.title = "Harry Potter and the Goblet of Fire"
#     db.session.commit()  
# # Flask-SQLAlchemy also has some handy extra query methods like get_or_404() that we can use. Since Flask-SQLAlchemy version 3.0 the previous query methods like Book.query.get() have been deprecated


# # Delete A Particular Record By PRIMARY KEY
# book_id = 1
# with app.app_context():
#     book_to_delete = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
#     # or book_to_delete = db.get_or_404(Book, book_id)
#     db.session.delete(book_to_delete)
#     db.session.commit()
# # You can also delete by querying for a particular value e.g. by title or one of the other properties. Again, the get_or_404() method is quite handy.