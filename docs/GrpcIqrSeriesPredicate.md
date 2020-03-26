# GrpcIqrSeriesPredicate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** |  | [optional] 
**window** | [**GrpcDataWindow**](GrpcDataWindow.md) | The window against which this predicate will be evaluated. | [optional] 
**label_equality_pairs** | [**list[GrpcLabelEqualityPair]**](GrpcLabelEqualityPair.md) |  | [optional] 
**median_interval** | **str** | The length of the moving window for the median. | [optional] 
**iqr_interval** | **str** | The length of the moving window for the IQR bounds. | [optional] 
**thresholds** | [**list[GrpcIqrSeriesPredicateThreshold]**](GrpcIqrSeriesPredicateThreshold.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


