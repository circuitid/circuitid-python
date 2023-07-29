# circuitid_python.models.invoices.Invoices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dueAt** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**amount** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer
**subtotal** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer
**status** | str,  | str,  |  | must be one of ["open", "closed", "collection", "onHold", "error", ] if omitted the server will use the default value of "open"
**tax** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**setup** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**discount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**closedAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**error** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

