from flask import Blueprint, current_app, redirect, render_template, url_for
from flask import request,make_response
from .models import User
import bcrypt
from datetime import datetime
from flask import Flask, render_template, url_for, redirect, session, flash, request, jsonify, json

views_bp = Blueprint('views',__name__)

app = current_app
utc_dt_aware = datetime.datetime.now(datetime.timezone.utc)

@app.route('/register', methods=['GET','POST'])
def register():
    content  = request.get_json(silent=True)
    if request.method=='POST':
        res=''
        username=content['email']
        password=content['password']
        confirm=content['confirm']
        isAdmin=content['isAdmin']
        loginType=content['loginType']
        secure_password = bcrypt.generate_password_hash(str(password)) 
        db=User.db
        usernamedata=db.execute('SELECT username FROM users WHERE username=:username',{'username':username}).fetchone()
        
        SignupDate=datetime.utcnow
        LastActive=datetime.utcnow
        #usernamedata=str(usernamedata)
        if usernamedata==None:
            if password==confirm:
                db.execute('INSERT INTO users(username,password,isAdmin) VALUES(:username,:password,:isAdmin)',{'username':username,'password':secure_password,'isAdmin':isAdmin})
                db.execute('INSERT INTO UserProfile(SignupDate, LastActive) VALUES(:SignupDate, :LastActive)',{'SignupDate' :SignupDate,'LastActive':LastActive})
                db.commit()
                res=json.dumps('You are registered and can now login','success')
                #return redirect(url_for('login'))
                mess_out = 'success'
            else:
                res=json.dumps('password does not match','danger')
                #return render_template('register.html')
                mess_out = 'fail'
        else:
            res=json.dumps('user already existed, please login or contact admin','danger')
            #return redirect(url_for('login'))
            mess_out = 'fail'
    
    return jsonify(message=mess_out, data=res)        
    #return render_template('register.html')