<a id="__pageTop"></a>
# circuitid_python.api.tags.holidays_api.HolidaysApi

All URIs are relative to *https://cloud9.circuitid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_holiday**](#create_holiday) | **post** /holidays | Create a new object
[**find_holidays**](#find_holidays) | **get** /holidays | Find multiple objects
[**get_holiday**](#get_holiday) | **get** /holidays/{id} | Get object by id
[**patch_holiday**](#patch_holiday) | **patch** /holidays/{id} | Patch object&#x27;s data
[**remove_holiday**](#remove_holiday) | **delete** /holidays/{id} | Delete object by id

# **create_holiday**
<a id="create_holiday"></a>
> bool, date, datetime, dict, float, int, list, str, none_type create_holiday(holidays_create_or_patch)

Create a new object

Add a new object to the system.

### Example

* Api Key Authentication (jwt):
```python
import circuitid_python
from circuitid_python.api.tags import holidays_api
from circuitid_python.models.response_error import ResponseError
from circuitid_python.models.holidays import Holidays
from circuitid_python.models.id import Id
from circuitid_python.models.response_date import ResponseDate
from circuitid_python.models.response_users import ResponseUsers
from circuitid_python.models.holidays_create_or_patch import HolidaysCreateOrPatch
from pprint import pprint
# Defining the host is optional and defaults to https://cloud9.circuitid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = circuitid_python.Configuration(
    host = "https://cloud9.circuitid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'
# Enter a context with an instance of the API client
with circuitid_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = holidays_api.HolidaysApi(api_client)

    # example passing only required values which don't have defaults set
    body = HolidaysCreateOrPatch(
        name="name_example",
        object="object_example",
        object_ref="object_ref_example",
        date_time_ranges=[
            [
                "1970-01-01T00:00:00.00Z"
            ]
        ],
        status=1,
        destination_type="announcements",
        destination="destination_example",
        ref="ref_example",
        call_forwarding_destination="call_forwarding_destination_example",
    )
    try:
        # Create a new object
        api_response = api_instance.create_holiday(
            body=body,
        )
        pprint(api_response)
    except circuitid_python.ApiException as e:
        print("Exception when calling HolidaysApi->create_holiday: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HolidaysCreateOrPatch**](../../models/HolidaysCreateOrPatch.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_holiday.ApiResponseFor200) | A JSON object containing the new object created
400 | [ApiResponseFor400](#create_holiday.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#create_holiday.ApiResponseFor401) | Not Authenticated
403 | [ApiResponseFor403](#create_holiday.ApiResponseFor403) | Forbidden
405 | [ApiResponseFor405](#create_holiday.ApiResponseFor405) | Method Not Allowed
406 | [ApiResponseFor406](#create_holiday.ApiResponseFor406) | Not Acceptable
408 | [ApiResponseFor408](#create_holiday.ApiResponseFor408) | Timeout
429 | [ApiResponseFor429](#create_holiday.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#create_holiday.ApiResponseFor500) | General Error
503 | [ApiResponseFor503](#create_holiday.ApiResponseFor503) | Unavailable

#### create_holiday.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Holidays]({{complexTypePrefix}}Holidays.md) | [**Holidays**]({{complexTypePrefix}}Holidays.md) | [**Holidays**]({{complexTypePrefix}}Holidays.md) |  | 
[Id]({{complexTypePrefix}}Id.md) | [**Id**]({{complexTypePrefix}}Id.md) | [**Id**]({{complexTypePrefix}}Id.md) |  | 
[ResponseUsers]({{complexTypePrefix}}ResponseUsers.md) | [**ResponseUsers**]({{complexTypePrefix}}ResponseUsers.md) | [**ResponseUsers**]({{complexTypePrefix}}ResponseUsers.md) |  | 
[ResponseDate]({{complexTypePrefix}}ResponseDate.md) | [**ResponseDate**]({{complexTypePrefix}}ResponseDate.md) | [**ResponseDate**]({{complexTypePrefix}}ResponseDate.md) |  | 

#### create_holiday.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### create_holiday.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### create_holiday.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### create_holiday.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor405ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor405ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### create_holiday.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor406ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor406ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### create_holiday.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### create_holiday.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### create_holiday.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### create_holiday.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


### Authorization

[jwt](../../../README.md#jwt)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **find_holidays**
<a id="find_holidays"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} find_holidays()

Find multiple objects

Search and retrieve multiple objects simultaneously. 

### Example

* Api Key Authentication (jwt):
```python
import circuitid_python
from circuitid_python.api.tags import holidays_api
from circuitid_python.models.response_error import ResponseError
from circuitid_python.models.holidays import Holidays
from circuitid_python.models.id import Id
from circuitid_python.models.response_date import ResponseDate
from circuitid_python.models.response_users import ResponseUsers
from pprint import pprint
# Defining the host is optional and defaults to https://cloud9.circuitid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = circuitid_python.Configuration(
    host = "https://cloud9.circuitid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'
# Enter a context with an instance of the API client
with circuitid_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = holidays_api.HolidaysApi(api_client)

    # example passing only optional values
    query_params = {
        '$search': "$search_example",
        '$limit': 1,
        '$skip': 1,
        '$sort': dict(),
        '$select': [
        "$select_example"
    ],
        '$or': [
        dict()
    ],
        '$and': [
        dict()
    ],
    }
    try:
        # Find multiple objects
        api_response = api_instance.find_holidays(
            query_params=query_params,
        )
        pprint(api_response)
    except circuitid_python.ApiException as e:
        print("Exception when calling HolidaysApi->find_holidays: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
$search | SearchSchema | | optional
$limit | LimitSchema | | optional
$skip | SkipSchema | | optional
$sort | SortSchema | | optional
$select | SelectSchema | | optional
$or | ModelOrSchema | | optional
$and | ModelAndSchema | | optional


# SearchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# SkipSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# SelectSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# ModelOrSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# ModelAndSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#find_holidays.ApiResponseFor200) | A JSON object containing the requested data
400 | [ApiResponseFor400](#find_holidays.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#find_holidays.ApiResponseFor401) | Not Authenticated
403 | [ApiResponseFor403](#find_holidays.ApiResponseFor403) | Forbidden
405 | [ApiResponseFor405](#find_holidays.ApiResponseFor405) | Method Not Allowed
406 | [ApiResponseFor406](#find_holidays.ApiResponseFor406) | Not Acceptable
408 | [ApiResponseFor408](#find_holidays.ApiResponseFor408) | Timeout
429 | [ApiResponseFor429](#find_holidays.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#find_holidays.ApiResponseFor500) | General Error
503 | [ApiResponseFor503](#find_holidays.ApiResponseFor503) | Unavailable

#### find_holidays.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer
**[data](#data)** | list, tuple,  | tuple,  |  | 
**limit** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer
**skip** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Holidays]({{complexTypePrefix}}Holidays.md) | [**Holidays**]({{complexTypePrefix}}Holidays.md) | [**Holidays**]({{complexTypePrefix}}Holidays.md) |  | 
[Id]({{complexTypePrefix}}Id.md) | [**Id**]({{complexTypePrefix}}Id.md) | [**Id**]({{complexTypePrefix}}Id.md) |  | 
[ResponseUsers]({{complexTypePrefix}}ResponseUsers.md) | [**ResponseUsers**]({{complexTypePrefix}}ResponseUsers.md) | [**ResponseUsers**]({{complexTypePrefix}}ResponseUsers.md) |  | 
[ResponseDate]({{complexTypePrefix}}ResponseDate.md) | [**ResponseDate**]({{complexTypePrefix}}ResponseDate.md) | [**ResponseDate**]({{complexTypePrefix}}ResponseDate.md) |  | 

#### find_holidays.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### find_holidays.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### find_holidays.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### find_holidays.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor405ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor405ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### find_holidays.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor406ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor406ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### find_holidays.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### find_holidays.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### find_holidays.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### find_holidays.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


### Authorization

[jwt](../../../README.md#jwt)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_holiday**
<a id="get_holiday"></a>
> bool, date, datetime, dict, float, int, list, str, none_type get_holiday(id)

Get object by id

Get an object from the REST API Endpoint by its unique id.

### Example

* Api Key Authentication (jwt):
```python
import circuitid_python
from circuitid_python.api.tags import holidays_api
from circuitid_python.models.response_error import ResponseError
from circuitid_python.models.holidays import Holidays
from circuitid_python.models.id import Id
from circuitid_python.models.response_date import ResponseDate
from circuitid_python.models.response_users import ResponseUsers
from pprint import pprint
# Defining the host is optional and defaults to https://cloud9.circuitid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = circuitid_python.Configuration(
    host = "https://cloud9.circuitid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'
# Enter a context with an instance of the API client
with circuitid_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = holidays_api.HolidaysApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Get object by id
        api_response = api_instance.get_holiday(
            path_params=path_params,
        )
        pprint(api_response)
    except circuitid_python.ApiException as e:
        print("Exception when calling HolidaysApi->get_holiday: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_holiday.ApiResponseFor200) | A JSON object containing the requested data.
400 | [ApiResponseFor400](#get_holiday.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_holiday.ApiResponseFor401) | Not Authenticated
403 | [ApiResponseFor403](#get_holiday.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_holiday.ApiResponseFor404) | Not Found
405 | [ApiResponseFor405](#get_holiday.ApiResponseFor405) | Method Not Allowed
406 | [ApiResponseFor406](#get_holiday.ApiResponseFor406) | Not Acceptable
408 | [ApiResponseFor408](#get_holiday.ApiResponseFor408) | Timeout
429 | [ApiResponseFor429](#get_holiday.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#get_holiday.ApiResponseFor500) | General Error
503 | [ApiResponseFor503](#get_holiday.ApiResponseFor503) | Unavailable

#### get_holiday.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Holidays]({{complexTypePrefix}}Holidays.md) | [**Holidays**]({{complexTypePrefix}}Holidays.md) | [**Holidays**]({{complexTypePrefix}}Holidays.md) |  | 
[Id]({{complexTypePrefix}}Id.md) | [**Id**]({{complexTypePrefix}}Id.md) | [**Id**]({{complexTypePrefix}}Id.md) |  | 
[ResponseUsers]({{complexTypePrefix}}ResponseUsers.md) | [**ResponseUsers**]({{complexTypePrefix}}ResponseUsers.md) | [**ResponseUsers**]({{complexTypePrefix}}ResponseUsers.md) |  | 
[ResponseDate]({{complexTypePrefix}}ResponseDate.md) | [**ResponseDate**]({{complexTypePrefix}}ResponseDate.md) | [**ResponseDate**]({{complexTypePrefix}}ResponseDate.md) |  | 

#### get_holiday.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### get_holiday.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### get_holiday.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### get_holiday.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### get_holiday.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor405ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor405ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### get_holiday.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor406ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor406ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### get_holiday.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### get_holiday.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### get_holiday.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### get_holiday.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


### Authorization

[jwt](../../../README.md#jwt)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_holiday**
<a id="patch_holiday"></a>
> bool, date, datetime, dict, float, int, list, str, none_type patch_holiday(idholidays_create_or_patch)

Patch object's data

Make updates to specific fields within the record without replacing the entire dataset.

### Example

* Api Key Authentication (jwt):
```python
import circuitid_python
from circuitid_python.api.tags import holidays_api
from circuitid_python.models.response_error import ResponseError
from circuitid_python.models.holidays import Holidays
from circuitid_python.models.id import Id
from circuitid_python.models.response_date import ResponseDate
from circuitid_python.models.response_users import ResponseUsers
from circuitid_python.models.holidays_create_or_patch import HolidaysCreateOrPatch
from pprint import pprint
# Defining the host is optional and defaults to https://cloud9.circuitid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = circuitid_python.Configuration(
    host = "https://cloud9.circuitid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'
# Enter a context with an instance of the API client
with circuitid_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = holidays_api.HolidaysApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    body = HolidaysCreateOrPatch(
        name="name_example",
        object="object_example",
        object_ref="object_ref_example",
        date_time_ranges=[
            [
                "1970-01-01T00:00:00.00Z"
            ]
        ],
        status=1,
        destination_type="announcements",
        destination="destination_example",
        ref="ref_example",
        call_forwarding_destination="call_forwarding_destination_example",
    )
    try:
        # Patch object's data
        api_response = api_instance.patch_holiday(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except circuitid_python.ApiException as e:
        print("Exception when calling HolidaysApi->patch_holiday: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HolidaysCreateOrPatch**](../../models/HolidaysCreateOrPatch.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#patch_holiday.ApiResponseFor200) | A JSON object containing the modified data.
400 | [ApiResponseFor400](#patch_holiday.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#patch_holiday.ApiResponseFor401) | Not Authenticated
403 | [ApiResponseFor403](#patch_holiday.ApiResponseFor403) | Forbidden
405 | [ApiResponseFor405](#patch_holiday.ApiResponseFor405) | Method Not Allowed
406 | [ApiResponseFor406](#patch_holiday.ApiResponseFor406) | Not Acceptable
408 | [ApiResponseFor408](#patch_holiday.ApiResponseFor408) | Timeout
429 | [ApiResponseFor429](#patch_holiday.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#patch_holiday.ApiResponseFor500) | General Error
503 | [ApiResponseFor503](#patch_holiday.ApiResponseFor503) | Unavailable

#### patch_holiday.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Holidays]({{complexTypePrefix}}Holidays.md) | [**Holidays**]({{complexTypePrefix}}Holidays.md) | [**Holidays**]({{complexTypePrefix}}Holidays.md) |  | 
[Id]({{complexTypePrefix}}Id.md) | [**Id**]({{complexTypePrefix}}Id.md) | [**Id**]({{complexTypePrefix}}Id.md) |  | 
[ResponseUsers]({{complexTypePrefix}}ResponseUsers.md) | [**ResponseUsers**]({{complexTypePrefix}}ResponseUsers.md) | [**ResponseUsers**]({{complexTypePrefix}}ResponseUsers.md) |  | 
[ResponseDate]({{complexTypePrefix}}ResponseDate.md) | [**ResponseDate**]({{complexTypePrefix}}ResponseDate.md) | [**ResponseDate**]({{complexTypePrefix}}ResponseDate.md) |  | 

#### patch_holiday.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### patch_holiday.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### patch_holiday.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### patch_holiday.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor405ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor405ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### patch_holiday.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor406ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor406ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### patch_holiday.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### patch_holiday.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### patch_holiday.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### patch_holiday.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


### Authorization

[jwt](../../../README.md#jwt)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **remove_holiday**
<a id="remove_holiday"></a>
> bool, date, datetime, dict, float, int, list, str, none_type remove_holiday(id)

Delete object by id

Delete an object by id, removing it from the service.

### Example

* Api Key Authentication (jwt):
```python
import circuitid_python
from circuitid_python.api.tags import holidays_api
from circuitid_python.models.response_error import ResponseError
from circuitid_python.models.holidays import Holidays
from circuitid_python.models.id import Id
from circuitid_python.models.response_date import ResponseDate
from circuitid_python.models.response_users import ResponseUsers
from pprint import pprint
# Defining the host is optional and defaults to https://cloud9.circuitid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = circuitid_python.Configuration(
    host = "https://cloud9.circuitid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'
# Enter a context with an instance of the API client
with circuitid_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = holidays_api.HolidaysApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Delete object by id
        api_response = api_instance.remove_holiday(
            path_params=path_params,
        )
        pprint(api_response)
    except circuitid_python.ApiException as e:
        print("Exception when calling HolidaysApi->remove_holiday: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#remove_holiday.ApiResponseFor200) | A JSON object containing the deleted data.
400 | [ApiResponseFor400](#remove_holiday.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#remove_holiday.ApiResponseFor401) | Not Authenticated
403 | [ApiResponseFor403](#remove_holiday.ApiResponseFor403) | Forbidden
405 | [ApiResponseFor405](#remove_holiday.ApiResponseFor405) | Method Not Allowed
406 | [ApiResponseFor406](#remove_holiday.ApiResponseFor406) | Not Acceptable
408 | [ApiResponseFor408](#remove_holiday.ApiResponseFor408) | Timeout
429 | [ApiResponseFor429](#remove_holiday.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#remove_holiday.ApiResponseFor500) | General Error
503 | [ApiResponseFor503](#remove_holiday.ApiResponseFor503) | Unavailable

#### remove_holiday.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Holidays]({{complexTypePrefix}}Holidays.md) | [**Holidays**]({{complexTypePrefix}}Holidays.md) | [**Holidays**]({{complexTypePrefix}}Holidays.md) |  | 
[Id]({{complexTypePrefix}}Id.md) | [**Id**]({{complexTypePrefix}}Id.md) | [**Id**]({{complexTypePrefix}}Id.md) |  | 
[ResponseUsers]({{complexTypePrefix}}ResponseUsers.md) | [**ResponseUsers**]({{complexTypePrefix}}ResponseUsers.md) | [**ResponseUsers**]({{complexTypePrefix}}ResponseUsers.md) |  | 
[ResponseDate]({{complexTypePrefix}}ResponseDate.md) | [**ResponseDate**]({{complexTypePrefix}}ResponseDate.md) | [**ResponseDate**]({{complexTypePrefix}}ResponseDate.md) |  | 

#### remove_holiday.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### remove_holiday.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### remove_holiday.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### remove_holiday.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor405ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor405ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### remove_holiday.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor406ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor406ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### remove_holiday.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### remove_holiday.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### remove_holiday.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### remove_holiday.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


### Authorization

[jwt](../../../README.md#jwt)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

