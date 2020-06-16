# GrpcEntityTimeseriesList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** | Metric for the timeseries included in this struct. | [optional] 
**series** | [**list[GrpcEntityTimeseries]**](GrpcEntityTimeseries.md) | Timeseries for the corresponding metric sorted by ________.  Note: we should define a meaningful sort order for these timeseries. Some possibilities are the max value or labels. | [optional] 
**total_count** | **int** | Total number of timeseries matching the specified query for this metric.  If this is greater than len(series), then we know that timeseries have been filtered from the response. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


