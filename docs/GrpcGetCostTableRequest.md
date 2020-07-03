# GrpcGetCostTableRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **datetime** |  | [optional] 
**duration** | **str** |  | [optional] 
**source_filters** | [**list[GrpcFilter]**](GrpcFilter.md) |  | [optional] 
**destination_filters** | [**list[GrpcFilter]**](GrpcFilter.md) |  | [optional] 
**source_grouping** | **list[str]** |  | [optional] 
**destination_grouping** | **list[str]** |  | [optional] 
**cross_az_dollars_per_gb** | **float** | Value used to estimate the cost of cross-zone traffic. Default is 0.  Queries that fail to specify either this or egress_dollars_per_gb will return an INVALID_ARGUMENT error as at least one cost must be &gt; 0. | [optional] 
**egress_dollars_per_gb** | **float** | Value used to estimate the cost of egress traffic. Default is 0.  Queries that fail to specify either this or cross_az_dollars_per_gb will return an INVALID_ARGUMENT error as at least one cost must be &gt; 0. | [optional] 
**minimum_cost_percent** | **float** | Return rows representing services that contribute &gt; minimum_cost_percent of total estimated costs.  Example: use 0.01 for all connections contributing to &gt; 1% of costs.  If unspecified, this will default to 0 (no filtering). | [optional] 
**no_rollups** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


