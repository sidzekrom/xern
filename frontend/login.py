from flask import *
import sys
sys.path.insert(0, '../backend')
from locations import *

app = Flask(__name__)

@app.route('/<user>', methods = ['GET', 'POST'])
def home(user):
    if (user == ""):
        return redirect(url_for('login'))
    return render_template('home.html', username = user)

@app.route('/login', methods = ['GET', 'POST'])
def login(error = "Gundumeshwar"):
    if (request.method == "POST"):
        if (request.form['submit'] == 'Login'):
            username = request.form['username']
            givenpass = request.form['password']
            if (not actionInst.userExists(username)):
                return redirect(url_for('home',\
                    username = "Not a valid user"))
            actualpass = mongohelper.retrieve(['password'], user_collection,\
                    to_search = {'user' : username})
            if (actualpass != givenpass):
                return redirect(url_for('home',\
                                    user = "imposter"))
            else:
                print url_for('home', user = username)
                return redirect(url_for('home', user = username))
        else:
            return redirect(url_for('signup'))
    return render_template('login.html', error = error)

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

app.debug = True
app.run()
