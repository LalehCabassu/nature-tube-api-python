from .video import VideoSchema
from marshmallow import Schema, fields, post_load

class Collection(object):
    def __init__(self, id: int, title: str, videos):
        self.id = id
        self.title = title
        self.videos = videos

    def __repr__(self) -> str:
        return '<Collection(title={title!r})>'.format(title=self.title)

class CollectionSchema(Schema):
    id = fields.Str()
    title = fields.Str()
    videos = fields.List(fields.Nested(VideoSchema))

    @post_load
    def make_colletcion(self, data, **kwargs):
        return Collection(**data)
