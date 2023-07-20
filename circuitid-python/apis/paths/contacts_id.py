from circuitid-python.paths.contacts_id.get import ApiForget
from circuitid-python.paths.contacts_id.delete import ApiFordelete
from circuitid-python.paths.contacts_id.patch import ApiForpatch


class ContactsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
