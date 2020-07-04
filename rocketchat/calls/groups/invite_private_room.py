import logging
import json

from rocketchat.calls.base import PostMixin, RocketChatBase

logger = logging.getLogger(__name__)


class InvitePrivateRoom(PostMixin, RocketChatBase):
    endpoint = '/api/v1/groups.invite'

    def build_endpoint(self, **kwargs):
        return self.endpoint

    def build_payload(self, **kwargs):
        return json.dumps({
                'roomId': kwargs.get('room_id'),
                'userId': kwargs.get('user_id')
        })

    def post_response(self, result):
        return result
