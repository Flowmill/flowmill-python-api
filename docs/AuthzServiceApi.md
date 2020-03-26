# flowmill.AuthzServiceApi

All URIs are relative to *https://app.flowmill.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_token_from_key**](AuthzServiceApi.md#get_token_from_key) | **GET** /api/v1/auth/keys/{keyId} | 
[**get_user_auth_tenant_token**](AuthzServiceApi.md#get_user_auth_tenant_token) | **GET** /api/v1/auth/tenants/{tenantId} | 
[**get_user_auth_tenant_token2**](AuthzServiceApi.md#get_user_auth_tenant_token2) | **GET** /api/v1/user/tenants/{tenantId} | 
[**get_user_auth_tenants**](AuthzServiceApi.md#get_user_auth_tenants) | **GET** /api/v1/auth/tenants | 
[**get_user_auth_tenants2**](AuthzServiceApi.md#get_user_auth_tenants2) | **GET** /api/v1/user/tenants | 


# **get_token_from_key**
> GrpcSignedToken get_token_from_key(key_id)



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
api_instance = flowmill.AuthzServiceApi(flowmill.ApiClient(configuration))
key_id = 'key_id_example' # str | 

try:
    api_response = api_instance.get_token_from_key(key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthzServiceApi->get_token_from_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**|  | 

### Return type

[**GrpcSignedToken**](GrpcSignedToken.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_auth_tenant_token**
> GrpcSignedToken get_user_auth_tenant_token(tenant_id)



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
api_instance = flowmill.AuthzServiceApi(flowmill.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 

try:
    api_response = api_instance.get_user_auth_tenant_token(tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthzServiceApi->get_user_auth_tenant_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**GrpcSignedToken**](GrpcSignedToken.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_auth_tenant_token2**
> GrpcSignedToken get_user_auth_tenant_token2(tenant_id)



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
api_instance = flowmill.AuthzServiceApi(flowmill.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 

try:
    api_response = api_instance.get_user_auth_tenant_token2(tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthzServiceApi->get_user_auth_tenant_token2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**GrpcSignedToken**](GrpcSignedToken.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_auth_tenants**
> GrpcAuthzTenantList get_user_auth_tenants()



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
api_instance = flowmill.AuthzServiceApi(flowmill.ApiClient(configuration))

try:
    api_response = api_instance.get_user_auth_tenants()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthzServiceApi->get_user_auth_tenants: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GrpcAuthzTenantList**](GrpcAuthzTenantList.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_auth_tenants2**
> GrpcAuthzTenantList get_user_auth_tenants2()



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
api_instance = flowmill.AuthzServiceApi(flowmill.ApiClient(configuration))

try:
    api_response = api_instance.get_user_auth_tenants2()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthzServiceApi->get_user_auth_tenants2: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GrpcAuthzTenantList**](GrpcAuthzTenantList.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

