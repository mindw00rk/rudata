# EfirDataHubModelsRequestsV2InfoHolidaysRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_id** | **int** | ID страны, для организации (правительства) которой выполняют запрос дат событий | [optional] 
**fininst_id** | **int** | ID организации, для которых выполняют запрос дат событий | [optional] 
**begin_date** | **datetime** | Дата начала периода | [optional] 
**end_date** | **datetime** | Дата окончания периода | [optional] 
**calendar_type_id** | **AllOfEfirDataHubModelsRequestsV2InfoHolidaysRequestCalendarTypeId** | Тип календаря, к которому принадлежит событие (страновой -2 или корпоративный -3 календарь)  0 &#x3D; Unknown  2 &#x3D; Country  3 &#x3D; Corporative | [optional] 
**filter** | **str** | Параметры фильтра данных | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

