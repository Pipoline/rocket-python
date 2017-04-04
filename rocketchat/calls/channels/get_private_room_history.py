import logging

from rocketchat.calls.base import RocketChatBase

logger = logging.getLogger(__name__)


class GetPrivateRoomHistory(RocketChatBase):
    endpoint = '/api/v1/groups.history'

    def build_endpoint(self, **kwargs):
        if 'oldest' in kwargs:
            return '{endpoint}?roomId={room_id}&oldest={oldest}'.format(
                endpoint=self.endpoint,
                oldest=kwargs.get('oldest'),
                room_id=kwargs.get('room_id')
            )
        else:
            return '{endpoint}?roomId={room_id}'.format(
                endpoint=self.endpoint,
                room_id=kwargs.get('room_id')
            )

    def post_response(self, result):
        return result
