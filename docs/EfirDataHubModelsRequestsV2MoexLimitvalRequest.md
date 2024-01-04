# EfirDataHubModelsRequestsV2MoexLimitvalRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fintool_id** | **int** | Идентификатор инструмента в БД Интерфакс.  Если не указан, то возвращаются данные только за одну дату - максимальную из startDate и endDate | [optional] 
**start_date** | **datetime** | Дата начала диапазона дат.  Если не задан, то устанавливается текущая дата | [optional] 
**end_date** | **datetime** | Необязательный параметр.  Дата окончания диапазона дат. Если не задан, то устанавливается текущая дата | [optional] 
**page_num** | **int** | Номер страницы выборки.  По умолчанию - 1(при значении меньше 0, принимает значение 1) | [optional] [default to 1]
**page_size** | **int** | Размер страницы выборки. Не более 100. | [optional] [default to 100]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

