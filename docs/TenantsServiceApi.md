# flowmill.TenantsServiceApi

All URIs are relative to *https://app.flowmill.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_agent_key**](TenantsServiceApi.md#create_agent_key) | **POST** /api/v1/keys/agent-keys | Add new agent key to the db. returns a \&quot;permission denied\&quot; error if user not authorized to create an agent key
[**create_api_key**](TenantsServiceApi.md#create_api_key) | **POST** /api/v1/keys/api-keys | Add new api key to the db. returns a \&quot;permission denied\&quot; error if user not authorized to create an api key
[**create_tenant**](TenantsServiceApi.md#create_tenant) | **POST** /api/v1/tenants | Create new tenant. This will send welcome email to a specified admin email address.
[**create_user**](TenantsServiceApi.md#create_user) | **POST** /api/v1/users | Create a user with specific tenant and role and send them welcome email. Only \&quot;admin\&quot; role allowed to create a user and will be verified. Receive: email, role Return: \&quot;permission denied\&quot; if not allowed to create new user.         \&quot;already exists\&quot; if user already exists for this tenant.         \&quot;internal\&quot; on fail         user_id if successful
[**delete_agent_key**](TenantsServiceApi.md#delete_agent_key) | **DELETE** /api/v1/keys/agent-keys/{keyId} | Delete an agent key given a specified key_id. returns a \&quot;permission denied\&quot; error if user not authorized to delete an agent key returns \&quot;Not Found\&quot; error if no such key id exists.
[**delete_api_key**](TenantsServiceApi.md#delete_api_key) | **DELETE** /api/v1/keys/api-keys/{keyId} | Delete an api key given a specified key_id. returns a \&quot;permission denied\&quot; error if user not authorized to delete an api key returns \&quot;Not Found\&quot; error if no such key id exists.
[**disable_tenant**](TenantsServiceApi.md#disable_tenant) | **POST** /api/v1/tenants/disable/{id} | 
[**get_tenant**](TenantsServiceApi.md#get_tenant) | **GET** /api/v1/tenants/{id} | 
[**list_agent_keys**](TenantsServiceApi.md#list_agent_keys) | **GET** /api/v1/keys/agent-keys | List all agent keys for a specific tenant. returns a \&quot;permission denied\&quot; error if user not authorized to ask for a list of agent keys, or an empty list if no keys exist.
[**list_api_keys**](TenantsServiceApi.md#list_api_keys) | **GET** /api/v1/keys/api-keys | List all keys for a specific user and tenant. returns a \&quot;permission denied\&quot; error if user not authorized to ask for a list of api keys, or an empty list if no keys exist.
[**list_tenants**](TenantsServiceApi.md#list_tenants) | **GET** /api/v1/tenants | Tenants
[**list_users**](TenantsServiceApi.md#list_users) | **GET** /api/v1/users | List of users, roles and status enabled/disabled Receive: empty message Return: \&quot;permission denied\&quot; on unauthorized/disabled user.         list of users for that same tenant, if successful
[**update_tenant**](TenantsServiceApi.md#update_tenant) | **POST** /api/v1/tenants/{id} | 
[**update_user**](TenantsServiceApi.md#update_user) | **PATCH** /api/v1/users/{userId} | Change user&#39;s permissions from USER to ADMIN or from \&quot;enabled\&quot; to \&quot;disabled\&quot; and vice versa. Admins cannot change their own role or status. Role must be &#39;user&#39; or &#39;admin, status musr be &#39;enabled&#39; or &#39;disabled&#39; Receive: user_id, role, status Return: \&quot;permission denied\&quot; if not allowed to make a change.         \&quot;internal error\&quot; if attempts to change \&quot;flowmill\&quot; role of if         transaction failed. \&quot;invalid argument\&quot; if an invalid role or status         has been used.          empty message if successful


# **create_agent_key**
> GrpcCreateKeyResponse create_agent_key(body)

Add new agent key to the db. returns a \"permission denied\" error if user not authorized to create an agent key

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
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))
body = NULL # object | 

try:
    # Add new agent key to the db. returns a \"permission denied\" error if user not authorized to create an agent key
    api_response = api_instance.create_agent_key(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->create_agent_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

[**GrpcCreateKeyResponse**](GrpcCreateKeyResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_api_key**
> GrpcCreateKeyResponse create_api_key(body)

Add new api key to the db. returns a \"permission denied\" error if user not authorized to create an api key

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
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))
body = NULL # object | 

try:
    # Add new api key to the db. returns a \"permission denied\" error if user not authorized to create an api key
    api_response = api_instance.create_api_key(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->create_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

[**GrpcCreateKeyResponse**](GrpcCreateKeyResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tenant**
> GrpcTenant create_tenant(body)

Create new tenant. This will send welcome email to a specified admin email address.

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
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))
body = flowmill.GrpcCreateTenantRequest() # GrpcCreateTenantRequest | 

try:
    # Create new tenant. This will send welcome email to a specified admin email address.
    api_response = api_instance.create_tenant(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->create_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrpcCreateTenantRequest**](GrpcCreateTenantRequest.md)|  | 

### Return type

[**GrpcTenant**](GrpcTenant.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> GrpcUser create_user(body)

Create a user with specific tenant and role and send them welcome email. Only \"admin\" role allowed to create a user and will be verified. Receive: email, role Return: \"permission denied\" if not allowed to create new user.         \"already exists\" if user already exists for this tenant.         \"internal\" on fail         user_id if successful

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
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))
body = flowmill.GrpcCreateUserRequest() # GrpcCreateUserRequest | 

try:
    # Create a user with specific tenant and role and send them welcome email. Only \"admin\" role allowed to create a user and will be verified. Receive: email, role Return: \"permission denied\" if not allowed to create new user.         \"already exists\" if user already exists for this tenant.         \"internal\" on fail         user_id if successful
    api_response = api_instance.create_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GrpcCreateUserRequest**](GrpcCreateUserRequest.md)|  | 

### Return type

[**GrpcUser**](GrpcUser.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent_key**
> object delete_agent_key(key_id)

Delete an agent key given a specified key_id. returns a \"permission denied\" error if user not authorized to delete an agent key returns \"Not Found\" error if no such key id exists.

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
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))
key_id = 'key_id_example' # str | 

try:
    # Delete an agent key given a specified key_id. returns a \"permission denied\" error if user not authorized to delete an agent key returns \"Not Found\" error if no such key id exists.
    api_response = api_instance.delete_agent_key(key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->delete_agent_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**|  | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key**
> object delete_api_key(key_id)

Delete an api key given a specified key_id. returns a \"permission denied\" error if user not authorized to delete an api key returns \"Not Found\" error if no such key id exists.

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
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))
key_id = 'key_id_example' # str | 

try:
    # Delete an api key given a specified key_id. returns a \"permission denied\" error if user not authorized to delete an api key returns \"Not Found\" error if no such key id exists.
    api_response = api_instance.delete_api_key(key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->delete_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**|  | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_tenant**
> GrpcTenant disable_tenant(id, body)



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
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))
id = 'id_example' # str | 
body = flowmill.GrpcDisableTenantRequest() # GrpcDisableTenantRequest | 

try:
    api_response = api_instance.disable_tenant(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->disable_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**GrpcDisableTenantRequest**](GrpcDisableTenantRequest.md)|  | 

### Return type

[**GrpcTenant**](GrpcTenant.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant**
> GrpcTenant get_tenant(id)



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
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_tenant(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->get_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GrpcTenant**](GrpcTenant.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_agent_keys**
> GrpcListKeysResponse list_agent_keys()

List all agent keys for a specific tenant. returns a \"permission denied\" error if user not authorized to ask for a list of agent keys, or an empty list if no keys exist.

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
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))

try:
    # List all agent keys for a specific tenant. returns a \"permission denied\" error if user not authorized to ask for a list of agent keys, or an empty list if no keys exist.
    api_response = api_instance.list_agent_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->list_agent_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GrpcListKeysResponse**](GrpcListKeysResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_keys**
> GrpcListKeysResponse list_api_keys()

List all keys for a specific user and tenant. returns a \"permission denied\" error if user not authorized to ask for a list of api keys, or an empty list if no keys exist.

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
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))

try:
    # List all keys for a specific user and tenant. returns a \"permission denied\" error if user not authorized to ask for a list of api keys, or an empty list if no keys exist.
    api_response = api_instance.list_api_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->list_api_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GrpcListKeysResponse**](GrpcListKeysResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tenants**
> GrpcTenantList list_tenants()

Tenants

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
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))

try:
    # Tenants
    api_response = api_instance.list_tenants()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->list_tenants: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GrpcTenantList**](GrpcTenantList.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> GrpcListUsersResponse list_users()

List of users, roles and status enabled/disabled Receive: empty message Return: \"permission denied\" on unauthorized/disabled user.         list of users for that same tenant, if successful

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
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))

