# GrpcDashboard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id associated with the dashboard This field is generated and handled by backend. | [optional] 
**created_at** | **datetime** | When this dashboard is first created. This field is populated and handled by backend. | [optional] 
**updated_at** | **datetime** | When this dashboard is last updated. This field is populated and handled by backend. | [optional] 
**owner_email** | **str** | Creator of the dashboard.  This field is set via authorization context from the &#39;POST&#39; request, instead of manually fill-out.  NOTE: Current API specification does NOT support transferring ownership.       Do it in next iteration. | [optional] 
**favorite** | **bool** | Whether the dashboard is marked as &#39;favorite&#39; by the requester.  Note that one can &#39;favor&#39; a dashboard created by other people, as long as the dashboard is marked &#39;global_readable&#39;. One can use the AdjustDashboard request to mark certain dashboard is &#39;favorite&#39;. | [optional] 
**permission** | [**DashboardPermission**](DashboardPermission.md) |  | [optional] 
**name** | **str** |  | [optional] 
**layout** | [**list[DashboardLayout]**](DashboardLayout.md) |  | [optional] 
**components** | [**list[DashboardComponent]**](DashboardComponent.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


