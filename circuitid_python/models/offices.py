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


class Offices(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "country",
            "streetName",
            "city",
            "streetNumber",
            "name",
            "streetSuffix",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            
            
            class streetNumber(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            
            
            class streetName(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 20
            
            
            class streetSuffix(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 4
                    min_length = 2
            
            
            class city(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            
            
            class country(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 2
                    min_length = 2
            
            
            class preDirection(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 2
            
            
            class state(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            
            
            class zipCode(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            
            
            class address2(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            region = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "streetNumber": streetNumber,
                "streetName": streetName,
                "streetSuffix": streetSuffix,
                "city": city,
                "country": country,
                "preDirection": preDirection,
                "state": state,
                "zipCode": zipCode,
                "address2": address2,
                "region": region,
            }
        min_properties = 1
    
    country: MetaOapg.properties.country
    streetName: MetaOapg.properties.streetName
    city: MetaOapg.properties.city
    streetNumber: MetaOapg.properties.streetNumber
    name: MetaOapg.properties.name
    streetSuffix: MetaOapg.properties.streetSuffix
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["streetNumber"]) -> MetaOapg.properties.streetNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["streetName"]) -> MetaOapg.properties.streetName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["streetSuffix"]) -> MetaOapg.properties.streetSuffix: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preDirection"]) -> MetaOapg.properties.preDirection: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zipCode"]) -> MetaOapg.properties.zipCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address2"]) -> MetaOapg.properties.address2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["region"]) -> MetaOapg.properties.region: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "streetNumber", "streetName", "streetSuffix", "city", "country", "preDirection", "state", "zipCode", "address2", "region", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["streetNumber"]) -> MetaOapg.properties.streetNumber: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["streetName"]) -> MetaOapg.properties.streetName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["streetSuffix"]) -> MetaOapg.properties.streetSuffix: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preDirection"]) -> typing.Union[MetaOapg.properties.preDirection, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zipCode"]) -> typing.Union[MetaOapg.properties.zipCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address2"]) -> typing.Union[MetaOapg.properties.address2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["region"]) -> typing.Union[MetaOapg.properties.region, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "streetNumber", "streetName", "streetSuffix", "city", "country", "preDirection", "state", "zipCode", "address2", "region", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        country: typing.Union[MetaOapg.properties.country, str, ],
        streetName: typing.Union[MetaOapg.properties.streetName, str, ],
        city: typing.Union[MetaOapg.properties.city, str, ],
        streetNumber: typing.Union[MetaOapg.properties.streetNumber, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        streetSuffix: typing.Union[MetaOapg.properties.streetSuffix, str, ],
        preDirection: typing.Union[MetaOapg.properties.preDirection, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        zipCode: typing.Union[MetaOapg.properties.zipCode, str, schemas.Unset] = schemas.unset,
        address2: typing.Union[MetaOapg.properties.address2, str, schemas.Unset] = schemas.unset,
        region: typing.Union[MetaOapg.properties.region, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Offices':
        return super().__new__(
            cls,
            *_args,
            country=country,
            streetName=streetName,
            city=city,
            streetNumber=streetNumber,
            name=name,
            streetSuffix=streetSuffix,
            preDirection=preDirection,
            state=state,
            zipCode=zipCode,
            address2=address2,
            region=region,
            _configuration=_configuration,
            **kwargs,
        )
