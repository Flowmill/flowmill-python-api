# GrpcGetSummaryTableRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **datetime** | See GetTimeSeriesRequestV2 for a description of end, duration, and num_steps. | [optional] 
**duration** | **str** |  | [optional] 
**num_steps** | **int** |  | [optional] 
**metrics** | **list[str]** | List of metrics to be returned for each row in the table.  When a row has no values for a specified metric, then that metric will be ommitted in the response. | [optional] 
**source_filters** | [**list[GrpcFilter]**](GrpcFilter.md) |  | [optional] 
**destination_filters** | [**list[GrpcFilter]**](GrpcFilter.md) |  | [optional] 
**source_grouping** | **list[str]** |  | [optional] 
**destination_grouping** | **list[str]** |  | [optional] 
**directionality** | [**GrpcDirectionality**](GrpcDirectionality.md) |  | [optional] 
**no_rollups** | **bool** |  | [optional] 
**no_zero_padding** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


