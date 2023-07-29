# circuitid_python.models.faxes.Faxes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**number** | str,  | str,  | ObjectId (unique 12 bytes ID) | 
**callerIdNumber** | str,  | str,  |  | 
**callerDestination** | str,  | str,  |  | 
**faxAccount** | str,  | str,  | ObjectId (unique 12 bytes ID) | 
**type** | str,  | str,  |  | must be one of ["send", "receive", ] 
**status** | str,  | str,  |  | must be one of ["failed", "success", "processing", ] if omitted the server will use the default value of "processing"
**pages** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0value must be a 32 bit integer
**statusCode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**transferedPages** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0value must be a 32 bit integer
**error** | str,  | str,  |  | [optional] 
**order** | str,  | str,  | ObjectId (unique 12 bytes ID) | [optional] 
**file** | str,  | str,  | ObjectId (unique 12 bytes ID) | [optional] 
**contact** | str,  | str,  | ObjectId (unique 12 bytes ID) | [optional] 
**retries** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0value must be a 32 bit integer
**invoice** | str,  | str,  | ObjectId (unique 12 bytes ID) | [optional] 
**senderEmail** | str,  | str,  |  | [optional] 
**senderName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

