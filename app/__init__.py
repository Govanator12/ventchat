import pusher
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

# setup app variables
app = Flask(__name__)

pusher_client = pusher.Pusher(
  app_id='785700',
  key='4f77cd0c59b6dd888f56',
  secret='7a6333d7c3dbce5f117c',
  cluster='us2',
  ssl=True
)

bootstrap = Bootstrap(app)
app.config.from_object(Config)

# go to routes
from app import routes
