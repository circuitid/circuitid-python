# coding: utf-8

"""
    Circuit ID REST API

    # Introduction Circuit ID&reg; is an innovative cloud communications platform that redefines your connectivity experience. Our cutting-edge AI-powered solution seamlessly integrates calling, meetings, messaging, voicemail, fax, SIP Trunking, mobile broadband, and mobile phone services, accessible wherever you and your devices go.                  Whether you are a beginner getting started with our API or an experienced developer looking for advanced features, this documentation site will serve as your comprehensive guide.   We are excited to have you on board and are confident that this documentation site will empower you to leverage the full potential of our REST API.  If you have any questions or require further assistance, please don't hesitate to reach out to our support team.                  Happy coding!  # noqa: E501

    The version of the OpenAPI document: 0.47.16
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


class Phoneoutboundruleactions(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "route",
            "name",
            "phoneoutboundrule",
            "priority",
        }
        
        class properties:
            
            
            class name(
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    max_length = 45
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'name':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            phoneoutboundrule = schemas.AnyTypeSchema
            
            
            class priority(
                schemas.Int32Base,
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    format = 'int32'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'priority':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class route(
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "default": "DEFAULT",
                        "group": "GROUP",
                        "pstn": "PSTN",
                    }
                
                @schemas.classproperty
                def DEFAULT(cls):
                    return cls("default")
                
                @schemas.classproperty
                def GROUP(cls):
                    return cls("group")
                
                @schemas.classproperty
                def PSTN(cls):
                    return cls("pstn")
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'route':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            group = schemas.AnyTypeSchema
            
            
            class status(
                schemas.Int32Base,
                schemas.AnyTypeSchema,
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
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'status':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class startingChars(
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    max_length = 20
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'startingChars':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class contains(
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    max_length = 20
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'contains':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class lengthType(
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "atleast": "ATLEAST",
                        "exactly": "EXACTLY",
                        "range": "RANGE",
                        "any": "ANY",
                        schemas.NoneClass.NONE: "NONE",
                    }
                
                @schemas.classproperty
                def ATLEAST(cls):
                    return cls("atleast")
                
                @schemas.classproperty
                def EXACTLY(cls):
                    return cls("exactly")
                
                @schemas.classproperty
                def RANGE(cls):
                    return cls("range")
                
                @schemas.classproperty
                def ANY(cls):
                    return cls("any")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls(None)
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'lengthType':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class length(
                schemas.Int32Base,
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    format = 'int32'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'length':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class appendChars(
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    max_length = 20
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'appendChars':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class prependChars(
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    max_length = 20
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'prependChars':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class rangeStart(
                schemas.Int32Base,
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    format = 'int32'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'rangeStart':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class rangeEnd(
                schemas.Int32Base,
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    format = 'int32'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'rangeEnd':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class removeStartingChars(
                schemas.Int32Base,
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    format = 'int32'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'removeStartingChars':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class removeEndingChars(
                schemas.Int32Base,
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    format = 'int32'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'removeEndingChars':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class routingType(
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "priority": "PRIORITY",
                        "lb": "LB",
                        "simultaneous": "SIMULTANEOUS",
                    }
                
                @schemas.classproperty
                def PRIORITY(cls):
                    return cls("priority")
                
                @schemas.classproperty
                def LB(cls):
                    return cls("lb")
                
                @schemas.classproperty
                def SIMULTANEOUS(cls):
                    return cls("simultaneous")
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'routingType':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "name": name,
                "phoneoutboundrule": phoneoutboundrule,
                "priority": priority,
                "route": route,
                "group": group,
                "status": status,
                "startingChars": startingChars,
                "contains": contains,
                "lengthType": lengthType,
                "length": length,
                "appendChars": appendChars,
                "prependChars": prependChars,
                "rangeStart": rangeStart,
                "rangeEnd": rangeEnd,
                "removeStartingChars": removeStartingChars,
                "removeEndingChars": removeEndingChars,
                "routingType": routingType,
            }

    
    route: MetaOapg.properties.route
    name: MetaOapg.properties.name
    phoneoutboundrule: MetaOapg.properties.phoneoutboundrule
    priority: MetaOapg.properties.priority
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneoutboundrule"]) -> MetaOapg.properties.phoneoutboundrule: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["route"]) -> MetaOapg.properties.route: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["group"]) -> MetaOapg.properties.group: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startingChars"]) -> MetaOapg.properties.startingChars: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contains"]) -> MetaOapg.properties.contains: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lengthType"]) -> MetaOapg.properties.lengthType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["length"]) -> MetaOapg.properties.length: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appendChars"]) -> MetaOapg.properties.appendChars: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prependChars"]) -> MetaOapg.properties.prependChars: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rangeStart"]) -> MetaOapg.properties.rangeStart: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rangeEnd"]) -> MetaOapg.properties.rangeEnd: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["removeStartingChars"]) -> MetaOapg.properties.removeStartingChars: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["removeEndingChars"]) -> MetaOapg.properties.removeEndingChars: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["routingType"]) -> MetaOapg.properties.routingType: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "phoneoutboundrule", "priority", "route", "group", "status", "startingChars", "contains", "lengthType", "length", "appendChars", "prependChars", "rangeStart", "rangeEnd", "removeStartingChars", "removeEndingChars", "routingType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneoutboundrule"]) -> MetaOapg.properties.phoneoutboundrule: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["route"]) -> MetaOapg.properties.route: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["group"]) -> typing.Union[MetaOapg.properties.group, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startingChars"]) -> typing.Union[MetaOapg.properties.startingChars, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contains"]) -> typing.Union[MetaOapg.properties.contains, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lengthType"]) -> typing.Union[MetaOapg.properties.lengthType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["length"]) -> typing.Union[MetaOapg.properties.length, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appendChars"]) -> typing.Union[MetaOapg.properties.appendChars, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prependChars"]) -> typing.Union[MetaOapg.properties.prependChars, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rangeStart"]) -> typing.Union[MetaOapg.properties.rangeStart, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rangeEnd"]) -> typing.Union[MetaOapg.properties.rangeEnd, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["removeStartingChars"]) -> typing.Union[MetaOapg.properties.removeStartingChars, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["removeEndingChars"]) -> typing.Union[MetaOapg.properties.removeEndingChars, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["routingType"]) -> typing.Union[MetaOapg.properties.routingType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "phoneoutboundrule", "priority", "route", "group", "status", "startingChars", "contains", "lengthType", "length", "appendChars", "prependChars", "rangeStart", "rangeEnd", "removeStartingChars", "removeEndingChars", "routingType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        route: typing.Union[MetaOapg.properties.route, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        name: typing.Union[MetaOapg.properties.name, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        phoneoutboundrule: typing.Union[MetaOapg.properties.phoneoutboundrule, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        priority: typing.Union[MetaOapg.properties.priority, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        group: typing.Union[MetaOapg.properties.group, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        startingChars: typing.Union[MetaOapg.properties.startingChars, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        contains: typing.Union[MetaOapg.properties.contains, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        lengthType: typing.Union[MetaOapg.properties.lengthType, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        length: typing.Union[MetaOapg.properties.length, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        appendChars: typing.Union[MetaOapg.properties.appendChars, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        prependChars: typing.Union[MetaOapg.properties.prependChars, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        rangeStart: typing.Union[MetaOapg.properties.rangeStart, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        rangeEnd: typing.Union[MetaOapg.properties.rangeEnd, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        removeStartingChars: typing.Union[MetaOapg.properties.removeStartingChars, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        removeEndingChars: typing.Union[MetaOapg.properties.removeEndingChars, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        routingType: typing.Union[MetaOapg.properties.routingType, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Phoneoutboundruleactions':
        return super().__new__(
            cls,
            *_args,
            route=route,
            name=name,
            phoneoutboundrule=phoneoutboundrule,
            priority=priority,
            group=group,
            status=status,
            startingChars=startingChars,
            contains=contains,
            lengthType=lengthType,
            length=length,
            appendChars=appendChars,
            prependChars=prependChars,
            rangeStart=rangeStart,
            rangeEnd=rangeEnd,
            removeStartingChars=removeStartingChars,
            removeEndingChars=removeEndingChars,
            routingType=routingType,
            _configuration=_configuration,
            **kwargs,
        )
