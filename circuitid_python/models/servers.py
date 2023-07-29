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


class Servers(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "domesticOutboundCallLimit",
            "port",
            "internationalOutboundCallLimit",
            "tollFreeChannelLimit",
            "host",
            "name",
            "domesticInboundCallLimit",
            "type",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            
            
            class host(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
                    min_length = 5
            port = schemas.Int32Schema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "sip": "SIP",
                        "skype": "SKYPE",
                    }
                
                @schemas.classproperty
                def SIP(cls):
                    return cls("sip")
                
                @schemas.classproperty
                def SKYPE(cls):
                    return cls("skype")
            domesticOutboundCallLimit = schemas.Int32Schema
            domesticInboundCallLimit = schemas.Int32Schema
            internationalOutboundCallLimit = schemas.Int32Schema
            tollFreeChannelLimit = schemas.Int32Schema
            
            
            class callerId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            inboundSipTrunkingOrder = schemas.StrSchema
            outboundSipTrunkingOrder = schemas.StrSchema
            
            
            class noInstantRingBack(
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
            
            
            class bypassMedia(
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
            
            
            class disableRTPAutoAdjust(
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
            __annotations__ = {
                "name": name,
                "host": host,
                "port": port,
                "type": type,
                "domesticOutboundCallLimit": domesticOutboundCallLimit,
                "domesticInboundCallLimit": domesticInboundCallLimit,
                "internationalOutboundCallLimit": internationalOutboundCallLimit,
                "tollFreeChannelLimit": tollFreeChannelLimit,
                "callerId": callerId,
                "inboundSipTrunkingOrder": inboundSipTrunkingOrder,
                "outboundSipTrunkingOrder": outboundSipTrunkingOrder,
                "noInstantRingBack": noInstantRingBack,
                "bypassMedia": bypassMedia,
                "disableRTPAutoAdjust": disableRTPAutoAdjust,
            }
        min_properties = 1
    
    domesticOutboundCallLimit: MetaOapg.properties.domesticOutboundCallLimit
    port: MetaOapg.properties.port
    internationalOutboundCallLimit: MetaOapg.properties.internationalOutboundCallLimit
    tollFreeChannelLimit: MetaOapg.properties.tollFreeChannelLimit
    host: MetaOapg.properties.host
    name: MetaOapg.properties.name
    domesticInboundCallLimit: MetaOapg.properties.domesticInboundCallLimit
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["host"]) -> MetaOapg.properties.host: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["port"]) -> MetaOapg.properties.port: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["domesticOutboundCallLimit"]) -> MetaOapg.properties.domesticOutboundCallLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["domesticInboundCallLimit"]) -> MetaOapg.properties.domesticInboundCallLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["internationalOutboundCallLimit"]) -> MetaOapg.properties.internationalOutboundCallLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tollFreeChannelLimit"]) -> MetaOapg.properties.tollFreeChannelLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["callerId"]) -> MetaOapg.properties.callerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inboundSipTrunkingOrder"]) -> MetaOapg.properties.inboundSipTrunkingOrder: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["outboundSipTrunkingOrder"]) -> MetaOapg.properties.outboundSipTrunkingOrder: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["noInstantRingBack"]) -> MetaOapg.properties.noInstantRingBack: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bypassMedia"]) -> MetaOapg.properties.bypassMedia: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["disableRTPAutoAdjust"]) -> MetaOapg.properties.disableRTPAutoAdjust: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "host", "port", "type", "domesticOutboundCallLimit", "domesticInboundCallLimit", "internationalOutboundCallLimit", "tollFreeChannelLimit", "callerId", "inboundSipTrunkingOrder", "outboundSipTrunkingOrder", "noInstantRingBack", "bypassMedia", "disableRTPAutoAdjust", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["host"]) -> MetaOapg.properties.host: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["port"]) -> MetaOapg.properties.port: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["domesticOutboundCallLimit"]) -> MetaOapg.properties.domesticOutboundCallLimit: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["domesticInboundCallLimit"]) -> MetaOapg.properties.domesticInboundCallLimit: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["internationalOutboundCallLimit"]) -> MetaOapg.properties.internationalOutboundCallLimit: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tollFreeChannelLimit"]) -> MetaOapg.properties.tollFreeChannelLimit: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["callerId"]) -> typing.Union[MetaOapg.properties.callerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inboundSipTrunkingOrder"]) -> typing.Union[MetaOapg.properties.inboundSipTrunkingOrder, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["outboundSipTrunkingOrder"]) -> typing.Union[MetaOapg.properties.outboundSipTrunkingOrder, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["noInstantRingBack"]) -> typing.Union[MetaOapg.properties.noInstantRingBack, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bypassMedia"]) -> typing.Union[MetaOapg.properties.bypassMedia, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["disableRTPAutoAdjust"]) -> typing.Union[MetaOapg.properties.disableRTPAutoAdjust, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "host", "port", "type", "domesticOutboundCallLimit", "domesticInboundCallLimit", "internationalOutboundCallLimit", "tollFreeChannelLimit", "callerId", "inboundSipTrunkingOrder", "outboundSipTrunkingOrder", "noInstantRingBack", "bypassMedia", "disableRTPAutoAdjust", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        domesticOutboundCallLimit: typing.Union[MetaOapg.properties.domesticOutboundCallLimit, decimal.Decimal, int, ],
        port: typing.Union[MetaOapg.properties.port, decimal.Decimal, int, ],
        internationalOutboundCallLimit: typing.Union[MetaOapg.properties.internationalOutboundCallLimit, decimal.Decimal, int, ],
        tollFreeChannelLimit: typing.Union[MetaOapg.properties.tollFreeChannelLimit, decimal.Decimal, int, ],
        host: typing.Union[MetaOapg.properties.host, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        domesticInboundCallLimit: typing.Union[MetaOapg.properties.domesticInboundCallLimit, decimal.Decimal, int, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        callerId: typing.Union[MetaOapg.properties.callerId, str, schemas.Unset] = schemas.unset,
        inboundSipTrunkingOrder: typing.Union[MetaOapg.properties.inboundSipTrunkingOrder, str, schemas.Unset] = schemas.unset,
        outboundSipTrunkingOrder: typing.Union[MetaOapg.properties.outboundSipTrunkingOrder, str, schemas.Unset] = schemas.unset,
        noInstantRingBack: typing.Union[MetaOapg.properties.noInstantRingBack, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        bypassMedia: typing.Union[MetaOapg.properties.bypassMedia, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        disableRTPAutoAdjust: typing.Union[MetaOapg.properties.disableRTPAutoAdjust, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Servers':
        return super().__new__(
            cls,
            *_args,
            domesticOutboundCallLimit=domesticOutboundCallLimit,
            port=port,
            internationalOutboundCallLimit=internationalOutboundCallLimit,
            tollFreeChannelLimit=tollFreeChannelLimit,
            host=host,
            name=name,
            domesticInboundCallLimit=domesticInboundCallLimit,
            type=type,
            callerId=callerId,
            inboundSipTrunkingOrder=inboundSipTrunkingOrder,
            outboundSipTrunkingOrder=outboundSipTrunkingOrder,
            noInstantRingBack=noInstantRingBack,
            bypassMedia=bypassMedia,
            disableRTPAutoAdjust=disableRTPAutoAdjust,
            _configuration=_configuration,
            **kwargs,
        )
