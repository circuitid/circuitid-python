from circuitid_python.paths.holidays_id.get import ApiForget
from circuitid_python.paths.holidays_id.delete import ApiFordelete
from circuitid_python.paths.holidays_id.patch import ApiForpatch


class HolidaysId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
