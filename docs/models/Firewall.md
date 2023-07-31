# circuitid_python.models.firewall.Firewall

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**param** | str,  | str,  |  | 
**name** | str,  | str,  |  | 
**priority** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer
**type** | str,  | str,  |  | must be one of ["allow", "deny", ] 
**target** | str,  | str,  |  | must be one of ["numbers", "ipaddresses", "sms", ] 
**description** | str,  | str,  |  | [optional] 
**direction** | str,  | str,  |  | [optional] must be one of ["inbound", "outbound", "both", ] 
**hits** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**status** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [0, 1, ] if omitted the server will use the default value of 1value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

