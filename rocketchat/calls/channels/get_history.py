import logging

from rocketchat.calls.base import RocketChatBase

logger = logging.getLogger(__name__)


class GetRoomHistory(RocketChatBase):
    endpoint = '/api/v1/channels.history'

    '''def build_endpoint(self, **kwargs):
        if 'oldest' in kwargs:
            return '{endpoint}?roomId={room_id}&oldest={oldest}'.format(
                endpoint=self.endpoint,
                oldest=kwargs.get('oldest'),
                room_id=kwargs.get('room_id')
            )
        else:
            return '{endpoint}?roomId={room_id}'.format(
                endpoint=self.endpoint,
                room_id=kwargs.get('room_id')
            )'''
    def build_endpoint (self, **kwargs):
        for x in kwargs:
            print("{} ist: {}".format(x,kwargs.get(x)))
        print('{endpoint}?roomId={room_id}&oldest={oldest}&latest={latest}&inclusive={inclusive}&count={count}&unreads={unreads}'.format(
                endpoint=self.endpoint,
                oldest=kwargs.get('oldest'),
                room_id=kwargs.get('room_id'),
                latest=kwargs.get('latest'),
                inclusive=str(kwargs.get('inclusive')).lower(),
                count=kwargs.get('count'),
                unreads=str(kwargs.get('unreads')).lower()
                ))
        #latest=None,inclusive=None, count=None,unreads=None,
        return '{endpoint}?roomId={room_id}&oldest={oldest}&inclusive={inclusive}&count={count}&unreads={unreads}&latest={latest}'.format(
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
