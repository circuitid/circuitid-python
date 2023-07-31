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


class Menus(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "maxExtensionLength",
            "name",
            "greetingType",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            maxExtensionLength = schemas.Int32Schema
            
            
            class greetingType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def TTS(cls):
                    return cls("tts")
                
                @schemas.classproperty
                def MP3(cls):
                    return cls("mp3")
            
            
            class speechRecognition(
                schemas.EnumBase,
                schemas.Int32Schema
            ):
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls(1)
                
                @schemas.classproperty
                def POSITIVE_0(cls):
                    return cls(0)
            directory = schemas.StrSchema
            greetingTTS = schemas.StrSchema
            menuVoice = schemas.StrSchema
            
            
            class exitSound(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DEFAULT(cls):
                    return cls("default")
                
                @schemas.classproperty
                def MP3(cls):
                    return cls("mp3")
            
            
            class transferAnnouncement(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DEFAULT(cls):
                    return cls("default")
                
                @schemas.classproperty
                def MP3(cls):
                    return cls("mp3")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls("none")
            maxFailures = schemas.Int32Schema
            maxTimeouts = schemas.Int32Schema
            timeout = schemas.Int32Schema
            
            
            class touchToneTerminators(
                schemas.EnumBase,
                schemas.Int32Schema
            ):
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls(1)
                
                @schemas.classproperty
                def POSITIVE_0(cls):
                    return cls(0)
            timeschedule = schemas.StrSchema
            
            
            class destinationType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
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
            destination = schemas.StrSchema
            
            
            class ref(
                schemas.StrSchema
            ):
                pass
            
            
            class callForwardingDestination(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "name": name,
                "maxExtensionLength": maxExtensionLength,
                "greetingType": greetingType,
                "speechRecognition": speechRecognition,
                "directory": directory,
                "greetingTTS": greetingTTS,
                "menuVoice": menuVoice,
                "exitSound": exitSound,
                "transferAnnouncement": transferAnnouncement,
                "maxFailures": maxFailures,
                "maxTimeouts": maxTimeouts,
                "timeout": timeout,
                "touchToneTerminators": touchToneTerminators,
                "timeschedule": timeschedule,
                "destinationType": destinationType,
                "destination": destination,
                "ref": ref,
                "callForwardingDestination": callForwardingDestination,
            }
    
    maxExtensionLength: MetaOapg.properties.maxExtensionLength
    name: MetaOapg.properties.name
    greetingType: MetaOapg.properties.greetingType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxExtensionLength"]) -> MetaOapg.properties.maxExtensionLength: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["greetingType"]) -> MetaOapg.properties.greetingType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["speechRecognition"]) -> MetaOapg.properties.speechRecognition: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["directory"]) -> MetaOapg.properties.directory: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["greetingTTS"]) -> MetaOapg.properties.greetingTTS: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["menuVoice"]) -> MetaOapg.properties.menuVoice: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exitSound"]) -> MetaOapg.properties.exitSound: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transferAnnouncement"]) -> MetaOapg.properties.transferAnnouncement: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxFailures"]) -> MetaOapg.properties.maxFailures: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxTimeouts"]) -> MetaOapg.properties.maxTimeouts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeout"]) -> MetaOapg.properties.timeout: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["touchToneTerminators"]) -> MetaOapg.properties.touchToneTerminators: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeschedule"]) -> MetaOapg.properties.timeschedule: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destinationType"]) -> MetaOapg.properties.destinationType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destination"]) -> MetaOapg.properties.destination: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ref"]) -> MetaOapg.properties.ref: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["callForwardingDestination"]) -> MetaOapg.properties.callForwardingDestination: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "maxExtensionLength", "greetingType", "speechRecognition", "directory", "greetingTTS", "menuVoice", "exitSound", "transferAnnouncement", "maxFailures", "maxTimeouts", "timeout", "touchToneTerminators", "timeschedule", "destinationType", "destination", "ref", "callForwardingDestination", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxExtensionLength"]) -> MetaOapg.properties.maxExtensionLength: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["greetingType"]) -> MetaOapg.properties.greetingType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["speechRecognition"]) -> typing.Union[MetaOapg.properties.speechRecognition, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["directory"]) -> typing.Union[MetaOapg.properties.directory, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["greetingTTS"]) -> typing.Union[MetaOapg.properties.greetingTTS, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["menuVoice"]) -> typing.Union[MetaOapg.properties.menuVoice, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exitSound"]) -> typing.Union[MetaOapg.properties.exitSound, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transferAnnouncement"]) -> typing.Union[MetaOapg.properties.transferAnnouncement, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxFailures"]) -> typing.Union[MetaOapg.properties.maxFailures, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxTimeouts"]) -> typing.Union[MetaOapg.properties.maxTimeouts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeout"]) -> typing.Union[MetaOapg.properties.timeout, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["touchToneTerminators"]) -> typing.Union[MetaOapg.properties.touchToneTerminators, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeschedule"]) -> typing.Union[MetaOapg.properties.timeschedule, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destinationType"]) -> typing.Union[MetaOapg.properties.destinationType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destination"]) -> typing.Union[MetaOapg.properties.destination, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ref"]) -> typing.Union[MetaOapg.properties.ref, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["callForwardingDestination"]) -> typing.Union[MetaOapg.properties.callForwardingDestination, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "maxExtensionLength", "greetingType", "speechRecognition", "directory", "greetingTTS", "menuVoice", "exitSound", "transferAnnouncement", "maxFailures", "maxTimeouts", "timeout", "touchToneTerminators", "timeschedule", "destinationType", "destination", "ref", "callForwardingDestination", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        maxExtensionLength: typing.Union[MetaOapg.properties.maxExtensionLength, decimal.Decimal, int, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        greetingType: typing.Union[MetaOapg.properties.greetingType, str, ],
        speechRecognition: typing.Union[MetaOapg.properties.speechRecognition, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        directory: typing.Union[MetaOapg.properties.directory, str, schemas.Unset] = schemas.unset,
        greetingTTS: typing.Union[MetaOapg.properties.greetingTTS, str, schemas.Unset] = schemas.unset,
        menuVoice: typing.Union[MetaOapg.properties.menuVoice, str, schemas.Unset] = schemas.unset,
        exitSound: typing.Union[MetaOapg.properties.exitSound, str, schemas.Unset] = schemas.unset,
        transferAnnouncement: typing.Union[MetaOapg.properties.transferAnnouncement, str, schemas.Unset] = schemas.unset,
        maxFailures: typing.Union[MetaOapg.properties.maxFailures, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        maxTimeouts: typing.Union[MetaOapg.properties.maxTimeouts, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        timeout: typing.Union[MetaOapg.properties.timeout, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        touchToneTerminators: typing.Union[MetaOapg.properties.touchToneTerminators, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        timeschedule: typing.Union[MetaOapg.properties.timeschedule, str, schemas.Unset] = schemas.unset,
        destinationType: typing.Union[MetaOapg.properties.destinationType, str, schemas.Unset] = schemas.unset,
        destination: typing.Union[MetaOapg.properties.destination, str, schemas.Unset] = schemas.unset,
        ref: typing.Union[MetaOapg.properties.ref, str, schemas.Unset] = schemas.unset,
        callForwardingDestination: typing.Union[MetaOapg.properties.callForwardingDestination, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Menus':
        return super().__new__(
            cls,
            *_args,
            maxExtensionLength=maxExtensionLength,
            name=name,
            greetingType=greetingType,
            speechRecognition=speechRecognition,
            directory=directory,
            greetingTTS=greetingTTS,
            menuVoice=menuVoice,
            exitSound=exitSound,
            transferAnnouncement=transferAnnouncement,
            maxFailures=maxFailures,
            maxTimeouts=maxTimeouts,
            timeout=timeout,
            touchToneTerminators=touchToneTerminators,
            timeschedule=timeschedule,
            destinationType=destinationType,
            destination=destination,
            ref=ref,
            callForwardingDestination=callForwardingDestination,
            _configuration=_configuration,
            **kwargs,
        )
