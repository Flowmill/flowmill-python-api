# GrpcEntityTimeseriesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeseries** | [**list[GrpcEntityTimeseriesList]**](GrpcEntityTimeseriesList.md) | Structures that include (metric, timeseries) for the specified query.  These structures are sorted by _______.  Note: we need to define a meaningful sort order for this list. We could either sort by the order of the request.metrics field or alphabetically by the timeseries.metric field. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


