import logging

from rocketchat.calls.base import RocketChatBase

logger = logging.getLogger(__name__)


class GetPublicRooms(RocketChatBase):
    endpoint = '/api/v1/channels.list'

    def build_endpoint(self):
        return self.endpoint

    def post_response(self, result):
        rooms = []

        try:
            _rooms = result.get('channels')

            for room in _rooms:
                room_dict = {}
                room_dict['name'] = room.get('name')
                room_dict['id'] = room.get('_id')
                rooms.append(room_dict)

        except Exception as e:
            logger.error('Exception in fetching public rooms {e}'.format(
                e=e
            ), exc_info=True)

        return rooms
