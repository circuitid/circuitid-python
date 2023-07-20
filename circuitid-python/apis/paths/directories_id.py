from circuitid-python.paths.directories_id.get import ApiForget
from circuitid-python.paths.directories_id.delete import ApiFordelete
from circuitid-python.paths.directories_id.patch import ApiForpatch


class DirectoriesId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
