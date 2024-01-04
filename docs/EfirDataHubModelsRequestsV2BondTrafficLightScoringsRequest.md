# EfirDataHubModelsRequestsV2BondTrafficLightScoringsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fintool_ids** | **list[int]** | Числовые идентификаторы в базе Интерфакс; если заданы и Codes и FintoolIds - используется FintoolIds;  Максимальное количество элементов: 100 | [optional] 
**codes** | **list[str]** | Идентификаторы инструментов: ISIN или регистрационный номер (RegCode) или код НРД (NRDCode);  Максимальное количество элементов: 100 | [optional] 
**actual_on_date** | **datetime** | Дата, на которую актуальны показатели кредитной оценки. По умолчанию - текущая дата. | [optional] 
**page_num** | **int** | Номер страницы для выборки. Если не задан - не используется, если  меньше 1, то устанавливается в 1 | [optional] 
**page_size** | **int** | Размер страницы выборки. Если не задан или меньше 1 - устанавливается в 300 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

