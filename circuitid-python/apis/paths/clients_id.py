from circuitid-python.paths.clients_id.get import ApiForget
from circuitid-python.paths.clients_id.delete import ApiFordelete
from circuitid-python.paths.clients_id.patch import ApiForpatch


class ClientsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
