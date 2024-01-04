# EfirDataHubModelsRequestsV2RiskRule421Request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isin** | **str** | ISIN (обязательный) | 
**_date** | **datetime** | Дата (обязательный) | 
**use_frozen_dates** | **bool** | TRUE - использовать даты рейтингов | [optional] 
**b_b_country** | **str** | Двухбуквенный код страны филиала банка (Alfa-2), например, KZ (необязательный), по умолчанию &#x3D; RU. | [optional] 
**vla_edition** | **str** | Редакция ВЛА | [optional] 
**ir_pd_level** | **int** | Уровень вероятности дефолта при использовании ПВР.  Принимает целые положительные значения.   Если значение не задано, то не используется. | [optional] 
**use_frozen_max30d_loss** | **bool** | Флаг использования значения обесценения на 18.02.2022 | [optional] [default to False]
**max30d_loss_source_name** | **str** | Наименование источника данных, по которым рассчитаны значения обесценения:  - &#x27;main&#x27; - источник, соответствующий основному торговому инструменту. Приоритет 1.  - &#x27;pcnrd&#x27; - ценовой центр НРД. Приоритет 2.  - &#x27;rudip&#x27; - данные RUDIP/MIFID. Приоритет 3.  - &#x27;moex&#x27; - данные Московской биржи. Приоритет 4.  - Наименование не указано - значение с наивысшим приоритетом из существующих на дату. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

