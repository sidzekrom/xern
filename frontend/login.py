from flask import *
import sys
sys.path.insert(0, '../backend')
from locations import *
import os
seckey = 'tM\x14\xdcS\xa3#0\xf0\xf5xeD\x7fW\xa3\xee:\xd3\xf6\xa6\xb9\x91\xa6'

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if (request.method == "POST"):
        if (request.form['submit'] == 'sign out'):
            session.pop('user', None)
    if ('user' not in session):
        return redirect(url_for('login'))
    return render_template('home.html', username = session['user'])

@app.route('/login', methods = ['GET', 'POST'])
def login(error = ""):
    if (request.method == "POST"):
        if (request.form['submit'] == 'Login'):
            username = request.form['username']
            givenpass = request.form['password']
            if (not actionInst.userExists(username)):
                return redirect(url_for('home'))
                session['user'] = "Not a valid user"
            actualpass = mongohelper.retrieve(['password'], user_collection,\
                    to_search = {'user' : username})
            if (actualpass != givenpass):
                session['user'] = 'imposter'
                return redirect(url_for('home'))
            else:
                session['user'] = username
                return redirect(url_for('home'))
        else: #else it is 'Create new account'
            return redirect(url_for('signup'))
    return render_template('login.html')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if (request.method == "POST"):
        username = request.form['username']
        password = request.form['password']
        emailid = request.form['emailid']
        actionInst.addUser({'user' : username, 'password' : password,\
            'emailid' : emailid})
        return redirect(url_for('login', error = "Thank you for signing\
           up on Xern! You may log in now :)"))
    return render_template('createaccount.html')

app.secret_key = seckey
app.debug = True
app.run()
