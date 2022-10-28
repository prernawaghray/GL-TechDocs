from flask import Flask
#from flask_cors import CORS



def create_app():

    app = Flask(__name__)
    #CORS(app)

    app.config['SECRET_KEY'] = 'something secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Root1234@localhost/dreamhome'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    with app.app_context():

        #import blueprints
        from .models import models_bp
        from .views import views_bp

        #register blueprints
        app.register_blueprint(models_bp)
        app.register_blueprint(views_bp)

    return app