import json
from flask import Blueprint, jsonify, request
from models.entitites.Publication import Publication
import uuid

# models
from models.PublicationModel import PublicationModel

main = Blueprint('publication_blueprint', __name__)

@main.route('/')
def get_publications():
    try:
        publications = PublicationModel.get_publications()
        return jsonify(publications)

    except Exception as ex:
        return jsonify({'Message':str(ex)}), 500

@main.route('/<id>')
def get_publication(id):
    try:
        publication = PublicationModel.get_publication(id)
        if publication:
            return jsonify(publication)
        else:
            return jsonify({}), 404

    except Exception as ex:
        return jsonify({'Message':str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_publication():
    try: # falta validar los datos

        id = uuid.uuid4()
        title = request.json['title']
        description = request.json['description']
        priority = int(request.json['priority'])
        stat = request.json['stat']
        usr = request.json['usr']

        publication = Publication(str(id), title, description, priority, stat, usr)
        affected_rows = PublicationModel.add_publication(publication)

        if affected_rows == 1:
            return jsonify(publication.id)
        else:
            return jsonify({'Message': 'Error on insert'}), 500

    except Exception as ex:
        print(ex)
        return jsonify({'Message':str(ex)}), 500

@main.route('/update/<id>', methods=['PUT'])
def update_publication(id):
    try:
        title = request.json['title']
        description = request.json['description']
        priority = int(request.json['priority'])
        stat = request.json['stat']
        usr = request.json['usr']

        publication = Publication(id, title, description, priority, stat, usr)
        affected_rows = PublicationModel.update_publication(publication)

        if affected_rows == 1:
            return jsonify(publication.id)
        else:
            return jsonify({'Message': 'No publication updated'}), 404

    except Exception as ex:
        print(ex)
        return jsonify({'Message':str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_publication(id):
    try:
        publication = Publication(id)
        affected_rows = PublicationModel.delete_publication(publication)

        if affected_rows == 1:
            return jsonify(publication.id)
        else:
            return jsonify({'Message': 'Publication not found'}), 404
    
    except Exception as ex:
        print(ex)
        return jsonify({'Message':str(ex)}), 500

# dff31161-e821-4ed2-abc9-19dee0a08b86