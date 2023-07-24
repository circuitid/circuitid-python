from circuitid_python.paths.groupmembers_id.get import ApiForget
from circuitid_python.paths.groupmembers_id.delete import ApiFordelete
from circuitid_python.paths.groupmembers_id.patch import ApiForpatch


class GroupmembersId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
