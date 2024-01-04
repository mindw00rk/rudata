# EfirDataHubModelsRequestsV2ScoringMainOwnersRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**list[EfirDataHubModelsRequestsV2ScoringCompanyCode]**](EfirDataHubModelsRequestsV2ScoringCompanyCode.md) | Идентификаторы компаний. Обязательный параметр. Не более 20 элементов. | 
**cutoff_sharepart** | **float** | Наименьшая доля владения, с которой акционер считается крупным. По умолчанию &#x3D; 0. Если не задана, то принимают &#x3D; 0 | 
**cutoff_rating** | **float** | Наименьшая доля, с которой акционер, имеющий рейтинг, считается крупным. По умолчанию &#x3D; 0. Если не задана, то принимают &#x3D; 0 | 
**cutoff_scoring** | **float** | Наименьшая доля владения, с которой акционер, имеющий скоринг и выручку не менее 5*10^8 р, считается крупным. По умолчанию &#x3D; 0. Если не задана, то принимают &#x3D; 0 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

