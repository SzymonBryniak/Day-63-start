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


class Books(db.Model):
    __tablename__ = 'Books'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    author: Mapped[str]
    review: Mapped[str]


engine = create_engine('sqlite:///./new-books-collection.db', echo = True)
Session = sessionmaker(bind = engine)
session = Session()


with app.app_context():
    db.create_all()


all_books = []


@app.route('/')
def home():
    return render_template('index.html', data=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    global all_books
    if request.form.get("bname") != None:
       

        book = Books(title=request.form.get("bname"),
                       author=request.form.get("bauthor"),
                       review=request.form.get("brating"))
        print(book)


        with app.app_context():
            db.session.add(book)
            db.session.commit()


    with app.app_context():
         database = db.session.query(Books).all()
         for i in database:
            to_append = [i.title, i.author, i.review]
            all_books.append(to_append)
    print(all_books)


    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

