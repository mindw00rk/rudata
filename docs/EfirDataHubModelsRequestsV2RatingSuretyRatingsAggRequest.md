# EfirDataHubModelsRequestsV2RatingSuretyRatingsAggRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **list[str]** | (обязательный) Список идентификаторов инструментов | 
**agg_type** | **str** | (необязательный) Идентификатор типа агрегата. Допустимые значения: MIN, MAX. По умолчанию MAX. | [optional] 
**company_name** | **str** | (необязательный) Тип наименования компании, выводимого в поле company_name. Возможные значения:  \&quot;SHORTNAME_RUS\&quot;  \&quot;FULLNAME_RUS\&quot;  \&quot;SHORTNAME_ENG\&quot;  \&quot;FULLNAME_ENG\&quot;  \&quot;SHORTNAME_RUS_NRD\&quot;  \&quot;FULLNAME_RUS_NRD\&quot;  \&quot;SHORTNAME_ENG_NRD\&quot;  \&quot;FULLNAME_ENG_NRD\&quot;  \&quot;SHORTNAME_RUS_SPARK\&quot;  \&quot;FULLNAME_RUS_SPARK\&quot;  \&quot;SHORTNAME_ENG_SPARK\&quot;  \&quot;FULLNAME_ENG_SPARK\&quot; | [optional] 
**_date** | **datetime** | (необязательный) Дата рейтингов. Если не задано, используется текущая дата. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

