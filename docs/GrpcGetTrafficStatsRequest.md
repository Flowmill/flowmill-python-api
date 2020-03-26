# GrpcGetTrafficStatsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 
**grouping** | [**GrpcGrouping**](GrpcGrouping.md) |  | [optional] 
**min_average_bytes_per_second** | **float** | only return connections that have entire_window_average_bytes_per_second greater than this value. default 0 (no filtering). | [optional] 
**min_absolute_percent_change** | **float** | only return connections that have percent_change_in_traffic greater than this value. default 0 (no filtering). | [optional] 
**source_filters** | [**list[GrpcFilter]**](GrpcFilter.md) |  | [optional] 
**destination_filters** | [**list[GrpcFilter]**](GrpcFilter.md) |  | [optional] 
**no_rollups** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


