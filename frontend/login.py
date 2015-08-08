from flask import *

app = Flask(__name__)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if (request.method == "POST"):
        if (request.form['username'] != 'sidzekrom' or\
            request.form['password'] != 'praful'):
            return render_template('home.html', username = "Not a valid person")
        else:
            return render_template('home.html', username =\
                request.form['username'])
    return render_template('login.html', error = "Gundumeshwar")

app.debug = True
app.run()
