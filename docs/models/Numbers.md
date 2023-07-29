# circuitid_python.models.numbers.Numbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**provider** | str,  | str,  | ObjectId (unique 12 bytes ID) | 
**countryCode** | str,  | str,  |  | 
**name** | str,  | str,  |  | 
**destinationType** | str,  | str,  |  | must be one of ["announcements", "directories", "park", "numbers", "menus", "users", "servers", "inboundrules", "callqueues", "faxaccounts", "callforwarding", "hangup", "phoneinboundrules", "voicemailaccounts", ] if omitted the server will use the default value of "park"
**inUse** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] if omitted the server will use the default value of 1value must be a 32 bit integer
**amount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**perMinuteRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**originalProvider** | str,  | str,  | ObjectId (unique 12 bytes ID) | [optional] 
**providerOrderId** | str,  | str,  |  | [optional] 
**fax** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] if omitted the server will use the default value of 0value must be a 32 bit integer
**voice** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] if omitted the server will use the default value of 0value must be a 32 bit integer
**status** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] if omitted the server will use the default value of 1value must be a 32 bit integer
**sms** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] if omitted the server will use the default value of 0value must be a 32 bit integer
**mms** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] if omitted the server will use the default value of 0value must be a 32 bit integer
**changeRegionOrderId** | str,  | str,  |  | [optional] 
**changeRegionOrderDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**directoryListing** | str,  | str,  | ObjectId (unique 12 bytes ID) | [optional] 
**directoryListingOrderId** | str,  | str,  |  | [optional] 
**directoryListingOrderDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**callerName** | str,  | str,  |  | [optional] 
**callerNameOrderId** | str,  | str,  |  | [optional] 
**callerNameOrderDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**e911** | str,  | str,  | ObjectId (unique 12 bytes ID) | [optional] 
**e911OrderId** | str,  | str,  |  | [optional] 
**e911OrderDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**messageCampaign** | str,  | str,  | ObjectId (unique 12 bytes ID) | [optional] 
**messageClass** | str,  | str,  |  | [optional] must be one of ["P2P", "A2PLC", "A2P8XX", ] 
**messageType** | str,  | str,  |  | [optional] must be one of ["SMS", "MMS", "SMSMMS", "SMS_ALT", "MMS_ALT", "SMSMMS_ALT", ] 
**messageCampaignOrderId** | str,  | str,  |  | [optional] 
**messageCampaignOrderDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**e911Supported** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] if omitted the server will use the default value of 0value must be a 32 bit integer
**callerNameSupported** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] if omitted the server will use the default value of 0value must be a 32 bit integer
**directoryListingSupported** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] if omitted the server will use the default value of 0value must be a 32 bit integer
**messagingSupported** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] if omitted the server will use the default value of 0value must be a 32 bit integer
**destination** | str,  | str,  | ObjectId (unique 12 bytes ID) | [optional] 
**ref** | str,  | str,  |  | [optional] 
**callForwardingDestination** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

