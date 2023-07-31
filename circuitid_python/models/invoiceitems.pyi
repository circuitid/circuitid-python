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


class Invoiceitems(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "amount",
            "quantity",
            "name",
            "invoice",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            amount = schemas.Int32Schema
            quantity = schemas.Int32Schema
            invoice = schemas.StrSchema
            setup = schemas.Int32Schema
            taxes = schemas.Int32Schema
            
            
            class ref(
                schemas.StrSchema
            ):
                pass
            object = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "amount": amount,
                "quantity": quantity,
                "invoice": invoice,
                "setup": setup,
                "taxes": taxes,
                "ref": ref,
                "object": object,
            }
    
    amount: MetaOapg.properties.amount
    quantity: MetaOapg.properties.quantity
    name: MetaOapg.properties.name
    invoice: MetaOapg.properties.invoice
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quantity"]) -> MetaOapg.properties.quantity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invoice"]) -> MetaOapg.properties.invoice: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["setup"]) -> MetaOapg.properties.setup: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxes"]) -> MetaOapg.properties.taxes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ref"]) -> MetaOapg.properties.ref: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "amount", "quantity", "invoice", "setup", "taxes", "ref", "object", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quantity"]) -> MetaOapg.properties.quantity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invoice"]) -> MetaOapg.properties.invoice: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["setup"]) -> typing.Union[MetaOapg.properties.setup, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxes"]) -> typing.Union[MetaOapg.properties.taxes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ref"]) -> typing.Union[MetaOapg.properties.ref, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> typing.Union[MetaOapg.properties.object, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "amount", "quantity", "invoice", "setup", "taxes", "ref", "object", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, ],
        quantity: typing.Union[MetaOapg.properties.quantity, decimal.Decimal, int, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        invoice: typing.Union[MetaOapg.properties.invoice, str, ],
        setup: typing.Union[MetaOapg.properties.setup, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        taxes: typing.Union[MetaOapg.properties.taxes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ref: typing.Union[MetaOapg.properties.ref, str, schemas.Unset] = schemas.unset,
        object: typing.Union[MetaOapg.properties.object, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Invoiceitems':
        return super().__new__(
            cls,
            *_args,
            amount=amount,
            quantity=quantity,
            name=name,
            invoice=invoice,
            setup=setup,
            taxes=taxes,
            ref=ref,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )
