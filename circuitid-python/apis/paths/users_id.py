from circuitid-python.paths.users_id.get import ApiForget
from circuitid-python.paths.users_id.delete import ApiFordelete
from circuitid-python.paths.users_id.patch import ApiForpatch


class UsersId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
