import logging

from rocketchat.calls.base import PostMixin, RocketChatBase

logger = logging.getLogger(__name__)


class CreatePublicRoom(PostMixin, RocketChatBase):
    endpoint = '/api/v1/channels.create'

    def build_endpoint(self, **kwargs):
        return self.endpoint

    def build_payload(self, **kwargs):
        return {
                'name': kwargs.get('name'),
                'members': kwargs.get('members', []),
                'readOnly': kwargs.get('read_only', False)
        }

    def post_response(self, result):
        return result
