<a id="__pageTop"></a>
# circuitid_python.api.tags.firewall_api.FirewallApi

All URIs are relative to *https://rest.circuitid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_firewall**](#create_firewall) | **post** /firewall | Create a new object
[**find_firewall**](#find_firewall) | **get** /firewall | Find multiple objects
[**get_firewall**](#get_firewall) | **get** /firewall/{id} | Get object by id
[**patch_firewall**](#patch_firewall) | **patch** /firewall/{id} | Patch object&#x27;s data
[**remove_firewall**](#remove_firewall) | **delete** /firewall/{id} | Delete object by id

# **create_firewall**
<a id="create_firewall"></a>
> bool, date, datetime, dict, float, int, list, str, none_type create_firewall(firewall_create_or_patch)

Create a new object

Add a new object to the system.

### Example

* Api Key Authentication (jwt):
```python
import circuitid_python
from circuitid_python.api.tags import firewall_api
from circuitid_python.models.firewall_create_or_patch import FirewallCreateOrPatch
from circuitid_python.models.response_error import ResponseError
from circuitid_python.models.firewall import Firewall
from circuitid_python.models.id import Id
from circuitid_python.models.response_date import ResponseDate
from circuitid_python.models.response_users import ResponseUsers
from pprint import pprint
# Defining the host is optional and defaults to https://rest.circuitid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = circuitid_python.Configuration(
    host = "https://rest.circuitid.com"
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
    api_instance = firewall_api.FirewallApi(api_client)

    # example passing only required values which don't have defaults set
    body = FirewallCreateOrPatch(
        name="name_example",
        description="description_example",
        type="allow",
        target="numbers",
        direction="inbound",
        param="param_example",
        status=1,
    )
    try:
        # Create a new object
        api_response = api_instance.create_firewall(
            body=body,
        )
        pprint(api_response)
    except circuitid_python.ApiException as e:
        print("Exception when calling FirewallApi->create_firewall: %s\n" % e)
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
[**FirewallCreateOrPatch**](../../models/FirewallCreateOrPatch.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_firewall.ApiResponseFor200) | A JSON object containing the new object created
400 | [ApiResponseFor400](#create_firewall.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#create_firewall.ApiResponseFor401) | Not Authenticated
403 | [ApiResponseFor403](#create_firewall.ApiResponseFor403) | Forbidden
405 | [ApiResponseFor405](#create_firewall.ApiResponseFor405) | Method Not Allowed
406 | [ApiResponseFor406](#create_firewall.ApiResponseFor406) | Not Acceptable
408 | [ApiResponseFor408](#create_firewall.ApiResponseFor408) | Timeout
429 | [ApiResponseFor429](#create_firewall.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#create_firewall.ApiResponseFor500) | General Error
503 | [ApiResponseFor503](#create_firewall.ApiResponseFor503) | Unavailable

#### create_firewall.ApiResponseFor200
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
[Firewall]({{complexTypePrefix}}Firewall.md) | [**Firewall**]({{complexTypePrefix}}Firewall.md) | [**Firewall**]({{complexTypePrefix}}Firewall.md) |  | 
[Id]({{complexTypePrefix}}Id.md) | [**Id**]({{complexTypePrefix}}Id.md) | [**Id**]({{complexTypePrefix}}Id.md) |  | 
[ResponseUsers]({{complexTypePrefix}}ResponseUsers.md) | [**ResponseUsers**]({{complexTypePrefix}}ResponseUsers.md) | [**ResponseUsers**]({{complexTypePrefix}}ResponseUsers.md) |  | 
[ResponseDate]({{complexTypePrefix}}ResponseDate.md) | [**ResponseDate**]({{complexTypePrefix}}ResponseDate.md) | [**ResponseDate**]({{complexTypePrefix}}ResponseDate.md) |  | 

#### create_firewall.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### create_firewall.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### create_firewall.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### create_firewall.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor405ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor405ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### create_firewall.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor406ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor406ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### create_firewall.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### create_firewall.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### create_firewall.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### create_firewall.ApiResponseFor503
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

# **find_firewall**
<a id="find_firewall"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} find_firewall()

Find multiple objects

Search and retrieve multiple objects simultaneously. 

### Example

* Api Key Authentication (jwt):
```python
import circuitid_python
from circuitid_python.api.tags import firewall_api
from circuitid_python.models.response_error import ResponseError
from circuitid_python.models.firewall import Firewall
from circuitid_python.models.id import Id
from circuitid_python.models.response_date import ResponseDate
from circuitid_python.models.response_users import ResponseUsers
from pprint import pprint
# Defining the host is optional and defaults to https://rest.circuitid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = circuitid_python.Configuration(
    host = "https://rest.circuitid.com"
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
    api_instance = firewall_api.FirewallApi(api_client)

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
        api_response = api_instance.find_firewall(
            query_params=query_params,
        )
        pprint(api_response)
    except circuitid_python.ApiException as e:
        print("Exception when calling FirewallApi->find_firewall: %s\n" % e)
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
200 | [ApiResponseFor200](#find_firewall.ApiResponseFor200) | A JSON object containing the requested data
400 | [ApiResponseFor400](#find_firewall.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#find_firewall.ApiResponseFor401) | Not Authenticated
403 | [ApiResponseFor403](#find_firewall.ApiResponseFor403) | Forbidden
405 | [ApiResponseFor405](#find_firewall.ApiResponseFor405) | Method Not Allowed
406 | [ApiResponseFor406](#find_firewall.ApiResponseFor406) | Not Acceptable
408 | [ApiResponseFor408](#find_firewall.ApiResponseFor408) | Timeout
429 | [ApiResponseFor429](#find_firewall.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#find_firewall.ApiResponseFor500) | General Error
503 | [ApiResponseFor503](#find_firewall.ApiResponseFor503) | Unavailable

#### find_firewall.ApiResponseFor200
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
[Firewall]({{complexTypePrefix}}Firewall.md) | [**Firewall**]({{complexTypePrefix}}Firewall.md) | [**Firewall**]({{complexTypePrefix}}Firewall.md) |  | 
[Id]({{complexTypePrefix}}Id.md) | [**Id**]({{complexTypePrefix}}Id.md) | [**Id**]({{complexTypePrefix}}Id.md) |  | 
[ResponseUsers]({{complexTypePrefix}}ResponseUsers.md) | [**ResponseUsers**]({{complexTypePrefix}}ResponseUsers.md) | [**ResponseUsers**]({{complexTypePrefix}}ResponseUsers.md) |  | 
[ResponseDate]({{complexTypePrefix}}ResponseDate.md) | [**ResponseDate**]({{complexTypePrefix}}ResponseDate.md) | [**ResponseDate**]({{complexTypePrefix}}ResponseDate.md) |  | 

#### find_firewall.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### find_firewall.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### find_firewall.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### find_firewall.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor405ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor405ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### find_firewall.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor406ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor406ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### find_firewall.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### find_firewall.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### find_firewall.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### find_firewall.ApiResponseFor503
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

# **get_firewall**
<a id="get_firewall"></a>
> bool, date, datetime, dict, float, int, list, str, none_type get_firewall(id)

Get object by id

Get an object from the REST API Endpoint by its unique id.

### Example

* Api Key Authentication (jwt):
```python
import circuitid_python
from circuitid_python.api.tags import firewall_api
from circuitid_python.models.response_error import ResponseError
from circuitid_python.models.firewall import Firewall
from circuitid_python.models.id import Id
from circuitid_python.models.response_date import ResponseDate
from circuitid_python.models.response_users import ResponseUsers
from pprint import pprint
# Defining the host is optional and defaults to https://rest.circuitid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = circuitid_python.Configuration(
    host = "https://rest.circuitid.com"
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
    api_instance = firewall_api.FirewallApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Get object by id
        api_response = api_instance.get_firewall(
            path_params=path_params,
        )
        pprint(api_response)
    except circuitid_python.ApiException as e:
        print("Exception when calling FirewallApi->get_firewall: %s\n" % e)
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
200 | [ApiResponseFor200](#get_firewall.ApiResponseFor200) | A JSON object containing the requested data.
400 | [ApiResponseFor400](#get_firewall.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_firewall.ApiResponseFor401) | Not Authenticated
403 | [ApiResponseFor403](#get_firewall.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_firewall.ApiResponseFor404) | Not Found
405 | [ApiResponseFor405](#get_firewall.ApiResponseFor405) | Method Not Allowed
406 | [ApiResponseFor406](#get_firewall.ApiResponseFor406) | Not Acceptable
408 | [ApiResponseFor408](#get_firewall.ApiResponseFor408) | Timeout
429 | [ApiResponseFor429](#get_firewall.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#get_firewall.ApiResponseFor500) | General Error
503 | [ApiResponseFor503](#get_firewall.ApiResponseFor503) | Unavailable

#### get_firewall.ApiResponseFor200
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
[Firewall]({{complexTypePrefix}}Firewall.md) | [**Firewall**]({{complexTypePrefix}}Firewall.md) | [**Firewall**]({{complexTypePrefix}}Firewall.md) |  | 
[Id]({{complexTypePrefix}}Id.md) | [**Id**]({{complexTypePrefix}}Id.md) | [**Id**]({{complexTypePrefix}}Id.md) |  | 
[ResponseUsers]({{complexTypePrefix}}ResponseUsers.md) | [**ResponseUsers**]({{complexTypePrefix}}ResponseUsers.md) | [**ResponseUsers**]({{complexTypePrefix}}ResponseUsers.md) |  | 
[ResponseDate]({{complexTypePrefix}}ResponseDate.md) | [**ResponseDate**]({{complexTypePrefix}}ResponseDate.md) | [**ResponseDate**]({{complexTypePrefix}}ResponseDate.md) |  | 

#### get_firewall.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### get_firewall.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### get_firewall.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### get_firewall.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### get_firewall.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor405ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor405ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### get_firewall.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor406ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor406ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### get_firewall.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### get_firewall.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### get_firewall.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### get_firewall.ApiResponseFor503
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

# **patch_firewall**
<a id="patch_firewall"></a>
> bool, date, datetime, dict, float, int, list, str, none_type patch_firewall(idfirewall_create_or_patch)

Patch object's data

Make updates to specific fields within the record without replacing the entire dataset.

### Example

* Api Key Authentication (jwt):
```python
import circuitid_python
from circuitid_python.api.tags import firewall_api
from circuitid_python.models.firewall_create_or_patch import FirewallCreateOrPatch
from circuitid_python.models.response_error import ResponseError
from circuitid_python.models.firewall import Firewall
from circuitid_python.models.id import Id
from circuitid_python.models.response_date import ResponseDate
from circuitid_python.models.response_users import ResponseUsers
from pprint import pprint
# Defining the host is optional and defaults to https://rest.circuitid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = circuitid_python.Configuration(
    host = "https://rest.circuitid.com"
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
    api_instance = firewall_api.FirewallApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    body = FirewallCreateOrPatch(
        name="name_example",
        description="description_example",
        type="allow",
        target="numbers",
        direction="inbound",
        param="param_example",
        status=1,
    )
    try:
        # Patch object's data
        api_response = api_instance.patch_firewall(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except circuitid_python.ApiException as e:
        print("Exception when calling FirewallApi->patch_firewall: %s\n" % e)
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
[**FirewallCreateOrPatch**](../../models/FirewallCreateOrPatch.md) |  | 


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
200 | [ApiResponseFor200](#patch_firewall.ApiResponseFor200) | A JSON object containing the modified data.
400 | [ApiResponseFor400](#patch_firewall.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#patch_firewall.ApiResponseFor401) | Not Authenticated
403 | [ApiResponseFor403](#patch_firewall.ApiResponseFor403) | Forbidden
405 | [ApiResponseFor405](#patch_firewall.ApiResponseFor405) | Method Not Allowed
406 | [ApiResponseFor406](#patch_firewall.ApiResponseFor406) | Not Acceptable
408 | [ApiResponseFor408](#patch_firewall.ApiResponseFor408) | Timeout
429 | [ApiResponseFor429](#patch_firewall.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#patch_firewall.ApiResponseFor500) | General Error
503 | [ApiResponseFor503](#patch_firewall.ApiResponseFor503) | Unavailable

#### patch_firewall.ApiResponseFor200
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
[Firewall]({{complexTypePrefix}}Firewall.md) | [**Firewall**]({{complexTypePrefix}}Firewall.md) | [**Firewall**]({{complexTypePrefix}}Firewall.md) |  | 
[Id]({{complexTypePrefix}}Id.md) | [**Id**]({{complexTypePrefix}}Id.md) | [**Id**]({{complexTypePrefix}}Id.md) |  | 
[ResponseUsers]({{complexTypePrefix}}ResponseUsers.md) | [**ResponseUsers**]({{complexTypePrefix}}ResponseUsers.md) | [**ResponseUsers**]({{complexTypePrefix}}ResponseUsers.md) |  | 
[ResponseDate]({{complexTypePrefix}}ResponseDate.md) | [**ResponseDate**]({{complexTypePrefix}}ResponseDate.md) | [**ResponseDate**]({{complexTypePrefix}}ResponseDate.md) |  | 

#### patch_firewall.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### patch_firewall.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### patch_firewall.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### patch_firewall.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor405ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor405ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### patch_firewall.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor406ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor406ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### patch_firewall.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### patch_firewall.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### patch_firewall.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### patch_firewall.ApiResponseFor503
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

# **remove_firewall**
<a id="remove_firewall"></a>
> bool, date, datetime, dict, float, int, list, str, none_type remove_firewall(id)

Delete object by id

Delete an object by id, removing it from the service.

### Example

* Api Key Authentication (jwt):
```python
import circuitid_python
from circuitid_python.api.tags import firewall_api
from circuitid_python.models.response_error import ResponseError
from circuitid_python.models.firewall import Firewall
from circuitid_python.models.id import Id
from circuitid_python.models.response_date import ResponseDate
from circuitid_python.models.response_users import ResponseUsers
from pprint import pprint
# Defining the host is optional and defaults to https://rest.circuitid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = circuitid_python.Configuration(
    host = "https://rest.circuitid.com"
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
    api_instance = firewall_api.FirewallApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Delete object by id
        api_response = api_instance.remove_firewall(
            path_params=path_params,
        )
        pprint(api_response)
    except circuitid_python.ApiException as e:
        print("Exception when calling FirewallApi->remove_firewall: %s\n" % e)
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
200 | [ApiResponseFor200](#remove_firewall.ApiResponseFor200) | A JSON object containing the deleted data.
400 | [ApiResponseFor400](#remove_firewall.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#remove_firewall.ApiResponseFor401) | Not Authenticated
403 | [ApiResponseFor403](#remove_firewall.ApiResponseFor403) | Forbidden
405 | [ApiResponseFor405](#remove_firewall.ApiResponseFor405) | Method Not Allowed
406 | [ApiResponseFor406](#remove_firewall.ApiResponseFor406) | Not Acceptable
408 | [ApiResponseFor408](#remove_firewall.ApiResponseFor408) | Timeout
429 | [ApiResponseFor429](#remove_firewall.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#remove_firewall.ApiResponseFor500) | General Error
503 | [ApiResponseFor503](#remove_firewall.ApiResponseFor503) | Unavailable

#### remove_firewall.ApiResponseFor200
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
[Firewall]({{complexTypePrefix}}Firewall.md) | [**Firewall**]({{complexTypePrefix}}Firewall.md) | [**Firewall**]({{complexTypePrefix}}Firewall.md) |  | 
[Id]({{complexTypePrefix}}Id.md) | [**Id**]({{complexTypePrefix}}Id.md) | [**Id**]({{complexTypePrefix}}Id.md) |  | 
[ResponseUsers]({{complexTypePrefix}}ResponseUsers.md) | [**ResponseUsers**]({{complexTypePrefix}}ResponseUsers.md) | [**ResponseUsers**]({{complexTypePrefix}}ResponseUsers.md) |  | 
[ResponseDate]({{complexTypePrefix}}ResponseDate.md) | [**ResponseDate**]({{complexTypePrefix}}ResponseDate.md) | [**ResponseDate**]({{complexTypePrefix}}ResponseDate.md) |  | 

#### remove_firewall.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### remove_firewall.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### remove_firewall.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### remove_firewall.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor405ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor405ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### remove_firewall.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor406ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor406ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### remove_firewall.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### remove_firewall.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### remove_firewall.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseError**](../../models/ResponseError.md) |  | 


#### remove_firewall.ApiResponseFor503
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

