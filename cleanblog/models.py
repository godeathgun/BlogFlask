import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cleanblog import login_manager, db
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    users = db.execute("select * from User where id='" + user_id + "'")
    user_1 = User()
    for user in users:
        user_1 = user
    return user_1


class User(Model, UserMixin):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    username = columns.Text()
    email = columns.Text()
    password = columns.Text()

    def get_id(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password
        }


class Post(Model):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    title = columns.Text()
    subtitle = columns.Text()
    content = columns.Text()
    date_posted = columns.DateTime()

    def __repr__(self):
        return {
            'title': self.title,
            'subtitle': self.subtitle,
            'date_posted': self.date_posted
        }
