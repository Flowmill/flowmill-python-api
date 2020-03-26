# flowmill.SystemOverviewServiceApi

All URIs are relative to *https://app.flowmill.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agent_info**](SystemOverviewServiceApi.md#get_agent_info) | **GET** /api/v1/system_overview/agent_info | 
[**get_connection_summary**](SystemOverviewServiceApi.md#get_connection_summary) | **POST** /api/v1/system_overview/connection_summary | 
[**get_connection_summary_v2**](SystemOverviewServiceApi.md#get_connection_summary_v2) | **POST** /api/v2/system_overview/connection_summary | 
[**get_latency_summary**](SystemOverviewServiceApi.md#get_latency_summary) | **POST** /api/v1/system_overview/latency_summary | 
[**get_latency_summary_v2**](SystemOverviewServiceApi.md#get_latency_summary_v2) | **POST** /api/v2/system_overview/latency_summary | 
[**get_traffic_stats**](SystemOverviewServiceApi.md#get_traffic_stats) | **POST** /api/v1/system_overview/traffic_stats | 
[**get_traffic_stats_v2**](SystemOverviewServiceApi.md#get_traffic_stats_v2) | **POST** /api/v2/system_overview/traffic_stats | 


# **get_agent_info**
> GrpcGetAgentInfoResponse get_agent_info(start=start, end=end, step=step)



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
api_instance = flowmill.SystemOverviewServiceApi(flowmill.ApiClient(configuration))
start = '2013-10-20T19:20:30+01:00' # datetime | start of the time interval, default 30 minutes from \"end\". (optional)
end = '2013-10-20T19:20:30+01:00' # datetime | end of the time interval, default current time. (optional)
step = 'step_example' # str | timeseries step, default 10 seconds. (optional)

try:
    api_response = api_instance.get_agent_info(start=start, end=end, step=step)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemOverviewServiceApi->get_agent_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **datetime**| start of the time interval, default 30 minutes from \&quot;end\&quot;. | [optional] 
 **end** | **datetime**| end of the time interval, default current time. | [optional] 
 **step** | **str**| timeseries step, default 10 seconds. | [optional] 

### Return type

[**GrpcGetAgentInfoResponse**](GrpcGetAgentInfoResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection_summary**
> GrpcGetConnectionSummaryResponse get_connection_summary(body)



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
api_instance = flowmill.SystemOverviewServiceApi(flowmill.ApiClient(configuration))
body = flowmill.GrpcGetConnectionSummaryRequest() # GrpcGetConnectionSummaryRequest | 

try:
    api_response = api_instance.get_connection_summary(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemOverviewServiceApi->get_connection_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrpcGetConnectionSummaryRequest**](GrpcGetConnectionSummaryRequest.md)|  | 

### Return type

[**GrpcGetConnectionSummaryResponse**](GrpcGetConnectionSummaryResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection_summary_v2**
> GrpcGetConnectionSummaryResponseV2 get_connection_summary_v2(body)



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
api_instance = flowmill.SystemOverviewServiceApi(flowmill.ApiClient(configuration))
body = flowmill.GrpcGetConnectionSummaryRequestV2() # GrpcGetConnectionSummaryRequestV2 | 

try:
    api_response = api_instance.get_connection_summary_v2(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemOverviewServiceApi->get_connection_summary_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrpcGetConnectionSummaryRequestV2**](GrpcGetConnectionSummaryRequestV2.md)|  | 

### Return type

[**GrpcGetConnectionSummaryResponseV2**](GrpcGetConnectionSummaryResponseV2.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latency_summary**
> GrpcGetLatencySummaryResponse get_latency_summary(body)



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
api_instance = flowmill.SystemOverviewServiceApi(flowmill.ApiClient(configuration))
body = flowmill.GrpcGetLatencySummaryRequest() # GrpcGetLatencySummaryRequest | 

try:
    api_response = api_instance.get_latency_summary(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemOverviewServiceApi->get_latency_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrpcGetLatencySummaryRequest**](GrpcGetLatencySummaryRequest.md)|  | 

### Return type

[**GrpcGetLatencySummaryResponse**](GrpcGetLatencySummaryResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latency_summary_v2**
> GrpcGetLatencySummaryResponse get_latency_summary_v2(body)



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
api_instance = flowmill.SystemOverviewServiceApi(flowmill.ApiClient(configuration))
body = flowmill.GrpcGetLatencySummaryRequestV2() # GrpcGetLatencySummaryRequestV2 | 

try:
    api_response = api_instance.get_latency_summary_v2(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemOverviewServiceApi->get_latency_summary_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrpcGetLatencySummaryRequestV2**](GrpcGetLatencySummaryRequestV2.md)|  | 

### Return type

[**GrpcGetLatencySummaryResponse**](GrpcGetLatencySummaryResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_traffic_stats**
> GrpcGetTrafficStatsResponse get_traffic_stats(body)



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
api_instance = flowmill.SystemOverviewServiceApi(flowmill.ApiClient(configuration))
body = flowmill.GrpcGetTrafficStatsRequest() # GrpcGetTrafficStatsRequest | 

try:
    api_response = api_instance.get_traffic_stats(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemOverviewServiceApi->get_traffic_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrpcGetTrafficStatsRequest**](GrpcGetTrafficStatsRequest.md)|  | 

### Return type

[**GrpcGetTrafficStatsResponse**](GrpcGetTrafficStatsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_traffic_stats_v2**
> GrpcGetTrafficStatsResponse get_traffic_stats_v2(body)



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
api_instance = flowmill.SystemOverviewServiceApi(flowmill.ApiClient(configuration))
body = flowmill.GrpcGetTrafficStatsRequestV2() # GrpcGetTrafficStatsRequestV2 | 

try:
    api_response = api_instance.get_traffic_stats_v2(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemOverviewServiceApi->get_traffic_stats_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrpcGetTrafficStatsRequestV2**](GrpcGetTrafficStatsRequestV2.md)|  | 

### Return type

[**GrpcGetTrafficStatsResponse**](GrpcGetTrafficStatsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

