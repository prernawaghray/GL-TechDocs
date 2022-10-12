from flask import render_template, request, url_for,session 
from flask import make_response, redirect, abort
from app import app, oauth


'''Login Authorization Wrapper'''
def login_required(function): 
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs) if session.get('user') else abort(401)
    return wrapper


def login_required(f):
    
    def wrap(*args, **kwargs):
        if  session.get('user') :
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return wrap

@app.route('/')
def home():
   return render_template('home-page/home.html')



@app.route('/register')
def register():
   return '<h1>Redirected to Register Page</h1>'



@app.route('/login', methods=['GET', 'POST'])
def login():
   if request.method != 'POST':
      return render_template('login/login.html') 

   if request.form['login_method'] == 'google':
        redirect_uri = url_for('auth', _external=True)
        return oauth.google.authorize_redirect(redirect_uri)

   elif request.form['login_method'] == 'email' and \
      request.form['email'] == 'admin@techdocs.com' and \
      request.form['password'] == 'admin123':
         # response = jsonify({"status": "false", "message":" User not registered "})
         # if response.status:
      session['user'] = {'email':request.form['email']}
      return redirect('/dashboard')
   else:
      return make_response({'email_status':0}, 401)


   
'''Google Authorization URL'''
@app.route('/auth')
def auth():
   token = oauth.google.authorize_access_token()
   session['user'] = token['userinfo']
   # session['user'] = {'email': token['userinfo']['email']}
   return redirect('/dashboard')



@app.route('/forgot_password')
def forgot_password():
   return make_response({'forgot_Password':True}, 302)


@app.route('/logout')
def logout():
   # session.clear()
   [session.pop(key) for key in list(session.keys())]
   return redirect('/')


@app.route('/dashboard')
@login_required
def dashboard():
   return render_template('user-dashboard/dashboard.html')
