from circuitid-python.paths.conversations_id.get import ApiForget
from circuitid-python.paths.conversations_id.delete import ApiFordelete
from circuitid-python.paths.conversations_id.patch import ApiForpatch


class ConversationsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
