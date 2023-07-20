from circuitid-python.paths.timeschedules_id.get import ApiForget
from circuitid-python.paths.timeschedules_id.delete import ApiFordelete
from circuitid-python.paths.timeschedules_id.patch import ApiForpatch


class TimeschedulesId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
