# GrpcEvaluateMonitorRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | **str** |  | [optional] 
**monitor** | [**GrpcMonitor**](GrpcMonitor.md) | The monitor to be evaluated. | [optional] 
**over_window** | [**EvaluateMonitorRequestWindowParams**](EvaluateMonitorRequestWindowParams.md) | Run the monitor for every step along the window. All fields (i.e. start, stop, step) must be present. | [optional] 
**once** | [**EvaluateMonitorRequestOnceParams**](EvaluateMonitorRequestOnceParams.md) | Execute the monitor once at the given time. Each MonitorEvaluationResult instance in the response will have a single point. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


