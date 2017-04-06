#!/usr/bin/python
"""
Add docstring here
"""
from flask_restful_swagger_2 import Resource, swagger

from qube.src.api.swagger_models.friday_demo import VersionModel
from qube.src.api.swagger_models.response_messages import \
    ErrorModel, response_msgs
from qube.src.commons.log import Log as LOG
from qube.src.commons.qube_config import QubeConfig

EMPTY = ''


class friday_demoItemVersionController(Resource):
    def __init__(self, *args, **kwargs):
        super(friday_demoItemVersionController, self).__init__(*args, **kwargs)
        self.config = QubeConfig.get_config()

    @swagger.doc(
        {
            'tags': ['friday_demo'],
            'description': 'friday_demo Version operation',
            'responses': response_msgs
        }
    )
    def get(self):
        """gets an friday_demo item that omar has changed
        """
        try:
            LOG.debug("Get version ")
            return VersionModel(**{'version': self.config.get_version()}), 200
        except Exception as ex:
            LOG.error(ex)
            return ErrorModel(**{'message': ex}), 500
