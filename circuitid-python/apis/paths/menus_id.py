from circuitid-python.paths.menus_id.get import ApiForget
from circuitid-python.paths.menus_id.delete import ApiFordelete
from circuitid-python.paths.menus_id.patch import ApiForpatch


class MenusId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
