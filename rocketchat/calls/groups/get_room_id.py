import logging

from rocketchat.calls.base import RocketChatBase

logger = logging.getLogger(__name__)


class GetRoomId(RocketChatBase):
    endpoint = '/api/v1/groups.info'

    def build_endpoint(self, **kwargs):

        return '{endpoint}?roomName={room_name}'.format(
            endpoint=self.endpoint,
            room_name=kwargs.get('room_name')
        )

    def post_response(self, result):
        # print(result['group']['_id'])
        return result['group']['_id']
