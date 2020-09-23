import logging

from rocketchat.calls.base import RocketChatBase, PostMixin

logger = logging.getLogger(__name__)


class Logout(PostMixin, RocketChatBase):
    endpoint = '/api/v1/logout'

    def build_endpoint(self, **kwargs):
        return self.endpoint
