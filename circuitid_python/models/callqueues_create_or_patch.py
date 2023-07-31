# coding: utf-8

"""
    Circuit ID REST API

    # Introduction Circuit ID&reg; is an innovative cloud communications platform that redefines your connectivity experience. Our cutting-edge AI-powered solution seamlessly integrates calling, meetings, messaging, voicemail, fax, SIP Trunking, mobile broadband, and mobile phone services, accessible wherever you and your devices go.                  Whether you are a beginner getting started with our API or an experienced developer looking for advanced features, this documentation site will serve as your comprehensive guide.   We are excited to have you on board and are confident that this documentation site will empower you to leverage the full potential of our REST API.  If you have any questions or require further assistance, please don't hesitate to reach out to our support team.                  Happy coding!  # noqa: E501

    The version of the OpenAPI document: 0.47.21
    Contact: support@circuitid.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from circuitid_python import schemas  # noqa: F401


class CallqueuesCreateOrPatch(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "abandonedResumeAllowed",
            "maxNoAnswer",
            "callerResumeTimeout",
            "maxWaitTime",
            "moh",
            "tierRulesApply",
            "maxWaitTimeNoAgentTimeReached",
            "tierRuleNoAgentNoWait",
            "timeBasedScore",
            "maxWaitTimeNoAgent",
            "name",
            "strategy",
            "tierRuleWaitMultiplyLevel",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            
            
            class strategy(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ring-all": "RINGALL",
                        "longest-idle-agent": "LONGESTIDLEAGENT",
                        "round-robin": "ROUNDROBIN",
                        "top-down": "TOPDOWN",
                        "agent-with-least-talk-time": "AGENTWITHLEASTTALKTIME",
                        "agent-with-fewest-calls": "AGENTWITHFEWESTCALLS",
                        "sequentially-by-agent-order": "SEQUENTIALLYBYAGENTORDER",
                        "random": "RANDOM",
                    }
                
                @schemas.classproperty
                def RINGALL(cls):
                    return cls("ring-all")
                
                @schemas.classproperty
                def LONGESTIDLEAGENT(cls):
                    return cls("longest-idle-agent")
                
                @schemas.classproperty
                def ROUNDROBIN(cls):
                    return cls("round-robin")
                
                @schemas.classproperty
                def TOPDOWN(cls):
                    return cls("top-down")
                
                @schemas.classproperty
                def AGENTWITHLEASTTALKTIME(cls):
                    return cls("agent-with-least-talk-time")
                
                @schemas.classproperty
                def AGENTWITHFEWESTCALLS(cls):
                    return cls("agent-with-fewest-calls")
                
                @schemas.classproperty
                def SEQUENTIALLYBYAGENTORDER(cls):
                    return cls("sequentially-by-agent-order")
                
                @schemas.classproperty
                def RANDOM(cls):
                    return cls("random")
            
            
            class moh(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 255
            callerResumeTimeout = schemas.Int32Schema
            maxWaitTime = schemas.Int32Schema
            maxWaitTimeNoAgent = schemas.Int32Schema
            maxNoAnswer = schemas.Int32Schema
            
            
            class timeBasedScore(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "queue": "QUEUE",
                        "system": "SYSTEM",
                    }
                
                @schemas.classproperty
                def QUEUE(cls):
                    return cls("queue")
                
                @schemas.classproperty
                def SYSTEM(cls):
                    return cls("system")
            tierRulesApply = schemas.BoolSchema
            tierRuleNoAgentNoWait = schemas.BoolSchema
            tierRuleWaitMultiplyLevel = schemas.BoolSchema
            abandonedResumeAllowed = schemas.BoolSchema
            maxWaitTimeNoAgentTimeReached = schemas.Int32Schema
            announcePosition = schemas.Int32Schema
            noAnswerDelayTimeout = schemas.Int32Schema
            rejectTimeout = schemas.Int32Schema
            busyTimeout = schemas.Int32Schema
            wrapUpTimeout = schemas.Int32Schema
            tierRuleWaitSecond = schemas.Int32Schema
            discardAbandonedAfter = schemas.Int32Schema
            __annotations__ = {
                "name": name,
                "strategy": strategy,
                "moh": moh,
                "callerResumeTimeout": callerResumeTimeout,
                "maxWaitTime": maxWaitTime,
                "maxWaitTimeNoAgent": maxWaitTimeNoAgent,
                "maxNoAnswer": maxNoAnswer,
                "timeBasedScore": timeBasedScore,
                "tierRulesApply": tierRulesApply,
                "tierRuleNoAgentNoWait": tierRuleNoAgentNoWait,
                "tierRuleWaitMultiplyLevel": tierRuleWaitMultiplyLevel,
                "abandonedResumeAllowed": abandonedResumeAllowed,
                "maxWaitTimeNoAgentTimeReached": maxWaitTimeNoAgentTimeReached,
                "announcePosition": announcePosition,
                "noAnswerDelayTimeout": noAnswerDelayTimeout,
                "rejectTimeout": rejectTimeout,
                "busyTimeout": busyTimeout,
                "wrapUpTimeout": wrapUpTimeout,
                "tierRuleWaitSecond": tierRuleWaitSecond,
                "discardAbandonedAfter": discardAbandonedAfter,
            }
        min_properties = 1
    
    abandonedResumeAllowed: MetaOapg.properties.abandonedResumeAllowed
    maxNoAnswer: MetaOapg.properties.maxNoAnswer
    callerResumeTimeout: MetaOapg.properties.callerResumeTimeout
    maxWaitTime: MetaOapg.properties.maxWaitTime
    moh: MetaOapg.properties.moh
    tierRulesApply: MetaOapg.properties.tierRulesApply
    maxWaitTimeNoAgentTimeReached: MetaOapg.properties.maxWaitTimeNoAgentTimeReached
    tierRuleNoAgentNoWait: MetaOapg.properties.tierRuleNoAgentNoWait
    timeBasedScore: MetaOapg.properties.timeBasedScore
    maxWaitTimeNoAgent: MetaOapg.properties.maxWaitTimeNoAgent
    name: MetaOapg.properties.name
    strategy: MetaOapg.properties.strategy
    tierRuleWaitMultiplyLevel: MetaOapg.properties.tierRuleWaitMultiplyLevel
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["strategy"]) -> MetaOapg.properties.strategy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["moh"]) -> MetaOapg.properties.moh: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["callerResumeTimeout"]) -> MetaOapg.properties.callerResumeTimeout: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxWaitTime"]) -> MetaOapg.properties.maxWaitTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxWaitTimeNoAgent"]) -> MetaOapg.properties.maxWaitTimeNoAgent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxNoAnswer"]) -> MetaOapg.properties.maxNoAnswer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeBasedScore"]) -> MetaOapg.properties.timeBasedScore: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tierRulesApply"]) -> MetaOapg.properties.tierRulesApply: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tierRuleNoAgentNoWait"]) -> MetaOapg.properties.tierRuleNoAgentNoWait: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tierRuleWaitMultiplyLevel"]) -> MetaOapg.properties.tierRuleWaitMultiplyLevel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["abandonedResumeAllowed"]) -> MetaOapg.properties.abandonedResumeAllowed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxWaitTimeNoAgentTimeReached"]) -> MetaOapg.properties.maxWaitTimeNoAgentTimeReached: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["announcePosition"]) -> MetaOapg.properties.announcePosition: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["noAnswerDelayTimeout"]) -> MetaOapg.properties.noAnswerDelayTimeout: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rejectTimeout"]) -> MetaOapg.properties.rejectTimeout: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["busyTimeout"]) -> MetaOapg.properties.busyTimeout: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wrapUpTimeout"]) -> MetaOapg.properties.wrapUpTimeout: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tierRuleWaitSecond"]) -> MetaOapg.properties.tierRuleWaitSecond: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["discardAbandonedAfter"]) -> MetaOapg.properties.discardAbandonedAfter: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "strategy", "moh", "callerResumeTimeout", "maxWaitTime", "maxWaitTimeNoAgent", "maxNoAnswer", "timeBasedScore", "tierRulesApply", "tierRuleNoAgentNoWait", "tierRuleWaitMultiplyLevel", "abandonedResumeAllowed", "maxWaitTimeNoAgentTimeReached", "announcePosition", "noAnswerDelayTimeout", "rejectTimeout", "busyTimeout", "wrapUpTimeout", "tierRuleWaitSecond", "discardAbandonedAfter", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["strategy"]) -> MetaOapg.properties.strategy: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["moh"]) -> MetaOapg.properties.moh: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["callerResumeTimeout"]) -> MetaOapg.properties.callerResumeTimeout: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxWaitTime"]) -> MetaOapg.properties.maxWaitTime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxWaitTimeNoAgent"]) -> MetaOapg.properties.maxWaitTimeNoAgent: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxNoAnswer"]) -> MetaOapg.properties.maxNoAnswer: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeBasedScore"]) -> MetaOapg.properties.timeBasedScore: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tierRulesApply"]) -> MetaOapg.properties.tierRulesApply: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tierRuleNoAgentNoWait"]) -> MetaOapg.properties.tierRuleNoAgentNoWait: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tierRuleWaitMultiplyLevel"]) -> MetaOapg.properties.tierRuleWaitMultiplyLevel: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["abandonedResumeAllowed"]) -> MetaOapg.properties.abandonedResumeAllowed: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxWaitTimeNoAgentTimeReached"]) -> MetaOapg.properties.maxWaitTimeNoAgentTimeReached: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["announcePosition"]) -> typing.Union[MetaOapg.properties.announcePosition, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["noAnswerDelayTimeout"]) -> typing.Union[MetaOapg.properties.noAnswerDelayTimeout, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rejectTimeout"]) -> typing.Union[MetaOapg.properties.rejectTimeout, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["busyTimeout"]) -> typing.Union[MetaOapg.properties.busyTimeout, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wrapUpTimeout"]) -> typing.Union[MetaOapg.properties.wrapUpTimeout, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tierRuleWaitSecond"]) -> typing.Union[MetaOapg.properties.tierRuleWaitSecond, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["discardAbandonedAfter"]) -> typing.Union[MetaOapg.properties.discardAbandonedAfter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "strategy", "moh", "callerResumeTimeout", "maxWaitTime", "maxWaitTimeNoAgent", "maxNoAnswer", "timeBasedScore", "tierRulesApply", "tierRuleNoAgentNoWait", "tierRuleWaitMultiplyLevel", "abandonedResumeAllowed", "maxWaitTimeNoAgentTimeReached", "announcePosition", "noAnswerDelayTimeout", "rejectTimeout", "busyTimeout", "wrapUpTimeout", "tierRuleWaitSecond", "discardAbandonedAfter", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        abandonedResumeAllowed: typing.Union[MetaOapg.properties.abandonedResumeAllowed, bool, ],
        maxNoAnswer: typing.Union[MetaOapg.properties.maxNoAnswer, decimal.Decimal, int, ],
        callerResumeTimeout: typing.Union[MetaOapg.properties.callerResumeTimeout, decimal.Decimal, int, ],
        maxWaitTime: typing.Union[MetaOapg.properties.maxWaitTime, decimal.Decimal, int, ],
        moh: typing.Union[MetaOapg.properties.moh, str, ],
        tierRulesApply: typing.Union[MetaOapg.properties.tierRulesApply, bool, ],
        maxWaitTimeNoAgentTimeReached: typing.Union[MetaOapg.properties.maxWaitTimeNoAgentTimeReached, decimal.Decimal, int, ],
        tierRuleNoAgentNoWait: typing.Union[MetaOapg.properties.tierRuleNoAgentNoWait, bool, ],
        timeBasedScore: typing.Union[MetaOapg.properties.timeBasedScore, str, ],
        maxWaitTimeNoAgent: typing.Union[MetaOapg.properties.maxWaitTimeNoAgent, decimal.Decimal, int, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        strategy: typing.Union[MetaOapg.properties.strategy, str, ],
        tierRuleWaitMultiplyLevel: typing.Union[MetaOapg.properties.tierRuleWaitMultiplyLevel, bool, ],
        announcePosition: typing.Union[MetaOapg.properties.announcePosition, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        noAnswerDelayTimeout: typing.Union[MetaOapg.properties.noAnswerDelayTimeout, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        rejectTimeout: typing.Union[MetaOapg.properties.rejectTimeout, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        busyTimeout: typing.Union[MetaOapg.properties.busyTimeout, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        wrapUpTimeout: typing.Union[MetaOapg.properties.wrapUpTimeout, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        tierRuleWaitSecond: typing.Union[MetaOapg.properties.tierRuleWaitSecond, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        discardAbandonedAfter: typing.Union[MetaOapg.properties.discardAbandonedAfter, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CallqueuesCreateOrPatch':
        return super().__new__(
            cls,
            *_args,
            abandonedResumeAllowed=abandonedResumeAllowed,
            maxNoAnswer=maxNoAnswer,
            callerResumeTimeout=callerResumeTimeout,
            maxWaitTime=maxWaitTime,
            moh=moh,
            tierRulesApply=tierRulesApply,
            maxWaitTimeNoAgentTimeReached=maxWaitTimeNoAgentTimeReached,
            tierRuleNoAgentNoWait=tierRuleNoAgentNoWait,
            timeBasedScore=timeBasedScore,
            maxWaitTimeNoAgent=maxWaitTimeNoAgent,
            name=name,
            strategy=strategy,
            tierRuleWaitMultiplyLevel=tierRuleWaitMultiplyLevel,
            announcePosition=announcePosition,
            noAnswerDelayTimeout=noAnswerDelayTimeout,
            rejectTimeout=rejectTimeout,
            busyTimeout=busyTimeout,
            wrapUpTimeout=wrapUpTimeout,
            tierRuleWaitSecond=tierRuleWaitSecond,
            discardAbandonedAfter=discardAbandonedAfter,
            _configuration=_configuration,
            **kwargs,
        )
