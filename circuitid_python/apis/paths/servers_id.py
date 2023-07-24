from circuitid_python.paths.servers_id.get import ApiForget
from circuitid_python.paths.servers_id.delete import ApiFordelete
from circuitid_python.paths.servers_id.patch import ApiForpatch


class ServersId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
