# coding: utf-8

"""
    Circuit ID REST API

    # Introduction Circuit ID&reg; is an innovative cloud communications platform that redefines your connectivity experience. Our cutting-edge AI-powered solution seamlessly integrates calling, meetings, messaging, voicemail, fax, SIP Trunking, mobile broadband, and mobile phone services, accessible wherever you and your devices go.                  Whether you are a beginner getting started with our API or an experienced developer looking for advanced features, this documentation site will serve as your comprehensive guide.   We are excited to have you on board and are confident that this documentation site will empower you to leverage the full potential of our REST API.  If you have any questions or require further assistance, please don't hesitate to reach out to our support team.                  Happy coding!  # noqa: E501

    The version of the OpenAPI document: 0.47.19
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


class Phoneinboundruleactions(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "phoneinboundrule",
            "name",
            "destinationType",
            "priority",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            phoneinboundrule = schemas.StrSchema
            priority = schemas.Int32Schema
            
            
            class destinationType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "announcements": "ANNOUNCEMENTS",
                        "directories": "DIRECTORIES",
                        "park": "PARK",
                        "numbers": "NUMBERS",
                        "menus": "MENUS",
                        "users": "USERS",
                        "servers": "SERVERS",
                        "inboundrules": "INBOUNDRULES",
                        "callqueues": "CALLQUEUES",
                        "faxaccounts": "FAXACCOUNTS",
                        "callforwarding": "CALLFORWARDING",
                        "hangup": "HANGUP",
                        "phoneinboundrules": "PHONEINBOUNDRULES",
                        "voicemailaccounts": "VOICEMAILACCOUNTS",
                    }
                
                @schemas.classproperty
                def ANNOUNCEMENTS(cls):
                    return cls("announcements")
                
                @schemas.classproperty
                def DIRECTORIES(cls):
                    return cls("directories")
                
                @schemas.classproperty
                def PARK(cls):
                    return cls("park")
                
                @schemas.classproperty
                def NUMBERS(cls):
                    return cls("numbers")
                
                @schemas.classproperty
                def MENUS(cls):
                    return cls("menus")
                
                @schemas.classproperty
                def USERS(cls):
                    return cls("users")
                
                @schemas.classproperty
                def SERVERS(cls):
                    return cls("servers")
                
                @schemas.classproperty
                def INBOUNDRULES(cls):
                    return cls("inboundrules")
                
                @schemas.classproperty
                def CALLQUEUES(cls):
                    return cls("callqueues")
                
                @schemas.classproperty
                def FAXACCOUNTS(cls):
                    return cls("faxaccounts")
                
                @schemas.classproperty
                def CALLFORWARDING(cls):
                    return cls("callforwarding")
                
                @schemas.classproperty
                def HANGUP(cls):
                    return cls("hangup")
                
                @schemas.classproperty
                def PHONEINBOUNDRULES(cls):
                    return cls("phoneinboundrules")
                
                @schemas.classproperty
                def VOICEMAILACCOUNTS(cls):
                    return cls("voicemailaccounts")
            timeschedule = schemas.StrSchema
            timeout = schemas.Int32Schema
            
            
            class status(
                schemas.EnumBase,
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    enum_value_to_name = {
                        1: "POSITIVE_1",
                        0: "POSITIVE_0",
                    }
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls(1)
                
                @schemas.classproperty
                def POSITIVE_0(cls):
                    return cls(0)
            destination = schemas.StrSchema
            
            
            class ref(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
                    min_length = 5
            
            
            class callForwardingDestination(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
                    min_length = 10
            __annotations__ = {
                "name": name,
                "phoneinboundrule": phoneinboundrule,
                "priority": priority,
                "destinationType": destinationType,
                "timeschedule": timeschedule,
                "timeout": timeout,
                "status": status,
                "destination": destination,
                "ref": ref,
                "callForwardingDestination": callForwardingDestination,
            }
        min_properties = 1
    
    phoneinboundrule: MetaOapg.properties.phoneinboundrule
    name: MetaOapg.properties.name
    destinationType: MetaOapg.properties.destinationType
    priority: MetaOapg.properties.priority
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneinboundrule"]) -> MetaOapg.properties.phoneinboundrule: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destinationType"]) -> MetaOapg.properties.destinationType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeschedule"]) -> MetaOapg.properties.timeschedule: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeout"]) -> MetaOapg.properties.timeout: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destination"]) -> MetaOapg.properties.destination: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ref"]) -> MetaOapg.properties.ref: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["callForwardingDestination"]) -> MetaOapg.properties.callForwardingDestination: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "phoneinboundrule", "priority", "destinationType", "timeschedule", "timeout", "status", "destination", "ref", "callForwardingDestination", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneinboundrule"]) -> MetaOapg.properties.phoneinboundrule: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destinationType"]) -> MetaOapg.properties.destinationType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeschedule"]) -> typing.Union[MetaOapg.properties.timeschedule, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeout"]) -> typing.Union[MetaOapg.properties.timeout, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destination"]) -> typing.Union[MetaOapg.properties.destination, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ref"]) -> typing.Union[MetaOapg.properties.ref, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["callForwardingDestination"]) -> typing.Union[MetaOapg.properties.callForwardingDestination, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "phoneinboundrule", "priority", "destinationType", "timeschedule", "timeout", "status", "destination", "ref", "callForwardingDestination", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        phoneinboundrule: typing.Union[MetaOapg.properties.phoneinboundrule, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        destinationType: typing.Union[MetaOapg.properties.destinationType, str, ],
        priority: typing.Union[MetaOapg.properties.priority, decimal.Decimal, int, ],
        timeschedule: typing.Union[MetaOapg.properties.timeschedule, str, schemas.Unset] = schemas.unset,
        timeout: typing.Union[MetaOapg.properties.timeout, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        destination: typing.Union[MetaOapg.properties.destination, str, schemas.Unset] = schemas.unset,
        ref: typing.Union[MetaOapg.properties.ref, str, schemas.Unset] = schemas.unset,
        callForwardingDestination: typing.Union[MetaOapg.properties.callForwardingDestination, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Phoneinboundruleactions':
        return super().__new__(
            cls,
            *_args,
            phoneinboundrule=phoneinboundrule,
            name=name,
            destinationType=destinationType,
            priority=priority,
            timeschedule=timeschedule,
            timeout=timeout,
            status=status,
            destination=destination,
            ref=ref,
            callForwardingDestination=callForwardingDestination,
            _configuration=_configuration,
            **kwargs,
        )
