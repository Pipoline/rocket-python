import logging

from rocketchat.calls.base import RocketChatBase

logger = logging.getLogger(__name__)


class GetRoomHistory(RocketChatBase):
    endpoint = '/api/v1/channels.history'

    def build_endpoint(self, **kwargs):
        return '{endpoint}?roomId={room_id}&oldest={oldest}&inclusive={inclusive}'\
                '&count={count}&unreads={unreads}&latest={latest}'.format(
                 endpoint=self.endpoint,
                 oldest=kwargs.get('oldest'),
                 room_id=kwargs.get('room_id'),
                 inclusive=kwargs.get('inclusive'),
                 count=kwargs.get('count'),
                 unreads=kwargs.get('unreads'),
                 latest=kwargs.get('latest')
                )

    def post_response(self, result):
        return result
