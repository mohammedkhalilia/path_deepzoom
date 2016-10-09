from flask import make_response, render_template
from flask_restful import Resource
from openslide import OpenSlide
import os

class Viewer(Resource):
	def __init__(self):
		pass

	def get(self, path):
		"""Get path
		Fetch a static HTML/JS/CSS files
		Args:
			path: path to static ID
		Returns:
			static file
		"""

		osr = OpenSlide("/" + path)
		
		data = {
			"filename": path,
			"width": osr.dimensions[0],
			"height": osr.dimensions[1],
			"tileWidth": 256,
			"tileHeight": 256,
			"levels": 10
		}

		headers = {'Content-Type': 'text/html'}

		return make_response(render_template("viewer.html", data=data), 200, headers)