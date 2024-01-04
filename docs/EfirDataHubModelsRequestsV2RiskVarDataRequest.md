# EfirDataHubModelsRequestsV2RiskVarDataRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (обязательный) Идентификатор инструмента может принимать значения:   ISIN  CUR – трехбуквенный код валюты(ОКВ Alfa-3),   ID_ISS – внутренний идентификатор ЭФИР | 
**_date** | **datetime** | Дата расчета | [optional] 
**alpha** | **float** | Доверительный уровень (confidence level) в % | [optional] 
**t_var** | **int** | Временной горизонт риска в днях. Обычно, 10 дней. | [optional] 
**fields** | **list[str]** | Названия и порядок значений (полей), возвращаемых функцией | [optional] 
**model_id** | **int** | Номер расчетной модели.  По-умолчанию, используется активная модель. | [optional] 
**cur_risk** | **int** | Признак учета риска в ОВП. Значения 0 или 1. | [optional] 
**last_known_data** | **bool** | True - возвращает данные за последний расчитанный день | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

