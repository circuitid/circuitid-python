from circuitid-python.paths.messagecampaigns_id.get import ApiForget
from circuitid-python.paths.messagecampaigns_id.delete import ApiFordelete
from circuitid-python.paths.messagecampaigns_id.patch import ApiForpatch


class MessagecampaignsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
