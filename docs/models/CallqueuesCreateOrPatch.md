# circuitid_python.models.callqueues_create_or_patch.CallqueuesCreateOrPatch

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**abandonedResumeAllowed** | bool,  | BoolClass,  |  | if omitted the server will use the default value of True
**maxNoAnswer** | decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1000000value must be a 32 bit integer
**callerResumeTimeout** | decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 3600value must be a 32 bit integer
**maxWaitTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 300value must be a 32 bit integer
**moh** | str,  | str,  |  | if omitted the server will use the default value of "deafult"
**tierRulesApply** | bool,  | BoolClass,  |  | if omitted the server will use the default value of False
**maxWaitTimeNoAgentTimeReached** | decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 5value must be a 32 bit integer
**tierRuleNoAgentNoWait** | bool,  | BoolClass,  |  | if omitted the server will use the default value of True
**timeBasedScore** | str,  | str,  |  | must be one of ["queue", "system", ] if omitted the server will use the default value of "queue"
**maxWaitTimeNoAgent** | decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 300value must be a 32 bit integer
**name** | str,  | str,  |  | 
**strategy** | str,  | str,  |  | must be one of ["ring-all", "longest-idle-agent", "round-robin", "top-down", "agent-with-least-talk-time", "agent-with-fewest-calls", "sequentially-by-agent-order", "random", ] 
**tierRuleWaitMultiplyLevel** | bool,  | BoolClass,  |  | if omitted the server will use the default value of True
**announcePosition** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**noAnswerDelayTimeout** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 60value must be a 32 bit integer
**rejectTimeout** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 60value must be a 32 bit integer
**busyTimeout** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 60value must be a 32 bit integer
**wrapUpTimeout** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 10value must be a 32 bit integer
**tierRuleWaitSecond** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 300value must be a 32 bit integer
**discardAbandonedAfter** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 14400value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

