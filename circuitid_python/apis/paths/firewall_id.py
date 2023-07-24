from circuitid_python.paths.firewall_id.get import ApiForget
from circuitid_python.paths.firewall_id.delete import ApiFordelete
from circuitid_python.paths.firewall_id.patch import ApiForpatch


class FirewallId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
