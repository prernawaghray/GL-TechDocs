from flask import render_template, request, url_for,session 
from flask import make_response, redirect, abort
from app import app, oauth
from flask import jsonify



'''Login Authorization Wrapper'''
#def login_required(function): 
#    def wrapper(*args, **kwargs):
#        return function(*args, **kwargs) if session.get('user') else abort(401)
#    return wrapper


def login_required(f):
    
   def wrap(*args, **kwargs):
      if  session.get('user') :
         return f(*args, **kwargs)
      else:
         return redirect(url_for('login'))
   wrap.__name__ = f.__name__
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



@app.route('/forgotpassword')
def forgot_password():
   return render_template('forgotpassword/forgotpassword.html')

@app.route('/password_reset')
def reset_password():
   return render_template('forgotpassword/resetpassword.html')

@app.route('/logout')
def logout():
   # session.clear()
   [session.pop(key) for key in list(session.keys())]
   return redirect('/')


@app.route('/dashboard')
# @login_required
def dashboard():
   return render_template('user-dashboard/dashboard.html')

@app.route('/latex-editor/new-document')
# @login_required
def latexEditor():
   return render_template('latex-editor/editor.html')

@app.route('/plans')
def plans():
   return render_template('plans-and-subscriptions/pricing.html')

@app.route('/payments')
def payments():
   return render_template('payments-page/payments-page.html')

@app.route('/profile')
@login_required
def profile():
   return render_template('profile/profile.html')

@app.route('/saveUserToken',methods=['POST'])
def saveToken():
   session['user'] = request.form['authToken']
   return  make_response({'status':True}, 200)

@app.route('/clearSession',methods=['POST'])
@login_required
def clearSession():
   [session.pop(key) for key in list(session.keys())]
   return  make_response({'status':True}, 200)
