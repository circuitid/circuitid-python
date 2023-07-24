from circuitid_python.paths.menuoptions_id.get import ApiForget
from circuitid_python.paths.menuoptions_id.delete import ApiFordelete
from circuitid_python.paths.menuoptions_id.patch import ApiForpatch


class MenuoptionsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
