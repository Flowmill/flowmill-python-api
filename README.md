# Flowmill REST API
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.8
- Package version: 0.8.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.flowmill.com](https://www.flowmill.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/Flowmill/flowmill-python-api.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Flowmill/flowmill-python-api.git`)

Then import the package:
```python
import flowmill 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import flowmill
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    # Get alert with specific id
    api_response = api_instance.get_alert(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->get_alert: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://app.flowmill.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AlertsApi* | [**get_alert**](docs/AlertsApi.md#get_alert) | **GET** /api/v1/alerts/{id} | Get alert with specific id
*AlertsApi* | [**post_alerts**](docs/AlertsApi.md#post_alerts) | **POST** /api/v1/alerts | Post an alert to our alert-access write endpoint
*AlertsApi* | [**read_alerts**](docs/AlertsApi.md#read_alerts) | **GET** /api/v1/alerts | Make a request to our alerts database
*AlertsApi* | [**update_alert_status**](docs/AlertsApi.md#update_alert_status) | **POST** /api/v1/alerts/{id} | Updates the Status of alerts
*AuthzServiceApi* | [**get_token_from_key**](docs/AuthzServiceApi.md#get_token_from_key) | **GET** /api/v1/auth/keys/{keyId} | if key id + secret in db, returns an Authz-signed token if the api key is not in the database or doesn&#39;t match the secret given \&quot;permission denied\&quot; error wil be returned.
*AuthzServiceApi* | [**get_user_auth_tenant_token**](docs/AuthzServiceApi.md#get_user_auth_tenant_token) | **GET** /api/v1/auth/tenants/{tenantId} | If user is authorized for the tenant, returns an Authz-signed token If user unauthorized for tenant, a \&quot;permission denied\&quot; error will be returned.
*AuthzServiceApi* | [**get_user_auth_tenant_token2**](docs/AuthzServiceApi.md#get_user_auth_tenant_token2) | **GET** /api/v1/user/tenants/{tenantId} | If user is authorized for the tenant, returns an Authz-signed token If user unauthorized for tenant, a \&quot;permission denied\&quot; error will be returned.
*AuthzServiceApi* | [**get_user_auth_tenants**](docs/AuthzServiceApi.md#get_user_auth_tenants) | **GET** /api/v1/auth/tenants | Return list of tenants that the user can access Will return an empty list if the user isn&#39;t allowed for any tenant.
*AuthzServiceApi* | [**get_user_auth_tenants2**](docs/AuthzServiceApi.md#get_user_auth_tenants2) | **GET** /api/v1/user/tenants | Return list of tenants that the user can access Will return an empty list if the user isn&#39;t allowed for any tenant.
*DashboardsApi* | [**delete_dashboard**](docs/DashboardsApi.md#delete_dashboard) | **DELETE** /api/v1/dashboards/{id} | 
*DashboardsApi* | [**delete_favorite**](docs/DashboardsApi.md#delete_favorite) | **DELETE** /api/v1/dashboards/{id}/favorite | 
*DashboardsApi* | [**get_dashboard**](docs/DashboardsApi.md#get_dashboard) | **GET** /api/v1/dashboards | 
*DashboardsApi* | [**get_dashboard2**](docs/DashboardsApi.md#get_dashboard2) | **GET** /api/v1/dashboards/{id} | 
*DashboardsApi* | [**post_dashboard**](docs/DashboardsApi.md#post_dashboard) | **POST** /api/v1/dashboards | 
*DashboardsApi* | [**post_favorite**](docs/DashboardsApi.md#post_favorite) | **POST** /api/v1/dashboards/{id}/favorite | Mark favorite
*DashboardsApi* | [**put_dashboard**](docs/DashboardsApi.md#put_dashboard) | **PUT** /api/v1/dashboards/{id} | 
*ExperimentalServiceApi* | [**get_cost_table**](docs/ExperimentalServiceApi.md#get_cost_table) | **POST** /api/v2/experimental/cost-table | 
*ExperimentalServiceApi* | [**get_summary_table**](docs/ExperimentalServiceApi.md#get_summary_table) | **POST** /api/v2/experimental/summary-table | 
*IntegrationsServiceApi* | [**authorize_pagerduty**](docs/IntegrationsServiceApi.md#authorize_pagerduty) | **POST** /api/v1/integrations/pagerduty/authorized | authorize new PagerDuty client and obtain an internal access token
*IntegrationsServiceApi* | [**authorize_slack**](docs/IntegrationsServiceApi.md#authorize_slack) | **POST** /api/v1/integrations/slack/authorized | authorize new slack team and obtain an internal access token
*IntegrationsServiceApi* | [**delete_pagerduty_authorized**](docs/IntegrationsServiceApi.md#delete_pagerduty_authorized) | **DELETE** /api/v1/integrations/pagerduty/authorized/{id} | delete token with specified id
*IntegrationsServiceApi* | [**delete_slack_authorized**](docs/IntegrationsServiceApi.md#delete_slack_authorized) | **DELETE** /api/v1/integrations/slack/authorized/{id} | delete token with specified id
*IntegrationsServiceApi* | [**list_pagerduty_authorized**](docs/IntegrationsServiceApi.md#list_pagerduty_authorized) | **GET** /api/v1/integrations/pagerduty/authorized | list all clients authorized for this tenant
*IntegrationsServiceApi* | [**list_slack_authorized**](docs/IntegrationsServiceApi.md#list_slack_authorized) | **GET** /api/v1/integrations/slack/authorized | list all teams authorized for this tenant
*IntegrationsServiceApi* | [**reauthorize_slack**](docs/IntegrationsServiceApi.md#reauthorize_slack) | **POST** /api/v1/integrations/slack/authorized/{id} | reauthorize slack team with the specified id
*MonitorsApi* | [**delete_monitor**](docs/MonitorsApi.md#delete_monitor) | **DELETE** /api/v1/monitors/{id} | 
*MonitorsApi* | [**get_monitor**](docs/MonitorsApi.md#get_monitor) | **GET** /api/v1/monitors | 
*MonitorsApi* | [**get_monitor2**](docs/MonitorsApi.md#get_monitor2) | **GET** /api/v1/monitors/{id} | 
*MonitorsApi* | [**post_monitor**](docs/MonitorsApi.md#post_monitor) | **POST** /api/v1/monitors | 
*MonitorsApi* | [**put_monitor**](docs/MonitorsApi.md#put_monitor) | **PUT** /api/v1/monitors/{id} | 
*SystemOverviewServiceApi* | [**get_agent_info**](docs/SystemOverviewServiceApi.md#get_agent_info) | **GET** /api/v1/system-overview/agent-info | Request info about connected agents
*SystemOverviewServiceApi* | [**get_connection_summary_v2**](docs/SystemOverviewServiceApi.md#get_connection_summary_v2) | **POST** /api/v2/system-overview/connection-summary | 
*SystemOverviewServiceApi* | [**get_latency_summary_v2**](docs/SystemOverviewServiceApi.md#get_latency_summary_v2) | **POST** /api/v2/system-overview/latency-summary | 
*SystemOverviewServiceApi* | [**get_traffic_stats_v2**](docs/SystemOverviewServiceApi.md#get_traffic_stats_v2) | **POST** /api/v2/system-overview/traffic-stats | 
*TenantsServiceApi* | [**create_agent_key**](docs/TenantsServiceApi.md#create_agent_key) | **POST** /api/v1/keys/agent-keys | Add new agent key to the db. returns a \&quot;permission denied\&quot; error if user not authorized to create an agent key
*TenantsServiceApi* | [**create_api_key**](docs/TenantsServiceApi.md#create_api_key) | **POST** /api/v1/keys/api-keys | Add new api key to the db. returns a \&quot;permission denied\&quot; error if user not authorized to create an api key
*TenantsServiceApi* | [**create_tenant**](docs/TenantsServiceApi.md#create_tenant) | **POST** /api/v1/tenants | Create new tenant. This will send welcome email to a specified admin email address.
*TenantsServiceApi* | [**create_user**](docs/TenantsServiceApi.md#create_user) | **POST** /api/v1/users | Create a user with specific tenant and role and send them welcome email. Only \&quot;admin\&quot; role allowed to create a user and will be verified. Receive: email, role Return: \&quot;permission denied\&quot; if not allowed to create new user.         \&quot;already exists\&quot; if user already exists for this tenant.         \&quot;internal\&quot; on fail         user_id if successful
*TenantsServiceApi* | [**delete_agent_key**](docs/TenantsServiceApi.md#delete_agent_key) | **DELETE** /api/v1/keys/agent-keys/{keyId} | Delete an agent key given a specified key_id. returns a \&quot;permission denied\&quot; error if user not authorized to delete an agent key returns \&quot;Not Found\&quot; error if no such key id exists.
*TenantsServiceApi* | [**delete_api_key**](docs/TenantsServiceApi.md#delete_api_key) | **DELETE** /api/v1/keys/api-keys/{keyId} | Delete an api key given a specified key_id. returns a \&quot;permission denied\&quot; error if user not authorized to delete an api key returns \&quot;Not Found\&quot; error if no such key id exists.
*TenantsServiceApi* | [**disable_tenant**](docs/TenantsServiceApi.md#disable_tenant) | **POST** /api/v1/tenants/disable/{id} | 
*TenantsServiceApi* | [**get_tenant**](docs/TenantsServiceApi.md#get_tenant) | **GET** /api/v1/tenants/{id} | 
*TenantsServiceApi* | [**list_agent_keys**](docs/TenantsServiceApi.md#list_agent_keys) | **GET** /api/v1/keys/agent-keys | List all agent keys for a specific tenant. returns a \&quot;permission denied\&quot; error if user not authorized to ask for a list of agent keys, or an empty list if no keys exist.
*TenantsServiceApi* | [**list_api_keys**](docs/TenantsServiceApi.md#list_api_keys) | **GET** /api/v1/keys/api-keys | List all keys for a specific user and tenant. returns a \&quot;permission denied\&quot; error if user not authorized to ask for a list of api keys, or an empty list if no keys exist.
*TenantsServiceApi* | [**list_tenants**](docs/TenantsServiceApi.md#list_tenants) | **GET** /api/v1/tenants | Tenants
*TenantsServiceApi* | [**list_users**](docs/TenantsServiceApi.md#list_users) | **GET** /api/v1/users | List of users, roles and status enabled/disabled Receive: empty message Return: \&quot;permission denied\&quot; on unauthorized/disabled user.         list of users for that same tenant, if successful
*TenantsServiceApi* | [**update_tenant**](docs/TenantsServiceApi.md#update_tenant) | **POST** /api/v1/tenants/{id} | 
*TenantsServiceApi* | [**update_user**](docs/TenantsServiceApi.md#update_user) | **PATCH** /api/v1/users/{userId} | Change user&#39;s permissions from USER to ADMIN or from \&quot;enabled\&quot; to \&quot;disabled\&quot; and vice versa. Admins cannot change their own role or status. Role must be &#39;user&#39; or &#39;admin, status musr be &#39;enabled&#39; or &#39;disabled&#39; Receive: user_id, role, status Return: \&quot;permission denied\&quot; if not allowed to make a change.         \&quot;internal error\&quot; if attempts to change \&quot;flowmill\&quot; role of if         transaction failed. \&quot;invalid argument\&quot; if an invalid role or status         has been used.          empty message if successful
*TimeSeriesApi* | [**get_autocomplete_options_v2**](docs/TimeSeriesApi.md#get_autocomplete_options_v2) | **POST** /api/v2/autocomplete | 
*TimeSeriesApi* | [**get_entity_timeseries**](docs/TimeSeriesApi.md#get_entity_timeseries) | **POST** /api/v2/entities | Returns non-zero one-sided timeseries matching the specified query.
*TimeSeriesApi* | [**get_flow_timeseries**](docs/TimeSeriesApi.md#get_flow_timeseries) | **POST** /api/v2/flows | Returns non-zero, two-sided timeseries matching the specified query.
*TimeSeriesApi* | [**get_time_series_v2**](docs/TimeSeriesApi.md#get_time_series_v2) | **POST** /api/v2/timeseries | Returns non-zero, two-sided timeseries matching the specified query.


## Documentation For Models

 - [AggregationMethodQuantileParams](docs/AggregationMethodQuantileParams.md)
 - [ComponentComponentTrafficFilter](docs/ComponentComponentTrafficFilter.md)
 - [ComponentTrafficFilterValueLabelPair](docs/ComponentTrafficFilterValueLabelPair.md)
 - [ConditionOp](docs/ConditionOp.md)
 - [DashboardComponent](docs/DashboardComponent.md)
 - [DashboardLayout](docs/DashboardLayout.md)
 - [DashboardPermission](docs/DashboardPermission.md)
 - [GetAgentInfoResponseAgentCount](docs/GetAgentInfoResponseAgentCount.md)
 - [GetAgentInfoResponseAgentInstance](docs/GetAgentInfoResponseAgentInstance.md)
 - [GetAgentInfoResponseDataPoint](docs/GetAgentInfoResponseDataPoint.md)
 - [GrpcAggregationMethod](docs/GrpcAggregationMethod.md)
 - [GrpcAlert](docs/GrpcAlert.md)
 - [GrpcAlertStatus](docs/GrpcAlertStatus.md)
 - [GrpcAlertsList](docs/GrpcAlertsList.md)
 - [GrpcAuthorizePagerdutyRequest](docs/GrpcAuthorizePagerdutyRequest.md)
 - [GrpcAuthorizePagerdutyResponse](docs/GrpcAuthorizePagerdutyResponse.md)
 - [GrpcAuthorizeSlackRequest](docs/GrpcAuthorizeSlackRequest.md)
 - [GrpcAuthorizeSlackResponse](docs/GrpcAuthorizeSlackResponse.md)
 - [GrpcAuthzTenant](docs/GrpcAuthzTenant.md)
 - [GrpcAuthzTenantList](docs/GrpcAuthzTenantList.md)
 - [GrpcAutocompleteRequestV2](docs/GrpcAutocompleteRequestV2.md)
 - [GrpcComparatorType](docs/GrpcComparatorType.md)
 - [GrpcConnectionSummaryV2](docs/GrpcConnectionSummaryV2.md)
 - [GrpcCostTableBreakdown](docs/GrpcCostTableBreakdown.md)
 - [GrpcCostTableResponse](docs/GrpcCostTableResponse.md)
 - [GrpcCostTableRow](docs/GrpcCostTableRow.md)
 - [GrpcCreateKeyResponse](docs/GrpcCreateKeyResponse.md)
 - [GrpcCreateTenantRequest](docs/GrpcCreateTenantRequest.md)
 - [GrpcCreateUserRequest](docs/GrpcCreateUserRequest.md)
 - [GrpcDashboard](docs/GrpcDashboard.md)
 - [GrpcDataWindow](docs/GrpcDataWindow.md)
 - [GrpcDirectionality](docs/GrpcDirectionality.md)
 - [GrpcDisableTenantRequest](docs/GrpcDisableTenantRequest.md)
 - [GrpcEntityTimeseries](docs/GrpcEntityTimeseries.md)
 - [GrpcEntityTimeseriesList](docs/GrpcEntityTimeseriesList.md)
 - [GrpcEntityTimeseriesRequest](docs/GrpcEntityTimeseriesRequest.md)
 - [GrpcEntityTimeseriesResponse](docs/GrpcEntityTimeseriesResponse.md)
 - [GrpcFilter](docs/GrpcFilter.md)
 - [GrpcFractionalCoveragePredicate](docs/GrpcFractionalCoveragePredicate.md)
 - [GrpcFractionalCoveragePredicateThreshold](docs/GrpcFractionalCoveragePredicateThreshold.md)
 - [GrpcGetAgentInfoResponse](docs/GrpcGetAgentInfoResponse.md)
 - [GrpcGetConnectionSummaryRequestV2](docs/GrpcGetConnectionSummaryRequestV2.md)
 - [GrpcGetConnectionSummaryResponseV2](docs/GrpcGetConnectionSummaryResponseV2.md)
 - [GrpcGetCostTableRequest](docs/GrpcGetCostTableRequest.md)
 - [GrpcGetDashboardResponse](docs/GrpcGetDashboardResponse.md)
 - [GrpcGetLatencySummaryRequestV2](docs/GrpcGetLatencySummaryRequestV2.md)
 - [GrpcGetLatencySummaryResponse](docs/GrpcGetLatencySummaryResponse.md)
 - [GrpcGetMonitorResponse](docs/GrpcGetMonitorResponse.md)
 - [GrpcGetSummaryTableRequest](docs/GrpcGetSummaryTableRequest.md)
 - [GrpcGetTrafficStatsRequestV2](docs/GrpcGetTrafficStatsRequestV2.md)
 - [GrpcGetTrafficStatsResponse](docs/GrpcGetTrafficStatsResponse.md)
 - [GrpcIqrSeriesPredicate](docs/GrpcIqrSeriesPredicate.md)
 - [GrpcIqrSeriesPredicateThreshold](docs/GrpcIqrSeriesPredicateThreshold.md)
 - [GrpcLabel](docs/GrpcLabel.md)
 - [GrpcLabelEqualityPair](docs/GrpcLabelEqualityPair.md)
 - [GrpcLatencyClass](docs/GrpcLatencyClass.md)
 - [GrpcLatencyMetric](docs/GrpcLatencyMetric.md)
 - [GrpcLatencySummary](docs/GrpcLatencySummary.md)
 - [GrpcListKeysResponse](docs/GrpcListKeysResponse.md)
 - [GrpcListPagerdutyAuthorizedResponse](docs/GrpcListPagerdutyAuthorizedResponse.md)
 - [GrpcListSlackAuthorizedResponse](docs/GrpcListSlackAuthorizedResponse.md)
 - [GrpcListUsersResponse](docs/GrpcListUsersResponse.md)
 - [GrpcLocality](docs/GrpcLocality.md)
 - [GrpcMetricValue](docs/GrpcMetricValue.md)
 - [GrpcMonitor](docs/GrpcMonitor.md)
 - [GrpcOptionsResponse](docs/GrpcOptionsResponse.md)
 - [GrpcPagedAlertsList](docs/GrpcPagedAlertsList.md)
 - [GrpcPostAlertsResponse](docs/GrpcPostAlertsResponse.md)
 - [GrpcPostDashboardRequest](docs/GrpcPostDashboardRequest.md)
 - [GrpcPostDashboardResponse](docs/GrpcPostDashboardResponse.md)
 - [GrpcPostFavoriteResponse](docs/GrpcPostFavoriteResponse.md)
 - [GrpcPostMonitorRequest](docs/GrpcPostMonitorRequest.md)
 - [GrpcPostMonitorResponse](docs/GrpcPostMonitorResponse.md)
 - [GrpcPutDashboardRequest](docs/GrpcPutDashboardRequest.md)
 - [GrpcPutDashboardResponse](docs/GrpcPutDashboardResponse.md)
 - [GrpcPutMonitorRequest](docs/GrpcPutMonitorRequest.md)
 - [GrpcPutMonitorResponse](docs/GrpcPutMonitorResponse.md)
 - [GrpcReauthorizeSlackRequest](docs/GrpcReauthorizeSlackRequest.md)
 - [GrpcReauthorizeSlackResponse](docs/GrpcReauthorizeSlackResponse.md)
 - [GrpcScalarReducerType](docs/GrpcScalarReducerType.md)
 - [GrpcScalarSeriesPredicate](docs/GrpcScalarSeriesPredicate.md)
 - [GrpcScalarSeriesPredicateThreshold](docs/GrpcScalarSeriesPredicateThreshold.md)
 - [GrpcSignedToken](docs/GrpcSignedToken.md)
 - [GrpcSortDirection](docs/GrpcSortDirection.md)
 - [GrpcSummaryTableResponse](docs/GrpcSummaryTableResponse.md)
 - [GrpcSummaryTableRow](docs/GrpcSummaryTableRow.md)
 - [GrpcSummaryType](docs/GrpcSummaryType.md)
 - [GrpcTenant](docs/GrpcTenant.md)
 - [GrpcTenantList](docs/GrpcTenantList.md)
 - [GrpcTimeSeriesRequestV2](docs/GrpcTimeSeriesRequestV2.md)
 - [GrpcTimeSeriesResponseV2](docs/GrpcTimeSeriesResponseV2.md)
 - [GrpcTimeSeriesV2](docs/GrpcTimeSeriesV2.md)
 - [GrpcTrafficStats](docs/GrpcTrafficStats.md)
 - [GrpcUpdateAlertStatusRequest](docs/GrpcUpdateAlertStatusRequest.md)
 - [GrpcUpdateTenantRequest](docs/GrpcUpdateTenantRequest.md)
 - [GrpcUser](docs/GrpcUser.md)
 - [GrpcUserUpdateRequest](docs/GrpcUserUpdateRequest.md)
 - [ListKeysResponseSingleKey](docs/ListKeysResponseSingleKey.md)
 - [ListPagerdutyAuthorizedResponseToken](docs/ListPagerdutyAuthorizedResponseToken.md)
 - [ListSlackAuthorizedResponseTeam](docs/ListSlackAuthorizedResponseTeam.md)
 - [ListUsersResponseUserStatus](docs/ListUsersResponseUserStatus.md)
 - [MonitorCondition](docs/MonitorCondition.md)
 - [MonitorSeverity](docs/MonitorSeverity.md)
 - [MonitorState](docs/MonitorState.md)
 - [ProtobufAny](docs/ProtobufAny.md)
 - [RuntimeError](docs/RuntimeError.md)


## Documentation For Authorization


## bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author