try:
    # List of users, roles and status enabled/disabled Receive: empty message Return: \"permission denied\" on unauthorized/disabled user.         list of users for that same tenant, if successful
    api_response = api_instance.list_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->list_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GrpcListUsersResponse**](GrpcListUsersResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tenant**
> GrpcTenant update_tenant(id, body)



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
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))
id = 'id_example' # str | 
body = flowmill.GrpcUpdateTenantRequest() # GrpcUpdateTenantRequest | 

try:
    api_response = api_instance.update_tenant(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->update_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**GrpcUpdateTenantRequest**](GrpcUpdateTenantRequest.md)|  | 

### Return type

[**GrpcTenant**](GrpcTenant.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> object update_user(user_id, body)

Change user's permissions from USER to ADMIN or from \"enabled\" to \"disabled\" and vice versa. Admins cannot change their own role or status. Role must be 'user' or 'admin, status musr be 'enabled' or 'disabled' Receive: user_id, role, status Return: \"permission denied\" if not allowed to make a change.         \"internal error\" if attempts to change \"flowmill\" role of if         transaction failed. \"invalid argument\" if an invalid role or status         has been used.          empty message if successful

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
api_instance = flowmill.TenantsServiceApi(flowmill.ApiClient(configuration))
user_id = 'user_id_example' # str | 
body = flowmill.GrpcUserUpdateRequest() # GrpcUserUpdateRequest | 

try:
    # Change user's permissions from USER to ADMIN or from \"enabled\" to \"disabled\" and vice versa. Admins cannot change their own role or status. Role must be 'user' or 'admin, status musr be 'enabled' or 'disabled' Receive: user_id, role, status Return: \"permission denied\" if not allowed to make a change.         \"internal error\" if attempts to change \"flowmill\" role of if         transaction failed. \"invalid argument\" if an invalid role or status         has been used.          empty message if successful
    api_response = api_instance.update_user(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsServiceApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **body** | [**GrpcUserUpdateRequest**](GrpcUserUpdateRequest.md)|  | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

