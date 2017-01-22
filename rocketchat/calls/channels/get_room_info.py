import logging

from rocketchat.calls.base import RocketChatBase

logger = logging.getLogger(__name__)


class GetRoomInfo(RocketChatBase):
    endpoint = '/api/v1/channels.info'

    def build_endpoint(self, **kwargs):
        return '{endpoint}?roomId={room_id}'.format(
            endpoint=self.endpoint,
            room_id=kwargs.get('room_id')
        )

    def post_response(self, result):
        return result
