from circuitid_python.paths.conversationmessages_id.get import ApiForget
from circuitid_python.paths.conversationmessages_id.delete import ApiFordelete
from circuitid_python.paths.conversationmessages_id.patch import ApiForpatch


class ConversationmessagesId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
