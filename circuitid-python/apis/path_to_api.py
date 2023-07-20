import typing_extensions

from circuitid-python.paths import PathValues
from circuitid-python.apis.paths.authentication import Authentication
from circuitid-python.apis.paths.acceptedsenders_id import AcceptedsendersId
from circuitid-python.apis.paths.acceptedsenders import Acceptedsenders
from circuitid-python.apis.paths.announcements_id import AnnouncementsId
from circuitid-python.apis.paths.announcements import Announcements
from circuitid-python.apis.paths.appmarketplace import Appmarketplace
from circuitid-python.apis.paths.contacts_id import ContactsId
from circuitid-python.apis.paths.contacts import Contacts
from circuitid-python.apis.paths.callqueues_id import CallqueuesId
from circuitid-python.apis.paths.callqueues import Callqueues
from circuitid-python.apis.paths.callqueueagents_id import CallqueueagentsId
from circuitid-python.apis.paths.callqueueagents import Callqueueagents
from circuitid-python.apis.paths.chatrooms_id import ChatroomsId
from circuitid-python.apis.paths.chatrooms import Chatrooms
from circuitid-python.apis.paths.clients_id import ClientsId
from circuitid-python.apis.paths.clients import Clients
from circuitid-python.apis.paths.conversations_id import ConversationsId
from circuitid-python.apis.paths.conversations import Conversations
from circuitid-python.apis.paths.conversationmessages_id import ConversationmessagesId
from circuitid-python.apis.paths.conversationmessages import Conversationmessages
from circuitid-python.apis.paths.conferencerooms_id import ConferenceroomsId
from circuitid-python.apis.paths.conferencerooms import Conferencerooms
from circuitid-python.apis.paths.conferencenumbers import Conferencenumbers
from circuitid-python.apis.paths.customers_id import CustomersId
from circuitid-python.apis.paths.customers import Customers
from circuitid-python.apis.paths.developerapps_id import DeveloperappsId
from circuitid-python.apis.paths.developerapps import Developerapps
from circuitid-python.apis.paths.developerappsubscriptions_id import DeveloperappsubscriptionsId
from circuitid-python.apis.paths.developerappsubscriptions import Developerappsubscriptions
from circuitid-python.apis.paths.directories_id import DirectoriesId
from circuitid-python.apis.paths.directories import Directories
from circuitid-python.apis.paths.domains_id import DomainsId
from circuitid-python.apis.paths.domains import Domains
from circuitid-python.apis.paths.dnsrecords import Dnsrecords
from circuitid-python.apis.paths.faxes_id import FaxesId
from circuitid-python.apis.paths.faxes import Faxes
from circuitid-python.apis.paths.faxaccounts_id import FaxaccountsId
from circuitid-python.apis.paths.faxaccounts import Faxaccounts
from circuitid-python.apis.paths.findnumbers import Findnumbers
from circuitid-python.apis.paths.firewall_id import FirewallId
from circuitid-python.apis.paths.firewall import Firewall
from circuitid-python.apis.paths.groups_id import GroupsId
from circuitid-python.apis.paths.groups import Groups
from circuitid-python.apis.paths.groupmembers_id import GroupmembersId
from circuitid-python.apis.paths.groupmembers import Groupmembers
from circuitid-python.apis.paths.holidays_id import HolidaysId
from circuitid-python.apis.paths.holidays import Holidays
from circuitid-python.apis.paths.info import Info
from circuitid-python.apis.paths.invoiceitems_id import InvoiceitemsId
from circuitid-python.apis.paths.invoiceitems import Invoiceitems
from circuitid-python.apis.paths.invoices_id import InvoicesId
from circuitid-python.apis.paths.invoices import Invoices
from circuitid-python.apis.paths.licenses_id import LicensesId
from circuitid-python.apis.paths.licenses import Licenses
from circuitid-python.apis.paths.menus_id import MenusId
from circuitid-python.apis.paths.menus import Menus
from circuitid-python.apis.paths.menuoptions_id import MenuoptionsId
from circuitid-python.apis.paths.menuoptions import Menuoptions
from circuitid-python.apis.paths.messagecampaigns_id import MessagecampaignsId
from circuitid-python.apis.paths.messagecampaigns import Messagecampaigns
from circuitid-python.apis.paths.messagebrands_id import MessagebrandsId
from circuitid-python.apis.paths.messagebrands import Messagebrands
from circuitid-python.apis.paths.numbers_id import NumbersId
from circuitid-python.apis.paths.numbers import Numbers
from circuitid-python.apis.paths.numberports_id import NumberportsId
from circuitid-python.apis.paths.numberports import Numberports
from circuitid-python.apis.paths.offices_id import OfficesId
from circuitid-python.apis.paths.offices import Offices
from circuitid-python.apis.paths.phoneinboundrules_id import PhoneinboundrulesId
from circuitid-python.apis.paths.phoneinboundrules import Phoneinboundrules
from circuitid-python.apis.paths.phoneoutboundrules_id import PhoneoutboundrulesId
from circuitid-python.apis.paths.phoneoutboundrules import Phoneoutboundrules
from circuitid-python.apis.paths.phoneinboundruleactions_id import PhoneinboundruleactionsId
from circuitid-python.apis.paths.phoneinboundruleactions import Phoneinboundruleactions
from circuitid-python.apis.paths.phoneoutboundruleactions_id import PhoneoutboundruleactionsId
from circuitid-python.apis.paths.phoneoutboundruleactions import Phoneoutboundruleactions
from circuitid-python.apis.paths.ratecenters_id import RatecentersId
from circuitid-python.apis.paths.ratecenters import Ratecenters
from circuitid-python.apis.paths.servers_id import ServersId
from circuitid-python.apis.paths.servers import Servers
from circuitid-python.apis.paths.timeschedules_id import TimeschedulesId
from circuitid-python.apis.paths.timeschedules import Timeschedules
from circuitid-python.apis.paths.users_id import UsersId
from circuitid-python.apis.paths.users import Users
from circuitid-python.apis.paths.usertokens_id import UsertokensId
from circuitid-python.apis.paths.usertokens import Usertokens
from circuitid-python.apis.paths.virtualextensions_id import VirtualextensionsId
from circuitid-python.apis.paths.virtualextensions import Virtualextensions
from circuitid-python.apis.paths.voicemail_id import VoicemailId
from circuitid-python.apis.paths.voicemail import Voicemail

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
