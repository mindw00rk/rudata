# EfirDataHubModelsRequestsV2EmitentBankruptListRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fininst_ids** | **list[int]** | ID компании в базе Интерфакс. Не более 100.  Если задан, то CompanyCodes не используется. | [optional] 
**company_codes** | **list[str]** | Массив идентификаторов организаций: ИНН или ОГРН. Не более 100. | [optional] 
**actual_on_date** | **datetime** | Дата, на которую актуальны статусы по банкротству организаций. По умолчанию - текущая дата | [optional] 
**filter** | **str** | Строка фильтрации (необязательный) | [optional] 
**page_num** | **int** | Номер страницы для выборки. Если не задан - не используется, если  меньше 1, то устанавливается в 1 | [optional] 
**page_size** | **int** | Размер страницы выборки. Если не задан или меньше 1 - устанавливается в 300 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

