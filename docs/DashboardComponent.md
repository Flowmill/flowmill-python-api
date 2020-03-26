# DashboardComponent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**metric** | **str** |  | [optional] 
**focus_zoom** | **str** |  | [optional] 
**peer_zoom** | **str** |  | [optional] 
**src_filters** | [**list[ComponentComponentTrafficFilter]**](ComponentComponentTrafficFilter.md) |  | [optional] 
**dst_filters** | [**list[ComponentComponentTrafficFilter]**](ComponentComponentTrafficFilter.md) |  | [optional] 
**source_filters** | [**list[GrpcFilter]**](GrpcFilter.md) |  | [optional] 
**destination_filters** | [**list[GrpcFilter]**](GrpcFilter.md) |  | [optional] 
**include_table** | **bool** |  | [optional] 
**section_type** | **str** |  | [optional] 
**id** | **str** | The Id of this component/section. This field is generated and handled by frontend, NOT backend. | [optional] 
**locality** | [**GrpcLocality**](GrpcLocality.md) |  | [optional] 
**directionality** | [**GrpcDirectionality**](GrpcDirectionality.md) |  | [optional] 
**top_n** | **int** |  | [optional] 
**top_n_sort** | **str** | Column to be sorted in the top n table. | [optional] 
**table_columns** | **list[str]** |  | [optional] 
**top_k** | **int** | Maximum number of time series to return. The default value is 30. Uses the default value if not set. | [optional] 
**label_equality** | [**list[GrpcLabelEqualityPair]**](GrpcLabelEqualityPair.md) |  | [optional] 
**equal_labels** | **list[str]** |  | [optional] 
**unequal_labels** | **list[str]** |  | [optional] 
**source_grouping** | **list[str]** |  | [optional] 
**destination_grouping** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


