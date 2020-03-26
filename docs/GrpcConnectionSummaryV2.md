# GrpcConnectionSummaryV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_labels** | [**list[GrpcLabel]**](GrpcLabel.md) | Labels identifying this connection. | [optional] 
**destination_labels** | [**list[GrpcLabel]**](GrpcLabel.md) |  | [optional] 
**num_ok** | **float** | Number of successes (delivered packets, HTTP 200 codes, etc). | [optional] 
**num_bad** | **float** | Number of failures (dropped packets, HTTP errors, etc). | [optional] 
**percent_bad** | **float** | Percent of bad events (percent packet dropps, HTTP error rate, etc).  100 * num_bad / (num_ok + num_bad). | [optional] 
**values_ok** | **list[float]** | Timeseries of the num_ok metric. | [optional] 
**values_bad** | **list[float]** | Timeseries of the num_bad metric. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


