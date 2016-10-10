from flask import Response, make_response, render_template
from flask_restful import Resource
from openslide import OpenSlide
from bson.json_util import dumps
import os

class Viewer(Resource):
	def __init__(self):
		pass

	def get(self, path):
		"""
        Get deep zoom image
        ---
        tags:
          - View
        parameters:
          - in: path
            name: path
            description: Example SLIDES/ADRC/DG_ADRC_Slides/ADRC59-164/aBeta/ADRC59-164_1A_AB.ndpi
            type: string
            required: true
            default: ""
        responses:
          200:
            description: Renders OpenSeadraon viewer
          404:
          	description: Invalid path or openslide error
        """

		if not os.path.exists("/" + path):
			resp = {"status": 404, "message": "Path not found: /" + path}
			return Response(dumps(resp), status=404, mimetype='application/json')

		osr = OpenSlide("/" + path)
		
		data = {
			"filename": path,
			"width": osr.dimensions[0],
			"height": osr.dimensions[1],
			"tileWidth": 256,
			"tileHeight": 256,
			"levels": osr.level_count
		}

		headers = {'Content-Type': 'text/html'}

		return make_response(render_template("viewer.html", data=data), 200, headers)
