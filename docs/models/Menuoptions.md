# circuitid_python.models.menuoptions.Menuoptions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | 
**destinationType** | str,  | str,  |  | must be one of ["announcements", "directories", "park", "numbers", "menus", "users", "servers", "inboundrules", "callqueues", "faxaccounts", "callforwarding", "hangup", "phoneinboundrules", "voicemailaccounts", ] 
**menus** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**digit** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer
**destination** | str,  | str,  | ObjectId (unique 12 bytes ID) | [optional] 
**ref** | str,  | str,  |  | [optional] 
**callForwardingDestination** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

