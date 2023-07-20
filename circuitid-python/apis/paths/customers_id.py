from circuitid-python.paths.customers_id.get import ApiForget
from circuitid-python.paths.customers_id.delete import ApiFordelete
from circuitid-python.paths.customers_id.patch import ApiForpatch


class CustomersId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
