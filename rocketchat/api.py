from rocketchat.calls.chat.send_message import SendMessage
from rocketchat.calls.channels.get_public_rooms import GetPublicRooms
from rocketchat.calls.groups.get_private_rooms import GetPrivateRooms
from rocketchat.calls.channels.get_room_info import GetRoomInfo
from rocketchat.calls.groups.get_private_room_info import GetPrivateRoomInfo
from rocketchat.calls.channels.get_history import GetRoomHistory
from rocketchat.calls.groups.get_private_room_history import GetPrivateRoomHistory
from rocketchat.calls.auth.get_me import GetMe
from datetime import datetime


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

    def get_private_rooms(self, **kwargs):
        """
        Get a listing of all private rooms with their names and IDs
        """
        return GetPrivateRooms(settings=self.settings, **kwargs).call(**kwargs)

    def get_private_room_history(self, room_id, oldest=None, **kwargs):
        """
        Get various history of specific private group in this case private

        :param room_id:
        :param kwargs:
        :return:
        """
        return GetPrivateRoomHistory(settings=self.settings, **kwargs).call(
            room_id=room_id,
            oldest=oldest,
            **kwargs
        )

    def get_public_rooms(self, **kwargs):
        """
        Get a listing of all public rooms with their names and IDs
        """
        return GetPublicRooms(settings=self.settings, **kwargs).call(**kwargs)

    def get_room_info(self, room_id, **kwargs):
        """
        Get various information about a specific channel/room

        :param room_id:
        :param kwargs:
        :return:
        """
        return GetRoomInfo(settings=self.settings, **kwargs).call(
            room_id=room_id,
            **kwargs
        )

    def get_private_room_info(self, room_id, **kwargs):
        """
        Get various information about a specific private group

        :param room_id:
        :param kwargs:
        :return:
        """
        return GetPrivateRoomInfo(settings=self.settings, **kwargs).call(
            room_id=room_id,
            **kwargs
        )

    def get_room_history(
                         self,
                         room_id,
                         oldest=None,
                         latest=datetime.now(),
                         inclusive=False,
                         count=20,
                         unreads=False,
                         **kwargs
                        ):
        """
        Get various history of specific channel/room

        :param room_id:
        :param kwargs:
        :return:
        """
        return GetRoomHistory(settings=self.settings, **kwargs).call(
            room_id=room_id,
            oldest=oldest,
            latest=latest,
            inclusive=inclusive,
            count=count,
            unreads=unreads,
            **kwargs
        )

    def get_my_info(self, **kwargs):

        return GetMe(settings=self.settings, **kwargs).call(**kwargs)
