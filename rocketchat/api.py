from rocketchat.calls.chat.send_message import SendMessage
from rocketchat.calls.channels.get_public_rooms import GetPublicRooms
from rocketchat.calls.groups.get_private_rooms import GetPrivateRooms
from rocketchat.calls.channels.get_room_info import GetRoomInfo
from rocketchat.calls.groups.get_private_room_info import GetPrivateRoomInfo
from rocketchat.calls.groups.get_room_id import GetRoomId
from rocketchat.calls.groups.set_room_topic import SetRoomTopic
from rocketchat.calls.channels.get_history import GetRoomHistory
from rocketchat.calls.groups.get_private_room_history import GetPrivateRoomHistory
from rocketchat.calls.channels.create_public_room import CreatePublicRoom
from rocketchat.calls.channels.delete_public_room import DeletePublicRoom
from rocketchat.calls.auth.get_me import GetMe
from rocketchat.calls.auth.logout import Logout
from rocketchat.calls.users.get_users import GetUsers
from rocketchat.calls.users.get_user_info import GetUserInfo
from rocketchat.calls.users.create_user import CreateUser
from rocketchat.calls.users.delete_user import DeleteUser
from rocketchat.calls.groups.upload_file import UploadFile
from rocketchat.calls.im.create_room import CreateImRoom
from rocketchat.calls.im.open_room import OpenImRoom
from rocketchat.calls.im.close_room import CloseImRoom
from rocketchat.calls.im.get_rooms import GetImRooms
from rocketchat.calls.im.get_history import GetImRoomHistory
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

    def upload_file(self, room_id, description, file, message, mime_type='text/plain', **kwargs):
        """
        Upload file to room
        :param room_id:
        :param description:
        :param file:
        :param kwargs:
        :return:
        """
        return UploadFile(settings=self.settings, **kwargs).call(
            room_id=room_id,
            description=description,
            file=file,
            message=message,
            mime_type=mime_type,
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

    def get_room_id(self, room_name, **kwargs):
        """
        Get room ID
        :param room_name:
        :param kwargs:
        :return:
        """
        return GetRoomId(settings=self.settings, **kwargs).call(
            room_name=room_name,
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

    def create_public_room(self, name, **kwargs):
        """
        Create room with given name
        :param name: Room name
        :param kwargs:
        members: The users to add to the channel when it is created.
            Optional; Ex.: ["rocket.cat"], Default: []
        read_only: Set if the channel is read only or not.
            Optional; Ex.: True, Default: False
        :return:
        """
        return CreatePublicRoom(settings=self.settings, **kwargs).call(name=name, **kwargs)

    def delete_public_room(self, room_id, **kwargs):
        """
        Delete room with given ID
        :param room_id: Room ID
        :param kwargs:
        :return:
        """
        return DeletePublicRoom(settings=self.settings, **kwargs).call(room_id=room_id, **kwargs)

    def get_my_info(self, **kwargs):
        return GetMe(settings=self.settings, **kwargs).call(**kwargs)

    def get_users(self, **kwargs):
        """
        Gets all of the users in the system and their information
        :param kwargs:
        :return:
        """
        return GetUsers(settings=self.settings, **kwargs).call(**kwargs)

    def get_user_info(self, user_id, **kwargs):
        """
        Retrieves information about a user,
        the result is only limited to what the callee has access to view.
        :param user_id:
        :param kwargs:
        :return:
        """
        return GetUserInfo(settings=self.settings, **kwargs).call(
            user_id=user_id,
            **kwargs
        )

    def create_user(self, email, name, password, username, **kwargs):
        """
        Create user
        :param email: E-mail
        :param name: Full name
        :param password: Password
        :param username: Username
        :param kwargs:
        active:
        roles:
        join_default_channels:
        require_password_change:
        send_welcome_email:
        verified:
        custom_fields:
        :return:
        """
        return CreateUser(settings=self.settings, **kwargs).call(
            email=email,
            name=name,
            password=password,
            username=username,
            **kwargs
        )

    def delete_user(self, user_id, **kwargs):
        """
        Delete user
        :param user_id: User ID
        :param kwargs:
        :return:
        """
        return DeleteUser(settings=self.settings, **kwargs).call(user_id=user_id, **kwargs)

    def set_room_topic(self, room_id, topic, **kwargs):
        return SetRoomTopic(settings=self.settings, **kwargs).call(
            room_id=room_id,
            topic=topic,
            **kwargs
        )

    def create_im_room(self, username, **kwargs):
        """
        Create direct message room with user

        :param username:
        :return:
        """
        return CreateImRoom(settings=self.settings, **kwargs).call(
            username=username,
            **kwargs
        )

    def open_im_room(self, room_id, **kwargs):
        """
        Open direct message room

        :param room_id:
        :return:
        """
        return OpenImRoom(settings=self.settings, **kwargs).call(
            room_id=room_id,
            **kwargs
        )

    def close_im_room(self, room_id, **kwargs):
        """
        Close direct message room

        :param room_id:
        :return:
        """
        return CloseImRoom(settings=self.settings, **kwargs).call(
            room_id=room_id,
            **kwargs
        )

    def get_im_rooms(self, **kwargs):
        """
        Get direct message rooms

        :return:
        """
        return GetImRooms(settings=self.settings, **kwargs).call(**kwargs)

    def get_im_room_history(
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
        Get various history of specific direct message room

        :param room_id:
        :param kwargs:
        :return:
        """
        return GetImRoomHistory(settings=self.settings, **kwargs).call(
            room_id=room_id,
            oldest=oldest,
            latest=latest,
            inclusive=inclusive,
            count=count,
            unreads=unreads,
            **kwargs
        )

    def logout(self, **kwargs):
        """
        Logout

        :return:
        """
        return Logout(settings=self.settings, **kwargs).call(**kwargs)
