from app import db


class Books(db.Model):
  __tablename__ = "books"
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(200), nullable=False)
  email = db.Column(db.String(120), nullable=False)

  def __repr__(self):
    return f'Book with name{self.title} and email {self.email}'