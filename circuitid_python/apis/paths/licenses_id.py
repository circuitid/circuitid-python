from circuitid_python.paths.licenses_id.get import ApiForget
from circuitid_python.paths.licenses_id.delete import ApiFordelete
from circuitid_python.paths.licenses_id.patch import ApiForpatch


class LicensesId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
