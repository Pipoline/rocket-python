import logging
import json

from rocketchat.calls.base import PostMixin, RocketChatBase

logger = logging.getLogger(__name__)


class CreateUser(PostMixin, RocketChatBase):
    endpoint = '/api/v1/users.create'

    def build_endpoint(self, **kwargs):
        return self.endpoint

    def build_payload(self, **kwargs):
        return json.dumps({
            'email': kwargs.get('email'),
            'name': kwargs.get('name'),
            'password': kwargs.get('password'),
            'username': kwargs.get('username'),
            'active': kwargs.get('active', True),
            'roles': kwargs.get('roles', ['user']),
            'joinDefaultChannels': kwargs.get('join_default_channels', True),
            'requirePasswordChange': kwargs.get('require_password_change', False),
            'sendWelcomeEmail': kwargs.get('send_welcome_email', False),
            'verified': kwargs.get('verified', False),
            'customFields': kwargs.get('customFields', {})
        })

    def post_response(self, result):
        return result
