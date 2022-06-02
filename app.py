from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello_world():  # put application's code here
    return render_template("index.html")

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route('/shop')
def shop():
    items = [
        {'bid': "AA7868", 'book_name': 'The Shining', 'Author': 'Stephen King', 'price': 500},
        {'bid': "TY8678", 'book_name': 'Tough Times Never LAst , But Tough People Do', 'Author': 'Schuller', 'price': 50},
        {'bid': "KJ5646", 'book_name': 'The Last Symbol', 'Author': 'Dan Brown', 'price': 150},
        {'bid': "AP4344", 'book_name': 'Growing Up Bin Laden', 'Author': 'Najwa & Omar Bin Laden', 'price': 500},
        {'bid': "AW89936", 'book_name': 'The White Tiger', 'Author': 'Arvind Adiga', 'price': 500},

    ]
    return render_template("shop.html",items=items)


if __name__ == '__main__':
    app.run(debug=True)
