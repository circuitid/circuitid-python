from circuitid_python.paths.developerapps_id.get import ApiForget
from circuitid_python.paths.developerapps_id.delete import ApiFordelete
from circuitid_python.paths.developerapps_id.patch import ApiForpatch


class DeveloperappsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
