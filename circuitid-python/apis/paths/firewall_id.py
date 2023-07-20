from circuitid-python.paths.firewall_id.get import ApiForget
from circuitid-python.paths.firewall_id.delete import ApiFordelete
from circuitid-python.paths.firewall_id.patch import ApiForpatch


class FirewallId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
