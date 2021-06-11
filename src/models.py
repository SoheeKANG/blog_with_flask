from dataclasses import dataclass
from sqlalchemy import Column, Integer, Text, TIMESTAMP


@dataclass
class Comment:
    post_num = Column(Integer)
    comment_body = Column(Text)
    comment_time = Column(TIMESTAMP)


@dataclass
class Post:
    post_number = Column(Integer, primary_key=True, autoincrement=True)
    post_title = Column(Text, nullable=False)
    post_body = Column(Text, nullable=False)
    post_time = Column(TIMESTAMP)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email
