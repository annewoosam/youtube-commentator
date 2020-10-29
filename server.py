"""Server for youtube_comments app."""

# increased flask

from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# created import allowing connection to database

from model import connect_to_db, Comment, db

app = Flask(__name__)

# imported Jinja secret key settings
from jinja2 import StrictUndefined

app.secret_key = "dev"

app.jinja_env.undefined = StrictUndefined

import crud

@app.route('/')

def all_comments():

    stats=crud.get_comments()
    
    channel_id=[q[0] for q in db.session.query(Comments.channel_id).all()]

    channel_name=[q[0] for q in db.session.query(Comments.channel_name).all()]

    video_number=[q[0] for q in db.session.query(Comments.video_number).all()]

    commentator=[q[0] for q in db.session.query(Comments.commentator).all()]

    commentary=[q[0] for q in db.session.query(Comments.commentary).all()]

    date=[q[0] for q in db.session.query(Comments.date).all()]
      
    replied_to=[q[0] for q in db.session.query(Comments.replied_to).all()]
    
    return render_template('comments.html', channel_id=channel_id, channel_name=channel_name, video_number=video_number, commentator=commentator, commentary=commentary, date=date, replied-to=replied_to)

if __name__ == '__main__':

# added connection to database

    connect_to_db(app)

# during development

    app.run(host='0.0.0.0', debug=True)

# in production

    #app.run()