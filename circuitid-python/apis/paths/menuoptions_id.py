from circuitid-python.paths.menuoptions_id.get import ApiForget
from circuitid-python.paths.menuoptions_id.delete import ApiFordelete
from circuitid-python.paths.menuoptions_id.patch import ApiForpatch


class MenuoptionsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
