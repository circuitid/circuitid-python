from circuitid_python.paths.usertokens_id.get import ApiForget
from circuitid_python.paths.usertokens_id.delete import ApiFordelete
from circuitid_python.paths.usertokens_id.patch import ApiForpatch


class UsertokensId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
