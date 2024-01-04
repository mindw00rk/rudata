# EfirDataHubModelsRequestsV2RatingCompanyRatingsTableRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**list[EfirDataHubModelsRequestsV2RatingCompanyId]**](EfirDataHubModelsRequestsV2RatingCompanyId.md) | Массив объектов с описанием идентификаторов компаний/стран и их типов | 
**_date** | **datetime** | Дата, на которую должны быть загружены данные (обязательный) | 
**company_name** | **str** | Тип наименования компании/страны, выводимого в результатах запроса. (необязательный) Возможные значения:  \&quot;SHORTNAME_RUS\&quot;  \&quot;FULLNAME_RUS\&quot;  \&quot;SHORTNAME_ENG\&quot;  \&quot;FULLNAME_ENG\&quot;  \&quot;SHORTNAME_RUS_NRD\&quot;  \&quot;FULLNAME_RUS_NRD\&quot;  \&quot;SHORTNAME_ENG_NRD\&quot;  \&quot;FULLNAME_ENG_NRD\&quot;  \&quot;SHORTNAME_RUS_SPARK\&quot;  \&quot;FULLNAME_RUS_SPARK\&quot;  \&quot;SHORTNAME_ENG_SPARK\&quot;  \&quot;FULLNAME_ENG_SPARK\&quot; | [optional] 
**filter** | **str** | Строка фильтрации. (необязательный) | [optional] 
**count** | **int** | Макимальное возвращаемое количество записей.  Если для count задано значение 0 или его присвоение отсутствует, то возвращается 1000 записей.  Чтобы получить все записи, надо указать заведомо большее возвращаемое число записей. Например: 1000000. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

