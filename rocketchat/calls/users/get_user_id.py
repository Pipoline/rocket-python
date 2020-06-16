import logging

from rocketchat.calls.base import RocketChatBase

logger = logging.getLogger(__name__)


class GetUserId(RocketChatBase):
    endpoint = '/api/v1/users.info'

    def build_endpoint(self, **kwargs):
        return '{endpoint}?roomName={user_name}'.format(
            endpoint=self.endpoint,
            user_name=kwargs.get('user_name')
        )

    def post_response(self, result):
        return result['user']['_id']
