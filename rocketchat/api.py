from rocketchat.calls.send_message import SendMessage


class RocketChatAPI(object):
    settings = None

    def __init__(self, settings=None, *args, **kwargs):
        if settings:
            self.settings = settings
        else:
            raise NotImplementedError('You must set ROCKETCHAT_API_SETTINGS')

    def send_message(self, message, room, **kwargs):
        return SendMessage().call()

    def create_channel(self):
        pass

    def get_public_rooms(self):
        pass
