from flask import Flask, render_template, request, redirect, url_for

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

all_books = ["Library is empty."]



@app.route('/')
def home():
    return render_template('index.html', data=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    global all_books
    if request.form.get("bname") != None:
        # all_books.append(request.form.get("bname"))
        # all_books.append(request.form.get("bauthor"))

        # all_books.append(request.form.get("brating"))
        
        all_books.append({"title": request.form.get("bname"),
                      "author": request.form.get("bauthor"),
                      "rating": request.form.get("brating")})
        print(all_books)
    

    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

