# EfirDataHubModelsRequestsV2SolvencyRatingAggSecurityRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_reinsurer_ratings** | **bool** | Использовать рейтинги перестраховщиков | 
**scale_code** | **int** | Идентификатор соотношения шкал. Допустимые значения см. Rating/AggregationScaleRatios. | [optional] [default to 2]
**fintool_ids** | **list[int]** | Идентификаторы инструментов в базе Интерфакс;  Максимальное количество элементов: 100 | 
**_date** | **datetime** | Дата, на которую получаются рейтинги; по умолчанию текущая | [optional] 
**use_freezing** | **bool** | Использовать заморозку рейтингов BIG3 | [optional] [default to False]
**freezing_type** | **AllOfEfirDataHubModelsRequestsV2SolvencyRatingAggSecurityRequestFreezingType** | Способ заморозки рейтингов при useFreezing&#x3D;true:  - RussianObjects - заморозка рейтингов BIG3 для российских объектов рейтинга (по умолчанию),  - AllObjects - заморозка рейтингов BIG3 для всех объектов рейтинга.  RussianObjects  AllObjects | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

