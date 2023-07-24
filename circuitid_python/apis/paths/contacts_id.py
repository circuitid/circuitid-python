from circuitid_python.paths.contacts_id.get import ApiForget
from circuitid_python.paths.contacts_id.delete import ApiFordelete
from circuitid_python.paths.contacts_id.patch import ApiForpatch


class ContactsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
