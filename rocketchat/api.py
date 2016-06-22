from rocketchat.calls.send_message import SendMessage


class RocketChatAPI(object):


    def send_message(self, message, room, **kwargs):
        return SendMessage().call()

    def create_channel():
        pass

    def get_public_rooms():
        pass
