# coding: utf-8

"""
    Circuit ID REST API

    # Introduction Circuit ID&reg; is an innovative cloud communications platform that redefines your connectivity experience. Our cutting-edge AI-powered solution seamlessly integrates calling, meetings, messaging, voicemail, fax, SIP Trunking, mobile broadband, and mobile phone services, accessible wherever you and your devices go.                  Whether you are a beginner getting started with our API or an experienced developer looking for advanced features, this documentation site will serve as your comprehensive guide.   We are excited to have you on board and are confident that this documentation site will empower you to leverage the full potential of our REST API.  If you have any questions or require further assistance, please don't hesitate to reach out to our support team.                  Happy coding!  # noqa: E501

    The version of the OpenAPI document: 0.47.22
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


class NumbersCreateOrPatch(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "destinationType",
        }
        
        class properties:
            
            
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
            directoryListing = schemas.StrSchema
            
            
            class callerName(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            e911 = schemas.StrSchema
            
            
            class messageCampaign(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            destination = schemas.StrSchema
            
            
            class callForwardingDestination(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
                    min_length = 10
            __annotations__ = {
                "destinationType": destinationType,
                "directoryListing": directoryListing,
                "callerName": callerName,
                "e911": e911,
                "messageCampaign": messageCampaign,
                "destination": destination,
                "callForwardingDestination": callForwardingDestination,
            }
        min_properties = 1
    
    destinationType: MetaOapg.properties.destinationType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destinationType"]) -> MetaOapg.properties.destinationType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["directoryListing"]) -> MetaOapg.properties.directoryListing: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["callerName"]) -> MetaOapg.properties.callerName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["e911"]) -> MetaOapg.properties.e911: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["messageCampaign"]) -> MetaOapg.properties.messageCampaign: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destination"]) -> MetaOapg.properties.destination: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["callForwardingDestination"]) -> MetaOapg.properties.callForwardingDestination: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["destinationType", "directoryListing", "callerName", "e911", "messageCampaign", "destination", "callForwardingDestination", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destinationType"]) -> MetaOapg.properties.destinationType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["directoryListing"]) -> typing.Union[MetaOapg.properties.directoryListing, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["callerName"]) -> typing.Union[MetaOapg.properties.callerName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["e911"]) -> typing.Union[MetaOapg.properties.e911, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["messageCampaign"]) -> typing.Union[MetaOapg.properties.messageCampaign, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destination"]) -> typing.Union[MetaOapg.properties.destination, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["callForwardingDestination"]) -> typing.Union[MetaOapg.properties.callForwardingDestination, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["destinationType", "directoryListing", "callerName", "e911", "messageCampaign", "destination", "callForwardingDestination", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        destinationType: typing.Union[MetaOapg.properties.destinationType, str, ],
        directoryListing: typing.Union[MetaOapg.properties.directoryListing, str, schemas.Unset] = schemas.unset,
        callerName: typing.Union[MetaOapg.properties.callerName, str, schemas.Unset] = schemas.unset,
        e911: typing.Union[MetaOapg.properties.e911, str, schemas.Unset] = schemas.unset,
        messageCampaign: typing.Union[MetaOapg.properties.messageCampaign, str, schemas.Unset] = schemas.unset,
        destination: typing.Union[MetaOapg.properties.destination, str, schemas.Unset] = schemas.unset,
        callForwardingDestination: typing.Union[MetaOapg.properties.callForwardingDestination, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NumbersCreateOrPatch':
        return super().__new__(
            cls,
            *_args,
            destinationType=destinationType,
            directoryListing=directoryListing,
            callerName=callerName,
            e911=e911,
            messageCampaign=messageCampaign,
            destination=destination,
            callForwardingDestination=callForwardingDestination,
            _configuration=_configuration,
            **kwargs,
        )
