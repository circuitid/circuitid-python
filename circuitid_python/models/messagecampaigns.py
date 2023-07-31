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


class Messagecampaigns(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "brandId",
            "name",
            "order",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            
            
            class brandId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            order = schemas.StrSchema
            
            
            class campaignId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            
            
            class subscriberOptin(
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
            
            
            class subscriberOptout(
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
            
            
            class subscriberHelp(
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
            
            
            class numberPool(
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
            
            
            class directLending(
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
            
            
            class embeddedLink(
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
            
            
            class embeddedPhone(
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
            
            
            class affiliateMarketing(
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
            
            
            class ageGated(
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
            mnos = schemas.DictSchema
            
            
            class referenceId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            
            
            class useCase(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            
            
            class subUseCases(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'subUseCases':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class sample1(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 255
            
            
            class sample2(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 255
            
            
            class sample3(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 255
            
            
            class sample4(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 255
            
            
            class sample5(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 255
            __annotations__ = {
                "name": name,
                "brandId": brandId,
                "order": order,
                "campaignId": campaignId,
                "subscriberOptin": subscriberOptin,
                "subscriberOptout": subscriberOptout,
                "subscriberHelp": subscriberHelp,
                "numberPool": numberPool,
                "directLending": directLending,
                "embeddedLink": embeddedLink,
                "embeddedPhone": embeddedPhone,
                "affiliateMarketing": affiliateMarketing,
                "ageGated": ageGated,
                "mnos": mnos,
                "referenceId": referenceId,
                "useCase": useCase,
                "subUseCases": subUseCases,
                "sample1": sample1,
                "sample2": sample2,
                "sample3": sample3,
                "sample4": sample4,
                "sample5": sample5,
            }
        min_properties = 1
    
    brandId: MetaOapg.properties.brandId
    name: MetaOapg.properties.name
    order: MetaOapg.properties.order
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["brandId"]) -> MetaOapg.properties.brandId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["campaignId"]) -> MetaOapg.properties.campaignId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscriberOptin"]) -> MetaOapg.properties.subscriberOptin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscriberOptout"]) -> MetaOapg.properties.subscriberOptout: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscriberHelp"]) -> MetaOapg.properties.subscriberHelp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numberPool"]) -> MetaOapg.properties.numberPool: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["directLending"]) -> MetaOapg.properties.directLending: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["embeddedLink"]) -> MetaOapg.properties.embeddedLink: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["embeddedPhone"]) -> MetaOapg.properties.embeddedPhone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["affiliateMarketing"]) -> MetaOapg.properties.affiliateMarketing: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ageGated"]) -> MetaOapg.properties.ageGated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mnos"]) -> MetaOapg.properties.mnos: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["referenceId"]) -> MetaOapg.properties.referenceId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["useCase"]) -> MetaOapg.properties.useCase: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subUseCases"]) -> MetaOapg.properties.subUseCases: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sample1"]) -> MetaOapg.properties.sample1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sample2"]) -> MetaOapg.properties.sample2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sample3"]) -> MetaOapg.properties.sample3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sample4"]) -> MetaOapg.properties.sample4: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sample5"]) -> MetaOapg.properties.sample5: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "brandId", "order", "campaignId", "subscriberOptin", "subscriberOptout", "subscriberHelp", "numberPool", "directLending", "embeddedLink", "embeddedPhone", "affiliateMarketing", "ageGated", "mnos", "referenceId", "useCase", "subUseCases", "sample1", "sample2", "sample3", "sample4", "sample5", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["brandId"]) -> MetaOapg.properties.brandId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["campaignId"]) -> typing.Union[MetaOapg.properties.campaignId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscriberOptin"]) -> typing.Union[MetaOapg.properties.subscriberOptin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscriberOptout"]) -> typing.Union[MetaOapg.properties.subscriberOptout, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscriberHelp"]) -> typing.Union[MetaOapg.properties.subscriberHelp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numberPool"]) -> typing.Union[MetaOapg.properties.numberPool, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["directLending"]) -> typing.Union[MetaOapg.properties.directLending, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["embeddedLink"]) -> typing.Union[MetaOapg.properties.embeddedLink, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["embeddedPhone"]) -> typing.Union[MetaOapg.properties.embeddedPhone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["affiliateMarketing"]) -> typing.Union[MetaOapg.properties.affiliateMarketing, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ageGated"]) -> typing.Union[MetaOapg.properties.ageGated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mnos"]) -> typing.Union[MetaOapg.properties.mnos, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["referenceId"]) -> typing.Union[MetaOapg.properties.referenceId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["useCase"]) -> typing.Union[MetaOapg.properties.useCase, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subUseCases"]) -> typing.Union[MetaOapg.properties.subUseCases, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sample1"]) -> typing.Union[MetaOapg.properties.sample1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sample2"]) -> typing.Union[MetaOapg.properties.sample2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sample3"]) -> typing.Union[MetaOapg.properties.sample3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sample4"]) -> typing.Union[MetaOapg.properties.sample4, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sample5"]) -> typing.Union[MetaOapg.properties.sample5, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "brandId", "order", "campaignId", "subscriberOptin", "subscriberOptout", "subscriberHelp", "numberPool", "directLending", "embeddedLink", "embeddedPhone", "affiliateMarketing", "ageGated", "mnos", "referenceId", "useCase", "subUseCases", "sample1", "sample2", "sample3", "sample4", "sample5", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        brandId: typing.Union[MetaOapg.properties.brandId, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        order: typing.Union[MetaOapg.properties.order, str, ],
        campaignId: typing.Union[MetaOapg.properties.campaignId, str, schemas.Unset] = schemas.unset,
        subscriberOptin: typing.Union[MetaOapg.properties.subscriberOptin, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        subscriberOptout: typing.Union[MetaOapg.properties.subscriberOptout, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        subscriberHelp: typing.Union[MetaOapg.properties.subscriberHelp, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        numberPool: typing.Union[MetaOapg.properties.numberPool, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        directLending: typing.Union[MetaOapg.properties.directLending, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        embeddedLink: typing.Union[MetaOapg.properties.embeddedLink, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        embeddedPhone: typing.Union[MetaOapg.properties.embeddedPhone, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        affiliateMarketing: typing.Union[MetaOapg.properties.affiliateMarketing, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ageGated: typing.Union[MetaOapg.properties.ageGated, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        mnos: typing.Union[MetaOapg.properties.mnos, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        referenceId: typing.Union[MetaOapg.properties.referenceId, str, schemas.Unset] = schemas.unset,
        useCase: typing.Union[MetaOapg.properties.useCase, str, schemas.Unset] = schemas.unset,
        subUseCases: typing.Union[MetaOapg.properties.subUseCases, list, tuple, schemas.Unset] = schemas.unset,
        sample1: typing.Union[MetaOapg.properties.sample1, str, schemas.Unset] = schemas.unset,
        sample2: typing.Union[MetaOapg.properties.sample2, str, schemas.Unset] = schemas.unset,
        sample3: typing.Union[MetaOapg.properties.sample3, str, schemas.Unset] = schemas.unset,
        sample4: typing.Union[MetaOapg.properties.sample4, str, schemas.Unset] = schemas.unset,
        sample5: typing.Union[MetaOapg.properties.sample5, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Messagecampaigns':
        return super().__new__(
            cls,
            *_args,
            brandId=brandId,
            name=name,
            order=order,
            campaignId=campaignId,
            subscriberOptin=subscriberOptin,
            subscriberOptout=subscriberOptout,
            subscriberHelp=subscriberHelp,
            numberPool=numberPool,
            directLending=directLending,
            embeddedLink=embeddedLink,
            embeddedPhone=embeddedPhone,
            affiliateMarketing=affiliateMarketing,
            ageGated=ageGated,
            mnos=mnos,
            referenceId=referenceId,
            useCase=useCase,
            subUseCases=subUseCases,
            sample1=sample1,
            sample2=sample2,
            sample3=sample3,
            sample4=sample4,
            sample5=sample5,
            _configuration=_configuration,
            **kwargs,
        )
