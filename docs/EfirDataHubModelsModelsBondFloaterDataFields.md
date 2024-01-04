# EfirDataHubModelsModelsBondFloaterDataFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fintool_id** | **int** | Идентификатор флоатера | [optional] 
**beg_period** | **datetime** | Начало периода действия модели | [optional] 
**end_period** | **datetime** | Окончание периода действия модели | [optional] 
**start_point** | **str** | Опорная точка - начало или окончание купонного периода, на который определяем ставку | [optional] 
**model_type** | **str** | Тип модели расчета - одна база расчета (single) или несколько баз расчета (max) | [optional] 
**date_pub_n** | **int** | Сдвиг даты публикации относительно опорной точки расчета в периодах | [optional] 
**date_pub_type** | **str** | Сдвиг даты публикации - тип периодов | [optional] 
**date_fix_n** | **int** | Сдвиг даты фиксации базы относительно опорной точки расчета в периодах | [optional] 
**date_fix_type** | **str** | Сдвиг даты фиксации - тип периодов | [optional] 
**bases** | [**list[EfirDataHubModelsModelsBondFloaterDataBases]**](EfirDataHubModelsModelsBondFloaterDataBases.md) | Базы расчета | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

