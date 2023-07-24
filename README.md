# circuitid-python
# Introduction
Circuit ID&reg; is an innovative cloud communications platform that redefines your connectivity experience. Our cutting-edge AI-powered solution seamlessly integrates calling, meetings, messaging, voicemail, fax, SIP Trunking, mobile broadband, and mobile phone services, accessible wherever you and your devices go.
                
Whether you are a beginner getting started with our API or an experienced developer looking for advanced features, this documentation site will serve as your comprehensive guide. 

We are excited to have you on board and are confident that this documentation site will empower you to leverage the full potential of our REST API.  If you have any questions or require further assistance, please don't hesitate to reach out to our support team.
                
Happy coding!


- API version: 0.47.15
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.circuitid.com/](https://www.circuitid.com/)

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/circuitid/circuitid-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/circuitid/circuitid-python.git`)

Then import the package:
```python
import circuitid_python
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import circuitid_python
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import circuitid_python
from pprint import pprint
from circuitid_python.rest.tags import accepted_senders_api
from circuitid_python.CircuitIDModel.acceptedsenders import Acceptedsenders
from circuitid_python.CircuitIDModel.response_error import ResponseError
# Defining the host is optional and defaults to https://cloud9.circuitid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = circuitid_python.Configuration(
    host = "https://cloud9.circuitid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Enter a context with an instance of the API client
with circuitid_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accepted_senders_api.AcceptedSendersApi(api_client)
    acceptedsenders = Acceptedsenders(None) # Acceptedsenders | The JSON object that will be posted to the REST API endpoint.

    try:
        # Create a new object
        api_response = api_instance.create_accepted_sender(acceptedsenders)
        pprint(api_response)
    except circuitid_python.ApiException as e:
        print("Exception when calling AcceptedSendersApi->create_accepted_sender: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://cloud9.circuitid.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AcceptedSendersApi* | [**create_accepted_sender**](docs/apis/tags/AcceptedSendersApi.md#create_accepted_sender) | **post** /acceptedsenders | Create a new object
*AcceptedSendersApi* | [**find_accepted_senders**](docs/apis/tags/AcceptedSendersApi.md#find_accepted_senders) | **get** /acceptedsenders | Find multiple objects
*AcceptedSendersApi* | [**get_accepted_sender**](docs/apis/tags/AcceptedSendersApi.md#get_accepted_sender) | **get** /acceptedsenders/{id} | Get object by id
*AcceptedSendersApi* | [**patch_accepted_sender**](docs/apis/tags/AcceptedSendersApi.md#patch_accepted_sender) | **patch** /acceptedsenders/{id} | Patch object&#x27;s data
*AcceptedSendersApi* | [**remove_accepted_sender**](docs/apis/tags/AcceptedSendersApi.md#remove_accepted_sender) | **delete** /acceptedsenders/{id} | Delete object by id
*AnnouncementsApi* | [**create_announcement**](docs/apis/tags/AnnouncementsApi.md#create_announcement) | **post** /announcements | Create a new object
*AnnouncementsApi* | [**find_announcements**](docs/apis/tags/AnnouncementsApi.md#find_announcements) | **get** /announcements | Find multiple objects
*AnnouncementsApi* | [**get_announcement**](docs/apis/tags/AnnouncementsApi.md#get_announcement) | **get** /announcements/{id} | Get object by id
*AnnouncementsApi* | [**patch_announcement**](docs/apis/tags/AnnouncementsApi.md#patch_announcement) | **patch** /announcements/{id} | Patch object&#x27;s data
*AnnouncementsApi* | [**remove_announcement**](docs/apis/tags/AnnouncementsApi.md#remove_announcement) | **delete** /announcements/{id} | Delete object by id
*AppMarketplaceApi* | [**find_app_marketplace**](docs/apis/tags/AppMarketplaceApi.md#find_app_marketplace) | **get** /appmarketplace | Find multiple objects
*AuthenticationApi* | [**create_authentication**](docs/apis/tags/AuthenticationApi.md#create_authentication) | **post** /authentication | Create a new object
*CallQueueAgentsApi* | [**create_call_queue_agent**](docs/apis/tags/CallQueueAgentsApi.md#create_call_queue_agent) | **post** /callqueueagents | Create a new object
*CallQueueAgentsApi* | [**find_call_queue_agents**](docs/apis/tags/CallQueueAgentsApi.md#find_call_queue_agents) | **get** /callqueueagents | Find multiple objects
*CallQueueAgentsApi* | [**get_call_queue_agent**](docs/apis/tags/CallQueueAgentsApi.md#get_call_queue_agent) | **get** /callqueueagents/{id} | Get object by id
*CallQueueAgentsApi* | [**patch_call_queue_agent**](docs/apis/tags/CallQueueAgentsApi.md#patch_call_queue_agent) | **patch** /callqueueagents/{id} | Patch object&#x27;s data
*CallQueueAgentsApi* | [**remove_call_queue_agent**](docs/apis/tags/CallQueueAgentsApi.md#remove_call_queue_agent) | **delete** /callqueueagents/{id} | Delete object by id
*CallQueuesApi* | [**create_call_queue**](docs/apis/tags/CallQueuesApi.md#create_call_queue) | **post** /callqueues | Create a new object
*CallQueuesApi* | [**find_call_queues**](docs/apis/tags/CallQueuesApi.md#find_call_queues) | **get** /callqueues | Find multiple objects
*CallQueuesApi* | [**get_call_queue**](docs/apis/tags/CallQueuesApi.md#get_call_queue) | **get** /callqueues/{id} | Get object by id
*CallQueuesApi* | [**patch_call_queue**](docs/apis/tags/CallQueuesApi.md#patch_call_queue) | **patch** /callqueues/{id} | Patch object&#x27;s data
*CallQueuesApi* | [**remove_call_queue**](docs/apis/tags/CallQueuesApi.md#remove_call_queue) | **delete** /callqueues/{id} | Delete object by id
*ChatRoomsApi* | [**create_chat_room**](docs/apis/tags/ChatRoomsApi.md#create_chat_room) | **post** /chatrooms | Create a new object
*ChatRoomsApi* | [**find_chat_rooms**](docs/apis/tags/ChatRoomsApi.md#find_chat_rooms) | **get** /chatrooms | Find multiple objects
*ChatRoomsApi* | [**get_chat_room**](docs/apis/tags/ChatRoomsApi.md#get_chat_room) | **get** /chatrooms/{id} | Get object by id
*ChatRoomsApi* | [**patch_chat_room**](docs/apis/tags/ChatRoomsApi.md#patch_chat_room) | **patch** /chatrooms/{id} | Patch object&#x27;s data
*ChatRoomsApi* | [**remove_chat_room**](docs/apis/tags/ChatRoomsApi.md#remove_chat_room) | **delete** /chatrooms/{id} | Delete object by id
*ClientsApi* | [**create_client**](docs/apis/tags/ClientsApi.md#create_client) | **post** /clients | Create a new object
*ClientsApi* | [**find_clients**](docs/apis/tags/ClientsApi.md#find_clients) | **get** /clients | Find multiple objects
*ClientsApi* | [**get_client**](docs/apis/tags/ClientsApi.md#get_client) | **get** /clients/{id} | Get object by id
*ClientsApi* | [**patch_client**](docs/apis/tags/ClientsApi.md#patch_client) | **patch** /clients/{id} | Patch object&#x27;s data
*ClientsApi* | [**remove_client**](docs/apis/tags/ClientsApi.md#remove_client) | **delete** /clients/{id} | Delete object by id
*ConferenceNumbersApi* | [**find_conference_numbers**](docs/apis/tags/ConferenceNumbersApi.md#find_conference_numbers) | **get** /conferencenumbers | Find multiple objects
*ConferenceRoomsApi* | [**create_conference_room**](docs/apis/tags/ConferenceRoomsApi.md#create_conference_room) | **post** /conferencerooms | Create a new object
*ConferenceRoomsApi* | [**find_conference_rooms**](docs/apis/tags/ConferenceRoomsApi.md#find_conference_rooms) | **get** /conferencerooms | Find multiple objects
*ConferenceRoomsApi* | [**get_conference_room**](docs/apis/tags/ConferenceRoomsApi.md#get_conference_room) | **get** /conferencerooms/{id} | Get object by id
*ConferenceRoomsApi* | [**patch_conference_room**](docs/apis/tags/ConferenceRoomsApi.md#patch_conference_room) | **patch** /conferencerooms/{id} | Patch object&#x27;s data
*ConferenceRoomsApi* | [**remove_conference_room**](docs/apis/tags/ConferenceRoomsApi.md#remove_conference_room) | **delete** /conferencerooms/{id} | Delete object by id
*ContactsApi* | [**create_contact**](docs/apis/tags/ContactsApi.md#create_contact) | **post** /contacts | Create a new object
*ContactsApi* | [**find_contacts**](docs/apis/tags/ContactsApi.md#find_contacts) | **get** /contacts | Find multiple objects
*ContactsApi* | [**get_contact**](docs/apis/tags/ContactsApi.md#get_contact) | **get** /contacts/{id} | Get object by id
*ContactsApi* | [**patch_contact**](docs/apis/tags/ContactsApi.md#patch_contact) | **patch** /contacts/{id} | Patch object&#x27;s data
*ContactsApi* | [**remove_contact**](docs/apis/tags/ContactsApi.md#remove_contact) | **delete** /contacts/{id} | Delete object by id
*ConversationMessagesApi* | [**create_conversation_message**](docs/apis/tags/ConversationMessagesApi.md#create_conversation_message) | **post** /conversationmessages | Create a new object
*ConversationMessagesApi* | [**find_conversation_messages**](docs/apis/tags/ConversationMessagesApi.md#find_conversation_messages) | **get** /conversationmessages | Find multiple objects
*ConversationMessagesApi* | [**get_conversation_message**](docs/apis/tags/ConversationMessagesApi.md#get_conversation_message) | **get** /conversationmessages/{id} | Get object by id
*ConversationMessagesApi* | [**patch_conversation_message**](docs/apis/tags/ConversationMessagesApi.md#patch_conversation_message) | **patch** /conversationmessages/{id} | Patch object&#x27;s data
*ConversationMessagesApi* | [**remove_conversation_message**](docs/apis/tags/ConversationMessagesApi.md#remove_conversation_message) | **delete** /conversationmessages/{id} | Delete object by id
*ConversationsApi* | [**create_conversation**](docs/apis/tags/ConversationsApi.md#create_conversation) | **post** /conversations | Create a new object
*ConversationsApi* | [**find_conversations**](docs/apis/tags/ConversationsApi.md#find_conversations) | **get** /conversations | Find multiple objects
*ConversationsApi* | [**get_conversation**](docs/apis/tags/ConversationsApi.md#get_conversation) | **get** /conversations/{id} | Get object by id
*ConversationsApi* | [**patch_conversation**](docs/apis/tags/ConversationsApi.md#patch_conversation) | **patch** /conversations/{id} | Patch object&#x27;s data
*ConversationsApi* | [**remove_conversation**](docs/apis/tags/ConversationsApi.md#remove_conversation) | **delete** /conversations/{id} | Delete object by id
*CustomersApi* | [**create_customer**](docs/apis/tags/CustomersApi.md#create_customer) | **post** /customers | Create a new object
*CustomersApi* | [**find_customers**](docs/apis/tags/CustomersApi.md#find_customers) | **get** /customers | Find multiple objects
*CustomersApi* | [**get_customer**](docs/apis/tags/CustomersApi.md#get_customer) | **get** /customers/{id} | Get object by id
*CustomersApi* | [**patch_customer**](docs/apis/tags/CustomersApi.md#patch_customer) | **patch** /customers/{id} | Patch object&#x27;s data
*CustomersApi* | [**remove_customer**](docs/apis/tags/CustomersApi.md#remove_customer) | **delete** /customers/{id} | Delete object by id
*DNSRecordsApi* | [**find_dns_records**](docs/apis/tags/DNSRecordsApi.md#find_dns_records) | **get** /dnsrecords | Find multiple objects
*DeveloperAppSubscriptionsApi* | [**create_developer_app_subscription**](docs/apis/tags/DeveloperAppSubscriptionsApi.md#create_developer_app_subscription) | **post** /developerappsubscriptions | Create a new object
*DeveloperAppSubscriptionsApi* | [**find_developer_app_subscriptions**](docs/apis/tags/DeveloperAppSubscriptionsApi.md#find_developer_app_subscriptions) | **get** /developerappsubscriptions | Find multiple objects
*DeveloperAppSubscriptionsApi* | [**get_developer_app_subscription**](docs/apis/tags/DeveloperAppSubscriptionsApi.md#get_developer_app_subscription) | **get** /developerappsubscriptions/{id} | Get object by id
*DeveloperAppSubscriptionsApi* | [**patch_developer_app_subscription**](docs/apis/tags/DeveloperAppSubscriptionsApi.md#patch_developer_app_subscription) | **patch** /developerappsubscriptions/{id} | Patch object&#x27;s data
*DeveloperAppSubscriptionsApi* | [**remove_developer_app_subscription**](docs/apis/tags/DeveloperAppSubscriptionsApi.md#remove_developer_app_subscription) | **delete** /developerappsubscriptions/{id} | Delete object by id
*DeveloperAppsApi* | [**create_developer_app**](docs/apis/tags/DeveloperAppsApi.md#create_developer_app) | **post** /developerapps | Create a new object
*DeveloperAppsApi* | [**find_developer_apps**](docs/apis/tags/DeveloperAppsApi.md#find_developer_apps) | **get** /developerapps | Find multiple objects
*DeveloperAppsApi* | [**get_developer_app**](docs/apis/tags/DeveloperAppsApi.md#get_developer_app) | **get** /developerapps/{id} | Get object by id
*DeveloperAppsApi* | [**patch_developer_app**](docs/apis/tags/DeveloperAppsApi.md#patch_developer_app) | **patch** /developerapps/{id} | Patch object&#x27;s data
*DeveloperAppsApi* | [**remove_developer_app**](docs/apis/tags/DeveloperAppsApi.md#remove_developer_app) | **delete** /developerapps/{id} | Delete object by id
*DirectoriesApi* | [**create_directorie**](docs/apis/tags/DirectoriesApi.md#create_directorie) | **post** /directories | Create a new object
*DirectoriesApi* | [**find_directories**](docs/apis/tags/DirectoriesApi.md#find_directories) | **get** /directories | Find multiple objects
*DirectoriesApi* | [**get_directorie**](docs/apis/tags/DirectoriesApi.md#get_directorie) | **get** /directories/{id} | Get object by id
*DirectoriesApi* | [**patch_directorie**](docs/apis/tags/DirectoriesApi.md#patch_directorie) | **patch** /directories/{id} | Patch object&#x27;s data
*DirectoriesApi* | [**remove_directorie**](docs/apis/tags/DirectoriesApi.md#remove_directorie) | **delete** /directories/{id} | Delete object by id
*DomainsApi* | [**create_domain**](docs/apis/tags/DomainsApi.md#create_domain) | **post** /domains | Create a new object
*DomainsApi* | [**find_domains**](docs/apis/tags/DomainsApi.md#find_domains) | **get** /domains | Find multiple objects
*DomainsApi* | [**get_domain**](docs/apis/tags/DomainsApi.md#get_domain) | **get** /domains/{id} | Get object by id
*DomainsApi* | [**patch_domain**](docs/apis/tags/DomainsApi.md#patch_domain) | **patch** /domains/{id} | Patch object&#x27;s data
*DomainsApi* | [**remove_domain**](docs/apis/tags/DomainsApi.md#remove_domain) | **delete** /domains/{id} | Delete object by id
*FaxAccountApi* | [**create_fax_account**](docs/apis/tags/FaxAccountApi.md#create_fax_account) | **post** /faxaccounts | Create a new object
*FaxAccountApi* | [**find_fax_account**](docs/apis/tags/FaxAccountApi.md#find_fax_account) | **get** /faxaccounts | Find multiple objects
*FaxAccountApi* | [**get_fax_account**](docs/apis/tags/FaxAccountApi.md#get_fax_account) | **get** /faxaccounts/{id} | Get object by id
*FaxAccountApi* | [**patch_fax_account**](docs/apis/tags/FaxAccountApi.md#patch_fax_account) | **patch** /faxaccounts/{id} | Patch object&#x27;s data
*FaxAccountApi* | [**remove_fax_account**](docs/apis/tags/FaxAccountApi.md#remove_fax_account) | **delete** /faxaccounts/{id} | Delete object by id
*FaxesApi* | [**create_faxe**](docs/apis/tags/FaxesApi.md#create_faxe) | **post** /faxes | Create a new object
*FaxesApi* | [**find_faxes**](docs/apis/tags/FaxesApi.md#find_faxes) | **get** /faxes | Find multiple objects
*FaxesApi* | [**get_faxe**](docs/apis/tags/FaxesApi.md#get_faxe) | **get** /faxes/{id} | Get object by id
*FaxesApi* | [**remove_faxe**](docs/apis/tags/FaxesApi.md#remove_faxe) | **delete** /faxes/{id} | Delete object by id
*FindNumbersApi* | [**find_find_numbers**](docs/apis/tags/FindNumbersApi.md#find_find_numbers) | **get** /findnumbers | Find multiple objects
*FirewallApi* | [**create_firewall**](docs/apis/tags/FirewallApi.md#create_firewall) | **post** /firewall | Create a new object
*FirewallApi* | [**find_firewall**](docs/apis/tags/FirewallApi.md#find_firewall) | **get** /firewall | Find multiple objects
*FirewallApi* | [**get_firewall**](docs/apis/tags/FirewallApi.md#get_firewall) | **get** /firewall/{id} | Get object by id
*FirewallApi* | [**patch_firewall**](docs/apis/tags/FirewallApi.md#patch_firewall) | **patch** /firewall/{id} | Patch object&#x27;s data
*FirewallApi* | [**remove_firewall**](docs/apis/tags/FirewallApi.md#remove_firewall) | **delete** /firewall/{id} | Delete object by id
*GroupMembersApi* | [**create_group_member**](docs/apis/tags/GroupMembersApi.md#create_group_member) | **post** /groupmembers | Create a new object
*GroupMembersApi* | [**find_group_members**](docs/apis/tags/GroupMembersApi.md#find_group_members) | **get** /groupmembers | Find multiple objects
*GroupMembersApi* | [**get_group_member**](docs/apis/tags/GroupMembersApi.md#get_group_member) | **get** /groupmembers/{id} | Get object by id
*GroupMembersApi* | [**patch_group_member**](docs/apis/tags/GroupMembersApi.md#patch_group_member) | **patch** /groupmembers/{id} | Patch object&#x27;s data
*GroupMembersApi* | [**remove_group_member**](docs/apis/tags/GroupMembersApi.md#remove_group_member) | **delete** /groupmembers/{id} | Delete object by id
*GroupsApi* | [**create_group**](docs/apis/tags/GroupsApi.md#create_group) | **post** /groups | Create a new object
*GroupsApi* | [**find_groups**](docs/apis/tags/GroupsApi.md#find_groups) | **get** /groups | Find multiple objects
*GroupsApi* | [**get_group**](docs/apis/tags/GroupsApi.md#get_group) | **get** /groups/{id} | Get object by id
*GroupsApi* | [**patch_group**](docs/apis/tags/GroupsApi.md#patch_group) | **patch** /groups/{id} | Patch object&#x27;s data
*GroupsApi* | [**remove_group**](docs/apis/tags/GroupsApi.md#remove_group) | **delete** /groups/{id} | Delete object by id
*HolidaysApi* | [**create_holiday**](docs/apis/tags/HolidaysApi.md#create_holiday) | **post** /holidays | Create a new object
*HolidaysApi* | [**find_holidays**](docs/apis/tags/HolidaysApi.md#find_holidays) | **get** /holidays | Find multiple objects
*HolidaysApi* | [**get_holiday**](docs/apis/tags/HolidaysApi.md#get_holiday) | **get** /holidays/{id} | Get object by id
*HolidaysApi* | [**patch_holiday**](docs/apis/tags/HolidaysApi.md#patch_holiday) | **patch** /holidays/{id} | Patch object&#x27;s data
*HolidaysApi* | [**remove_holiday**](docs/apis/tags/HolidaysApi.md#remove_holiday) | **delete** /holidays/{id} | Delete object by id
*InfoApi* | [**find_info**](docs/apis/tags/InfoApi.md#find_info) | **get** /info | Get object
*InvoiceItemsApi* | [**find_invoice_items**](docs/apis/tags/InvoiceItemsApi.md#find_invoice_items) | **get** /invoiceitems | Find multiple objects
*InvoiceItemsApi* | [**get_invoice_item**](docs/apis/tags/InvoiceItemsApi.md#get_invoice_item) | **get** /invoiceitems/{id} | Get object by id
*InvoicesApi* | [**find_invoices**](docs/apis/tags/InvoicesApi.md#find_invoices) | **get** /invoices | Find multiple objects
*InvoicesApi* | [**get_invoice**](docs/apis/tags/InvoicesApi.md#get_invoice) | **get** /invoices/{id} | Get object by id
*LicensesApi* | [**create_license**](docs/apis/tags/LicensesApi.md#create_license) | **post** /licenses | Create a new object
*LicensesApi* | [**find_licenses**](docs/apis/tags/LicensesApi.md#find_licenses) | **get** /licenses | Find multiple objects
*LicensesApi* | [**get_license**](docs/apis/tags/LicensesApi.md#get_license) | **get** /licenses/{id} | Get object by id
*LicensesApi* | [**patch_license**](docs/apis/tags/LicensesApi.md#patch_license) | **patch** /licenses/{id} | Patch object&#x27;s data
*LicensesApi* | [**remove_license**](docs/apis/tags/LicensesApi.md#remove_license) | **delete** /licenses/{id} | Delete object by id
*MenuOptionsApi* | [**create_menu_option**](docs/apis/tags/MenuOptionsApi.md#create_menu_option) | **post** /menuoptions | Create a new object
*MenuOptionsApi* | [**find_menu_options**](docs/apis/tags/MenuOptionsApi.md#find_menu_options) | **get** /menuoptions | Find multiple objects
*MenuOptionsApi* | [**get_menu_option**](docs/apis/tags/MenuOptionsApi.md#get_menu_option) | **get** /menuoptions/{id} | Get object by id
*MenuOptionsApi* | [**patch_menu_option**](docs/apis/tags/MenuOptionsApi.md#patch_menu_option) | **patch** /menuoptions/{id} | Patch object&#x27;s data
*MenuOptionsApi* | [**remove_menu_option**](docs/apis/tags/MenuOptionsApi.md#remove_menu_option) | **delete** /menuoptions/{id} | Delete object by id
*MenusApi* | [**create_menu**](docs/apis/tags/MenusApi.md#create_menu) | **post** /menus | Create a new object
*MenusApi* | [**find_menus**](docs/apis/tags/MenusApi.md#find_menus) | **get** /menus | Find multiple objects
*MenusApi* | [**get_menu**](docs/apis/tags/MenusApi.md#get_menu) | **get** /menus/{id} | Get object by id
*MenusApi* | [**patch_menu**](docs/apis/tags/MenusApi.md#patch_menu) | **patch** /menus/{id} | Patch object&#x27;s data
*MenusApi* | [**remove_menu**](docs/apis/tags/MenusApi.md#remove_menu) | **delete** /menus/{id} | Delete object by id
*MessageBrandsApi* | [**create_message_brand**](docs/apis/tags/MessageBrandsApi.md#create_message_brand) | **post** /messagebrands | Create a new object
*MessageBrandsApi* | [**find_message_brands**](docs/apis/tags/MessageBrandsApi.md#find_message_brands) | **get** /messagebrands | Find multiple objects
*MessageBrandsApi* | [**get_message_brand**](docs/apis/tags/MessageBrandsApi.md#get_message_brand) | **get** /messagebrands/{id} | Get object by id
*MessageBrandsApi* | [**patch_message_brand**](docs/apis/tags/MessageBrandsApi.md#patch_message_brand) | **patch** /messagebrands/{id} | Patch object&#x27;s data
*MessageBrandsApi* | [**remove_message_brand**](docs/apis/tags/MessageBrandsApi.md#remove_message_brand) | **delete** /messagebrands/{id} | Delete object by id
*MessageCampaignsApi* | [**create_message_campaign**](docs/apis/tags/MessageCampaignsApi.md#create_message_campaign) | **post** /messagecampaigns | Create a new object
*MessageCampaignsApi* | [**find_message_campaigns**](docs/apis/tags/MessageCampaignsApi.md#find_message_campaigns) | **get** /messagecampaigns | Find multiple objects
*MessageCampaignsApi* | [**get_message_campaign**](docs/apis/tags/MessageCampaignsApi.md#get_message_campaign) | **get** /messagecampaigns/{id} | Get object by id
*MessageCampaignsApi* | [**patch_message_campaign**](docs/apis/tags/MessageCampaignsApi.md#patch_message_campaign) | **patch** /messagecampaigns/{id} | Patch object&#x27;s data
*MessageCampaignsApi* | [**remove_message_campaign**](docs/apis/tags/MessageCampaignsApi.md#remove_message_campaign) | **delete** /messagecampaigns/{id} | Delete object by id
*NumberPortsApi* | [**create_number_port**](docs/apis/tags/NumberPortsApi.md#create_number_port) | **post** /numberports | Create a new object
*NumberPortsApi* | [**find_number_ports**](docs/apis/tags/NumberPortsApi.md#find_number_ports) | **get** /numberports | Find multiple objects
*NumberPortsApi* | [**get_number_port**](docs/apis/tags/NumberPortsApi.md#get_number_port) | **get** /numberports/{id} | Get object by id
*NumberPortsApi* | [**patch_number_port**](docs/apis/tags/NumberPortsApi.md#patch_number_port) | **patch** /numberports/{id} | Patch object&#x27;s data
*NumbersApi* | [**find_numbers**](docs/apis/tags/NumbersApi.md#find_numbers) | **get** /numbers | Find multiple objects
*NumbersApi* | [**get_number**](docs/apis/tags/NumbersApi.md#get_number) | **get** /numbers/{id} | Get object by id
*NumbersApi* | [**patch_number**](docs/apis/tags/NumbersApi.md#patch_number) | **patch** /numbers/{id} | Patch object&#x27;s data
*OfficesApi* | [**create_office**](docs/apis/tags/OfficesApi.md#create_office) | **post** /offices | Create a new object
*OfficesApi* | [**find_offices**](docs/apis/tags/OfficesApi.md#find_offices) | **get** /offices | Find multiple objects
*OfficesApi* | [**get_office**](docs/apis/tags/OfficesApi.md#get_office) | **get** /offices/{id} | Get object by id
*OfficesApi* | [**patch_office**](docs/apis/tags/OfficesApi.md#patch_office) | **patch** /offices/{id} | Patch object&#x27;s data
*OfficesApi* | [**remove_office**](docs/apis/tags/OfficesApi.md#remove_office) | **delete** /offices/{id} | Delete object by id
*PhoneInboundRuleActionsApi* | [**create_phone_inbound_rule_action**](docs/apis/tags/PhoneInboundRuleActionsApi.md#create_phone_inbound_rule_action) | **post** /phoneinboundruleactions | Create a new object
*PhoneInboundRuleActionsApi* | [**find_phone_inbound_rule_actions**](docs/apis/tags/PhoneInboundRuleActionsApi.md#find_phone_inbound_rule_actions) | **get** /phoneinboundruleactions | Find multiple objects
*PhoneInboundRuleActionsApi* | [**get_phone_inbound_rule_action**](docs/apis/tags/PhoneInboundRuleActionsApi.md#get_phone_inbound_rule_action) | **get** /phoneinboundruleactions/{id} | Get object by id
*PhoneInboundRuleActionsApi* | [**patch_phone_inbound_rule_action**](docs/apis/tags/PhoneInboundRuleActionsApi.md#patch_phone_inbound_rule_action) | **patch** /phoneinboundruleactions/{id} | Patch object&#x27;s data
*PhoneInboundRuleActionsApi* | [**remove_phone_inbound_rule_action**](docs/apis/tags/PhoneInboundRuleActionsApi.md#remove_phone_inbound_rule_action) | **delete** /phoneinboundruleactions/{id} | Delete object by id
*PhoneInboundRulesApi* | [**create_phone_inbound_rule**](docs/apis/tags/PhoneInboundRulesApi.md#create_phone_inbound_rule) | **post** /phoneinboundrules | Create a new object
*PhoneInboundRulesApi* | [**find_phone_inbound_rules**](docs/apis/tags/PhoneInboundRulesApi.md#find_phone_inbound_rules) | **get** /phoneinboundrules | Find multiple objects
*PhoneInboundRulesApi* | [**get_phone_inbound_rule**](docs/apis/tags/PhoneInboundRulesApi.md#get_phone_inbound_rule) | **get** /phoneinboundrules/{id} | Get object by id
*PhoneInboundRulesApi* | [**patch_phone_inbound_rule**](docs/apis/tags/PhoneInboundRulesApi.md#patch_phone_inbound_rule) | **patch** /phoneinboundrules/{id} | Patch object&#x27;s data
*PhoneInboundRulesApi* | [**remove_phone_inbound_rule**](docs/apis/tags/PhoneInboundRulesApi.md#remove_phone_inbound_rule) | **delete** /phoneinboundrules/{id} | Delete object by id
*PhoneOutboundRuleActionsApi* | [**create_phone_outbound_rule_action**](docs/apis/tags/PhoneOutboundRuleActionsApi.md#create_phone_outbound_rule_action) | **post** /phoneoutboundruleactions | Create a new object
*PhoneOutboundRuleActionsApi* | [**find_phone_outbound_rule_actions**](docs/apis/tags/PhoneOutboundRuleActionsApi.md#find_phone_outbound_rule_actions) | **get** /phoneoutboundruleactions | Find multiple objects
*PhoneOutboundRuleActionsApi* | [**get_phone_outbound_rule_action**](docs/apis/tags/PhoneOutboundRuleActionsApi.md#get_phone_outbound_rule_action) | **get** /phoneoutboundruleactions/{id} | Get object by id
*PhoneOutboundRuleActionsApi* | [**patch_phone_outbound_rule_action**](docs/apis/tags/PhoneOutboundRuleActionsApi.md#patch_phone_outbound_rule_action) | **patch** /phoneoutboundruleactions/{id} | Patch object&#x27;s data
*PhoneOutboundRuleActionsApi* | [**remove_phone_outbound_rule_action**](docs/apis/tags/PhoneOutboundRuleActionsApi.md#remove_phone_outbound_rule_action) | **delete** /phoneoutboundruleactions/{id} | Delete object by id
*PhoneOutboundRulesApi* | [**create_phone_outbound_rule**](docs/apis/tags/PhoneOutboundRulesApi.md#create_phone_outbound_rule) | **post** /phoneoutboundrules | Create a new object
*PhoneOutboundRulesApi* | [**find_phone_outbound_rules**](docs/apis/tags/PhoneOutboundRulesApi.md#find_phone_outbound_rules) | **get** /phoneoutboundrules | Find multiple objects
*PhoneOutboundRulesApi* | [**get_phone_outbound_rule**](docs/apis/tags/PhoneOutboundRulesApi.md#get_phone_outbound_rule) | **get** /phoneoutboundrules/{id} | Get object by id
*PhoneOutboundRulesApi* | [**patch_phone_outbound_rule**](docs/apis/tags/PhoneOutboundRulesApi.md#patch_phone_outbound_rule) | **patch** /phoneoutboundrules/{id} | Patch object&#x27;s data
*PhoneOutboundRulesApi* | [**remove_phone_outbound_rule**](docs/apis/tags/PhoneOutboundRulesApi.md#remove_phone_outbound_rule) | **delete** /phoneoutboundrules/{id} | Delete object by id
*RateCentersApi* | [**find_rate_centers**](docs/apis/tags/RateCentersApi.md#find_rate_centers) | **get** /ratecenters | Find multiple objects
*RateCentersApi* | [**get_rate_center**](docs/apis/tags/RateCentersApi.md#get_rate_center) | **get** /ratecenters/{id} | Get object by id
*ServersApi* | [**create_server**](docs/apis/tags/ServersApi.md#create_server) | **post** /servers | Create a new object
*ServersApi* | [**find_servers**](docs/apis/tags/ServersApi.md#find_servers) | **get** /servers | Find multiple objects
*ServersApi* | [**get_server**](docs/apis/tags/ServersApi.md#get_server) | **get** /servers/{id} | Get object by id
*ServersApi* | [**patch_server**](docs/apis/tags/ServersApi.md#patch_server) | **patch** /servers/{id} | Patch object&#x27;s data
*ServersApi* | [**remove_server**](docs/apis/tags/ServersApi.md#remove_server) | **delete** /servers/{id} | Delete object by id
*TimeSchedulesApi* | [**create_time_schedule**](docs/apis/tags/TimeSchedulesApi.md#create_time_schedule) | **post** /timeschedules | Create a new object
*TimeSchedulesApi* | [**find_time_schedules**](docs/apis/tags/TimeSchedulesApi.md#find_time_schedules) | **get** /timeschedules | Find multiple objects
*TimeSchedulesApi* | [**get_time_schedule**](docs/apis/tags/TimeSchedulesApi.md#get_time_schedule) | **get** /timeschedules/{id} | Get object by id
*TimeSchedulesApi* | [**patch_time_schedule**](docs/apis/tags/TimeSchedulesApi.md#patch_time_schedule) | **patch** /timeschedules/{id} | Patch object&#x27;s data
*TimeSchedulesApi* | [**remove_time_schedule**](docs/apis/tags/TimeSchedulesApi.md#remove_time_schedule) | **delete** /timeschedules/{id} | Delete object by id
*UserTokensApi* | [**create_user_token**](docs/apis/tags/UserTokensApi.md#create_user_token) | **post** /usertokens | Create a new object
*UserTokensApi* | [**find_user_tokens**](docs/apis/tags/UserTokensApi.md#find_user_tokens) | **get** /usertokens | Find multiple objects
*UserTokensApi* | [**get_user_token**](docs/apis/tags/UserTokensApi.md#get_user_token) | **get** /usertokens/{id} | Get object by id
*UserTokensApi* | [**patch_user_token**](docs/apis/tags/UserTokensApi.md#patch_user_token) | **patch** /usertokens/{id} | Patch object&#x27;s data
*UserTokensApi* | [**remove_user_token**](docs/apis/tags/UserTokensApi.md#remove_user_token) | **delete** /usertokens/{id} | Delete object by id
*UsersApi* | [**create_user**](docs/apis/tags/UsersApi.md#create_user) | **post** /users | Create a new object
*UsersApi* | [**find_users**](docs/apis/tags/UsersApi.md#find_users) | **get** /users | Find multiple objects
*UsersApi* | [**get_user**](docs/apis/tags/UsersApi.md#get_user) | **get** /users/{id} | Get object by id
*UsersApi* | [**patch_user**](docs/apis/tags/UsersApi.md#patch_user) | **patch** /users/{id} | Patch object&#x27;s data
*UsersApi* | [**remove_user**](docs/apis/tags/UsersApi.md#remove_user) | **delete** /users/{id} | Delete object by id
*VirtualExtensionsApi* | [**create_virtual_extension**](docs/apis/tags/VirtualExtensionsApi.md#create_virtual_extension) | **post** /virtualextensions | Create a new object
*VirtualExtensionsApi* | [**find_virtual_extensions**](docs/apis/tags/VirtualExtensionsApi.md#find_virtual_extensions) | **get** /virtualextensions | Find multiple objects
*VirtualExtensionsApi* | [**get_virtual_extension**](docs/apis/tags/VirtualExtensionsApi.md#get_virtual_extension) | **get** /virtualextensions/{id} | Get object by id
*VirtualExtensionsApi* | [**patch_virtual_extension**](docs/apis/tags/VirtualExtensionsApi.md#patch_virtual_extension) | **patch** /virtualextensions/{id} | Patch object&#x27;s data
*VirtualExtensionsApi* | [**remove_virtual_extension**](docs/apis/tags/VirtualExtensionsApi.md#remove_virtual_extension) | **delete** /virtualextensions/{id} | Delete object by id
*VoicemailApi* | [**find_voicemail**](docs/apis/tags/VoicemailApi.md#find_voicemail) | **get** /voicemail | Find multiple objects
*VoicemailApi* | [**get_voicemail**](docs/apis/tags/VoicemailApi.md#get_voicemail) | **get** /voicemail/{id} | Get object by id

## Documentation For Models

 - [Acceptedsenders](docs/models/Acceptedsenders.md)
 - [Announcements](docs/models/Announcements.md)
 - [Authentication](docs/models/Authentication.md)
 - [Callqueueagents](docs/models/Callqueueagents.md)
 - [Callqueues](docs/models/Callqueues.md)
 - [Chatrooms](docs/models/Chatrooms.md)
 - [Clients](docs/models/Clients.md)
 - [Conferencerooms](docs/models/Conferencerooms.md)
 - [Contacts](docs/models/Contacts.md)
 - [Conversationmessages](docs/models/Conversationmessages.md)
 - [Conversations](docs/models/Conversations.md)
 - [Customers](docs/models/Customers.md)
 - [Developerapps](docs/models/Developerapps.md)
 - [Developerappsubscriptions](docs/models/Developerappsubscriptions.md)
 - [Directories](docs/models/Directories.md)
 - [Domains](docs/models/Domains.md)
 - [Faxaccounts](docs/models/Faxaccounts.md)
 - [Faxes](docs/models/Faxes.md)
 - [Find](docs/models/Find.md)
 - [Firewall](docs/models/Firewall.md)
 - [Groupmembers](docs/models/Groupmembers.md)
 - [Groups](docs/models/Groups.md)
 - [Holidays](docs/models/Holidays.md)
 - [Invoiceitems](docs/models/Invoiceitems.md)
 - [Invoices](docs/models/Invoices.md)
 - [Licenses](docs/models/Licenses.md)
 - [Menuoptions](docs/models/Menuoptions.md)
 - [Menus](docs/models/Menus.md)
 - [Messagebrands](docs/models/Messagebrands.md)
 - [Messagecampaigns](docs/models/Messagecampaigns.md)
 - [Numberports](docs/models/Numberports.md)
 - [Numbers](docs/models/Numbers.md)
 - [Offices](docs/models/Offices.md)
 - [Phoneinboundruleactions](docs/models/Phoneinboundruleactions.md)
 - [Phoneinboundrules](docs/models/Phoneinboundrules.md)
 - [Phoneoutboundruleactions](docs/models/Phoneoutboundruleactions.md)
 - [Phoneoutboundrules](docs/models/Phoneoutboundrules.md)
 - [Ratecenters](docs/models/Ratecenters.md)
 - [ResponseDate](docs/models/ResponseDate.md)
 - [ResponseError](docs/models/ResponseError.md)
 - [ResponseUsers](docs/models/ResponseUsers.md)
 - [Servers](docs/models/Servers.md)
 - [Timeschedules](docs/models/Timeschedules.md)
 - [Users](docs/models/Users.md)
 - [Usertokens](docs/models/Usertokens.md)
 - [Virtualextensions](docs/models/Virtualextensions.md)

## Documentation For Authorization

Authentication schemes defined for the API:
<a id="jwt"></a>
### jwt

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in circuitid_python.apis and circuitid_python.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from circuitid_python.rest.default_api import DefaultApi`
- `from circuitid_python.CircuitIDModel.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import circuitid_python
from circuitid_python.apis import *
from circuitid_python.models import *
```
