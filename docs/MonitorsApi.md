# flowmill.MonitorsApi

All URIs are relative to *https://app.flowmill.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_monitor**](MonitorsApi.md#delete_monitor) | **DELETE** /api/v1/monitors/{id} | 
[**get_monitor**](MonitorsApi.md#get_monitor) | **GET** /api/v1/monitors | 
[**get_monitor2**](MonitorsApi.md#get_monitor2) | **GET** /api/v1/monitors/{id} | 
[**post_monitor**](MonitorsApi.md#post_monitor) | **POST** /api/v1/monitors | 
[**put_monitor**](MonitorsApi.md#put_monitor) | **PUT** /api/v1/monitors/{id} | 


# **delete_monitor**
> object delete_monitor(id, tenant=tenant)



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
api_instance = flowmill.MonitorsApi(flowmill.ApiClient(configuration))
id = 'id_example' # str | 
tenant = 'tenant_example' # str |  (optional)

try:
    api_response = api_instance.delete_monitor(id, tenant=tenant)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorsApi->delete_monitor: %s\n" % e)
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

# **get_monitor**
> GrpcGetMonitorResponse get_monitor(tenant=tenant, id=id)



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
api_instance = flowmill.MonitorsApi(flowmill.ApiClient(configuration))
tenant = 'tenant_example' # str |  (optional)
id = 'id_example' # str |  (optional)

try:
    api_response = api_instance.get_monitor(tenant=tenant, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorsApi->get_monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 

### Return type

[**GrpcGetMonitorResponse**](GrpcGetMonitorResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitor2**
> GrpcGetMonitorResponse get_monitor2(id, tenant=tenant)



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
api_instance = flowmill.MonitorsApi(flowmill.ApiClient(configuration))
id = 'id_example' # str | 
tenant = 'tenant_example' # str |  (optional)

try:
    api_response = api_instance.get_monitor2(id, tenant=tenant)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorsApi->get_monitor2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **tenant** | **str**|  | [optional] 

### Return type

[**GrpcGetMonitorResponse**](GrpcGetMonitorResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_monitor**
> GrpcPostMonitorResponse post_monitor(body)



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
api_instance = flowmill.MonitorsApi(flowmill.ApiClient(configuration))
body = flowmill.GrpcPostMonitorRequest() # GrpcPostMonitorRequest | 

try:
    api_response = api_instance.post_monitor(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorsApi->post_monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrpcPostMonitorRequest**](GrpcPostMonitorRequest.md)|  | 

### Return type

[**GrpcPostMonitorResponse**](GrpcPostMonitorResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_monitor**
> GrpcPutMonitorResponse put_monitor(id, body)



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
api_instance = flowmill.MonitorsApi(flowmill.ApiClient(configuration))
id = 'id_example' # str | 
body = flowmill.GrpcPutMonitorRequest() # GrpcPutMonitorRequest | 

try:
    api_response = api_instance.put_monitor(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorsApi->put_monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**GrpcPutMonitorRequest**](GrpcPutMonitorRequest.md)|  | 

### Return type

[**GrpcPutMonitorResponse**](GrpcPutMonitorResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

