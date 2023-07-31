# circuitid_python.models.customers_create_or_patch.CustomersCreateOrPatch

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**defaultBillMethod** | str,  | str,  |  | must be one of ["credit", "paymentmethod", ] if omitted the server will use the default value of "credit"
**name** | str,  | str,  |  | 
**websiteUrl** | str,  | str,  |  | [optional] 
**logo** | str,  | str,  |  | [optional] 
**credit** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0value must be a 32 bit integer
**adminUserId** | str,  | str,  | ObjectId (unique 12 bytes ID) | [optional] 
**billingUserId** | str,  | str,  | ObjectId (unique 12 bytes ID) | [optional] 
**callRecordingUserId** | str,  | str,  | ObjectId (unique 12 bytes ID) | [optional] 
**supportUserId** | str,  | str,  | ObjectId (unique 12 bytes ID) | [optional] 
**automaticRefillAmount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0value must be a 32 bit integer
**lowBalanceAlertAmount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0value must be a 32 bit integer
**internationalCalling** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] if omitted the server will use the default value of 0value must be a 32 bit integer
**createdByIP** | str,  | str,  |  | [optional] 
**mediaBypass** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] if omitted the server will use the default value of 0value must be a 32 bit integer
**accountLock** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] if omitted the server will use the default value of 1value must be a 32 bit integer
**callRecording** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] if omitted the server will use the default value of 0value must be a 32 bit integer
**cdrRetention** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 12value must be a 32 bit integer
**cnamLookUps** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] if omitted the server will use the default value of 0value must be a 32 bit integer
**holdMusic** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] if omitted the server will use the default value of 0value must be a 32 bit integer
**transcribeCalls** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] value must be a 32 bit integer
**maxOutboundCallRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 1value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

