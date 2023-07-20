from circuitid-python.paths.groups_id.get import ApiForget
from circuitid-python.paths.groups_id.delete import ApiFordelete
from circuitid-python.paths.groups_id.patch import ApiForpatch


class GroupsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
