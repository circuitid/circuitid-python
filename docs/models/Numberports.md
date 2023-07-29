# circuitid_python.models.numberports.Numberports

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**accountPhoneNumber** | str,  | str,  |  | 
**typeOfService** | str,  | str,  |  | must be one of ["business", "residence", ] 
**name** | str,  | str,  |  | 
**destinationType** | str,  | str,  |  | must be one of ["announcements", "directories", "park", "numbers", "menus", "users", "servers", "inboundrules", "callqueues", "faxaccounts", "callforwarding", "hangup", "phoneinboundrules", "voicemailaccounts", ] 
**invoice** | str,  | str,  | ObjectId (unique 12 bytes ID) | 
**office** | str,  | str,  | ObjectId (unique 12 bytes ID) | 
**accountNumber** | str,  | str,  |  | 
**type** | str,  | str,  |  | must be one of ["port in", "port out", ] 
**authorizedPerson** | str,  | str,  |  | 
**desiredDueDate** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**status** | str,  | str,  |  | must be one of ["processing", "failed", "error", "completed", ] if omitted the server will use the default value of "processing"
**e911** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] if omitted the server will use the default value of 0value must be a 32 bit integer
**destination** | str,  | str,  | ObjectId (unique 12 bytes ID) | [optional] 
**ref** | str,  | str,  |  | [optional] 
**callForwardingDestination** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

