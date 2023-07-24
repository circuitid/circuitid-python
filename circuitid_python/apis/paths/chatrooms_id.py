from circuitid_python.paths.chatrooms_id.get import ApiForget
from circuitid_python.paths.chatrooms_id.delete import ApiFordelete
from circuitid_python.paths.chatrooms_id.patch import ApiForpatch


class ChatroomsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
