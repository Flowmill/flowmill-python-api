# GrpcTimeSeriesResponseV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series** | [**list[GrpcTimeSeriesV2]**](GrpcTimeSeriesV2.md) | List of timeseries that match the specified query. | [optional] 
**total_count** | **int** | Total number of timeseries matching the specified query. If this is greater than len(series), then we filtered the results by top_k. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


