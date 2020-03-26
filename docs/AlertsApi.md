# flowmill.AlertsApi

All URIs are relative to *https://app.flowmill.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_alert**](AlertsApi.md#get_alert) | **GET** /api/v1/alerts/{id} | 
[**post_alerts**](AlertsApi.md#post_alerts) | **POST** /api/v1/alerts | 
[**read_alerts**](AlertsApi.md#read_alerts) | **GET** /api/v1/alerts | 
[**update_alert_status**](AlertsApi.md#update_alert_status) | **POST** /api/v1/alerts/{id} | 


# **get_alert**
> GrpcAlertsList get_alert(id)



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
api_instance = flowmill.AlertsApi(flowmill.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_alert(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->get_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GrpcAlertsList**](GrpcAlertsList.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_alerts**
> GrpcPostAlertsResponse post_alerts(body)



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
api_instance = flowmill.AlertsApi(flowmill.ApiClient(configuration))
body = flowmill.GrpcAlertsList() # GrpcAlertsList | 

try:
    api_response = api_instance.post_alerts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->post_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrpcAlertsList**](GrpcAlertsList.md)|  | 

### Return type

[**GrpcPostAlertsResponse**](GrpcPostAlertsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_alerts**
> GrpcPagedAlertsList read_alerts(_from=_from, to=to, filters=filters, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search)



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
api_instance = flowmill.AlertsApi(flowmill.ApiClient(configuration))
_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filters = 'filters_example' # str | repeated messages aren't supported in query strings, so use a stringified json string instead repeated Filter filters = 6;. (optional)
limit = 56 # int | We return at most \"limit\" records, but we may return less even if more entries can be read. See alert_access/read.go for enforced limit. (optional)
offset = 'offset_example' # str | Offset is used for paging. This needs to be the same as the \"offset\" returned in the previous list of alerts. 0 will return whatever alerts are from the beginning of specified time range. For the first page, omit \"offset\" or set to 0. (optional)
sort_by = 'sort_by_example' # str | Alert field to sort by. (optional)
sort_direction = 'ASCENDING' # str | Ascending or descending sort. (optional) (default to ASCENDING)
search = 'search_example' # str | Search for an alert that contains the provided string. (optional)

try:
    api_response = api_instance.read_alerts(_from=_from, to=to, filters=filters, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->read_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**|  | [optional] 
 **to** | **datetime**|  | [optional] 
 **filters** | **str**| repeated messages aren&#39;t supported in query strings, so use a stringified json string instead repeated Filter filters &#x3D; 6;. | [optional] 
 **limit** | **int**| We return at most \&quot;limit\&quot; records, but we may return less even if more entries can be read. See alert_access/read.go for enforced limit. | [optional] 
 **offset** | **str**| Offset is used for paging. This needs to be the same as the \&quot;offset\&quot; returned in the previous list of alerts. 0 will return whatever alerts are from the beginning of specified time range. For the first page, omit \&quot;offset\&quot; or set to 0. | [optional] 
 **sort_by** | **str**| Alert field to sort by. | [optional] 
 **sort_direction** | **str**| Ascending or descending sort. | [optional] [default to ASCENDING]
 **search** | **str**| Search for an alert that contains the provided string. | [optional] 

### Return type

[**GrpcPagedAlertsList**](GrpcPagedAlertsList.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_status**
> object update_alert_status(id, body)



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
api_instance = flowmill.AlertsApi(flowmill.ApiClient(configuration))
id = 'id_example' # str | 
body = flowmill.GrpcUpdateAlertStatusRequest() # GrpcUpdateAlertStatusRequest | 

try:
    api_response = api_instance.update_alert_status(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->update_alert_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**GrpcUpdateAlertStatusRequest**](GrpcUpdateAlertStatusRequest.md)|  | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

