# GrpcTimeSeriesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 
**step** | **str** | Note: if using grpc-gateway, protobuf.Duration should be received as nanoseconds. The number of points returned is capped at a maximum, currently MaxPointsPerTimeseries &#x3D; 10000. The returned result&#39;s step might be adjusted. | [optional] 
**filters** | [**list[GrpcFilter]**](GrpcFilter.md) |  | [optional] 
**source_filters** | [**list[GrpcFilter]**](GrpcFilter.md) | Lists of filters for the source and destinations. The &#x60;directionality&#x60; field determines how these labels get converted to labels queried against the backing TSDB.  For instance, lets say I do a query with &#x60;role&#x3D;\&quot;my-role\&quot;&#x60; in &#x60;source_filters&#x60; and &#x60;az&#x3D;\&quot;my-az\&quot;&#x60; in &#x60;destination_filters&#x60;. If &#x60;directionality&#x60; is ...   - ...FORWARD, then these become &#x60;{saz&#x3D;\&quot;my-az\&quot;, drole&#x3D;\&quot;my-role\&quot;}&#x60;   - ...BACKWARD, then these become &#x60;{srole&#x3D;\&quot;my-role\&quot;, daz&#x3D;\&quot;my-az\&quot;}&#x60;   - ...BOTH, then both of the above queries are done and the results are        merged together. | [optional] 
**destination_filters** | [**list[GrpcFilter]**](GrpcFilter.md) |  | [optional] 
**metric** | **str** |  | [optional] 
**focus_zoom** | **str** |  | [optional] 
**peer_zoom** | **str** |  | [optional] 
**source_grouping** | **list[str]** | A list of labels that the returned timeseries will include.  If only one side of the groupings are specified, then the returned timeseries will be aggregated for that one side. E.g., if we specify a query for source_grouping &#x3D; [&#39;address&#39;], then the returned timeseries will be the sum of the specified metric aggregated by source address. If no grouping is specified, no cross-timeseries aggregation is performed.  Note: The response&#39;s &#x60;series.source_labels&#x60; and &#x60;series.destination_labels&#x60; will contain &#x60;source_grouping&#x60; and &#x60;destination_grouping&#x60;, for both FORWARD and REVERSED responses, i.e., reversed timeseries don&#39;t reverse the source and destination grouping labels. | [optional] 
**destination_grouping** | **list[str]** |  | [optional] 
**edge_grouping** | **list[str]** | No longer supported. Returns an unimplemented error if defined. | [optional] 
**anonymize** | **bool** | No longer supported. Returns an unimplemented error if defined. | [optional] 
**directionality** | [**GrpcDirectionality**](GrpcDirectionality.md) | Used to conditionally reverse the specified filters.  For example, if we query for flows with srole&#x3D;(a), then we would get these results for different directionality values:  - FORWARD - all flows with srole&#x3D;(a),  - REVERSE - all flows with drole&#x3D;(a), and  - BOTH - the union of forward and reverse. | [optional] 
**locality** | [**GrpcLocality**](GrpcLocality.md) | No longer supported. Returns an unimplemented error if defined. | [optional] 
**top_k** | **int** | Maximum number of time series to return. The default value is 30. Uses the default value if not set. The hit_limit field in the response is set to true if some time series have been omitted. Returns all time series if set to -1. | [optional] 
**min_total_values_threshold** | **float** | No longer supported. Returns an unimplemented error if defined. | [optional] 
**no_rollups** | **bool** | If true, the service will disable use of rolled-up timeseries in the request. The rollups are currently 30 seconds. I.e., each timeseries is stored as a 30 second aggregate in the timeseries database. Rollups can significantly speed up large queries due to less points needed to cover the interval. | [optional] 
**label_equality** | [**list[GrpcLabelEqualityPair]**](GrpcLabelEqualityPair.md) |  | [optional] 
**aggregation** | [**GrpcAggregationMethod**](GrpcAggregationMethod.md) | What type of aggregation to perform. See comment in GetTimeSeriesRequestV2 for more details. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


