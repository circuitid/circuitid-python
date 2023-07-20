from circuitid-python.paths.announcements_id.get import ApiForget
from circuitid-python.paths.announcements_id.delete import ApiFordelete
from circuitid-python.paths.announcements_id.patch import ApiForpatch


class AnnouncementsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
