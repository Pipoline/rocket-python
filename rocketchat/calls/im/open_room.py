import json
import logging

from rocketchat.calls.base import PostMixin, RocketChatBase

logger = logging.getLogger(__name__)


class OpenImRoom(PostMixin, RocketChatBase):
    endpoint = "/api/v1/im.create"

    def build_endpoint(self, **kwargs):
        return self.endpoint

    def build_payload(self, **kwargs):
        return json.dumps({"roomId": kwargs.get("room_id")})

    def post_response(self, result):
        return result
