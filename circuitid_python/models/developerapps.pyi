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


class Developerapps(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "integrationType",
            "visibility",
            "name",
            "services",
            "type",
            "user",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EVENTS(cls):
                    return cls("events")
            
            
            class visibility(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def PRIVATE(cls):
                    return cls("private")
                
                @schemas.classproperty
                def PUBLIC(cls):
                    return cls("public")
            
            
            class integrationType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def WEBHOOK(cls):
                    return cls("webhook")
                
                @schemas.classproperty
                def CLIENT(cls):
                    return cls("client")
            
            
            class services(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
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
            user = schemas.StrSchema
            
            
            class description(
                schemas.StrSchema
            ):
                pass
            
            
            class requireId(
                schemas.EnumBase,
                schemas.Int32Schema
            ):
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls(1)
                
                @schemas.classproperty
                def POSITIVE_0(cls):
                    return cls(0)
            
            
            class isFree(
                schemas.EnumBase,
                schemas.Int32Schema
            ):
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls(1)
                
                @schemas.classproperty
                def POSITIVE_0(cls):
                    return cls(0)
            
            
            class feeDescription(
                schemas.StrSchema
            ):
                pass
            
            
            class events(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
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
            
            
            class webhookUrl(
                schemas.StrSchema
            ):
                pass
            
            
            class termsOfServiceUrl(
                schemas.StrSchema
            ):
                pass
            
            
            class privacyPolicyUrl(
                schemas.StrSchema
            ):
                pass
            permissions = schemas.DictSchema
            
            
            class webhookAuthType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def HEADER(cls):
                    return cls("header")
                
                @schemas.classproperty
                def USERNAME_AND_PASSWORD(cls):
                    return cls("usernameAndPassword")
            
            
            class webhookUsername(
                schemas.StrSchema
            ):
                pass
            
            
            class webhookPassword(
                schemas.StrSchema
            ):
                pass
            
            
            class webhookTokenName(
                schemas.StrSchema
            ):
                pass
            
            
            class webhookToken(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "name": name,
                "type": type,
                "visibility": visibility,
                "integrationType": integrationType,
                "services": services,
                "user": user,
                "description": description,
                "requireId": requireId,
                "isFree": isFree,
                "feeDescription": feeDescription,
                "events": events,
                "webhookUrl": webhookUrl,
                "termsOfServiceUrl": termsOfServiceUrl,
                "privacyPolicyUrl": privacyPolicyUrl,
                "permissions": permissions,
                "webhookAuthType": webhookAuthType,
                "webhookUsername": webhookUsername,
                "webhookPassword": webhookPassword,
                "webhookTokenName": webhookTokenName,
                "webhookToken": webhookToken,
            }
    
    integrationType: MetaOapg.properties.integrationType
    visibility: MetaOapg.properties.visibility
    name: MetaOapg.properties.name
    services: MetaOapg.properties.services
    type: MetaOapg.properties.type
    user: MetaOapg.properties.user
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["visibility"]) -> MetaOapg.properties.visibility: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["integrationType"]) -> MetaOapg.properties.integrationType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["services"]) -> MetaOapg.properties.services: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> MetaOapg.properties.user: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requireId"]) -> MetaOapg.properties.requireId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isFree"]) -> MetaOapg.properties.isFree: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["feeDescription"]) -> MetaOapg.properties.feeDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["events"]) -> MetaOapg.properties.events: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhookUrl"]) -> MetaOapg.properties.webhookUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["termsOfServiceUrl"]) -> MetaOapg.properties.termsOfServiceUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["privacyPolicyUrl"]) -> MetaOapg.properties.privacyPolicyUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["permissions"]) -> MetaOapg.properties.permissions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhookAuthType"]) -> MetaOapg.properties.webhookAuthType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhookUsername"]) -> MetaOapg.properties.webhookUsername: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhookPassword"]) -> MetaOapg.properties.webhookPassword: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhookTokenName"]) -> MetaOapg.properties.webhookTokenName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhookToken"]) -> MetaOapg.properties.webhookToken: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "type", "visibility", "integrationType", "services", "user", "description", "requireId", "isFree", "feeDescription", "events", "webhookUrl", "termsOfServiceUrl", "privacyPolicyUrl", "permissions", "webhookAuthType", "webhookUsername", "webhookPassword", "webhookTokenName", "webhookToken", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["visibility"]) -> MetaOapg.properties.visibility: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["integrationType"]) -> MetaOapg.properties.integrationType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["services"]) -> MetaOapg.properties.services: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> MetaOapg.properties.user: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requireId"]) -> typing.Union[MetaOapg.properties.requireId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isFree"]) -> typing.Union[MetaOapg.properties.isFree, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["feeDescription"]) -> typing.Union[MetaOapg.properties.feeDescription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["events"]) -> typing.Union[MetaOapg.properties.events, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhookUrl"]) -> typing.Union[MetaOapg.properties.webhookUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["termsOfServiceUrl"]) -> typing.Union[MetaOapg.properties.termsOfServiceUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["privacyPolicyUrl"]) -> typing.Union[MetaOapg.properties.privacyPolicyUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["permissions"]) -> typing.Union[MetaOapg.properties.permissions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhookAuthType"]) -> typing.Union[MetaOapg.properties.webhookAuthType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhookUsername"]) -> typing.Union[MetaOapg.properties.webhookUsername, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhookPassword"]) -> typing.Union[MetaOapg.properties.webhookPassword, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhookTokenName"]) -> typing.Union[MetaOapg.properties.webhookTokenName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhookToken"]) -> typing.Union[MetaOapg.properties.webhookToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "type", "visibility", "integrationType", "services", "user", "description", "requireId", "isFree", "feeDescription", "events", "webhookUrl", "termsOfServiceUrl", "privacyPolicyUrl", "permissions", "webhookAuthType", "webhookUsername", "webhookPassword", "webhookTokenName", "webhookToken", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        integrationType: typing.Union[MetaOapg.properties.integrationType, str, ],
        visibility: typing.Union[MetaOapg.properties.visibility, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        services: typing.Union[MetaOapg.properties.services, list, tuple, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        user: typing.Union[MetaOapg.properties.user, str, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        requireId: typing.Union[MetaOapg.properties.requireId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        isFree: typing.Union[MetaOapg.properties.isFree, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        feeDescription: typing.Union[MetaOapg.properties.feeDescription, str, schemas.Unset] = schemas.unset,
        events: typing.Union[MetaOapg.properties.events, list, tuple, schemas.Unset] = schemas.unset,
        webhookUrl: typing.Union[MetaOapg.properties.webhookUrl, str, schemas.Unset] = schemas.unset,
        termsOfServiceUrl: typing.Union[MetaOapg.properties.termsOfServiceUrl, str, schemas.Unset] = schemas.unset,
        privacyPolicyUrl: typing.Union[MetaOapg.properties.privacyPolicyUrl, str, schemas.Unset] = schemas.unset,
        permissions: typing.Union[MetaOapg.properties.permissions, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        webhookAuthType: typing.Union[MetaOapg.properties.webhookAuthType, str, schemas.Unset] = schemas.unset,
        webhookUsername: typing.Union[MetaOapg.properties.webhookUsername, str, schemas.Unset] = schemas.unset,
        webhookPassword: typing.Union[MetaOapg.properties.webhookPassword, str, schemas.Unset] = schemas.unset,
        webhookTokenName: typing.Union[MetaOapg.properties.webhookTokenName, str, schemas.Unset] = schemas.unset,
        webhookToken: typing.Union[MetaOapg.properties.webhookToken, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Developerapps':
        return super().__new__(
            cls,
            *_args,
            integrationType=integrationType,
            visibility=visibility,
            name=name,
            services=services,
            type=type,
            user=user,
            description=description,
            requireId=requireId,
            isFree=isFree,
            feeDescription=feeDescription,
            events=events,
            webhookUrl=webhookUrl,
            termsOfServiceUrl=termsOfServiceUrl,
            privacyPolicyUrl=privacyPolicyUrl,
            permissions=permissions,
            webhookAuthType=webhookAuthType,
            webhookUsername=webhookUsername,
            webhookPassword=webhookPassword,
            webhookTokenName=webhookTokenName,
            webhookToken=webhookToken,
            _configuration=_configuration,
            **kwargs,
        )
