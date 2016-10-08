import os
from flask_restful import Resource
from flask import Response
from utils.cache import cache
from utils.deepzoom import get_slide

class DeepZoom(Resource):
	def __init__(self, config):
		"""initialize DeepZoom resource

		Args:
			db: mongo db connection
			config: application configurations
			opt: deep zoom configurations

		Returns:
			None
		"""
		self.config = config

	@cache.cached()	
	def get(self, path):
		"""
        Get deep zoom image
        ---
        tags:
          - Deep Zoom
        parameters:
          - in: path
            name: path
            description: Example ADRC/DG_ADRC_Slides/ADRC59-164/aBeta/ADRC59-164_1A_AB.ndpi
            type: string
        responses:
          200:
            description: Returns the slide information
          404:
          	description: Invalid slide Id or slide not found
        """

		path = os.path.join(self.config["slides_dir"], path)
		slide = get_slide(path)

		if slide == None:
			Response("", status=404, mimetype='application/xml')
		else:
			return Response(slide.get_dzi(self.config['deepzoom_format']), status=200, mimetype='application/xml')
	
