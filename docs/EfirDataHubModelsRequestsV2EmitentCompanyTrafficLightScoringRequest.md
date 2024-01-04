# EfirDataHubModelsRequestsV2EmitentCompanyTrafficLightScoringRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fininst_ids** | **list[int]** | Список идентификаторов эмитентов.  Не более 100 элементов.  Если задан, то Codes не используется. | [optional] 
**codes** | **list[str]** | Список кодов эмитентов (ИНН, ОГРН или LEI).  Не более 100 элементов.  Если задан FininstIds, то не используется. | [optional] 
**actual_on_date** | **datetime** | Дата, на которую актуальны показатели кредитной оценки.  По умолчанию - текущая дата. | [optional] 
**page_num** | **int** | Номер страницы выборки. По-умолчанию - 1 | [optional] 
**page_size** | **int** | Размер страницы выборки. По-умолчанию - 100.  Максимум - 100. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

