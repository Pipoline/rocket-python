from rocketchat.calls.send_message import SendMessage
from rocketchat.calls.get_public_rooms import GetPublicRooms


class RocketChatAPI(object):
    settings = None

    def __init__(self, settings=None, *args, **kwargs):
        if settings:
            self.settings = settings
        else:
            raise NotImplementedError('You must pass in settings for RocketChat')

    def send_message(self, message, room_id, **kwargs):
        """
        Send a message to a given room
        """
        return SendMessage(settings=self.settings, **kwargs).call(
            message=message,
            room_id=room_id,
            **kwargs
        )

    def get_public_rooms(self, **kwargs):
        """
        Get a listing of all public rooms with their names and IDs
        """
        return GetPublicRooms(settings=self.settings, **kwargs).call(**kwargs)
