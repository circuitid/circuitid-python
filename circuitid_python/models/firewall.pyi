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


class Firewall(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "param",
            "name",
            "priority",
            "type",
            "target",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            priority = schemas.Int32Schema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ALLOW(cls):
                    return cls("allow")
                
                @schemas.classproperty
                def DENY(cls):
                    return cls("deny")
            
            
            class target(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def NUMBERS(cls):
                    return cls("numbers")
                
                @schemas.classproperty
                def IPADDRESSES(cls):
                    return cls("ipaddresses")
                
                @schemas.classproperty
                def SMS(cls):
                    return cls("sms")
            
            
            class param(
                schemas.StrSchema
            ):
                pass
            
            
            class description(
                schemas.StrSchema
            ):
                pass
            
            
            class direction(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def INBOUND(cls):
                    return cls("inbound")
                
                @schemas.classproperty
                def OUTBOUND(cls):
                    return cls("outbound")
                
                @schemas.classproperty
                def BOTH(cls):
                    return cls("both")
            hits = schemas.Int32Schema
            
            
            class status(
                schemas.EnumBase,
                schemas.Int32Schema
            ):
                
                @schemas.classproperty
                def POSITIVE_0(cls):
                    return cls(0)
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls(1)
            __annotations__ = {
                "name": name,
                "priority": priority,
                "type": type,
                "target": target,
                "param": param,
                "description": description,
                "direction": direction,
                "hits": hits,
                "status": status,
            }
    
    param: MetaOapg.properties.param
    name: MetaOapg.properties.name
    priority: MetaOapg.properties.priority
    type: MetaOapg.properties.type
    target: MetaOapg.properties.target
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target"]) -> MetaOapg.properties.target: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["param"]) -> MetaOapg.properties.param: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["direction"]) -> MetaOapg.properties.direction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hits"]) -> MetaOapg.properties.hits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "priority", "type", "target", "param", "description", "direction", "hits", "status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target"]) -> MetaOapg.properties.target: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["param"]) -> MetaOapg.properties.param: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["direction"]) -> typing.Union[MetaOapg.properties.direction, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hits"]) -> typing.Union[MetaOapg.properties.hits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "priority", "type", "target", "param", "description", "direction", "hits", "status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        param: typing.Union[MetaOapg.properties.param, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        priority: typing.Union[MetaOapg.properties.priority, decimal.Decimal, int, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        target: typing.Union[MetaOapg.properties.target, str, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        direction: typing.Union[MetaOapg.properties.direction, str, schemas.Unset] = schemas.unset,
        hits: typing.Union[MetaOapg.properties.hits, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Firewall':
        return super().__new__(
            cls,
            *_args,
            param=param,
            name=name,
            priority=priority,
            type=type,
            target=target,
            description=description,
            direction=direction,
            hits=hits,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )
