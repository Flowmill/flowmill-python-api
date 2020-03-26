# flowmill.DashboardsApi

All URIs are relative to *https://app.flowmill.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_dashboard**](DashboardsApi.md#delete_dashboard) | **DELETE** /api/v1/dashboards/{id} | 
[**delete_favorite**](DashboardsApi.md#delete_favorite) | **DELETE** /api/v1/dashboards/{id}/favorite | 
[**get_dashboard**](DashboardsApi.md#get_dashboard) | **GET** /api/v1/dashboards | 
[**get_dashboard2**](DashboardsApi.md#get_dashboard2) | **GET** /api/v1/dashboards/{id} | 
[**post_dashboard**](DashboardsApi.md#post_dashboard) | **POST** /api/v1/dashboards | 
[**post_favorite**](DashboardsApi.md#post_favorite) | **POST** /api/v1/dashboards/{id}/favorite | 
[**put_dashboard**](DashboardsApi.md#put_dashboard) | **PUT** /api/v1/dashboards/{id} | 


# **delete_dashboard**
> object delete_dashboard(id, tenant=tenant)



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
api_instance = flowmill.DashboardsApi(flowmill.ApiClient(configuration))
id = 'id_example' # str | 
tenant = 'tenant_example' # str |  (optional)

try:
    api_response = api_instance.delete_dashboard(id, tenant=tenant)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->delete_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **tenant** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_favorite**
> object delete_favorite(id, tenant=tenant)



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
api_instance = flowmill.DashboardsApi(flowmill.ApiClient(configuration))
id = 'id_example' # str | 
tenant = 'tenant_example' # str |  (optional)

try:
    api_response = api_instance.delete_favorite(id, tenant=tenant)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->delete_favorite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **tenant** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard**
> GrpcGetDashboardResponse get_dashboard(tenant=tenant, id=id, owned=owned, favorite=favorite)



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
api_instance = flowmill.DashboardsApi(flowmill.ApiClient(configuration))
tenant = 'tenant_example' # str | Tenant field is now read from the JWT token. (optional)
id = 'id_example' # str | Optional, if set, returns the specific dashboard. If it's set, |owned| and |favorite| fields below are ignored. (optional)
owned = true # bool | Optional, act as a filter. If set, only return the dashboard(s) owned by the requester. (optional)
favorite = true # bool | Optional, act as a filter. If set only return the dashboards(s) marked as 'favorite' by the request. (optional)

try:
    api_response = api_instance.get_dashboard(tenant=tenant, id=id, owned=owned, favorite=favorite)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->get_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str**| Tenant field is now read from the JWT token. | [optional] 
 **id** | **str**| Optional, if set, returns the specific dashboard. If it&#39;s set, |owned| and |favorite| fields below are ignored. | [optional] 
 **owned** | **bool**| Optional, act as a filter. If set, only return the dashboard(s) owned by the requester. | [optional] 
 **favorite** | **bool**| Optional, act as a filter. If set only return the dashboards(s) marked as &#39;favorite&#39; by the request. | [optional] 

### Return type

[**GrpcGetDashboardResponse**](GrpcGetDashboardResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard2**
> GrpcGetDashboardResponse get_dashboard2(id, tenant=tenant, owned=owned, favorite=favorite)



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
api_instance = flowmill.DashboardsApi(flowmill.ApiClient(configuration))
id = 'id_example' # str | Optional, if set, returns the specific dashboard. If it's set, |owned| and |favorite| fields below are ignored.
tenant = 'tenant_example' # str | Tenant field is now read from the JWT token. (optional)
owned = true # bool | Optional, act as a filter. If set, only return the dashboard(s) owned by the requester. (optional)
favorite = true # bool | Optional, act as a filter. If set only return the dashboards(s) marked as 'favorite' by the request. (optional)

try:
    api_response = api_instance.get_dashboard2(id, tenant=tenant, owned=owned, favorite=favorite)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->get_dashboard2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Optional, if set, returns the specific dashboard. If it&#39;s set, |owned| and |favorite| fields below are ignored. | 
 **tenant** | **str**| Tenant field is now read from the JWT token. | [optional] 
 **owned** | **bool**| Optional, act as a filter. If set, only return the dashboard(s) owned by the requester. | [optional] 
 **favorite** | **bool**| Optional, act as a filter. If set only return the dashboards(s) marked as &#39;favorite&#39; by the request. | [optional] 

### Return type

[**GrpcGetDashboardResponse**](GrpcGetDashboardResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_dashboard**
> GrpcPostDashboardResponse post_dashboard(body)



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
api_instance = flowmill.DashboardsApi(flowmill.ApiClient(configuration))
body = flowmill.GrpcPostDashboardRequest() # GrpcPostDashboardRequest | 

try:
    api_response = api_instance.post_dashboard(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->post_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrpcPostDashboardRequest**](GrpcPostDashboardRequest.md)|  | 

### Return type

[**GrpcPostDashboardResponse**](GrpcPostDashboardResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_favorite**
> GrpcPostFavoriteResponse post_favorite(id)



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
api_instance = flowmill.DashboardsApi(flowmill.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.post_favorite(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->post_favorite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GrpcPostFavoriteResponse**](GrpcPostFavoriteResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_dashboard**
> GrpcPutDashboardResponse put_dashboard(id, body)



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
api_instance = flowmill.DashboardsApi(flowmill.ApiClient(configuration))
id = 'id_example' # str | 
body = flowmill.GrpcPutDashboardRequest() # GrpcPutDashboardRequest | 

try:
    api_response = api_instance.put_dashboard(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->put_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**GrpcPutDashboardRequest**](GrpcPutDashboardRequest.md)|  | 

### Return type

[**GrpcPutDashboardResponse**](GrpcPutDashboardResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

