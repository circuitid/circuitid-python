from circuitid-python.paths.servers_id.get import ApiForget
from circuitid-python.paths.servers_id.delete import ApiFordelete
from circuitid-python.paths.servers_id.patch import ApiForpatch


class ServersId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
