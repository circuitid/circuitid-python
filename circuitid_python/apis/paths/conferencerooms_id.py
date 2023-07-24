from circuitid_python.paths.conferencerooms_id.get import ApiForget
from circuitid_python.paths.conferencerooms_id.delete import ApiFordelete
from circuitid_python.paths.conferencerooms_id.patch import ApiForpatch


class ConferenceroomsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
