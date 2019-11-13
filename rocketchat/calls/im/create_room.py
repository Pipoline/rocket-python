import json
import logging

from rocketchat.calls.base import PostMixin, RocketChatBase

logger = logging.getLogger(__name__)


class CreateImRoom(PostMixin, RocketChatBase):
    endpoint = "/api/v1/im.create"

    def build_endpoint(self, **kwargs):
        return self.endpoint

    def build_payload(self, **kwargs):
        return json.dumps({"username": kwargs.get("username")})

    def post_response(self, result):
        try:
            _room = result.get('room')
            room_dict = dict()
            room_dict['id'] = _room.get('_id')

            for username in _room.get("usernames"):
                if username != self.settings["username"]:
                    room_dict['username'] = username
                    break

        except Exception as e:
            logger.error('Exception in creating im rooms {e}'.format(
                e=e
            ), exc_info=True)

        return room_dict
