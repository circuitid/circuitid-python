from circuitid-python.paths.domains_id.get import ApiForget
from circuitid-python.paths.domains_id.delete import ApiFordelete
from circuitid-python.paths.domains_id.patch import ApiForpatch


class DomainsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
