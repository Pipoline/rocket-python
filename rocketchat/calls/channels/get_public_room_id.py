import logging

from rocketchat.calls.base import RocketChatBase

logger = logging.getLogger(__name__)


class GetPublicRoomId(RocketChatBase):
    endpoint = '/api/v1/channels.info'

    def build_endpoint(self, **kwargs):
        return '{endpoint}?roomName={room_name}'.format(
            endpoint=self.endpoint,
            room_id=kwargs.get('room_name')
        )

    def post_response(self, result):
        return result['channel']['_id']
