import logging


from rocketchat.calls.base import RocketChatBase

logger = logging.getLogger(__name__)


class GetUserInfo(RocketChatBase):
    endpoint = '/api/v1/users.info'

    def build_endpoint(self, **kwargs):
        return '{endpoint}?userId={room_id}'.format(
            endpoint=self.endpoint,
            room_id=kwargs.get('user_id')
        )

    def post_response(self, result):
        return result
