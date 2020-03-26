# GrpcScalarSeriesPredicate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** |  | [optional] 
**window** | [**GrpcDataWindow**](GrpcDataWindow.md) |  | [optional] 
**label_equality_pairs** | [**list[GrpcLabelEqualityPair]**](GrpcLabelEqualityPair.md) |  | [optional] 
**comparator** | [**GrpcComparatorType**](GrpcComparatorType.md) | First operand is the reduced time series value, second is the threshold. | [optional] 
**reducer** | [**GrpcScalarReducerType**](GrpcScalarReducerType.md) | Describes how to reduce the time series to a single value. | [optional] 
**thresholds** | [**list[GrpcScalarSeriesPredicateThreshold]**](GrpcScalarSeriesPredicateThreshold.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


