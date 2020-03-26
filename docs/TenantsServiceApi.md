# flowmill.TenantsServiceApi

All URIs are relative to *https://app.flowmill.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_agent_key**](TenantsServiceApi.md#create_agent_key) | **POST** /api/v1/keys/agent_keys | 
[**create_api_key**](TenantsServiceApi.md#create_api_key) | **POST** /api/v1/keys/api_keys | 
[**create_tenant**](TenantsServiceApi.md#create_tenant) | **POST** /api/v1/tenants | 
[**create_user**](TenantsServiceApi.md#create_user) | **POST** /api/v1/users | 
[**delete_agent_key**](TenantsServiceApi.md#delete_agent_key) | **DELETE** /api/v1/keys/agent_keys/{keyId} | 
[**delete_api_key**](TenantsServiceApi.md#delete_api_key) | **DELETE** /api/v1/keys/api_keys/{keyId} | 
[**disable_tenant**](TenantsServiceApi.md#disable_tenant) | **POST** /api/v1/tenants/disable/{id} | 
[**get_tenant**](TenantsServiceApi.md#get_tenant) | **GET** /api/v1/tenants/{id} | 
[**list_agent_keys**](TenantsServiceApi.md#list_agent_keys) | **GET** /api/v1/keys/agent_keys | 
[**list_api_keys**](TenantsServiceApi.md#list_api_keys) | **GET** /api/v1/keys/api_keys | 
[**list_tenants**](TenantsServiceApi.md#list_tenants) | **GET** /api/v1/tenants | 
[**list_users**](TenantsServiceApi.md#list_users) | **GET** /api/v1/users | 
[**update_tenant**](TenantsServiceApi.md#update_tenant) | **POST** /api/v1/tenants/{id} | 
[**update_user**](TenantsServiceApi.md#update_user) | **PATCH** /api/v1/users/{userId} | 


# **create_agent_key**
> GrpcCreateKeyResponse create_agent_key(body)



### Example
```python
from __future__ import print_function
import time
import flowmill
from flowmill.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = flowmill.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))
body = NULL # object | 

try:
    api_response = api_instance.create_agent_key(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->create_agent_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

[**GrpcCreateKeyResponse**](GrpcCreateKeyResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_api_key**
> GrpcCreateKeyResponse create_api_key(body)



### Example
```python
from __future__ import print_function
import time
import flowmill
from flowmill.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = flowmill.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))
body = NULL # object | 

try:
    api_response = api_instance.create_api_key(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->create_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

[**GrpcCreateKeyResponse**](GrpcCreateKeyResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tenant**
> GrpcTenant create_tenant(body)



### Example
```python
from __future__ import print_function
import time
import flowmill
from flowmill.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = flowmill.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))
body = flowmill.GrpcCreateTenantRequest() # GrpcCreateTenantRequest | 

try:
    api_response = api_instance.create_tenant(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->create_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrpcCreateTenantRequest**](GrpcCreateTenantRequest.md)|  | 

### Return type

[**GrpcTenant**](GrpcTenant.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> GrpcUser create_user(body)



### Example
```python
from __future__ import print_function
import time
import flowmill
from flowmill.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = flowmill.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))
body = flowmill.GrpcCreateUserRequest() # GrpcCreateUserRequest | 

try:
    api_response = api_instance.create_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrpcCreateUserRequest**](GrpcCreateUserRequest.md)|  | 

### Return type

[**GrpcUser**](GrpcUser.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent_key**
> object delete_agent_key(key_id)



### Example
```python
from __future__ import print_function
import time
import flowmill
from flowmill.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = flowmill.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))
key_id = 'key_id_example' # str | 

try:
    api_response = api_instance.delete_agent_key(key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->delete_agent_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**|  | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key**
> object delete_api_key(key_id)



### Example
```python
from __future__ import print_function
import time
import flowmill
from flowmill.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = flowmill.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))
key_id = 'key_id_example' # str | 

try:
    api_response = api_instance.delete_api_key(key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->delete_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**|  | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_tenant**
> GrpcTenant disable_tenant(id, body)



### Example
```python
from __future__ import print_function
import time
import flowmill
from flowmill.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = flowmill.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))
id = 'id_example' # str | 
body = flowmill.GrpcDisableTenantRequest() # GrpcDisableTenantRequest | 

try:
    api_response = api_instance.disable_tenant(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->disable_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**GrpcDisableTenantRequest**](GrpcDisableTenantRequest.md)|  | 

### Return type

[**GrpcTenant**](GrpcTenant.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant**
> GrpcTenant get_tenant(id)



### Example
```python
from __future__ import print_function
import time
import flowmill
from flowmill.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = flowmill.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_tenant(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->get_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GrpcTenant**](GrpcTenant.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_agent_keys**
> GrpcListKeysResponse list_agent_keys()



### Example
```python
from __future__ import print_function
import time
import flowmill
from flowmill.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = flowmill.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))

try:
    api_response = api_instance.list_agent_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->list_agent_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GrpcListKeysResponse**](GrpcListKeysResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_keys**
> GrpcListKeysResponse list_api_keys()



### Example
```python
from __future__ import print_function
import time
import flowmill
from flowmill.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = flowmill.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))

try:
    api_response = api_instance.list_api_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->list_api_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GrpcListKeysResponse**](GrpcListKeysResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tenants**
> GrpcTenantList list_tenants()



### Example
```python
from __future__ import print_function
import time
import flowmill
from flowmill.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = flowmill.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))

try:
    api_response = api_instance.list_tenants()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->list_tenants: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GrpcTenantList**](GrpcTenantList.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> GrpcListUsersResponse list_users()



### Example
```python
from __future__ import print_function
import time
import flowmill
from flowmill.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = flowmill.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))

try:
    api_response = api_instance.list_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->list_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GrpcListUsersResponse**](GrpcListUsersResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tenant**
> GrpcTenant update_tenant(id, body)



### Example
```python
from __future__ import print_function
import time
import flowmill
from flowmill.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = flowmill.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))
id = 'id_example' # str | 
body = flowmill.GrpcUpdateTenantRequest() # GrpcUpdateTenantRequest | 

try:
    api_response = api_instance.update_tenant(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->update_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**GrpcUpdateTenantRequest**](GrpcUpdateTenantRequest.md)|  | 

### Return type

[**GrpcTenant**](GrpcTenant.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> object update_user(user_id, body)



### Example
```python
from __future__ import print_function
import time
import flowmill
from flowmill.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = flowmill.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))
user_id = 'user_id_example' # str | 
body = flowmill.GrpcUserUpdateRequest() # GrpcUserUpdateRequest | 

try:
    api_response = api_instance.update_user(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **body** | [**GrpcUserUpdateRequest**](GrpcUserUpdateRequest.md)|  | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

