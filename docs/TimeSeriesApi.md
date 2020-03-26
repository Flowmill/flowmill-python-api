# flowmill.TimeSeriesApi

All URIs are relative to *https://app.flowmill.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_autocomplete_options**](TimeSeriesApi.md#get_autocomplete_options) | **POST** /api/v1/autocomplete | 
[**get_autocomplete_options_v2**](TimeSeriesApi.md#get_autocomplete_options_v2) | **POST** /api/v2/autocomplete | 
[**get_time_series**](TimeSeriesApi.md#get_time_series) | **POST** /api/v1/timeseries | 
[**get_time_series_v2**](TimeSeriesApi.md#get_time_series_v2) | **POST** /api/v2/timeseries | 


# **get_autocomplete_options**
> GrpcOptionsResponse get_autocomplete_options(body)



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
body = flowmill.GrpcAutocompleteRequest() # GrpcAutocompleteRequest | 

try:
    api_response = api_instance.get_autocomplete_options(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeSeriesApi->get_autocomplete_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrpcAutocompleteRequest**](GrpcAutocompleteRequest.md)|  | 

### Return type

[**GrpcOptionsResponse**](GrpcOptionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **get_time_series**
> GrpcTimeSeriesResponse get_time_series(body)



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
body = flowmill.GrpcTimeSeriesRequest() # GrpcTimeSeriesRequest | 

try:
    api_response = api_instance.get_time_series(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeSeriesApi->get_time_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrpcTimeSeriesRequest**](GrpcTimeSeriesRequest.md)|  | 

### Return type

[**GrpcTimeSeriesResponse**](GrpcTimeSeriesResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_series_v2**
> GrpcTimeSeriesResponseV2 get_time_series_v2(body)



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

