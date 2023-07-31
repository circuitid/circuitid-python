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


class Numbers(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "countryCode",
            "name",
            "destinationType",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 20
                    min_length = 10
            
            
            class countryCode(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 4
                    min_length = 1
            
            
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
            
            
            class inUse(
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
            amount = schemas.Int32Schema
            perMinuteRate = schemas.Int32Schema
            
            
            class fax(
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
            
            
            class voice(
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
            
            
            class sms(
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
            
            
            class mms(
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
            
            
            class messageClass(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "P2P": "P2P",
                        "A2PLC": "A2PLC",
                        "A2P8XX": "A2P8XX",
                    }
                
                @schemas.classproperty
                def P2P(cls):
                    return cls("P2P")
                
                @schemas.classproperty
                def A2PLC(cls):
                    return cls("A2PLC")
                
                @schemas.classproperty
                def A2P8XX(cls):
                    return cls("A2P8XX")
            
            
            class messageType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "SMS": "SMS",
                        "MMS": "MMS",
                        "SMSMMS": "SMSMMS",
                        "SMS_ALT": "SMS_ALT",
                        "MMS_ALT": "MMS_ALT",
                        "SMSMMS_ALT": "SMSMMS_ALT",
                    }
                
                @schemas.classproperty
                def SMS(cls):
                    return cls("SMS")
                
                @schemas.classproperty
                def MMS(cls):
                    return cls("MMS")
                
                @schemas.classproperty
                def SMSMMS(cls):
                    return cls("SMSMMS")
                
                @schemas.classproperty
                def SMS_ALT(cls):
                    return cls("SMS_ALT")
                
                @schemas.classproperty
                def MMS_ALT(cls):
                    return cls("MMS_ALT")
                
                @schemas.classproperty
                def SMSMMS_ALT(cls):
                    return cls("SMSMMS_ALT")
            
            
            class e911Supported(
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
            
            
            class callerNameSupported(
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
            
            
            class directoryListingSupported(
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
            
            
            class messagingSupported(
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
                "countryCode": countryCode,
                "destinationType": destinationType,
                "inUse": inUse,
                "amount": amount,
                "perMinuteRate": perMinuteRate,
                "fax": fax,
                "voice": voice,
                "status": status,
                "sms": sms,
                "mms": mms,
                "directoryListing": directoryListing,
                "callerName": callerName,
                "e911": e911,
                "messageCampaign": messageCampaign,
                "messageClass": messageClass,
                "messageType": messageType,
                "e911Supported": e911Supported,
                "callerNameSupported": callerNameSupported,
                "directoryListingSupported": directoryListingSupported,
                "messagingSupported": messagingSupported,
                "destination": destination,
                "ref": ref,
                "callForwardingDestination": callForwardingDestination,
            }
        min_properties = 1
    
    countryCode: MetaOapg.properties.countryCode
    name: MetaOapg.properties.name
    destinationType: MetaOapg.properties.destinationType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countryCode"]) -> MetaOapg.properties.countryCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destinationType"]) -> MetaOapg.properties.destinationType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inUse"]) -> MetaOapg.properties.inUse: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["perMinuteRate"]) -> MetaOapg.properties.perMinuteRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fax"]) -> MetaOapg.properties.fax: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["voice"]) -> MetaOapg.properties.voice: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sms"]) -> MetaOapg.properties.sms: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mms"]) -> MetaOapg.properties.mms: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["directoryListing"]) -> MetaOapg.properties.directoryListing: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["callerName"]) -> MetaOapg.properties.callerName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["e911"]) -> MetaOapg.properties.e911: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["messageCampaign"]) -> MetaOapg.properties.messageCampaign: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["messageClass"]) -> MetaOapg.properties.messageClass: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["messageType"]) -> MetaOapg.properties.messageType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["e911Supported"]) -> MetaOapg.properties.e911Supported: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["callerNameSupported"]) -> MetaOapg.properties.callerNameSupported: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["directoryListingSupported"]) -> MetaOapg.properties.directoryListingSupported: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["messagingSupported"]) -> MetaOapg.properties.messagingSupported: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destination"]) -> MetaOapg.properties.destination: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ref"]) -> MetaOapg.properties.ref: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["callForwardingDestination"]) -> MetaOapg.properties.callForwardingDestination: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "countryCode", "destinationType", "inUse", "amount", "perMinuteRate", "fax", "voice", "status", "sms", "mms", "directoryListing", "callerName", "e911", "messageCampaign", "messageClass", "messageType", "e911Supported", "callerNameSupported", "directoryListingSupported", "messagingSupported", "destination", "ref", "callForwardingDestination", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countryCode"]) -> MetaOapg.properties.countryCode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destinationType"]) -> MetaOapg.properties.destinationType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inUse"]) -> typing.Union[MetaOapg.properties.inUse, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["perMinuteRate"]) -> typing.Union[MetaOapg.properties.perMinuteRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fax"]) -> typing.Union[MetaOapg.properties.fax, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["voice"]) -> typing.Union[MetaOapg.properties.voice, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sms"]) -> typing.Union[MetaOapg.properties.sms, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mms"]) -> typing.Union[MetaOapg.properties.mms, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["directoryListing"]) -> typing.Union[MetaOapg.properties.directoryListing, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["callerName"]) -> typing.Union[MetaOapg.properties.callerName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["e911"]) -> typing.Union[MetaOapg.properties.e911, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["messageCampaign"]) -> typing.Union[MetaOapg.properties.messageCampaign, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["messageClass"]) -> typing.Union[MetaOapg.properties.messageClass, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["messageType"]) -> typing.Union[MetaOapg.properties.messageType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["e911Supported"]) -> typing.Union[MetaOapg.properties.e911Supported, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["callerNameSupported"]) -> typing.Union[MetaOapg.properties.callerNameSupported, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["directoryListingSupported"]) -> typing.Union[MetaOapg.properties.directoryListingSupported, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["messagingSupported"]) -> typing.Union[MetaOapg.properties.messagingSupported, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destination"]) -> typing.Union[MetaOapg.properties.destination, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ref"]) -> typing.Union[MetaOapg.properties.ref, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["callForwardingDestination"]) -> typing.Union[MetaOapg.properties.callForwardingDestination, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "countryCode", "destinationType", "inUse", "amount", "perMinuteRate", "fax", "voice", "status", "sms", "mms", "directoryListing", "callerName", "e911", "messageCampaign", "messageClass", "messageType", "e911Supported", "callerNameSupported", "directoryListingSupported", "messagingSupported", "destination", "ref", "callForwardingDestination", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        countryCode: typing.Union[MetaOapg.properties.countryCode, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        destinationType: typing.Union[MetaOapg.properties.destinationType, str, ],
        inUse: typing.Union[MetaOapg.properties.inUse, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        perMinuteRate: typing.Union[MetaOapg.properties.perMinuteRate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        fax: typing.Union[MetaOapg.properties.fax, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        voice: typing.Union[MetaOapg.properties.voice, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sms: typing.Union[MetaOapg.properties.sms, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        mms: typing.Union[MetaOapg.properties.mms, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        directoryListing: typing.Union[MetaOapg.properties.directoryListing, str, schemas.Unset] = schemas.unset,
        callerName: typing.Union[MetaOapg.properties.callerName, str, schemas.Unset] = schemas.unset,
        e911: typing.Union[MetaOapg.properties.e911, str, schemas.Unset] = schemas.unset,
        messageCampaign: typing.Union[MetaOapg.properties.messageCampaign, str, schemas.Unset] = schemas.unset,
        messageClass: typing.Union[MetaOapg.properties.messageClass, str, schemas.Unset] = schemas.unset,
        messageType: typing.Union[MetaOapg.properties.messageType, str, schemas.Unset] = schemas.unset,
        e911Supported: typing.Union[MetaOapg.properties.e911Supported, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        callerNameSupported: typing.Union[MetaOapg.properties.callerNameSupported, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        directoryListingSupported: typing.Union[MetaOapg.properties.directoryListingSupported, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        messagingSupported: typing.Union[MetaOapg.properties.messagingSupported, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        destination: typing.Union[MetaOapg.properties.destination, str, schemas.Unset] = schemas.unset,
        ref: typing.Union[MetaOapg.properties.ref, str, schemas.Unset] = schemas.unset,
        callForwardingDestination: typing.Union[MetaOapg.properties.callForwardingDestination, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Numbers':
        return super().__new__(
            cls,
            *_args,
            countryCode=countryCode,
            name=name,
            destinationType=destinationType,
            inUse=inUse,
            amount=amount,
            perMinuteRate=perMinuteRate,
            fax=fax,
            voice=voice,
            status=status,
            sms=sms,
            mms=mms,
            directoryListing=directoryListing,
            callerName=callerName,
            e911=e911,
            messageCampaign=messageCampaign,
            messageClass=messageClass,
            messageType=messageType,
            e911Supported=e911Supported,
            callerNameSupported=callerNameSupported,
            directoryListingSupported=directoryListingSupported,
            messagingSupported=messagingSupported,
            destination=destination,
            ref=ref,
            callForwardingDestination=callForwardingDestination,
            _configuration=_configuration,
            **kwargs,
        )
