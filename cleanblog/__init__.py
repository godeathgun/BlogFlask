from cassandra.cluster import Cluster
from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b75be7a62b04856194475b9c39f61e60'
cluster = Cluster()
db = cluster.connect('cleanblog')
login_manager = LoginManager(app)

from cleanblog import route