import logging

from rocketchat.calls.base import PostMixin, RocketChatBase

logger = logging.getLogger(__name__)


class SetRoomTopic(PostMixin, RocketChatBase):
    endpoint = '/api/v1/groups.setTopic'

    def build_endpoint(self, **kwargs):
        return self.endpoint

    def build_payload(self, **kwargs):
        return {
            'topic': kwargs.get('topic'),
            'roomId': kwargs.get('room_id')
        }

    def post_response(self, result):
        return result['success']
