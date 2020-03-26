# GrpcGetConnectionSummaryRequestV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **datetime** | See GetTimeSeriesRequestV2 for a description of constraints on time ranges. | [optional] 
**duration** | **str** |  | [optional] 
**num_steps** | **int** |  | [optional] 
**summary_type** | [**GrpcSummaryType**](GrpcSummaryType.md) |  | [optional] 
**min_percent_bad** | **float** | Only returns connections with percent bad greater than this value.  We use this to query for connections experiencing packet loss &gt; 1% or connection failures &gt; 5%. | [optional] 
**source_grouping** | **list[str]** | See GetTimeSeriesRequestV2 for a description of groupings and filters. | [optional] 
**destination_grouping** | **list[str]** |  | [optional] 
**source_filters** | [**list[GrpcFilter]**](GrpcFilter.md) |  | [optional] 
**destination_filters** | [**list[GrpcFilter]**](GrpcFilter.md) |  | [optional] 
**no_rollups** | **bool** | See GetTimeSeriesRequestV2 for a description of no_rollups. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


