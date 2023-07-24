from circuitid_python.paths.callqueueagents_id.get import ApiForget
from circuitid_python.paths.callqueueagents_id.delete import ApiFordelete
from circuitid_python.paths.callqueueagents_id.patch import ApiForpatch


class CallqueueagentsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
