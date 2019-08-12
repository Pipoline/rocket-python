import unittest
import mock

from rocketchat.api import RocketChatAPI
from rocketchat.calls.chat.send_message import SendMessage


from .data import PUBLIC_ROOM_TEST, GET_ROOM_INFO_TEST, GET_USERS_TEST, GET_USER_INFO_TEST, GET_ME_TEST, UPLOAD_FILE_TEST, SET_ROOM_TOPIC_TEST


class APITestCase(object):

    def setUp(self):
        self.settings = {'username': 'something',
                         'password': 'something',
                         'domain': 'https://www.example.com'}
        self.api = RocketChatAPI(settings=self.settings)


class SendMessageTestCase(APITestCase, unittest.TestCase):

    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_token')
    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_headers')
    def test_send_message_payload(self, set_auth_headers_mock, set_auth_mock):
        set_auth_mock.return_value = None
        set_auth_headers_mock.return_value = None

        send_message = SendMessage(settings=self.settings)

        self.assertEqual(send_message.build_payload(message='Test message', room_id="#general"),
                         {'roomId': '#general', 'text': 'Test message'})

    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_token')
    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_headers')
    @mock.patch('requests.Session.request')
    def test_send_message_api(self, request_mock, set_auth_headers_mock, set_auth_mock):
        set_auth_mock.return_value = None
        set_auth_headers_mock.return_value = None

        mock_response = mock.Mock()
        mock_response.json.return_value = {}
        request_mock.return_value = mock_response

        self.api.send_message('12312', 'Test message')


class GetPublicRoomTestCase(APITestCase, unittest.TestCase):

    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_token')
    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_headers')
    @mock.patch('requests.Session.request')
    def test_get_public_rooms(self, mock_request, set_auth_headers_mock, set_auth_mock):
        set_auth_mock.return_value = None
        set_auth_headers_mock.return_value = None

        mock_response = mock.Mock()
        mock_response.json.return_value = PUBLIC_ROOM_TEST

        mock_request.return_value = mock_response

        pub_rooms = self.api.get_public_rooms()
        self.assertEqual(pub_rooms[0]['name'], 'Test Room')
        self.assertEqual(pub_rooms[0]['id'], '123456')


class GetRoomInfoTestCase(APITestCase, unittest.TestCase):

    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_token')
    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_headers')
    @mock.patch('requests.Session.request')
    def test_get_room_info(self, mock_request, set_auth_headers_mock, set_auth_mock):
        set_auth_mock.return_value = None
        set_auth_headers_mock.return_value = None

        mock_response = mock.Mock()
        mock_response.json.return_value = GET_ROOM_INFO_TEST

        mock_request.return_value = mock_response

        room_data = self.api.get_room_info(room_id='123')

        self.assertEqual(room_data['channel']['usernames'], ['testing', 'testing1', 'testing2'])


class CreatePublicRoomTestCase(APITestCase, unittest.TestCase):

    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_token')
    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_headers')
    @mock.patch('requests.Session.request')
    def test_create_public_rooms(self, mock_request, set_auth_headers_mock, set_auth_mock):
        set_auth_mock.return_value = None
        set_auth_headers_mock.return_value = None

        mock_response = mock.Mock()
        mock_response.json.return_value = {}

        mock_request.return_value = mock_response

        self.api.create_public_room('Test Room #2')


class DeletePublicRoomTestCase(APITestCase, unittest.TestCase):

    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_token')
    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_headers')
    @mock.patch('requests.Session.request')
    def test_create_public_rooms(self, mock_request, set_auth_headers_mock, set_auth_mock):
        set_auth_mock.return_value = None
        set_auth_headers_mock.return_value = None

        mock_response = mock.Mock()
        mock_response.json.return_value = {}

        mock_request.return_value = mock_response

        self.api.delete_public_room('123456')


