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


class Ratecenters(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "lata",
            "locState",
            "rcAbbre",
            "npa",
            "nxx",
        }
        
        class properties:
            
            
            class npa(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 3
                    min_length = 3
            
            
            class nxx(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 3
                    min_length = 3
            
            
            class lata(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 3
                    min_length = 3
            
            
            class locState(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 2
                    min_length = 2
            
            
            class rcAbbre(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 45
            __annotations__ = {
                "npa": npa,
                "nxx": nxx,
                "lata": lata,
                "locState": locState,
                "rcAbbre": rcAbbre,
            }
        min_properties = 1
    
    lata: MetaOapg.properties.lata
    locState: MetaOapg.properties.locState
    rcAbbre: MetaOapg.properties.rcAbbre
    npa: MetaOapg.properties.npa
    nxx: MetaOapg.properties.nxx
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["npa"]) -> MetaOapg.properties.npa: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nxx"]) -> MetaOapg.properties.nxx: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lata"]) -> MetaOapg.properties.lata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locState"]) -> MetaOapg.properties.locState: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rcAbbre"]) -> MetaOapg.properties.rcAbbre: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["npa", "nxx", "lata", "locState", "rcAbbre", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["npa"]) -> MetaOapg.properties.npa: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nxx"]) -> MetaOapg.properties.nxx: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lata"]) -> MetaOapg.properties.lata: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locState"]) -> MetaOapg.properties.locState: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rcAbbre"]) -> MetaOapg.properties.rcAbbre: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["npa", "nxx", "lata", "locState", "rcAbbre", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        lata: typing.Union[MetaOapg.properties.lata, str, ],
        locState: typing.Union[MetaOapg.properties.locState, str, ],
        rcAbbre: typing.Union[MetaOapg.properties.rcAbbre, str, ],
        npa: typing.Union[MetaOapg.properties.npa, str, ],
        nxx: typing.Union[MetaOapg.properties.nxx, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Ratecenters':
        return super().__new__(
            cls,
            *_args,
            lata=lata,
            locState=locState,
            rcAbbre=rcAbbre,
            npa=npa,
            nxx=nxx,
            _configuration=_configuration,
            **kwargs,
        )
