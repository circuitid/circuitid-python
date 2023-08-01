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


class CustomersCreateOrPatch(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "defaultBillMethod",
            "name",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            
            
            class defaultBillMethod(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CREDIT(cls):
                    return cls("credit")
                
                @schemas.classproperty
                def PAYMENTMETHOD(cls):
                    return cls("paymentmethod")
            
            
            class websiteUrl(
                schemas.StrSchema
            ):
                pass
            
            
            class logo(
                schemas.StrSchema
            ):
                pass
            credit = schemas.Int32Schema
            adminUserId = schemas.StrSchema
            billingUserId = schemas.StrSchema
            callRecordingUserId = schemas.StrSchema
            supportUserId = schemas.StrSchema
            automaticRefillAmount = schemas.Int32Schema
            lowBalanceAlertAmount = schemas.Int32Schema
            
            
            class internationalCalling(
                schemas.EnumBase,
                schemas.Int32Schema
            ):
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls(1)
                
                @schemas.classproperty
                def POSITIVE_0(cls):
                    return cls(0)
            
            
            class createdByIP(
                schemas.StrSchema
            ):
                pass
            
            
            class mediaBypass(
                schemas.EnumBase,
                schemas.Int32Schema
            ):
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls(1)
                
                @schemas.classproperty
                def POSITIVE_0(cls):
                    return cls(0)
            
            
            class accountLock(
                schemas.EnumBase,
                schemas.Int32Schema
            ):
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls(1)
                
                @schemas.classproperty
                def POSITIVE_0(cls):
                    return cls(0)
            
            
            class callRecording(
                schemas.EnumBase,
                schemas.Int32Schema
            ):
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls(1)
                
                @schemas.classproperty
                def POSITIVE_0(cls):
                    return cls(0)
            cdrRetention = schemas.Int32Schema
            
            
            class cnamLookUps(
                schemas.EnumBase,
                schemas.Int32Schema
            ):
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls(1)
                
                @schemas.classproperty
                def POSITIVE_0(cls):
                    return cls(0)
            
            
            class holdMusic(
                schemas.EnumBase,
                schemas.Int32Schema
            ):
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls(1)
                
                @schemas.classproperty
                def POSITIVE_0(cls):
                    return cls(0)
            
            
            class transcribeCalls(
                schemas.EnumBase,
                schemas.Int32Schema
            ):
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls(1)
                
                @schemas.classproperty
                def POSITIVE_0(cls):
                    return cls(0)
            maxOutboundCallRate = schemas.Int32Schema
            __annotations__ = {
                "name": name,
                "defaultBillMethod": defaultBillMethod,
                "websiteUrl": websiteUrl,
                "logo": logo,
                "credit": credit,
                "adminUserId": adminUserId,
                "billingUserId": billingUserId,
                "callRecordingUserId": callRecordingUserId,
                "supportUserId": supportUserId,
                "automaticRefillAmount": automaticRefillAmount,
                "lowBalanceAlertAmount": lowBalanceAlertAmount,
                "internationalCalling": internationalCalling,
                "createdByIP": createdByIP,
                "mediaBypass": mediaBypass,
                "accountLock": accountLock,
                "callRecording": callRecording,
                "cdrRetention": cdrRetention,
                "cnamLookUps": cnamLookUps,
                "holdMusic": holdMusic,
                "transcribeCalls": transcribeCalls,
                "maxOutboundCallRate": maxOutboundCallRate,
            }
    
    defaultBillMethod: MetaOapg.properties.defaultBillMethod
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultBillMethod"]) -> MetaOapg.properties.defaultBillMethod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["websiteUrl"]) -> MetaOapg.properties.websiteUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logo"]) -> MetaOapg.properties.logo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["credit"]) -> MetaOapg.properties.credit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["adminUserId"]) -> MetaOapg.properties.adminUserId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billingUserId"]) -> MetaOapg.properties.billingUserId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["callRecordingUserId"]) -> MetaOapg.properties.callRecordingUserId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supportUserId"]) -> MetaOapg.properties.supportUserId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["automaticRefillAmount"]) -> MetaOapg.properties.automaticRefillAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lowBalanceAlertAmount"]) -> MetaOapg.properties.lowBalanceAlertAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["internationalCalling"]) -> MetaOapg.properties.internationalCalling: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdByIP"]) -> MetaOapg.properties.createdByIP: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mediaBypass"]) -> MetaOapg.properties.mediaBypass: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountLock"]) -> MetaOapg.properties.accountLock: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["callRecording"]) -> MetaOapg.properties.callRecording: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cdrRetention"]) -> MetaOapg.properties.cdrRetention: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cnamLookUps"]) -> MetaOapg.properties.cnamLookUps: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["holdMusic"]) -> MetaOapg.properties.holdMusic: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transcribeCalls"]) -> MetaOapg.properties.transcribeCalls: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxOutboundCallRate"]) -> MetaOapg.properties.maxOutboundCallRate: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "defaultBillMethod", "websiteUrl", "logo", "credit", "adminUserId", "billingUserId", "callRecordingUserId", "supportUserId", "automaticRefillAmount", "lowBalanceAlertAmount", "internationalCalling", "createdByIP", "mediaBypass", "accountLock", "callRecording", "cdrRetention", "cnamLookUps", "holdMusic", "transcribeCalls", "maxOutboundCallRate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultBillMethod"]) -> MetaOapg.properties.defaultBillMethod: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["websiteUrl"]) -> typing.Union[MetaOapg.properties.websiteUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logo"]) -> typing.Union[MetaOapg.properties.logo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["credit"]) -> typing.Union[MetaOapg.properties.credit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["adminUserId"]) -> typing.Union[MetaOapg.properties.adminUserId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billingUserId"]) -> typing.Union[MetaOapg.properties.billingUserId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["callRecordingUserId"]) -> typing.Union[MetaOapg.properties.callRecordingUserId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supportUserId"]) -> typing.Union[MetaOapg.properties.supportUserId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["automaticRefillAmount"]) -> typing.Union[MetaOapg.properties.automaticRefillAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lowBalanceAlertAmount"]) -> typing.Union[MetaOapg.properties.lowBalanceAlertAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["internationalCalling"]) -> typing.Union[MetaOapg.properties.internationalCalling, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdByIP"]) -> typing.Union[MetaOapg.properties.createdByIP, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mediaBypass"]) -> typing.Union[MetaOapg.properties.mediaBypass, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountLock"]) -> typing.Union[MetaOapg.properties.accountLock, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["callRecording"]) -> typing.Union[MetaOapg.properties.callRecording, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cdrRetention"]) -> typing.Union[MetaOapg.properties.cdrRetention, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cnamLookUps"]) -> typing.Union[MetaOapg.properties.cnamLookUps, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["holdMusic"]) -> typing.Union[MetaOapg.properties.holdMusic, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transcribeCalls"]) -> typing.Union[MetaOapg.properties.transcribeCalls, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxOutboundCallRate"]) -> typing.Union[MetaOapg.properties.maxOutboundCallRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "defaultBillMethod", "websiteUrl", "logo", "credit", "adminUserId", "billingUserId", "callRecordingUserId", "supportUserId", "automaticRefillAmount", "lowBalanceAlertAmount", "internationalCalling", "createdByIP", "mediaBypass", "accountLock", "callRecording", "cdrRetention", "cnamLookUps", "holdMusic", "transcribeCalls", "maxOutboundCallRate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        defaultBillMethod: typing.Union[MetaOapg.properties.defaultBillMethod, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        websiteUrl: typing.Union[MetaOapg.properties.websiteUrl, str, schemas.Unset] = schemas.unset,
        logo: typing.Union[MetaOapg.properties.logo, str, schemas.Unset] = schemas.unset,
        credit: typing.Union[MetaOapg.properties.credit, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        adminUserId: typing.Union[MetaOapg.properties.adminUserId, str, schemas.Unset] = schemas.unset,
        billingUserId: typing.Union[MetaOapg.properties.billingUserId, str, schemas.Unset] = schemas.unset,
        callRecordingUserId: typing.Union[MetaOapg.properties.callRecordingUserId, str, schemas.Unset] = schemas.unset,
        supportUserId: typing.Union[MetaOapg.properties.supportUserId, str, schemas.Unset] = schemas.unset,
        automaticRefillAmount: typing.Union[MetaOapg.properties.automaticRefillAmount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        lowBalanceAlertAmount: typing.Union[MetaOapg.properties.lowBalanceAlertAmount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        internationalCalling: typing.Union[MetaOapg.properties.internationalCalling, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        createdByIP: typing.Union[MetaOapg.properties.createdByIP, str, schemas.Unset] = schemas.unset,
        mediaBypass: typing.Union[MetaOapg.properties.mediaBypass, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        accountLock: typing.Union[MetaOapg.properties.accountLock, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        callRecording: typing.Union[MetaOapg.properties.callRecording, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        cdrRetention: typing.Union[MetaOapg.properties.cdrRetention, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        cnamLookUps: typing.Union[MetaOapg.properties.cnamLookUps, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        holdMusic: typing.Union[MetaOapg.properties.holdMusic, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        transcribeCalls: typing.Union[MetaOapg.properties.transcribeCalls, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        maxOutboundCallRate: typing.Union[MetaOapg.properties.maxOutboundCallRate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomersCreateOrPatch':
        return super().__new__(
            cls,
            *_args,
            defaultBillMethod=defaultBillMethod,
            name=name,
            websiteUrl=websiteUrl,
            logo=logo,
            credit=credit,
            adminUserId=adminUserId,
            billingUserId=billingUserId,
            callRecordingUserId=callRecordingUserId,
            supportUserId=supportUserId,
            automaticRefillAmount=automaticRefillAmount,
            lowBalanceAlertAmount=lowBalanceAlertAmount,
            internationalCalling=internationalCalling,
            createdByIP=createdByIP,
            mediaBypass=mediaBypass,
            accountLock=accountLock,
            callRecording=callRecording,
            cdrRetention=cdrRetention,
            cnamLookUps=cnamLookUps,
            holdMusic=holdMusic,
            transcribeCalls=transcribeCalls,
            maxOutboundCallRate=maxOutboundCallRate,
            _configuration=_configuration,
            **kwargs,
        )
