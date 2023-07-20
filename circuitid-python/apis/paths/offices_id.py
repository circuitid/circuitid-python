from circuitid-python.paths.offices_id.get import ApiForget
from circuitid-python.paths.offices_id.delete import ApiFordelete
from circuitid-python.paths.offices_id.patch import ApiForpatch


class OfficesId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
