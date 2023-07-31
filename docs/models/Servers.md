# circuitid_python.models.servers.Servers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**port** | decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 5060value must be a 32 bit integer
**host** | str,  | str,  |  | 
**name** | str,  | str,  |  | 
**type** | str,  | str,  |  | must be one of ["sip", "skype", ] 
**callerId** | str,  | str,  |  | [optional] 
**inboundSipTrunkingOrder** | str,  | str,  | ObjectId (unique 12 bytes ID) | [optional] 
**outboundSipTrunkingOrder** | str,  | str,  | ObjectId (unique 12 bytes ID) | [optional] 
**noInstantRingBack** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] value must be a 32 bit integer
**bypassMedia** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] if omitted the server will use the default value of 0value must be a 32 bit integer
**disableRTPAutoAdjust** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] if omitted the server will use the default value of 0value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

