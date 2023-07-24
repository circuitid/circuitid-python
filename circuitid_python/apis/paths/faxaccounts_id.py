from circuitid_python.paths.faxaccounts_id.get import ApiForget
from circuitid_python.paths.faxaccounts_id.delete import ApiFordelete
from circuitid_python.paths.faxaccounts_id.patch import ApiForpatch


class FaxaccountsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
