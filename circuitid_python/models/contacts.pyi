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


class Contacts(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "first",
        }
        
        class properties:
            
            
            class first(
                schemas.StrSchema
            ):
                pass
            
            
            class email(
                schemas.StrSchema
            ):
                pass
            
            
            class last(
                schemas.StrSchema
            ):
                pass
            
            
            class mobilePhone(
                schemas.StrSchema
            ):
                pass
            
            
            class businessPhone(
                schemas.StrSchema
            ):
                pass
            
            
            class faxPhone(
                schemas.StrSchema
            ):
                pass
            extension = schemas.Int32Schema
            
            
            class jobTitle(
                schemas.StrSchema
            ):
                pass
            
            
            class department(
                schemas.StrSchema
            ):
                pass
            
            
            class avatar(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "first": first,
                "email": email,
                "last": last,
                "mobilePhone": mobilePhone,
                "businessPhone": businessPhone,
                "faxPhone": faxPhone,
                "extension": extension,
                "jobTitle": jobTitle,
                "department": department,
                "avatar": avatar,
            }
    
    first: MetaOapg.properties.first
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first"]) -> MetaOapg.properties.first: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last"]) -> MetaOapg.properties.last: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mobilePhone"]) -> MetaOapg.properties.mobilePhone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["businessPhone"]) -> MetaOapg.properties.businessPhone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["faxPhone"]) -> MetaOapg.properties.faxPhone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extension"]) -> MetaOapg.properties.extension: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobTitle"]) -> MetaOapg.properties.jobTitle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["department"]) -> MetaOapg.properties.department: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["avatar"]) -> MetaOapg.properties.avatar: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["first", "email", "last", "mobilePhone", "businessPhone", "faxPhone", "extension", "jobTitle", "department", "avatar", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first"]) -> MetaOapg.properties.first: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last"]) -> typing.Union[MetaOapg.properties.last, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mobilePhone"]) -> typing.Union[MetaOapg.properties.mobilePhone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["businessPhone"]) -> typing.Union[MetaOapg.properties.businessPhone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["faxPhone"]) -> typing.Union[MetaOapg.properties.faxPhone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extension"]) -> typing.Union[MetaOapg.properties.extension, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobTitle"]) -> typing.Union[MetaOapg.properties.jobTitle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["department"]) -> typing.Union[MetaOapg.properties.department, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["avatar"]) -> typing.Union[MetaOapg.properties.avatar, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["first", "email", "last", "mobilePhone", "businessPhone", "faxPhone", "extension", "jobTitle", "department", "avatar", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        first: typing.Union[MetaOapg.properties.first, str, ],
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        last: typing.Union[MetaOapg.properties.last, str, schemas.Unset] = schemas.unset,
        mobilePhone: typing.Union[MetaOapg.properties.mobilePhone, str, schemas.Unset] = schemas.unset,
        businessPhone: typing.Union[MetaOapg.properties.businessPhone, str, schemas.Unset] = schemas.unset,
        faxPhone: typing.Union[MetaOapg.properties.faxPhone, str, schemas.Unset] = schemas.unset,
        extension: typing.Union[MetaOapg.properties.extension, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        jobTitle: typing.Union[MetaOapg.properties.jobTitle, str, schemas.Unset] = schemas.unset,
        department: typing.Union[MetaOapg.properties.department, str, schemas.Unset] = schemas.unset,
        avatar: typing.Union[MetaOapg.properties.avatar, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Contacts':
        return super().__new__(
            cls,
            *_args,
            first=first,
            email=email,
            last=last,
            mobilePhone=mobilePhone,
            businessPhone=businessPhone,
            faxPhone=faxPhone,
            extension=extension,
            jobTitle=jobTitle,
            department=department,
            avatar=avatar,
            _configuration=_configuration,
            **kwargs,
        )
