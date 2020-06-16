# flowmill.TimeSeriesApi

All URIs are relative to *https://app.flowmill.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_autocomplete_options_v2**](TimeSeriesApi.md#get_autocomplete_options_v2) | **POST** /api/v2/autocomplete | 
[**get_entity_timeseries**](TimeSeriesApi.md#get_entity_timeseries) | **POST** /api/v2/entities | Returns non-zero one-sided timeseries matching the specified query.
[**get_flow_timeseries**](TimeSeriesApi.md#get_flow_timeseries) | **POST** /api/v2/flows | Returns non-zero, two-sided timeseries matching the specified query.
[**get_time_series_v2**](TimeSeriesApi.md#get_time_series_v2) | **POST** /api/v2/timeseries | Returns non-zero, two-sided timeseries matching the specified query.


# **get_autocomplete_options_v2**
> GrpcOptionsResponse get_autocomplete_options_v2(body)



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
api_instance = flowmill.TimeSeriesApi(flowmill.ApiClient(configuration))
body = flowmill.GrpcAutocompleteRequestV2() # GrpcAutocompleteRequestV2 | 

try:
    api_response = api_instance.get_autocomplete_options_v2(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeSeriesApi->get_autocomplete_options_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrpcAutocompleteRequestV2**](GrpcAutocompleteRequestV2.md)|  | 

### Return type

[**GrpcOptionsResponse**](GrpcOptionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_timeseries**
> GrpcEntityTimeseriesResponse get_entity_timeseries(body)

Returns non-zero one-sided timeseries matching the specified query.

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
api_instance = flowmill.TimeSeriesApi(flowmill.ApiClient(configuration))
body = flowmill.GrpcEntityTimeseriesRequest() # GrpcEntityTimeseriesRequest | 

try:
    # Returns non-zero one-sided timeseries matching the specified query.
    api_response = api_instance.get_entity_timeseries(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeSeriesApi->get_entity_timeseries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrpcEntityTimeseriesRequest**](GrpcEntityTimeseriesRequest.md)|  | 

### Return type

[**GrpcEntityTimeseriesResponse**](GrpcEntityTimeseriesResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flow_timeseries**
> GrpcTimeSeriesResponseV2 get_flow_timeseries(body)

Returns non-zero, two-sided timeseries matching the specified query.

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
api_instance = flowmill.TimeSeriesApi(flowmill.ApiClient(configuration))
body = flowmill.GrpcTimeSeriesRequestV2() # GrpcTimeSeriesRequestV2 | 

try:
    # Returns non-zero, two-sided timeseries matching the specified query.
    api_response = api_instance.get_flow_timeseries(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeSeriesApi->get_flow_timeseries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrpcTimeSeriesRequestV2**](GrpcTimeSeriesRequestV2.md)|  | 

### Return type

[**GrpcTimeSeriesResponseV2**](GrpcTimeSeriesResponseV2.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_series_v2**
> GrpcTimeSeriesResponseV2 get_time_series_v2(body)

Returns non-zero, two-sided timeseries matching the specified query.

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
api_instance = flowmill.TimeSeriesApi(flowmill.ApiClient(configuration))
body = flowmill.GrpcTimeSeriesRequestV2() # GrpcTimeSeriesRequestV2 | 

try:
    # Returns non-zero, two-sided timeseries matching the specified query.
    api_response = api_instance.get_time_series_v2(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeSeriesApi->get_time_series_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrpcTimeSeriesRequestV2**](GrpcTimeSeriesRequestV2.md)|  | 

### Return type

[**GrpcTimeSeriesResponseV2**](GrpcTimeSeriesResponseV2.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

