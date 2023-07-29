# circuitid_python.models.menus.Menus

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**maxExtensionLength** | decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 4value must be a 32 bit integer
**name** | str,  | str,  |  | 
**greetingType** | str,  | str,  |  | must be one of ["tts", "mp3", ] 
**speechRecognition** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] if omitted the server will use the default value of 0value must be a 32 bit integer
**directory** | str,  | str,  | ObjectId (unique 12 bytes ID) | [optional] 
**greetingTTS** | str,  | str,  |  | [optional] 
**menuVoice** | str,  | str,  |  | [optional] 
**exitSound** | str,  | str,  |  | [optional] must be one of ["default", "mp3", ] if omitted the server will use the default value of "default"
**transferAnnouncement** | str,  | str,  |  | [optional] must be one of ["default", "mp3", "none", ] if omitted the server will use the default value of "default"
**maxFailures** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 3value must be a 32 bit integer
**maxTimeouts** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 3value must be a 32 bit integer
**timeout** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 10value must be a 32 bit integer
**touchToneTerminators** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [1, 0, ] if omitted the server will use the default value of 1value must be a 32 bit integer
**timeschedule** | str,  | str,  | ObjectId (unique 12 bytes ID) | [optional] 
**destinationType** | str,  | str,  |  | [optional] must be one of ["announcements", "directories", "park", "numbers", "menus", "users", "servers", "inboundrules", "callqueues", "faxaccounts", "callforwarding", "hangup", "phoneinboundrules", "voicemailaccounts", ] 
**destination** | str,  | str,  | ObjectId (unique 12 bytes ID) | [optional] 
**ref** | str,  | str,  |  | [optional] 
**callForwardingDestination** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

