# circuitid_python.models.messagecampaigns.Messagecampaigns

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**brandId** | str,  | str,  |  | 
**name** | str,  | str,  |  | 
**order** | str,  | str,  | ObjectId (unique 12 bytes ID) | 
**campaignId** | str,  | str,  |  | [optional] 
**subscriberOptin** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] value must be a 32 bit integer
**subscriberOptout** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] value must be a 32 bit integer
**subscriberHelp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] value must be a 32 bit integer
**numberPool** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] value must be a 32 bit integer
**directLending** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] value must be a 32 bit integer
**embeddedLink** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] value must be a 32 bit integer
**embeddedPhone** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] value must be a 32 bit integer
**affiliateMarketing** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] value must be a 32 bit integer
**ageGated** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] value must be a 32 bit integer
**[mnos](#mnos)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**referenceId** | str,  | str,  |  | [optional] 
**useCase** | str,  | str,  |  | [optional] 
**[subUseCases](#subUseCases)** | list, tuple,  | tuple,  |  | [optional] 
**sample1** | str,  | str,  |  | [optional] 
**sample2** | str,  | str,  |  | [optional] 
**sample3** | str,  | str,  |  | [optional] 
**sample4** | str,  | str,  |  | [optional] 
**sample5** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mnos

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# subUseCases

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

