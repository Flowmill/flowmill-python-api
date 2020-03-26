# GrpcTimeSeriesV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_labels** | [**list[GrpcLabel]**](GrpcLabel.md) | Set of labels identifying this timeseries. | [optional] 
**destination_labels** | [**list[GrpcLabel]**](GrpcLabel.md) |  | [optional] 
**directionality** | [**GrpcDirectionality**](GrpcDirectionality.md) | Specified the directionality of the timeseries relative to how the query was written, either FORWARD or REVERSE. | [optional] 
**max_value** | **float** | Max value of the returned values. | [optional] 
**values** | **list[float]** | List of points for this timeseries.  The points in values correspond to TSDB samples in the range such that: values[i] is for the range (start, start + (step * i)].  See GetTimeSeriesRequestV2 for a more complete description of how values map to time ranges. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


