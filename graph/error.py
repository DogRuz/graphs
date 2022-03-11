from rest_framework.exceptions import APIException


class GraphNotFound(APIException):
    status_code = 404
    default_detail = 'Graph not found, please try again later'
    default_code = 'graph_not_found'


class VectorsNotFound(APIException):
    status_code = 404
    default_detail = 'Vector not found, please try again later'
    default_code = 'vector_not_found'
