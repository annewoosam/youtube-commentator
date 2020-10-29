from flask_sqlalchemy import SQLAlchemy

import datetime

db = SQLAlchemy()

# test = Comment(channel_name='WinningCheckers', email_date='2020-01-31',number_subscribers = '1', month_end_at='2019-12-31', subscribers='0', views='1', minutes_watched='2', likes='3', comments='4', posts='5', shares='6')

class Comment(db.Model):
    """A class for Comment."""
    
    __tablename__ = 'comments'

    channel_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    channel_name = db.Column(db.String)

    video_number = db.Column(db.Integer)

    commentator = db.Column(db.String)

    commentary = db.Column(db.String)

    date = db.Column(db.Date)
    
    replied_to = db.Column(db.Boolean)

    def __repr__(self):
        return f'<Comment channel_id={self.channel_id} channel_name={self.channel_name}>'

def connect_to_db(flask_app, db_uri='postgresql:///youtube_comments', echo=True):
   
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
   
    flask_app.config['SQLALCHEMY_ECHO'] = echo
   
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':

    from server import app

    connect_to_db(app)