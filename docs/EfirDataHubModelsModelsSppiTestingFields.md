# EfirDataHubModelsModelsSppiTestingFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fintool_id** | **int** | Идентификатор бумаги в БД Интерфакс | [optional] 
**calc_date** | **datetime** | Дата тестирования | [optional] 
**isin_code** | **str** | Код инструмента ISIN | [optional] 
**overallresult** | **str** | Общий результат тестирования | [optional] 
**full_name** | **str** | Полное наименование облигации | [optional] 
**coupon_type** | **str** | Тип купона | [optional] 
**mty_date** | **datetime** | Дата погашения | [optional] 
**face_value_currency** | **str** | Валюта долга | [optional] 
**rate_formula** | **str** | Формула для плавающей и переменной ставок | [optional] 
**multiplier** | **float** | Множитель перед рыночным показателем | [optional] 
**specified_rate_period** | **int** | Период действия заданной ставки купона (в месяцах) | [optional] 
**base_rate_period** | **int** | Срок базовой процентной ставки (в месяцах) | [optional] 
**base_rate_currency** | **str** | Валюта базовой процентной ставки | [optional] 
**base_rate_country** | **str** | Страна базовой процентной ставки в соответствии с ОКСМ | [optional] 
**base_rate_type** | **str** | Тип базовой процентной ставки | [optional] 
**convertibility** | **bool** | Конвертируемость | [optional] 
**have_early_eedemption_offer** | **bool** | Оферты типа \&quot;Досрочное погашение (ковенант)\&quot; | [optional] 
**is_subordinated** | **bool** | Субординированность | [optional] 
**criteria_check** | [**list[EfirDataHubModelsModelsSppiTestingCriteriaCheck]**](EfirDataHubModelsModelsSppiTestingCriteriaCheck.md) | Массив результатов тестирования по критериям | [optional] 
**covenants** | [**list[EfirDataHubModelsModelsSppiTestingCovenant]**](EfirDataHubModelsModelsSppiTestingCovenant.md) | Список ковенантов | [optional] 
**counter** | **int** | Общее количество записей в выборке | [optional] 
**rn** | **int** | Номер записи в выборке | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

