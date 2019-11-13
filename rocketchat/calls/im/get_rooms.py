import logging

from rocketchat.calls.base import RocketChatBase

logger = logging.getLogger(__name__)


class GetImRooms(RocketChatBase):
    endpoint = "/api/v1/im.list"

    def build_endpoint(self):
        return self.endpoint

    def post_response(self, result):
        rooms = []

        try:
            _rooms = result.get("ims")

            for room in _rooms:
                if not room.get("usernames"):
                    continue

                for username in room.get("usernames"):
                    if username != self.settings["username"]:
                        break

                room_dict = {}
                room_dict["username"] = username
                room_dict["id"] = room.get("_id")
                rooms.append(room_dict)

        except Exception as e:
            logger.error(
                "Exception in fetching im rooms {e}".format(e=e),
                exc_info=True,
            )

        return rooms
