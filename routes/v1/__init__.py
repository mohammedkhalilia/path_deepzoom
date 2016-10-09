from flask_restful import Api
from flask_swagger import swagger
from flask_restful.utils import cors
from flask import Blueprint, current_app, jsonify
from DeepZoom import DeepZoom
from Tile import Tile
from Viewer import Viewer
from utils.config import get_app_configurations

# Get app configurations
config = get_app_configurations()

# Prepare arguments to pass to the resources
params = {'config': config}

# Create a blueprint for API v1
# It is prefixed with /v1
# Add CORS decorator for all endpoints
v1 = Blueprint('v1', __name__)
api = Api(v1, prefix="/v1")

@v1.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin','*')
    response.headers.add('Access-Control-Allow-Headers', "Authorization, Content-Type")
    response.headers.add('Access-Control-Expose-Headers', "Authorization")
    response.headers.add('Access-Control-Allow-Methods', "GET, POST, PUT, DELETE, OPTIONS")
    response.headers.add('Access-Control-Allow-Credentials', "true")
    response.headers.add('Access-Control-Max-Age', 60 * 60 * 24 * 20)
    return response

@v1.route("/v1/docs")
def spec():
    swag = swagger(current_app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Digital Slide Archive Deep Zoom API"
    swag['info']['base_path'] = "http://digitalslidearchive.emory.edu:8003"
    return jsonify(swag)

# Attach all endpoints to the v1 API
api.add_resource(
		DeepZoom,
		"/<path:path>", 
		resource_class_kwargs=params)

api.add_resource(
		Tile,
		"/<path:path>/<int:level>/<int:x>/<int:y>", 
		resource_class_kwargs=params)

api.add_resource(
        Viewer,
        "/view/<path:path>")
