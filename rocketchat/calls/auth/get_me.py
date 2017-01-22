import logging

from rocketchat.calls.base import RocketChatBase

logger = logging.getLogger(__name__)


class GetMe(RocketChatBase):
    endpoint = '/api/v1/me'

    def build_endpoint(self, **kwargs):
        return self.endpoint

    def post_response(self, result):
        return result
