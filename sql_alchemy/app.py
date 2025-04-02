from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_migrate import Migrate


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


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    author: Mapped[str]
    review: Mapped[float]


with app.app_context():
    db.create_all()

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run()

# @app.route("/users")
# def user_list():
#     users = db.session.execute(db.select(User).order_by(User.username)).scalars()
#     return render_template("user/list.html", users=users)

# @app.route("/users/create", methods=["GET", "POST"])
# def user_create():
#     if request.method == "POST":
#         user = User(
#             username=request.form["username"],
#             email=request.form["email"],
#         )
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for("user_detail", id=user.id))

#     return render_template("user/create.html")

# @app.route("/user/<int:id>")
# def user_detail(id):
#     user = db.get_or_404(User, id)
#     return render_template("user/detail.html", user=user)

# @app.route("/user/<int:id>/delete", methods=["GET", "POST"])
# def user_delete(id):
#     user = db.get_or_404(User, id)

#     if request.method == "POST":
#         db.session.delete(user)
#         db.session.commit()
#         return redirect(url_for("user_list"))

#     return render_template("user/delete.html", user=user)