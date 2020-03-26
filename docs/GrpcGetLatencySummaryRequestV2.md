# GrpcGetLatencySummaryRequestV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **datetime** | See GetTimeSeriesRequestV2 for a description of constraints on time ranges. | [optional] 
**duration** | **str** |  | [optional] 
**num_steps** | **int** | See GetTrafficStatsRequestV2 for a description of why num_steps is exposed in this context. | [optional] 
**latency_class** | [**GrpcLatencyClass**](GrpcLatencyClass.md) | Only return connections in this latency class. | [optional] 
**min_latency_sec** | **float** | Only return connections with latency &gt; min_latency_sec. Default &#x3D; 0. | [optional] 
**latency_metric** | [**GrpcLatencyMetric**](GrpcLatencyMetric.md) | Latency metric to use. Default is MRTT. | [optional] 
**source_grouping** | **list[str]** | See GetTimeSeriesRequestV2 for a description of groupings and filters. | [optional] 
**destination_grouping** | **list[str]** |  | [optional] 
**source_filters** | [**list[GrpcFilter]**](GrpcFilter.md) |  | [optional] 
**destination_filters** | [**list[GrpcFilter]**](GrpcFilter.md) |  | [optional] 
**no_rollups** | **bool** | See GetTimeSeriesRequestV2 for a description of no_rollups. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


