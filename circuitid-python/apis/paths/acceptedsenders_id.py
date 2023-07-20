from circuitid-python.paths.acceptedsenders_id.get import ApiForget
from circuitid-python.paths.acceptedsenders_id.delete import ApiFordelete
from circuitid-python.paths.acceptedsenders_id.patch import ApiForpatch


class AcceptedsendersId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
