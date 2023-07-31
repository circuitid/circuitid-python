# circuitid_python.models.clients_create_or_patch.ClientsCreateOrPatch

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | 
**user** | str,  | str,  | ObjectId (unique 12 bytes ID) | 
**mac** | str,  | str,  |  | 
**httpUserAgent** | str,  | str,  |  | [optional] 
**manufacture** | str,  | str,  |  | [optional] must be one of ["cisco", "grandstream", "polycom", ] 
**status** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] if omitted the server will use the default value of 1value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

