import logging

from rocketchat.calls.base import RocketChatBase

logger = logging.getLogger(__name__)


class GetImRooms(RocketChatBase):
    endpoint = "/api/v1/im.list"

    def build_endpoint(self):
        return self.endpoint

    def post_response(self, result):
        return result['ims']
