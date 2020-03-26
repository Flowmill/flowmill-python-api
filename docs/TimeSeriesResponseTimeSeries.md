# TimeSeriesResponseTimeSeries

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | [**list[GrpcLabel]**](GrpcLabel.md) | This is the response in v1 queries. Deprecated in v2. | [optional] 
**source_labels** | [**list[GrpcLabel]**](GrpcLabel.md) | v2 response returns the source, destination, and edge labels specified by the *_grouping fields in the request. If a requested label is not presesent it will be populated with an empty string. | [optional] 
**destination_labels** | [**list[GrpcLabel]**](GrpcLabel.md) |  | [optional] 
**directionality** | [**GrpcDirectionality**](GrpcDirectionality.md) | v2 also returns whether the timeseries is FORWARD or REVERSED. These series are returned based on the query&#39;s request of FORWARD, REVERSED, or BOTH. in the response, &#x60;source_labels&#x60; will contain the request&#39;s &#x60;source_grouping&#x60;, and &#x60;destination_labels&#x60; will contain the request&#39;s &#x60;destination_grouping&#x60;. This holds to true even if direction &#x3D; REVERSED; the idea is both directions would have the same schema so could be displayed in one table. | [optional] 
**max_value** | **float** |  | [optional] 
**points** | [**GrpcPoint**](GrpcPoint.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


