# GrpcEntityTimeseries

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | [**list[GrpcLabel]**](GrpcLabel.md) | Labels identifying this timeseries.  We enforce that these labels are alphabetically sorted by their &#x60;name&#x60;. | [optional] 
**values** | **list[float]** | List of points for this timeseries.  The points in values correspond to TSDB samples aggregated over time ranges:    - values[0] is the range (start, start + (step)]    - values[1] is the range (start + step, start + (step * 2)]    - values[2] is the range (start + (step * 2), start + (step * 3)]      ...    - values[i] is the range (start + (step * i), start + (step * (i +    1))]  If we do not have samples for a given value, then the API will either:   1) fill the value with a 0 if the pipeline uses \&quot;no samples\&quot; to encode      a zero value.   2) fill the value with a -1 if the pipeline uses \&quot;no samples\&quot; to mean      that we have no data for a given time range.  Our documentation *must* explicitly include a description of which metrics will get 0 or -1 for no sample periods. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


