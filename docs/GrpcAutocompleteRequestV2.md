# GrpcAutocompleteRequestV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **datetime** | Returns autocomplete options in the range (end - duration, end]. | [optional] 
**duration** | **str** |  | [optional] 
**source_filters** | [**list[GrpcFilter]**](GrpcFilter.md) | Returns autocomplete options within this set of filters.  We can use this to provide typeahead hints for a partially constructed query. For example, we can query: give me all the options within a specific environment or namespace. | [optional] 
**destination_filters** | [**list[GrpcFilter]**](GrpcFilter.md) |  | [optional] 
**label_side_pair** | [**AutocompleteRequestV2LabelSidePair**](AutocompleteRequestV2LabelSidePair.md) | The label and side of flow for which we&#39;ll return autocomplete options.  Examples:  { label &#x3D; &#39;role&#39;, side &#x3D; &#39;SOURCE&#39; } will return options for &#39;srole&#39;.  { label &#x3D; &#39;id&#39;, side &#x3D; &#39;DESTINATION&#39;} will return options for &#39;did&#39;. | [optional] 
**metrics** | **list[str]** | List of metrics to search for autocomplete options.  We commonly use [&#39;bytes&#39;, &#39;udp_bytes&#39;] when populating the environment selector in the frontend. | [optional] 
**directionality** | [**GrpcDirectionality**](GrpcDirectionality.md) | Query for timeseries matching this directionality. See TimeSeriesRequestV2.directionality for more context. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


