import logging

from rocketchat.calls.base import RocketChatBase, PostMixin, logger
import sys
if sys.version_info[0] == 2:
    import urllib
else:
    import urllib.request as urllib
logger.setLevel(logging.DEBUG)


class UploadRemoteFile(PostMixin, RocketChatBase):
    endpoint = '/api/v1/rooms.upload'

    def build_endpoint(self, **kwargs):
        return '{endpoint}/{room_id}'.format(endpoint=self.endpoint,
                                             room_id=kwargs.get('room_id'))

    def build_files(self, **kwargs):
        return {'file': (kwargs.get('filename'),
                         urllib.urlopen(kwargs.get('url')),
                         kwargs.get('mime_type'))}

    def build_payload(self, **kwargs):
        return {'description': kwargs.get('description'), 'msg': kwargs.get('message')}

    def post_response(self, result):
        return result
