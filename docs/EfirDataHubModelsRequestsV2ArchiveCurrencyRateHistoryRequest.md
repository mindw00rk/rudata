# EfirDataHubModelsRequestsV2ArchiveCurrencyRateHistoryRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_currency** | **str** | Базовая валюта, чей курс нужно узнать (трехбуквенный код) | [default to 'USD']
**quoted_currency** | **str** | Котируемая валюта, в которой нужно выразить курсы (трехбуквенный код) | [default to 'RUB']
**date_from** | **datetime** | Дата начала выборки (по умолчанию текущая дата) | [optional] 
**date_to** | **datetime** | Дата окончания выборки (по умолчанию текущая дата) | [optional] 
**with_holidays** | **bool** | С курсом валюты в праздничные и выходные дни | [optional] [default to True]
**page_num** | **int** | Номер страницы для выборки (по-умолчанию 1) | [optional] [default to 1]
**page_size** | **int** | Размер страницы выборки (по-умолчаню - 1000) | [optional] [default to 100]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

