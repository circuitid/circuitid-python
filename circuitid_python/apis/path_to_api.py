import typing_extensions

from circuitid_python.paths import PathValues
from circuitid_python.apis.paths.authentication import Authentication
from circuitid_python.apis.paths.acceptedsenders_id import AcceptedsendersId
from circuitid_python.apis.paths.acceptedsenders import Acceptedsenders
from circuitid_python.apis.paths.announcements_id import AnnouncementsId
from circuitid_python.apis.paths.announcements import Announcements
from circuitid_python.apis.paths.appmarketplace import Appmarketplace
from circuitid_python.apis.paths.contacts_id import ContactsId
from circuitid_python.apis.paths.contacts import Contacts
from circuitid_python.apis.paths.callqueues_id import CallqueuesId
from circuitid_python.apis.paths.callqueues import Callqueues
from circuitid_python.apis.paths.callqueueagents_id import CallqueueagentsId
from circuitid_python.apis.paths.callqueueagents import Callqueueagents
from circuitid_python.apis.paths.chatrooms_id import ChatroomsId
from circuitid_python.apis.paths.chatrooms import Chatrooms
from circuitid_python.apis.paths.clients_id import ClientsId
from circuitid_python.apis.paths.clients import Clients
from circuitid_python.apis.paths.conversations_id import ConversationsId
from circuitid_python.apis.paths.conversations import Conversations
from circuitid_python.apis.paths.conversationmessages_id import ConversationmessagesId
from circuitid_python.apis.paths.conversationmessages import Conversationmessages
from circuitid_python.apis.paths.conferencerooms_id import ConferenceroomsId
from circuitid_python.apis.paths.conferencerooms import Conferencerooms
from circuitid_python.apis.paths.conferencenumbers import Conferencenumbers
from circuitid_python.apis.paths.customers_id import CustomersId
from circuitid_python.apis.paths.customers import Customers
from circuitid_python.apis.paths.developerapps_id import DeveloperappsId
from circuitid_python.apis.paths.developerapps import Developerapps
from circuitid_python.apis.paths.developerappsubscriptions_id import DeveloperappsubscriptionsId
from circuitid_python.apis.paths.developerappsubscriptions import Developerappsubscriptions
from circuitid_python.apis.paths.directories_id import DirectoriesId
from circuitid_python.apis.paths.directories import Directories
from circuitid_python.apis.paths.domains_id import DomainsId
from circuitid_python.apis.paths.domains import Domains
from circuitid_python.apis.paths.dnsrecords import Dnsrecords
from circuitid_python.apis.paths.faxes_id import FaxesId
from circuitid_python.apis.paths.faxes import Faxes
from circuitid_python.apis.paths.faxaccounts_id import FaxaccountsId
from circuitid_python.apis.paths.faxaccounts import Faxaccounts
from circuitid_python.apis.paths.findnumbers import Findnumbers
from circuitid_python.apis.paths.firewall_id import FirewallId
from circuitid_python.apis.paths.firewall import Firewall
from circuitid_python.apis.paths.groups_id import GroupsId
from circuitid_python.apis.paths.groups import Groups
from circuitid_python.apis.paths.groupmembers_id import GroupmembersId
from circuitid_python.apis.paths.groupmembers import Groupmembers
from circuitid_python.apis.paths.holidays_id import HolidaysId
from circuitid_python.apis.paths.holidays import Holidays
from circuitid_python.apis.paths.info import Info
from circuitid_python.apis.paths.invoiceitems_id import InvoiceitemsId
from circuitid_python.apis.paths.invoiceitems import Invoiceitems
from circuitid_python.apis.paths.invoices_id import InvoicesId
from circuitid_python.apis.paths.invoices import Invoices
from circuitid_python.apis.paths.licenses_id import LicensesId
from circuitid_python.apis.paths.licenses import Licenses
from circuitid_python.apis.paths.menus_id import MenusId
from circuitid_python.apis.paths.menus import Menus
from circuitid_python.apis.paths.menuoptions_id import MenuoptionsId
from circuitid_python.apis.paths.menuoptions import Menuoptions
from circuitid_python.apis.paths.messagecampaigns_id import MessagecampaignsId
from circuitid_python.apis.paths.messagecampaigns import Messagecampaigns
from circuitid_python.apis.paths.messagebrands_id import MessagebrandsId
from circuitid_python.apis.paths.messagebrands import Messagebrands
from circuitid_python.apis.paths.numbers_id import NumbersId
from circuitid_python.apis.paths.numbers import Numbers
from circuitid_python.apis.paths.numberports_id import NumberportsId
from circuitid_python.apis.paths.numberports import Numberports
from circuitid_python.apis.paths.offices_id import OfficesId
from circuitid_python.apis.paths.offices import Offices
from circuitid_python.apis.paths.phoneinboundrules_id import PhoneinboundrulesId
from circuitid_python.apis.paths.phoneinboundrules import Phoneinboundrules
from circuitid_python.apis.paths.phoneoutboundrules_id import PhoneoutboundrulesId
from circuitid_python.apis.paths.phoneoutboundrules import Phoneoutboundrules
from circuitid_python.apis.paths.phoneinboundruleactions_id import PhoneinboundruleactionsId
from circuitid_python.apis.paths.phoneinboundruleactions import Phoneinboundruleactions
from circuitid_python.apis.paths.phoneoutboundruleactions_id import PhoneoutboundruleactionsId
from circuitid_python.apis.paths.phoneoutboundruleactions import Phoneoutboundruleactions
from circuitid_python.apis.paths.ratecenters_id import RatecentersId
from circuitid_python.apis.paths.ratecenters import Ratecenters
from circuitid_python.apis.paths.servers_id import ServersId
from circuitid_python.apis.paths.servers import Servers
from circuitid_python.apis.paths.timeschedules_id import TimeschedulesId
from circuitid_python.apis.paths.timeschedules import Timeschedules
from circuitid_python.apis.paths.users_id import UsersId
from circuitid_python.apis.paths.users import Users
from circuitid_python.apis.paths.usertokens_id import UsertokensId
from circuitid_python.apis.paths.usertokens import Usertokens
from circuitid_python.apis.paths.virtualextensions_id import VirtualextensionsId
from circuitid_python.apis.paths.virtualextensions import Virtualextensions
from circuitid_python.apis.paths.voicemail_id import VoicemailId
from circuitid_python.apis.paths.voicemail import Voicemail

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.AUTHENTICATION: Authentication,
        PathValues.ACCEPTEDSENDERS_ID: AcceptedsendersId,
        PathValues.ACCEPTEDSENDERS: Acceptedsenders,
        PathValues.ANNOUNCEMENTS_ID: AnnouncementsId,
        PathValues.ANNOUNCEMENTS: Announcements,
        PathValues.APPMARKETPLACE: Appmarketplace,
        PathValues.CONTACTS_ID: ContactsId,
        PathValues.CONTACTS: Contacts,
        PathValues.CALLQUEUES_ID: CallqueuesId,
        PathValues.CALLQUEUES: Callqueues,
        PathValues.CALLQUEUEAGENTS_ID: CallqueueagentsId,
        PathValues.CALLQUEUEAGENTS: Callqueueagents,
        PathValues.CHATROOMS_ID: ChatroomsId,
        PathValues.CHATROOMS: Chatrooms,
        PathValues.CLIENTS_ID: ClientsId,
        PathValues.CLIENTS: Clients,
        PathValues.CONVERSATIONS_ID: ConversationsId,
        PathValues.CONVERSATIONS: Conversations,
        PathValues.CONVERSATIONMESSAGES_ID: ConversationmessagesId,
        PathValues.CONVERSATIONMESSAGES: Conversationmessages,
        PathValues.CONFERENCEROOMS_ID: ConferenceroomsId,
        PathValues.CONFERENCEROOMS: Conferencerooms,
        PathValues.CONFERENCENUMBERS: Conferencenumbers,
        PathValues.CUSTOMERS_ID: CustomersId,
        PathValues.CUSTOMERS: Customers,
        PathValues.DEVELOPERAPPS_ID: DeveloperappsId,
        PathValues.DEVELOPERAPPS: Developerapps,
        PathValues.DEVELOPERAPPSUBSCRIPTIONS_ID: DeveloperappsubscriptionsId,
        PathValues.DEVELOPERAPPSUBSCRIPTIONS: Developerappsubscriptions,
        PathValues.DIRECTORIES_ID: DirectoriesId,
        PathValues.DIRECTORIES: Directories,
        PathValues.DOMAINS_ID: DomainsId,
        PathValues.DOMAINS: Domains,
        PathValues.DNSRECORDS: Dnsrecords,
        PathValues.FAXES_ID: FaxesId,
        PathValues.FAXES: Faxes,
        PathValues.FAXACCOUNTS_ID: FaxaccountsId,
        PathValues.FAXACCOUNTS: Faxaccounts,
        PathValues.FINDNUMBERS: Findnumbers,
        PathValues.FIREWALL_ID: FirewallId,
        PathValues.FIREWALL: Firewall,
        PathValues.GROUPS_ID: GroupsId,
        PathValues.GROUPS: Groups,
        PathValues.GROUPMEMBERS_ID: GroupmembersId,
        PathValues.GROUPMEMBERS: Groupmembers,
        PathValues.HOLIDAYS_ID: HolidaysId,
        PathValues.HOLIDAYS: Holidays,
        PathValues.INFO: Info,
        PathValues.INVOICEITEMS_ID: InvoiceitemsId,
        PathValues.INVOICEITEMS: Invoiceitems,
        PathValues.INVOICES_ID: InvoicesId,
        PathValues.INVOICES: Invoices,
        PathValues.LICENSES_ID: LicensesId,
        PathValues.LICENSES: Licenses,
        PathValues.MENUS_ID: MenusId,
        PathValues.MENUS: Menus,
        PathValues.MENUOPTIONS_ID: MenuoptionsId,
        PathValues.MENUOPTIONS: Menuoptions,
        PathValues.MESSAGECAMPAIGNS_ID: MessagecampaignsId,
        PathValues.MESSAGECAMPAIGNS: Messagecampaigns,
        PathValues.MESSAGEBRANDS_ID: MessagebrandsId,
        PathValues.MESSAGEBRANDS: Messagebrands,
        PathValues.NUMBERS_ID: NumbersId,
        PathValues.NUMBERS: Numbers,
        PathValues.NUMBERPORTS_ID: NumberportsId,
        PathValues.NUMBERPORTS: Numberports,
        PathValues.OFFICES_ID: OfficesId,
        PathValues.OFFICES: Offices,
        PathValues.PHONEINBOUNDRULES_ID: PhoneinboundrulesId,
        PathValues.PHONEINBOUNDRULES: Phoneinboundrules,
        PathValues.PHONEOUTBOUNDRULES_ID: PhoneoutboundrulesId,
        PathValues.PHONEOUTBOUNDRULES: Phoneoutboundrules,
        PathValues.PHONEINBOUNDRULEACTIONS_ID: PhoneinboundruleactionsId,
        PathValues.PHONEINBOUNDRULEACTIONS: Phoneinboundruleactions,
        PathValues.PHONEOUTBOUNDRULEACTIONS_ID: PhoneoutboundruleactionsId,
        PathValues.PHONEOUTBOUNDRULEACTIONS: Phoneoutboundruleactions,
        PathValues.RATECENTERS_ID: RatecentersId,
        PathValues.RATECENTERS: Ratecenters,
        PathValues.SERVERS_ID: ServersId,
        PathValues.SERVERS: Servers,
        PathValues.TIMESCHEDULES_ID: TimeschedulesId,
        PathValues.TIMESCHEDULES: Timeschedules,
        PathValues.USERS_ID: UsersId,
        PathValues.USERS: Users,
        PathValues.USERTOKENS_ID: UsertokensId,
        PathValues.USERTOKENS: Usertokens,
        PathValues.VIRTUALEXTENSIONS_ID: VirtualextensionsId,
        PathValues.VIRTUALEXTENSIONS: Virtualextensions,
        PathValues.VOICEMAIL_ID: VoicemailId,
        PathValues.VOICEMAIL: Voicemail,
    }
)

