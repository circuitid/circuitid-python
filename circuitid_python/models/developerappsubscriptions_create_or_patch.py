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


class DeveloperappsubscriptionsCreateOrPatch(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "developerApp",
            "services",
        }
        
        class properties:
            developerApp = schemas.StrSchema
            
            
            class services(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "calendarevents": "CALENDAREVENTS",
                                "callqueues": "CALLQUEUES",
                                "cdrs": "CDRS",
                                "chatmessages": "CHATMESSAGES",
                                "contacts": "CONTACTS",
                                "conversationmessages": "CONVERSATIONMESSAGES",
                                "faxes": "FAXES",
                                "firewall": "FIREWALL",
                                "users": "USERS",
                                "voicemail": "VOICEMAIL",
                            }
                        
                        @schemas.classproperty
                        def CALENDAREVENTS(cls):
                            return cls("calendarevents")
                        
                        @schemas.classproperty
                        def CALLQUEUES(cls):
                            return cls("callqueues")
                        
                        @schemas.classproperty
                        def CDRS(cls):
                            return cls("cdrs")
                        
                        @schemas.classproperty
                        def CHATMESSAGES(cls):
                            return cls("chatmessages")
                        
                        @schemas.classproperty
                        def CONTACTS(cls):
                            return cls("contacts")
                        
                        @schemas.classproperty
                        def CONVERSATIONMESSAGES(cls):
                            return cls("conversationmessages")
                        
                        @schemas.classproperty
                        def FAXES(cls):
                            return cls("faxes")
                        
                        @schemas.classproperty
                        def FIREWALL(cls):
                            return cls("firewall")
                        
                        @schemas.classproperty
                        def USERS(cls):
                            return cls("users")
                        
                        @schemas.classproperty
                        def VOICEMAIL(cls):
                            return cls("voicemail")
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'services':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            object = schemas.StrSchema
            
            
            class ref(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            permissions = schemas.DictSchema
            
            
            class requireId(
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
            
            
            class events(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "create": "CREATE",
                                "patch": "PATCH",
                                "removed": "REMOVED",
                            }
                        
                        @schemas.classproperty
                        def CREATE(cls):
                            return cls("create")
                        
                        @schemas.classproperty
                        def PATCH(cls):
                            return cls("patch")
                        
                        @schemas.classproperty
                        def REMOVED(cls):
                            return cls("removed")
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'events':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "developerApp": developerApp,
                "services": services,
                "object": object,
                "ref": ref,
                "permissions": permissions,
                "requireId": requireId,
                "events": events,
            }
        min_properties = 1
    
    developerApp: MetaOapg.properties.developerApp
    services: MetaOapg.properties.services
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["developerApp"]) -> MetaOapg.properties.developerApp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["services"]) -> MetaOapg.properties.services: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ref"]) -> MetaOapg.properties.ref: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["permissions"]) -> MetaOapg.properties.permissions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requireId"]) -> MetaOapg.properties.requireId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["events"]) -> MetaOapg.properties.events: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["developerApp", "services", "object", "ref", "permissions", "requireId", "events", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["developerApp"]) -> MetaOapg.properties.developerApp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["services"]) -> MetaOapg.properties.services: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> typing.Union[MetaOapg.properties.object, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ref"]) -> typing.Union[MetaOapg.properties.ref, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["permissions"]) -> typing.Union[MetaOapg.properties.permissions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requireId"]) -> typing.Union[MetaOapg.properties.requireId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["events"]) -> typing.Union[MetaOapg.properties.events, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["developerApp", "services", "object", "ref", "permissions", "requireId", "events", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        developerApp: typing.Union[MetaOapg.properties.developerApp, str, ],
        services: typing.Union[MetaOapg.properties.services, list, tuple, ],
        object: typing.Union[MetaOapg.properties.object, str, schemas.Unset] = schemas.unset,
        ref: typing.Union[MetaOapg.properties.ref, str, schemas.Unset] = schemas.unset,
        permissions: typing.Union[MetaOapg.properties.permissions, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        requireId: typing.Union[MetaOapg.properties.requireId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        events: typing.Union[MetaOapg.properties.events, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DeveloperappsubscriptionsCreateOrPatch':
        return super().__new__(
            cls,
            *_args,
            developerApp=developerApp,
            services=services,
            object=object,
            ref=ref,
            permissions=permissions,
            requireId=requireId,
            events=events,
            _configuration=_configuration,
            **kwargs,
        )
