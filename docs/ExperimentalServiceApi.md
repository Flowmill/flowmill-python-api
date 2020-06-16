# flowmill.ExperimentalServiceApi

All URIs are relative to *https://app.flowmill.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cost_table**](ExperimentalServiceApi.md#get_cost_table) | **POST** /api/v2/experimental/cost-table | 
[**get_summary_table**](ExperimentalServiceApi.md#get_summary_table) | **POST** /api/v2/experimental/summary-table | 


# **get_cost_table**
> GrpcCostTableResponse get_cost_table(body)



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
api_instance = flowmill.ExperimentalServiceApi(flowmill.ApiClient(configuration))
body = flowmill.GrpcGetCostTableRequest() # GrpcGetCostTableRequest | 

try:
    api_response = api_instance.get_cost_table(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentalServiceApi->get_cost_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrpcGetCostTableRequest**](GrpcGetCostTableRequest.md)|  | 

### Return type

[**GrpcCostTableResponse**](GrpcCostTableResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary_table**
> GrpcSummaryTableResponse get_summary_table(body)



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
api_instance = flowmill.ExperimentalServiceApi(flowmill.ApiClient(configuration))
body = flowmill.GrpcGetSummaryTableRequest() # GrpcGetSummaryTableRequest | 

try:
    api_response = api_instance.get_summary_table(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentalServiceApi->get_summary_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrpcGetSummaryTableRequest**](GrpcGetSummaryTableRequest.md)|  | 

### Return type

[**GrpcSummaryTableResponse**](GrpcSummaryTableResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

