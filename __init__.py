from flask import Flask, jsonify, request

from .video import Video, VideoSchema
from .collection import Collection, CollectionSchema

app = Flask(__name__)

collections = [
    Collection('1', 'first collection', [Video('title1', 'https://youtu.be/ud7gPra9CGU')]),
    Collection('2', 'second collection', [Video('title2', 'https://www.youtube.com/live/6uVUv8gZHBE?feature=share')])
]


@app.route('/collections')
def get_colletcions():
    schema = CollectionSchema(many=True)
    result = schema.dump(collections)
    return jsonify(result)

@app.route('/collection')
def get_collection_by_title():
    title = request.args.get('title')
    schema = CollectionSchema(many=True)
    result = schema.dump(
        filter(lambda c: title in c.title, collections)
    )
    return jsonify(result)

@app.route('/collection', methods=['POST'])
def add_colletcion():
    newCollection = request.get_json()
    collections.append(newCollection)
    return '', 204
