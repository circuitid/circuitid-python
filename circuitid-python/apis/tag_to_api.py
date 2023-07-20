import typing_extensions

from circuitid-python.apis.tags import TagValues
from circuitid-python.apis.tags.authentication_api import AuthenticationApi
from circuitid-python.apis.tags.accepted_senders_api import AcceptedSendersApi
from circuitid-python.apis.tags.announcements_api import AnnouncementsApi
from circuitid-python.apis.tags.app_marketplace_api import AppMarketplaceApi
from circuitid-python.apis.tags.contacts_api import ContactsApi
from circuitid-python.apis.tags.call_queues_api import CallQueuesApi
from circuitid-python.apis.tags.call_queue_agents_api import CallQueueAgentsApi
from circuitid-python.apis.tags.chat_rooms_api import ChatRoomsApi
from circuitid-python.apis.tags.clients_api import ClientsApi
from circuitid-python.apis.tags.conversations_api import ConversationsApi
from circuitid-python.apis.tags.conversation_messages_api import ConversationMessagesApi
from circuitid-python.apis.tags.conference_rooms_api import ConferenceRoomsApi
from circuitid-python.apis.tags.conference_numbers_api import ConferenceNumbersApi
from circuitid-python.apis.tags.customers_api import CustomersApi
from circuitid-python.apis.tags.developer_apps_api import DeveloperAppsApi
from circuitid-python.apis.tags.developer_app_subscriptions_api import DeveloperAppSubscriptionsApi
from circuitid-python.apis.tags.directories_api import DirectoriesApi
from circuitid-python.apis.tags.domains_api import DomainsApi
from circuitid-python.apis.tags.dns_records_api import DNSRecordsApi
from circuitid-python.apis.tags.faxes_api import FaxesApi
from circuitid-python.apis.tags.fax_account_api import FaxAccountApi
from circuitid-python.apis.tags.find_numbers_api import FindNumbersApi
from circuitid-python.apis.tags.firewall_api import FirewallApi
from circuitid-python.apis.tags.groups_api import GroupsApi
from circuitid-python.apis.tags.group_members_api import GroupMembersApi
from circuitid-python.apis.tags.holidays_api import HolidaysApi
from circuitid-python.apis.tags.info_api import InfoApi
from circuitid-python.apis.tags.invoice_items_api import InvoiceItemsApi
from circuitid-python.apis.tags.invoices_api import InvoicesApi
from circuitid-python.apis.tags.licenses_api import LicensesApi
from circuitid-python.apis.tags.menus_api import MenusApi
from circuitid-python.apis.tags.menu_options_api import MenuOptionsApi
from circuitid-python.apis.tags.message_campaigns_api import MessageCampaignsApi
from circuitid-python.apis.tags.message_brands_api import MessageBrandsApi
from circuitid-python.apis.tags.numbers_api import NumbersApi
from circuitid-python.apis.tags.number_ports_api import NumberPortsApi
from circuitid-python.apis.tags.offices_api import OfficesApi
from circuitid-python.apis.tags.phone_inbound_rules_api import PhoneInboundRulesApi
from circuitid-python.apis.tags.phone_outbound_rules_api import PhoneOutboundRulesApi
from circuitid-python.apis.tags.phone_inbound_rule_actions_api import PhoneInboundRuleActionsApi
from circuitid-python.apis.tags.phone_outbound_rule_actions_api import PhoneOutboundRuleActionsApi
from circuitid-python.apis.tags.rate_centers_api import RateCentersApi
from circuitid-python.apis.tags.servers_api import ServersApi
from circuitid-python.apis.tags.time_schedules_api import TimeSchedulesApi
from circuitid-python.apis.tags.users_api import UsersApi
from circuitid-python.apis.tags.user_tokens_api import UserTokensApi
from circuitid-python.apis.tags.virtual_extensions_api import VirtualExtensionsApi
from circuitid-python.apis.tags.voicemail_api import VoicemailApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.ACCEPTED_SENDERS: AcceptedSendersApi,
        TagValues.ANNOUNCEMENTS: AnnouncementsApi,
        TagValues.APP_MARKETPLACE: AppMarketplaceApi,
        TagValues.CONTACTS: ContactsApi,
        TagValues.CALL_QUEUES: CallQueuesApi,
        TagValues.CALL_QUEUE_AGENTS: CallQueueAgentsApi,
        TagValues.CHAT_ROOMS: ChatRoomsApi,
        TagValues.CLIENTS: ClientsApi,
        TagValues.CONVERSATIONS: ConversationsApi,
        TagValues.CONVERSATION_MESSAGES: ConversationMessagesApi,
        TagValues.CONFERENCE_ROOMS: ConferenceRoomsApi,
        TagValues.CONFERENCE_NUMBERS: ConferenceNumbersApi,
        TagValues.CUSTOMERS: CustomersApi,
        TagValues.DEVELOPER_APPS: DeveloperAppsApi,
        TagValues.DEVELOPER_APP_SUBSCRIPTIONS: DeveloperAppSubscriptionsApi,
        TagValues.DIRECTORIES: DirectoriesApi,
        TagValues.DOMAINS: DomainsApi,
        TagValues.DNS_RECORDS: DNSRecordsApi,
        TagValues.FAXES: FaxesApi,
        TagValues.FAX_ACCOUNT: FaxAccountApi,
        TagValues.FIND_NUMBERS: FindNumbersApi,
        TagValues.FIREWALL: FirewallApi,
        TagValues.GROUPS: GroupsApi,
        TagValues.GROUP_MEMBERS: GroupMembersApi,
        TagValues.HOLIDAYS: HolidaysApi,
        TagValues.INFO: InfoApi,
        TagValues.INVOICE_ITEMS: InvoiceItemsApi,
        TagValues.INVOICES: InvoicesApi,
        TagValues.LICENSES: LicensesApi,
        TagValues.MENUS: MenusApi,
        TagValues.MENU_OPTIONS: MenuOptionsApi,
        TagValues.MESSAGE_CAMPAIGNS: MessageCampaignsApi,
        TagValues.MESSAGE_BRANDS: MessageBrandsApi,
        TagValues.NUMBERS: NumbersApi,
        TagValues.NUMBER_PORTS: NumberPortsApi,
        TagValues.OFFICES: OfficesApi,
        TagValues.PHONE_INBOUND_RULES: PhoneInboundRulesApi,
        TagValues.PHONE_OUTBOUND_RULES: PhoneOutboundRulesApi,
        TagValues.PHONE_INBOUND_RULE_ACTIONS: PhoneInboundRuleActionsApi,
        TagValues.PHONE_OUTBOUND_RULE_ACTIONS: PhoneOutboundRuleActionsApi,
        TagValues.RATE_CENTERS: RateCentersApi,
        TagValues.SERVERS: ServersApi,
        TagValues.TIME_SCHEDULES: TimeSchedulesApi,
        TagValues.USERS: UsersApi,
        TagValues.USER_TOKENS: UserTokensApi,
        TagValues.VIRTUAL_EXTENSIONS: VirtualExtensionsApi,
        TagValues.VOICEMAIL: VoicemailApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.ACCEPTED_SENDERS: AcceptedSendersApi,
        TagValues.ANNOUNCEMENTS: AnnouncementsApi,
        TagValues.APP_MARKETPLACE: AppMarketplaceApi,
        TagValues.CONTACTS: ContactsApi,
        TagValues.CALL_QUEUES: CallQueuesApi,
        TagValues.CALL_QUEUE_AGENTS: CallQueueAgentsApi,
        TagValues.CHAT_ROOMS: ChatRoomsApi,
        TagValues.CLIENTS: ClientsApi,
        TagValues.CONVERSATIONS: ConversationsApi,
        TagValues.CONVERSATION_MESSAGES: ConversationMessagesApi,
        TagValues.CONFERENCE_ROOMS: ConferenceRoomsApi,
        TagValues.CONFERENCE_NUMBERS: ConferenceNumbersApi,
        TagValues.CUSTOMERS: CustomersApi,
        TagValues.DEVELOPER_APPS: DeveloperAppsApi,
        TagValues.DEVELOPER_APP_SUBSCRIPTIONS: DeveloperAppSubscriptionsApi,
        TagValues.DIRECTORIES: DirectoriesApi,
        TagValues.DOMAINS: DomainsApi,
        TagValues.DNS_RECORDS: DNSRecordsApi,
        TagValues.FAXES: FaxesApi,
        TagValues.FAX_ACCOUNT: FaxAccountApi,
        TagValues.FIND_NUMBERS: FindNumbersApi,
        TagValues.FIREWALL: FirewallApi,
        TagValues.GROUPS: GroupsApi,
        TagValues.GROUP_MEMBERS: GroupMembersApi,
        TagValues.HOLIDAYS: HolidaysApi,
        TagValues.INFO: InfoApi,
        TagValues.INVOICE_ITEMS: InvoiceItemsApi,
        TagValues.INVOICES: InvoicesApi,
        TagValues.LICENSES: LicensesApi,
        TagValues.MENUS: MenusApi,
        TagValues.MENU_OPTIONS: MenuOptionsApi,
        TagValues.MESSAGE_CAMPAIGNS: MessageCampaignsApi,
        TagValues.MESSAGE_BRANDS: MessageBrandsApi,
        TagValues.NUMBERS: NumbersApi,
        TagValues.NUMBER_PORTS: NumberPortsApi,
        TagValues.OFFICES: OfficesApi,
        TagValues.PHONE_INBOUND_RULES: PhoneInboundRulesApi,
        TagValues.PHONE_OUTBOUND_RULES: PhoneOutboundRulesApi,
        TagValues.PHONE_INBOUND_RULE_ACTIONS: PhoneInboundRuleActionsApi,
        TagValues.PHONE_OUTBOUND_RULE_ACTIONS: PhoneOutboundRuleActionsApi,
        TagValues.RATE_CENTERS: RateCentersApi,
        TagValues.SERVERS: ServersApi,
        TagValues.TIME_SCHEDULES: TimeSchedulesApi,
        TagValues.USERS: UsersApi,
        TagValues.USER_TOKENS: UserTokensApi,
        TagValues.VIRTUAL_EXTENSIONS: VirtualExtensionsApi,
        TagValues.VOICEMAIL: VoicemailApi,
    }
)
