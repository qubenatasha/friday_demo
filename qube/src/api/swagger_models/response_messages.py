from flask_restful_swagger_2 import Schema

from qube.src.api.swagger_models.friday_demo import friday_demoErrorModel
from qube.src.api.swagger_models.friday_demo import friday_demoModel
from qube.src.api.swagger_models.friday_demo import friday_demoModelPostResponse

"""
the common response messages printed in swagger UI
"""

post_response_msgs = {
    '201': {
        'description': 'CREATED',
        'schema': friday_demoModelPostResponse
    },
    '401': {
        'description': 'Unauthorized'
    },
    '400': {
        'description': 'Bad Request'
    },
    '404': {
        'description': 'Not found'
    },
    '500': {
        'description': 'Internal server error',
        'schema': friday_demoErrorModel
    }
}

get_response_msgs = {
    '200': {
        'description': 'OK',
        'schema': friday_demoModel
    },
    '401': {
        'description': 'Unauthorized'
    },
    '400': {
        'description': 'Bad Request'
    },
    '404': {
        'description': 'Not found'
    },
    '500': {
        'description': 'Internal server error',
        'schema': friday_demoErrorModel
    }
}

put_response_msgs = {
    '204': {
        'description': 'No Content'
    },
    '401': {
        'description': 'Unauthorized'
    },
    '400': {
        'description': 'Bad Request'
    },
    '404': {
        'description': 'Not found'
    },
    '500': {
        'description': 'Internal server error',
        'schema': friday_demoErrorModel
    }
}

del_response_msgs = {
    '204': {
        'description': 'No Content'
    },
    '401': {
        'description': 'Unauthorized'
    },
    '400': {
        'description': 'Bad Request'
    },
    '404': {
        'description': 'Not found'
    },
    '500': {
        'description': 'Internal server error',
        'schema': friday_demoErrorModel
    }
}

response_msgs = {
    '200': {
        'description': 'OK'
    },
    '401': {
        'description': 'Unauthorized'
    },
    '400': {
        'description': 'Bad Request'
    },
    '404': {
        'description': 'Not found'
    },
    '500': {
        'description': 'Internal server error'
    }
}


class ErrorModel(Schema):
    type = 'object'
    properties = {
        'error_code': {
            'type': 'string'
        },
        'error_message': {
            'type': 'string'
        }
    }
