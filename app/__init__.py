from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

# setup app variables
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(Config)


# when a page requires somebody to logged in the application will by default
# send them back to the previous page. However, we will make them go back to
# the login instead
login.login_view = 'login'

# go to routes
from app import routes
