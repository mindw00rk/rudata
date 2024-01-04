# EfirDataHubModelsModelsRatingListRatingsFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Идентификатор рейтинга (устарел, надо использовать rating_id) | [optional] 
**rating_id** | **int** | Идентификатор вида рейтинга | [optional] 
**code_name** | **str** | Символьный код рейтинга | [optional] 
**agency** | **str** | Рейтинговое агентство (рус) | [optional] 
**fullname_rus** | **str** | Русское наименование рейтинга | [optional] 
**fullname_eng** | **str** | Английское наименование рейтинга | [optional] 
**for_instrument** | **int** | &#x3D; 1, если рейтинг относится к инструменту | [optional] 
**for_company** | **int** | &#x3D; 1, если рейтинг относится к эмитенту | [optional] 
**agency_eng** | **str** | Рейтинговое агентство (анг) | [optional] 
**official_name** | **str** | Официальное наименование рейтинга | [optional] 
**is_credit** | **int** | &#x3D; 1 для кредитных рейтингов | [optional] 
**term_type** | **str** | Идентификатор типа срочности | [optional] 
**term_type_name** | **str** | Наименование типа срочности | [optional] 
**currency_type** | **str** | Идентификатор типа валюты | [optional] 
**currency_type_name** | **str** | Наименование типа валюты | [optional] 
**scale_type** | **str** | Идентификатор типа шкалы | [optional] 
**scale_type_name** | **str** | Наименование типа шкалы | [optional] 
**is_archive** | **int** | &#x3D; 1 для архивных (не используемых на текущий момент) рейтингов | [optional] 
**is_accred_br** | **int** | Аккредитация Банка России | [optional] 
**doc_511p** | **str** | 511-П | [optional] 
**doc_421p** | **str** | 421-П | [optional] 
**doc_180i** | **str** | 180-И | [optional] 
**agency_id** | **int** | Идентификатор агентства | [optional] 
**used_in_agg** | **bool** | Флаг участия в расчёте агрегированных рейтингов. | [optional] 
**scale_id** | **int** | Идентификатор шкалы | [optional] 
**aggregation_type** | **str** | Тип агрегации (&#x27;RU&#x27; или &#x27;BIG3&#x27;) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

