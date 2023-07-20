from circuitid-python.paths.callqueues_id.get import ApiForget
from circuitid-python.paths.callqueues_id.delete import ApiFordelete
from circuitid-python.paths.callqueues_id.patch import ApiForpatch


class CallqueuesId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
