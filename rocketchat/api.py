from rocketchat.calls.send_message import SendMessage


class RocketChatAPI(object):
    settings = None

    def __init__(self, settings=None, *args, **kwargs):
        if settings:
            self.settings = settings
        else:
            raise NotImplementedError('You must pass in settings for RocketChat')

    def send_message(self, message, room_id, **kwargs):
        return SendMessage(settings=self.settings, **kwargs).call(
            message=message,
            room_id=room_id,
            **kwargs
        )