path_to_api = PathToApi(
    {
        PathValues.AUTHENTICATION: Authentication,
        PathValues.ACCEPTEDSENDERS_ID: AcceptedsendersId,
        PathValues.ACCEPTEDSENDERS: Acceptedsenders,
        PathValues.ANNOUNCEMENTS_ID: AnnouncementsId,
        PathValues.ANNOUNCEMENTS: Announcements,
        PathValues.APPMARKETPLACE: Appmarketplace,
        PathValues.CONTACTS_ID: ContactsId,
        PathValues.CONTACTS: Contacts,
        PathValues.CALLQUEUES_ID: CallqueuesId,
        PathValues.CALLQUEUES: Callqueues,
        PathValues.CALLQUEUEAGENTS_ID: CallqueueagentsId,
        PathValues.CALLQUEUEAGENTS: Callqueueagents,
        PathValues.CHATROOMS_ID: ChatroomsId,
        PathValues.CHATROOMS: Chatrooms,
        PathValues.CLIENTS_ID: ClientsId,
        PathValues.CLIENTS: Clients,
        PathValues.CONVERSATIONS_ID: ConversationsId,
        PathValues.CONVERSATIONS: Conversations,
        PathValues.CONVERSATIONMESSAGES_ID: ConversationmessagesId,
        PathValues.CONVERSATIONMESSAGES: Conversationmessages,
        PathValues.CONFERENCEROOMS_ID: ConferenceroomsId,
        PathValues.CONFERENCEROOMS: Conferencerooms,
        PathValues.CONFERENCENUMBERS: Conferencenumbers,
        PathValues.CUSTOMERS_ID: CustomersId,
        PathValues.CUSTOMERS: Customers,
        PathValues.DEVELOPERAPPS_ID: DeveloperappsId,
        PathValues.DEVELOPERAPPS: Developerapps,
        PathValues.DEVELOPERAPPSUBSCRIPTIONS_ID: DeveloperappsubscriptionsId,
        PathValues.DEVELOPERAPPSUBSCRIPTIONS: Developerappsubscriptions,
        PathValues.DIRECTORIES_ID: DirectoriesId,
        PathValues.DIRECTORIES: Directories,
        PathValues.DOMAINS_ID: DomainsId,
        PathValues.DOMAINS: Domains,
        PathValues.DNSRECORDS: Dnsrecords,
        PathValues.FAXES_ID: FaxesId,
        PathValues.FAXES: Faxes,
        PathValues.FAXACCOUNTS_ID: FaxaccountsId,
        PathValues.FAXACCOUNTS: Faxaccounts,
        PathValues.FINDNUMBERS: Findnumbers,
        PathValues.FIREWALL_ID: FirewallId,
        PathValues.FIREWALL: Firewall,
        PathValues.GROUPS_ID: GroupsId,
        PathValues.GROUPS: Groups,
        PathValues.GROUPMEMBERS_ID: GroupmembersId,
        PathValues.GROUPMEMBERS: Groupmembers,
        PathValues.HOLIDAYS_ID: HolidaysId,
        PathValues.HOLIDAYS: Holidays,
        PathValues.INFO: Info,
        PathValues.INVOICEITEMS_ID: InvoiceitemsId,
        PathValues.INVOICEITEMS: Invoiceitems,
        PathValues.INVOICES_ID: InvoicesId,
        PathValues.INVOICES: Invoices,
        PathValues.LICENSES_ID: LicensesId,
        PathValues.LICENSES: Licenses,
        PathValues.MENUS_ID: MenusId,
        PathValues.MENUS: Menus,
        PathValues.MENUOPTIONS_ID: MenuoptionsId,
        PathValues.MENUOPTIONS: Menuoptions,
        PathValues.MESSAGECAMPAIGNS_ID: MessagecampaignsId,
        PathValues.MESSAGECAMPAIGNS: Messagecampaigns,
        PathValues.MESSAGEBRANDS_ID: MessagebrandsId,
        PathValues.MESSAGEBRANDS: Messagebrands,
        PathValues.NUMBERS_ID: NumbersId,
        PathValues.NUMBERS: Numbers,
        PathValues.NUMBERPORTS_ID: NumberportsId,
        PathValues.NUMBERPORTS: Numberports,
        PathValues.OFFICES_ID: OfficesId,
        PathValues.OFFICES: Offices,
        PathValues.PHONEINBOUNDRULES_ID: PhoneinboundrulesId,
        PathValues.PHONEINBOUNDRULES: Phoneinboundrules,
        PathValues.PHONEOUTBOUNDRULES_ID: PhoneoutboundrulesId,
        PathValues.PHONEOUTBOUNDRULES: Phoneoutboundrules,
        PathValues.PHONEINBOUNDRULEACTIONS_ID: PhoneinboundruleactionsId,
        PathValues.PHONEINBOUNDRULEACTIONS: Phoneinboundruleactions,
        PathValues.PHONEOUTBOUNDRULEACTIONS_ID: PhoneoutboundruleactionsId,
        PathValues.PHONEOUTBOUNDRULEACTIONS: Phoneoutboundruleactions,
        PathValues.RATECENTERS_ID: RatecentersId,
        PathValues.RATECENTERS: Ratecenters,
        PathValues.SERVERS_ID: ServersId,
        PathValues.SERVERS: Servers,
        PathValues.TIMESCHEDULES_ID: TimeschedulesId,
        PathValues.TIMESCHEDULES: Timeschedules,
        PathValues.USERS_ID: UsersId,
        PathValues.USERS: Users,
        PathValues.USERTOKENS_ID: UsertokensId,
        PathValues.USERTOKENS: Usertokens,
        PathValues.VIRTUALEXTENSIONS_ID: VirtualextensionsId,
        PathValues.VIRTUALEXTENSIONS: Virtualextensions,
        PathValues.VOICEMAIL_ID: VoicemailId,
        PathValues.VOICEMAIL: Voicemail,
    }
)
