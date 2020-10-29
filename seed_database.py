"""Script to seed database."""

import os

import json

from datetime import datetime

import crud

import model

import server


os.system('dropdb youtube_comments')

os.system('createdb youtube_comments')

model.connect_to_db(server.app)

model.db.create_all()


# Create comment table's initial data.

with open('data/comment.json') as f:

    comment_data = json.loads(f.read())

comment_in_db = []

for comment in comment_data:
    columnNamesSeparatedbyCommasUntilLastOne= (
                                   comment['channel_name'],
                                   comment['video_number'],
                                   comment['commentator'],
                                   comment['commentary'],
                                   comment['date'],                                                                                                       
                                   comment['replied_to'])

    db_comment = crud.create_comment(
                                 channel_name,
                                 video-number,
                                 commentator,
                                 commentary,
                                 date,                                                                                                                              
                                 replied_to)

    comment_in_db.append(db_comment)
