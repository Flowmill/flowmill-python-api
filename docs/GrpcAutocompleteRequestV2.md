# GrpcAutocompleteRequestV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **datetime** | Returns autocomplete options in the range (end - duration, end]. | [optional] 
**duration** | **str** |  | [optional] 
**filters** | [**list[GrpcFilter]**](GrpcFilter.md) | Returns autocomplete options within this set of filters.  We can use this to provide typeahead hints for a partially constructed query. For example, we can query: give me all the options within a specific environment or namespace. | [optional] 
**label** | **str** | Label to return options for.  Note: this expects a label with our legacy &#39;s&#39; and &#39;d&#39; prefixes, such as, for example, &#39;senv&#39; or &#39;drole&#39;. | [optional] 
**metrics** | **list[str]** | List of metrics to search for autocomplete options.  We commonly use [&#39;bytes&#39;, &#39;udp_bytes&#39;] when populating the environment selector in the frontend. | [optional] 
**directionality** | [**GrpcDirectionality**](GrpcDirectionality.md) | Query for timeseries matching this directionality. See TimeSeriesRequestV2.directionality for more context. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


