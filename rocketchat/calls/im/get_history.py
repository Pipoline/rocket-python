import logging

from rocketchat.calls.base import RocketChatBase

logger = logging.getLogger(__name__)


class GetImRoomHistory(RocketChatBase):
    endpoint = '/api/v1/im.history'

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
        messages = []

        try:
            _messages = result.get('messages')

            for msg in _messages:
                msg_dict = dict()
                msg_dict['msg'] = msg.get('msg')
                msg_dict['room_id'] = msg.get('rid')
                msg_dict['ts'] = msg.get('ts')
                msg_dict['user'] = {
                    'id': msg.get('u', {}).get('_id'),
                    'username': msg.get('u', {}).get('username'),
                }
                msg_dict['id'] = msg.get('_id')

                messages.append(msg_dict)

        except Exception as e:
            logger.error('Exception in fetching direct message rooms {e}'.format(
                e=e
            ), exc_info=True)

        return messages
