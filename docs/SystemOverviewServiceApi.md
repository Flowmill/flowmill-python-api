# flowmill.SystemOverviewServiceApi

All URIs are relative to *https://app.flowmill.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agent_info_v2**](SystemOverviewServiceApi.md#get_agent_info_v2) | **POST** /api/v2/system-overview/agent-info | Request info about connected agents.
[**get_connection_summary_v2**](SystemOverviewServiceApi.md#get_connection_summary_v2) | **POST** /api/v2/system-overview/connection-summary | 
[**get_latency_summary_v2**](SystemOverviewServiceApi.md#get_latency_summary_v2) | **POST** /api/v2/system-overview/latency-summary | 
[**get_traffic_stats_v2**](SystemOverviewServiceApi.md#get_traffic_stats_v2) | **POST** /api/v2/system-overview/traffic-stats | 


# **get_agent_info_v2**
> GrpcGetAgentInfoResponse get_agent_info_v2(body)

Request info about connected agents.

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
body = flowmill.GrpcGetAgentInfoRequestV2() # GrpcGetAgentInfoRequestV2 | 

try:
    # Request info about connected agents.
    api_response = api_instance.get_agent_info_v2(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemOverviewServiceApi->get_agent_info_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrpcGetAgentInfoRequestV2**](GrpcGetAgentInfoRequestV2.md)|  | 

### Return type

[**GrpcGetAgentInfoResponse**](GrpcGetAgentInfoResponse.md)

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

