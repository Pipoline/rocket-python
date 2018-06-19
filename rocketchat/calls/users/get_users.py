import logging


from rocketchat.calls.base import RocketChatBase

logger = logging.getLogger(__name__)


class GetUsers(RocketChatBase):
    endpoint = '/api/v1/users.list'

    def build_endpoint(self):
        return self.endpoint

    def post_response(self, result):
        users = []

        try:
            _users = result.get('users')

            for user in _users:
                user_dict = dict()
                user_dict['name'] = user.get('name')
                user_dict['emails'] = [email['address'] for email in user.get('emails')]
                user_dict['username'] = user.get('username')
                user_dict['type'] = user.get('type')
                user_dict['status'] = user.get('status')
                user_dict['roles'] = user.get('roles')
                user_dict['id'] = user.get('_id')
                users.append(user_dict)

        except Exception as e:
            logger.error('Exception in fetching public rooms {e}'.format(
                e=e
            ), exc_info=True)

        return users
