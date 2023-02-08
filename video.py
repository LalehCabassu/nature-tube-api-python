from marshmallow import Schema, fields, post_load

class Video(object):
    def __init__(self, title: str, uri: str):
        self.title = title
        self.uri = uri

    def __repr__(self) -> str:
        return '<Video(title={self.title})>'

class VideoSchema(Schema):
    title = fields.Str()
    uri = fields.Str()

    @post_load
    def make_video(self, data, **kwargs):
        return Video(**data)
