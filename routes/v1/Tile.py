import os
import cStringIO
from openslide import OpenSlideError
from flask_restful import Resource
from flask import Response
from utils.deepzoom import get_slide, PILBytesIO
from bson.json_util import dumps

class Tile(Resource):
	def __init__(self, config):
		"""initialize DeepZoom resource
		Args:
			config: application configurations
		Returns:
			None
		"""
		self.config = config

	def get(self, path, level, x, y):
		"""
        Get slide tile
        ---
        tags:
          - Tile
        parameters:
          - in: path
            name: path
            description: Example SLIDES/ADRC/DG_ADRC_Slides/ADRC59-164/aBeta/ADRC59-164_1A_AB.ndpi
            type: string
          - in: path
            name: level
            description: The zoom level
            type: integer
          - in: path
            name: x
            description: The column
            type: integer
          - in: path
            name: y
            description: The row
            type: integer
        responses:
          200:
            description: Returns the tile
          404:
          	description: Invalid path or openslide error
		"""

		path = "/" + path

		if not os.path.exists(path):
			resp = {"status": 404, "message": "Path not found: " + path}
			return Response(dumps(resp), status=404, mimetype='application/json')

		slide = get_slide(path)
		
		try:
			tile = slide.get_tile(level, (x, y))
			buf = cStringIO.StringIO() 
			tile.save(buf, format='jpeg', quality=90)
			return Response(buf.getvalue(), status=200, mimetype='image/jpeg')
		except OpenSlideError, e:
			resp = {"status": 404, "message": "OpenSlideError: " + str(e)}
			return Response(dumps(resp), status=404, mimetype='application/json')
		except ValueError, e:
			resp = {"status": 404, "message": "VaueError: " + str(e)}
			return Response(dumps(resp), status=404, mimetype='application/json')
