# flowmill.IntegrationsServiceApi

All URIs are relative to *https://app.flowmill.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_pagerduty**](IntegrationsServiceApi.md#authorize_pagerduty) | **POST** /api/v1/integrations/pagerduty/authorized | authorize new PagerDuty client and obtain an internal access token
[**authorize_slack**](IntegrationsServiceApi.md#authorize_slack) | **POST** /api/v1/integrations/slack/authorized | authorize new slack team and obtain an internal access token
[**delete_pagerduty_authorized**](IntegrationsServiceApi.md#delete_pagerduty_authorized) | **DELETE** /api/v1/integrations/pagerduty/authorized/{id} | delete token with specified id
[**delete_slack_authorized**](IntegrationsServiceApi.md#delete_slack_authorized) | **DELETE** /api/v1/integrations/slack/authorized/{id} | delete token with specified id
[**list_pagerduty_authorized**](IntegrationsServiceApi.md#list_pagerduty_authorized) | **GET** /api/v1/integrations/pagerduty/authorized | list all clients authorized for this tenant
[**list_slack_authorized**](IntegrationsServiceApi.md#list_slack_authorized) | **GET** /api/v1/integrations/slack/authorized | list all teams authorized for this tenant
[**reauthorize_slack**](IntegrationsServiceApi.md#reauthorize_slack) | **POST** /api/v1/integrations/slack/authorized/{id} | reauthorize slack team with the specified id


# **authorize_pagerduty**
> GrpcAuthorizePagerdutyResponse authorize_pagerduty(body)

authorize new PagerDuty client and obtain an internal access token

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
api_instance = flowmill.IntegrationsServiceApi(flowmill.ApiClient(configuration))
body = flowmill.GrpcAuthorizePagerdutyRequest() # GrpcAuthorizePagerdutyRequest | 

try:
    # authorize new PagerDuty client and obtain an internal access token
    api_response = api_instance.authorize_pagerduty(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsServiceApi->authorize_pagerduty: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrpcAuthorizePagerdutyRequest**](GrpcAuthorizePagerdutyRequest.md)|  | 

### Return type

[**GrpcAuthorizePagerdutyResponse**](GrpcAuthorizePagerdutyResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorize_slack**
> GrpcAuthorizeSlackResponse authorize_slack(body)

authorize new slack team and obtain an internal access token

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
api_instance = flowmill.IntegrationsServiceApi(flowmill.ApiClient(configuration))
body = flowmill.GrpcAuthorizeSlackRequest() # GrpcAuthorizeSlackRequest | 

try:
    # authorize new slack team and obtain an internal access token
    api_response = api_instance.authorize_slack(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsServiceApi->authorize_slack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrpcAuthorizeSlackRequest**](GrpcAuthorizeSlackRequest.md)|  | 

### Return type

[**GrpcAuthorizeSlackResponse**](GrpcAuthorizeSlackResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pagerduty_authorized**
> object delete_pagerduty_authorized(id)

delete token with specified id

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
api_instance = flowmill.IntegrationsServiceApi(flowmill.ApiClient(configuration))
id = 56 # int | internal database id of the token

try:
    # delete token with specified id
    api_response = api_instance.delete_pagerduty_authorized(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsServiceApi->delete_pagerduty_authorized: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| internal database id of the token | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_slack_authorized**
> object delete_slack_authorized(id)

delete token with specified id

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
api_instance = flowmill.IntegrationsServiceApi(flowmill.ApiClient(configuration))
id = 56 # int | internal database id of the token

try:
    # delete token with specified id
    api_response = api_instance.delete_slack_authorized(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsServiceApi->delete_slack_authorized: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| internal database id of the token | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pagerduty_authorized**
> GrpcListPagerdutyAuthorizedResponse list_pagerduty_authorized()

list all clients authorized for this tenant

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
api_instance = flowmill.IntegrationsServiceApi(flowmill.ApiClient(configuration))

try:
    # list all clients authorized for this tenant
    api_response = api_instance.list_pagerduty_authorized()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsServiceApi->list_pagerduty_authorized: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GrpcListPagerdutyAuthorizedResponse**](GrpcListPagerdutyAuthorizedResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_slack_authorized**
> GrpcListSlackAuthorizedResponse list_slack_authorized()

list all teams authorized for this tenant

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
api_instance = flowmill.IntegrationsServiceApi(flowmill.ApiClient(configuration))

try:
    # list all teams authorized for this tenant
    api_response = api_instance.list_slack_authorized()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsServiceApi->list_slack_authorized: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GrpcListSlackAuthorizedResponse**](GrpcListSlackAuthorizedResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reauthorize_slack**
> GrpcReauthorizeSlackResponse reauthorize_slack(id, body)

reauthorize slack team with the specified id

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
api_instance = flowmill.IntegrationsServiceApi(flowmill.ApiClient(configuration))
id = 56 # int | internal database id of the token
body = flowmill.GrpcReauthorizeSlackRequest() # GrpcReauthorizeSlackRequest | 

try:
    # reauthorize slack team with the specified id
    api_response = api_instance.reauthorize_slack(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsServiceApi->reauthorize_slack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| internal database id of the token | 
 **body** | [**GrpcReauthorizeSlackRequest**](GrpcReauthorizeSlackRequest.md)|  | 

### Return type

[**GrpcReauthorizeSlackResponse**](GrpcReauthorizeSlackResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

