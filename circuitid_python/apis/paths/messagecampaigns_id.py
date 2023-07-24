from circuitid_python.paths.messagecampaigns_id.get import ApiForget
from circuitid_python.paths.messagecampaigns_id.delete import ApiFordelete
from circuitid_python.paths.messagecampaigns_id.patch import ApiForpatch


class MessagecampaignsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
