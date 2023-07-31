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


class MessagebrandsCreateOrPatch(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "name",
            "ein",
            "user",
            "order",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            
            
            class ein(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 20
            user = schemas.StrSchema
            order = schemas.StrSchema
            
            
            class brandId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            
            
            class brandRelationship(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            
            
            class vertical(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            
            
            class entityType(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            
            
            class cspId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            
            
            class einIssuingCountry(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 2
            
            
            class universalEin(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            __annotations__ = {
                "name": name,
                "ein": ein,
                "user": user,
                "order": order,
                "brandId": brandId,
                "brandRelationship": brandRelationship,
                "vertical": vertical,
                "entityType": entityType,
                "cspId": cspId,
                "einIssuingCountry": einIssuingCountry,
                "universalEin": universalEin,
            }
        min_properties = 1
    
    name: MetaOapg.properties.name
    ein: MetaOapg.properties.ein
    user: MetaOapg.properties.user
    order: MetaOapg.properties.order
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ein"]) -> MetaOapg.properties.ein: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> MetaOapg.properties.user: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["brandId"]) -> MetaOapg.properties.brandId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["brandRelationship"]) -> MetaOapg.properties.brandRelationship: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vertical"]) -> MetaOapg.properties.vertical: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entityType"]) -> MetaOapg.properties.entityType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cspId"]) -> MetaOapg.properties.cspId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["einIssuingCountry"]) -> MetaOapg.properties.einIssuingCountry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["universalEin"]) -> MetaOapg.properties.universalEin: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "ein", "user", "order", "brandId", "brandRelationship", "vertical", "entityType", "cspId", "einIssuingCountry", "universalEin", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ein"]) -> MetaOapg.properties.ein: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> MetaOapg.properties.user: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["brandId"]) -> typing.Union[MetaOapg.properties.brandId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["brandRelationship"]) -> typing.Union[MetaOapg.properties.brandRelationship, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vertical"]) -> typing.Union[MetaOapg.properties.vertical, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entityType"]) -> typing.Union[MetaOapg.properties.entityType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cspId"]) -> typing.Union[MetaOapg.properties.cspId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["einIssuingCountry"]) -> typing.Union[MetaOapg.properties.einIssuingCountry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["universalEin"]) -> typing.Union[MetaOapg.properties.universalEin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "ein", "user", "order", "brandId", "brandRelationship", "vertical", "entityType", "cspId", "einIssuingCountry", "universalEin", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        ein: typing.Union[MetaOapg.properties.ein, str, ],
        user: typing.Union[MetaOapg.properties.user, str, ],
        order: typing.Union[MetaOapg.properties.order, str, ],
        brandId: typing.Union[MetaOapg.properties.brandId, str, schemas.Unset] = schemas.unset,
        brandRelationship: typing.Union[MetaOapg.properties.brandRelationship, str, schemas.Unset] = schemas.unset,
        vertical: typing.Union[MetaOapg.properties.vertical, str, schemas.Unset] = schemas.unset,
        entityType: typing.Union[MetaOapg.properties.entityType, str, schemas.Unset] = schemas.unset,
        cspId: typing.Union[MetaOapg.properties.cspId, str, schemas.Unset] = schemas.unset,
        einIssuingCountry: typing.Union[MetaOapg.properties.einIssuingCountry, str, schemas.Unset] = schemas.unset,
        universalEin: typing.Union[MetaOapg.properties.universalEin, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MessagebrandsCreateOrPatch':
        return super().__new__(
            cls,
            *_args,
            name=name,
            ein=ein,
            user=user,
            order=order,
            brandId=brandId,
            brandRelationship=brandRelationship,
            vertical=vertical,
            entityType=entityType,
            cspId=cspId,
            einIssuingCountry=einIssuingCountry,
            universalEin=universalEin,
            _configuration=_configuration,
            **kwargs,
        )
