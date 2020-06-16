# GrpcEntityTimeseriesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **datetime** | See GetTimeSeriesRequestV2 for a description of constraints on time ranges.  Note: queries in this form implicitly define:    step_size &#x3D; duration / num_steps We must place a meaningful restriction on step_size and reject queries that violate those restrictions. | [optional] 
**duration** | **str** |  | [optional] 
**num_steps** | **int** |  | [optional] 
**metric** | **list[str]** | Requested metrics to be returned.  If any of the specified metrics are not recognized, then we consider the query invalid and return a list of supported metrics.  Note: we need to define metrics such that they: 1) have human readable names; and 2) hide unnecessary complexity from the API consumer.  For example, we should expose a metric with a name like &#x60;cpu_usage&#x60; instead of &#x60;utime_ns&#x60; and &#x60;stime_ns&#x60;. See, for example, the graphs here: https://grafana.monitoring.flowmill.io/d/RlaZgKRMz/pipeline-generated-data?orgId&#x3D;1&amp;from&#x3D;now-15m&amp;to&#x3D;now&amp;var-env&#x3D;All&amp;var-az&#x3D;All&amp;var-role&#x3D;All&amp;var-host&#x3D;ip-172-31-81-129.ec2.internal&amp;var-comm&#x3D;All&amp;fullscreen&amp;edit&amp;panelId&#x3D;14 | [optional] 
**grouping** | **list[str]** | List of groupings applied to the entity timeseries.  Queries that fail to specify at least one grouping are considered invalid.  If a grouping is specified for a label that is not meaningful for entity metrics (or not supported at all), then we consider the query invalid and return a list of groupings that can be supported. | [optional] 
**filters** | [**list[GrpcFilter]**](GrpcFilter.md) | Lists of filters for the entity timeseries.  If a filter is specified on a label that is not meaningful for entity metrics, then we consider the query invalid and return a list of labels that we can use in filters. For example: &#x60;port&#x60; is not meaningful in the context of entity timeseries. | [optional] 
**top_k** | **int** | Maximum number of time series to return. Defaults to 30 if unspecified. If set to -1, then we&#39;ll return all timeseries.  Note: we&#39;ll need to define the meaning of &#x60;top_k&#x60; when multiple metrics are requested. We could either: 1) enforce the top_k on each metric individually (this is annoying for the    consumer though) 2) enforce the top_k on the *first* metric specified, and then filter    other metrics s.t. they include the entities of the first metric. 3) require the client to specify a &#39;sort-by&#39; field when using the top_k    field.  There are use cases for all three of these behaviors. We should pick something that behaves well in a default case, but allows us to customize the behavior as needed. | [optional] 
**no_rollups** | **bool** | If true, the service will disable use of rolled-up timeseries in the request. The rollups are currently 30 seconds. I.e., each timeseries is stored as a 30 second aggregate in the timeseries database. Rollups can significantly speed up large queries due to less points needed to cover the interval. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


