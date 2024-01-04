# EfirDataHubModelsRequestsV2RatingSecurityRatingsHistRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isin** | **str** | ISIN инструмента или регистрационный номер (reg_code).   Если не указан, то возвращаются рейтинги, присвоенные в интервале с dateFrom по dateTo, но не более чем за неделю (с dateTo-6 по dateTo). | [optional] 
**date_from** | **datetime** | Дата актуальности рейтингов (обязательный) | 
**date_to** | **datetime** | Дата актуальности рейтингов (обязательный) | 
**sort** | **int** | Тип сортировки | [optional] 
**flags** | **int** | Опциональные флаги рейтингов (1 – эмитент, 2 – заемщик, 3 – эмитент или заемщик, 4 - гарант или поручитель, 5 - эмитент или гарант или поручитель, 6 - заемщик или гарант или поручитель, 7 - все) | [optional] 
**bond_ratings** | **list[int]** | Список идентификаторов рейтингов бумаг(необязательный). | [optional] 
**company_ratings** | **list[int]** | Список идентификаторов рейтингов компаний (необязательный). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

