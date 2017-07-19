import logging

from flask import request
import flask_restful
from six.moves import http_client

from column.api import manager

LOG = logging.getLogger(__name__)


class Credential(flask_restful.Resource):
    """Column api credential resource class

    Attributes:
         manager (obj): manager interface for calling column library method to
                        get/update the credential
    """

    def __init__(self):
        self.manager = manager.get_manager('credential')

    def get(self):
        """Get a credential by file path"""
        cred_payload = request.get_json(silent=True)
        cred = self.manager.get_credential(cred_payload)
        return cred

    def put(self):
        """Update a credential by file path"""
        cred_payload = request.get_json(silent=True)
        cred = self.manager.update_credential(cred_payload)
        return '', http_client.NO_CONTENT
