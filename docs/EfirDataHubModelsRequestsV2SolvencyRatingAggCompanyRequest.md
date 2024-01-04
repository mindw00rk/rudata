# EfirDataHubModelsRequestsV2SolvencyRatingAggCompanyRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_reinsurer_ratings** | **bool** | Использовать рейтинги перестраховщиков | 
**fininst_ids** | **list[int]** | Идентификаторы компаний в базе Интерфакс;  Максимальное количество элементов: 100 | 
**_date** | **datetime** | Дата, на которую получаются рейтинги; по умолчанию текущая | [optional] 
**scale_code** | **int** | Идентификатор соотношения шкал. Допустимые значения см. Rating/AggregationScaleRatios. | [optional] [default to 2]
**use_freezing** | **bool** | Использовать заморозку рейтингов BIG3 | [optional] [default to False]
**freezing_type** | **AllOfEfirDataHubModelsRequestsV2SolvencyRatingAggCompanyRequestFreezingType** | Способ заморозки рейтингов при useFreezing&#x3D;true:  - RussianObjects - заморозка рейтингов BIG3 для российских объектов рейтинга (по умолчанию),  - AllObjects - заморозка рейтингов BIG3 для всех объектов рейтинга.  RussianObjects  AllObjects | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

