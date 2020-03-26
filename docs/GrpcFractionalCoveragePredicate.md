# GrpcFractionalCoveragePredicate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** |  | [optional] 
**window** | [**GrpcDataWindow**](GrpcDataWindow.md) |  | [optional] 
**label_equality_pairs** | [**list[GrpcLabelEqualityPair]**](GrpcLabelEqualityPair.md) |  | [optional] 
**value_comparator** | [**GrpcComparatorType**](GrpcComparatorType.md) | The criteria for evaluating whether any point in the time series should be counted in the numerator of the computed fraction. The time series value will be the first operand and &#x60;value&#x60; will be the second. | [optional] 
**value** | **float** |  | [optional] 
**threshold_comparator** | [**GrpcComparatorType**](GrpcComparatorType.md) | How the threshold will be compared against the fraction of values meeting the above criteria. Computed fraction is first operand, &#x60;Threshold.second&#x60; is second. | [optional] 
**thresholds** | [**list[GrpcFractionalCoveragePredicateThreshold]**](GrpcFractionalCoveragePredicateThreshold.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


