from circuitid-python.paths.virtualextensions_id.get import ApiForget
from circuitid-python.paths.virtualextensions_id.delete import ApiFordelete
from circuitid-python.paths.virtualextensions_id.patch import ApiForpatch


class VirtualextensionsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
