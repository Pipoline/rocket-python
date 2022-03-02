import logging

from rocketchat.calls.base import PostMixin, RocketChatBase

logger = logging.getLogger(__name__)


class DeleteUser(PostMixin, RocketChatBase):
    endpoint = '/api/v1/users.delete'

    def build_endpoint(self, **kwargs):
        return self.endpoint

    def build_payload(self, **kwargs):
        return {
            'userId': kwargs.get('user_id')
        }

    def post_response(self, result):
        return result
