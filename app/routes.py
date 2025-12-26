from flask import Blueprint, jsonify

bp = Blueprint("main", __name__)

@bp.get("/")
def hello():
    return jsonify(message="Hello, World!")
