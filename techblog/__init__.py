import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)

#############################################################################
############ CONFIGURATIONS  ###############################################
###########################################################################


app.config['SECRET_KEY'] = 'mysecret'

#################################
### DATABASE SETUPS ############
###############################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app,db)


###########################
#### LOGIN CONFIGS #######
#########################

login_manager = LoginManager()

# We can now pass in our app to the login manager
login_manager.init_app(app)

# Tell users what view to go to when they need to login.
login_manager.login_view = "users.login"


###########################
#### BLUEPRINT CONFIGS #######
#########################

# Import these at the top if you want
# We've imported them here for easy reference
from techblog.core.views import core
from techblog.users.views import users
from techblog.blog_posts.views import blog_posts
from techblog.error_pages.handlers import error_pages

# Register the apps
app.register_blueprint(users)
app.register_blueprint(blog_posts)
app.register_blueprint(core)
app.register_blueprint(error_pages)
