# EfirDataHubModelsRequestsV2RatingCompanyRatingsHistRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_type** | **str** | Возможные значения: “FININSTID”(по умолчанию), “A2”, “A3”, “ОГРН”, “OGRN”, “ИНН”, “INN” | [optional] 
**date_from** | **datetime** | Дата актуальности рейтингов (обязательный). | 
**date_to** | **datetime** | Дата актуальности рейтингов (обязательный). | 
**sort** | **int** | Тип сортировки | [optional] 
**ratings** | **list[str]** | Список идентификаторов рейтингов | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

