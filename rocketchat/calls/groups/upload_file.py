import logging

from rocketchat.calls.base import RocketChatBase, PostMixin, logger
logger.setLevel(logging.DEBUG)


class UploadFile(PostMixin, RocketChatBase):
    endpoint = '/api/v1/rooms.upload'

    def build_endpoint(self, **kwargs):
        return '{endpoint}/{room_id}'.format(endpoint=self.endpoint,
                                             room_id=kwargs.get('room_id'))

    def build_files(self, **kwargs):
        return {'file': (kwargs.get('file'),
                         open(kwargs.get('file'), 'rb'),
                         kwargs.get('mime_type'))}

    def build_payload(self, **kwargs):
        return {'description': kwargs.get('description'), 'msg': kwargs.get('message')}

    def post_response(self, result):
        return result
