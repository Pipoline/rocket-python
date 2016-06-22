from rocketchat.calls.base import PostMixin, RocketChatBase


class SendMessage(PostMixin, RocketChatBase):
    endpoint = '/api/rooms/{room_id}/send'

    def build_endpoint(self, **kwargs):
        return self.endpoint.format(
            room_id=kwargs.get('room_id')
        )

    def build_payload(self, **kwargs):
        return {'msg': kwargs.get('message')}
