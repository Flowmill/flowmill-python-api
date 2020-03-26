# GrpcAlert

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**monitor_id** | **str** | The id of the monitor that triggers the alert. | [optional] 
**alert_status** | [**GrpcAlertStatus**](GrpcAlertStatus.md) | Status of the alert. | [optional] 
**severity** | [**MonitorSeverity**](MonitorSeverity.md) | Severity of this alert. | [optional] 
**monitor** | [**GrpcMonitor**](GrpcMonitor.md) | Monitor that triggers the alert. | [optional] 
**labels** | [**list[GrpcLabel]**](GrpcLabel.md) | A set of labels that can be used to distinguish multiple distinct alerts produced from the same monitor. | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