class GetMeTestCase(APITestCase, unittest.TestCase):

    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_token')
    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_headers')
    @mock.patch('requests.Session.request')
    def test_get_me(self, mock_request, set_auth_headers_mock, set_auth_mock):
        set_auth_mock.return_value = None
        set_auth_headers_mock.return_value = None

        mock_response = mock.Mock()
        mock_response.json.return_value = GET_ME_TEST

        mock_request.return_value = mock_response

        user_info = self.api.get_my_info()

        self.assertEqual(user_info['name'], 'Example User')


class GetUsersTestCase(APITestCase, unittest.TestCase):

    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_token')
    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_headers')
    @mock.patch('requests.Session.request')
    def test_get_user_list(self, mock_request, set_auth_headers_mock, set_auth_mock):
        set_auth_mock.return_value = None
        set_auth_headers_mock.return_value = None

        mock_response = mock.Mock()
        mock_response.json.return_value = GET_USERS_TEST

        mock_request.return_value = mock_response

        users = self.api.get_users()

        self.assertEqual(users[0]['username'], 'example')
        self.assertEqual(users[0]['name'], 'Example User')
        self.assertEqual(users[0]['id'], 'nSYqWzZ4GsKTX4dyK')


class GetUserInfoTestCase(APITestCase, unittest.TestCase):

    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_token')
    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_headers')
    @mock.patch('requests.Session.request')
    def test_get_room_info(self, mock_request, set_auth_headers_mock, set_auth_mock):
        set_auth_mock.return_value = None
        set_auth_headers_mock.return_value = None

        mock_response = mock.Mock()
        mock_response.json.return_value = GET_USER_INFO_TEST

        mock_request.return_value = mock_response

        room_data = self.api.get_user_info(user_id='nSYqWzZ4GsKTX4dyK')

        self.assertEqual(room_data['user']['username'], 'example')


class CreateUserTestCase(APITestCase, unittest.TestCase):

    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_token')
    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_headers')
    @mock.patch('requests.Session.request')
    def test_create_public_rooms(self, mock_request, set_auth_headers_mock, set_auth_mock):
        set_auth_mock.return_value = None
        set_auth_headers_mock.return_value = None

        mock_response = mock.Mock()
        mock_response.json.return_value = {}

        mock_request.return_value = mock_response

        self.api.create_user('example@example.com', 'Example User', 'qwerty', 'example', active=True)


class DeleteUserTestCase(APITestCase, unittest.TestCase):

    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_token')
    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_headers')
    @mock.patch('requests.Session.request')
    def test_create_public_rooms(self, mock_request, set_auth_headers_mock, set_auth_mock):
        set_auth_mock.return_value = None
        set_auth_headers_mock.return_value = None

        mock_response = mock.Mock()
        mock_response.json.return_value = {}

        mock_request.return_value = mock_response

        self.api.delete_user('123456')


class UploadFileTestCase(APITestCase, unittest.TestCase):

    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_token')
    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_headers')
    @mock.patch('requests.Session.request')
    def test_upload_file(self, mock_request, set_auth_headers_mock, set_auth_mock):
        set_auth_mock.return_value = None
        set_auth_headers_mock.return_value = None

        mock_response = mock.Mock()
        mock_response.json.return_value = UPLOAD_FILE_TEST

        mock_request.return_value = mock_response

        self.api.upload_file(room_id='123',
                             file="requirements.txt",
                             description="File description",
                             message="Example message")


class SetRoomTopicTestCase(APITestCase, unittest.TestCase):

    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_token')
    @mock.patch('rocketchat.calls.base.RocketChatBase.set_auth_headers')
    @mock.patch('requests.Session.request')
    def test_set_room_topic(self, mock_request, set_auth_headers_mock, set_auth_mock):
        set_auth_mock.return_value = None
        set_auth_headers_mock.return_value = None

        mock_response = mock.Mock()
        mock_response.json.return_value = SET_ROOM_TOPIC_TEST

        mock_request.return_value = mock_response

        self.api.set_room_topic(room_id='123', topic='test topic')
