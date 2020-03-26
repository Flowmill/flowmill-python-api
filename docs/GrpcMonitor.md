# GrpcMonitor

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the monitor. | [optional] 
**description** | **str** | A human-readable description of the monitor. | [optional] 
**id** | **str** |  | [optional] 
**created_at** | **datetime** | When this monitor is first created. This field is populated and handled by backend. | [optional] 
**updated_at** | **datetime** | When this monitor is last updated. This field is populated and handled by backend. | [optional] 
**focus_zoom** | **str** | Breakdown/label grouping fields. Prefer explicit labels over zoom fields. | [optional] 
**peer_zoom** | **str** |  | [optional] 
**source_grouping** | **list[str]** |  | [optional] 
**destination_grouping** | **list[str]** |  | [optional] 
**src_filters** | [**list[GrpcFilter]**](GrpcFilter.md) |  | [optional] 
**dst_filters** | [**list[GrpcFilter]**](GrpcFilter.md) |  | [optional] 
**primary_condition** | [**MonitorCondition**](MonitorCondition.md) |  | [optional] 
**secondary_conditions** | [**list[MonitorCondition]**](MonitorCondition.md) |  | [optional] 
**slack** | **str** |  | [optional] 
**webhook** | **str** |  | [optional] 
**msg** | **str** |  | [optional] 
**slack_token_ids** | **list[int]** | Ids of Slack tokens identifying channels to which alerts will be fired. These are the DB ids, not the actual tokens themselves. | [optional] 
**pagerduty_token_ids** | **list[int]** | Ids of pagerduty account tokens where the alerts will be fired. These are the DB ids, not the actual tokens themselves. | [optional] 
**state** | [**MonitorState**](MonitorState.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


