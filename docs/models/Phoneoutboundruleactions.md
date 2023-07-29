# circuitid_python.models.phoneoutboundruleactions.Phoneoutboundruleactions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**route** | str,  | str,  |  | must be one of ["default", "group", "pstn", ] if omitted the server will use the default value of "default"
**name** | str,  | str,  |  | 
**phoneoutboundrule** | str,  | str,  | ObjectId (unique 12 bytes ID) | 
**priority** | decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer
**group** | str,  | str,  | ObjectId (unique 12 bytes ID) | [optional] 
**status** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] if omitted the server will use the default value of 1value must be a 32 bit integer
**startingChars** | str,  | str,  |  | [optional] 
**contains** | str,  | str,  |  | [optional] 
**lengthType** | None, str,  | NoneClass, str,  |  | [optional] must be one of ["atleast", "exactly", "range", "any", ] 
**length** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**appendChars** | str,  | str,  |  | [optional] 
**prependChars** | str,  | str,  |  | [optional] 
**rangeStart** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**rangeEnd** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**removeStartingChars** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**removeEndingChars** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**routingType** | str,  | str,  |  | [optional] must be one of ["priority", "lb", "simultaneous", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

