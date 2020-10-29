"""CRUD operations."""

from model import db, Comment, connect_to_db

import datetime


def create_comment(channel_name, video_number, commentator, commentary, date, replied_to):
   

    comment = Comment(channel_name=channel_name,
                  video_number=video_number,
                  commentator=commentator,
                  commentary=commentary,
                  date=date,
                  replied_to=replied_to)

    db.session.add(comment)

    db.session.commit()

    return comment

def get_comments():
    """Return all rows of comment data."""

    return Comment.query.all()
 
if __name__ == '__main__':
    from server import app
    connect_to_db(app)
