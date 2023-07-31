# circuitid_python.models.developerapps_create_or_patch.DeveloperappsCreateOrPatch

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**integrationType** | str,  | str,  |  | must be one of ["webhook", "client", ] 
**visibility** | str,  | str,  |  | must be one of ["private", "public", ] 
**name** | str,  | str,  |  | 
**[services](#services)** | list, tuple,  | tuple,  |  | 
**type** | str,  | str,  |  | must be one of ["events", ] 
**user** | str,  | str,  | ObjectId (unique 12 bytes ID) | 
**description** | str,  | str,  |  | [optional] 
**requireId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] if omitted the server will use the default value of 0value must be a 32 bit integer
**isFree** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] if omitted the server will use the default value of 1value must be a 32 bit integer
**feeDescription** | str,  | str,  |  | [optional] 
**[events](#events)** | list, tuple,  | tuple,  |  | [optional] 
**webhookUrl** | str,  | str,  |  | [optional] 
**termsOfServiceUrl** | str,  | str,  |  | [optional] 
**privacyPolicyUrl** | str,  | str,  |  | [optional] 
**[permissions](#permissions)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**webhookAuthType** | str,  | str,  |  | [optional] must be one of ["header", "usernameAndPassword", ] 
**webhookUsername** | str,  | str,  |  | [optional] 
**webhookPassword** | str,  | str,  |  | [optional] 
**webhookTokenName** | str,  | str,  |  | [optional] 
**webhookToken** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# services

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["calendarevents", "callqueues", "cdrs", "chatmessages", "contacts", "conversationmessages", "faxes", "firewall", "users", "voicemail", ] 

# events

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["create", "patch", "removed", ] 

# permissions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

