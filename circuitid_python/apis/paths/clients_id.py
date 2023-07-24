from circuitid_python.paths.clients_id.get import ApiForget
from circuitid_python.paths.clients_id.delete import ApiFordelete
from circuitid_python.paths.clients_id.patch import ApiForpatch


class ClientsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
