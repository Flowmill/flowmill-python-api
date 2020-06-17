# GrpcTimeSeriesV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_labels** | [**list[GrpcLabel]**](GrpcLabel.md) | Set of labels identifying this timeseries. | [optional] 
**destination_labels** | [**list[GrpcLabel]**](GrpcLabel.md) |  | [optional] 
**directionality** | [**GrpcDirectionality**](GrpcDirectionality.md) | Specified the directionality of the timeseries relative to how the query was written, either FORWARD or REVERSE. | [optional] 
**max_value** | **float** | Max value of the returned values. | [optional] 
**values** | **list[float]** | List of points for this timeseries.  The points in values correspond to TSDB samples aggregated over time ranges:    - values[0] is the range (start, start + (step)]    - values[1] is the range (start + step, start + (step * 2)]    - values[2] is the range (start + (step * 2), start + (step * 3)]      ...    - values[i] is the range (start + (step * i), start + (step * (i +    1))]  If there are no TSDB samples for a given step in (start, end], we will fill that step with a value using the requested no_zero_padding (see GetTimeSeriesV2 request above). | [optional] 
**ok_values** | **list[float]** | When returning percent metrics, we also include the values used to compute the percent. These will be undefined for non-percent metrics.  Except for &#39;drops&#39;, all of the percent metrics have a suffix &#39;_percent&#39;.  Examples:  - for the metric &#39;drops&#39; the ok_values will be &#39;tcp_packets&#39; and    bad_values will be &#39;tcp_retrans&#39;  - for the metric &#39;connection_errors_percent&#39; the ok_values will be    &#39;new_sockets&#39; and the bad_values will be &#39;syn_timeouts&#39; | [optional] 
**bad_values** | **list[float]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


