# EfirDataHubModelsModelsMoexHistoryColumnsFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Идентификатор поля (на MOEX используется сквозная нумерация полей по всем рынкам) | [optional] 
**engine_name** | **str** | Подсистема MOEX: stock, state, currency и т.д. | [optional] 
**market_name** | **str** | Рынок MOEX: index, shares, bonds, ndm и т.д. | [optional] 
**column_id** | **int** | Идентификатор колонки на MOEX | [optional] 
**market_id** | **int** | Идентификатор рынка MOEX, для которого применима данная колонка | [optional] 
**name** | **str** | Код поля | [optional] 
**short_title** | **str** | Короткое название | [optional] 
**title** | **str** | Полное название | [optional] 
**is_ordered** | **int** | Флаг «заказной» | [optional] 
**is_system** | **int** | Флаг «системный» | [optional] 
**is_hidden** | **int** | Флаг «невидимый» | [optional] 
**trend_by** | **int** | Флаг тренда (направление последней сделки) | [optional] 
**is_signed** | **int** | Флаг наличия знака (отрицательных величин) | [optional] 
**has_percent** | **int** | Флаг наличия знака процента | [optional] 
**data_type** | **str** | string, date, number и т.д. | [optional] 
**decimals** | **int** | Количество знаков после запятой | [optional] 
**is_linked** | **int** |  | [optional] 
**sort_order** | **int** | Порядок сортировки полей в пользовательском интерфейсе.По-умолчанию – NULL (тогда можно сортировать по алфавиту). | [optional] 
**is_default** | **int** | Флаг поля, которое предлагается для использования в пользовательском интерфейсе по-умолчанию. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

