from flask import Blueprint, request, jsonify
from function_jwt import write_token

routes_auth = Blueprint("routes_auth", __name__)

@routes_auth.route("/login", methods=["POST"])
def login():
    data = request.json["username"]
    if data == "Augusto Carmona":
        return write_token(data=request.get_json())
    else:
        response = jsonify({"Message":"User not found"})
        response.status_code = 404
        return response