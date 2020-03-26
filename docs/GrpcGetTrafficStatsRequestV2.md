# GrpcGetTrafficStatsRequestV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **datetime** | See GetTimeSeriesRequestV2 for a description of constraints on time ranges. | [optional] 
**duration** | **str** |  | [optional] 
**num_steps** | **int** | The number of steps used when loading data from the TSDB.  Although GetTrafficStats returns a set of scalar values, we expose num_steps to provide control of what is essentially the sampling rate of the timeseries that we use to derive the results.  If we expect the results of multiple API calls to be meaningfully comparable, then we must use the same num_steps in all of them --- especially for high frequency or spikey data, which suffer from aliasing if num_steps is not large enough. | [optional] 
**min_average_bytes_per_second** | **float** | Only return connections that have entire_window_average_bytes_per_second greater than this value. Default 0 (no filtering). | [optional] 
**min_absolute_percent_change** | **float** | Only return connections that have percent_change_in_traffic greater than this value. Default 0 (no filtering). | [optional] 
**source_grouping** | **list[str]** | See GetTimeSeriesRequestV2 for a description of groupings and filters. | [optional] 
**destination_grouping** | **list[str]** |  | [optional] 
**source_filters** | [**list[GrpcFilter]**](GrpcFilter.md) |  | [optional] 
**destination_filters** | [**list[GrpcFilter]**](GrpcFilter.md) |  | [optional] 
**no_rollups** | **bool** | See GetTimeSeriesRequestV2 for a description of no_rollups. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


