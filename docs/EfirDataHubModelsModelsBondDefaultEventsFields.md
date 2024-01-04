# EfirDataHubModelsModelsBondDefaultEventsFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_fintool** | **int** | Идентификатор облигации | [optional] 
**default_type** | **str** | Тип дефолта | [optional] 
**event_type** | **str** | Тип события, по которому наступил дефолт | [optional] 
**id_event** | **int** | Номер события(в рамках конкретных обязательств, для купонов – номер купона, для выкупов – номер выкупа, для погашения или 1 (в случае отсутствия амортизационного погашения) или номер погашения) | [optional] 
**pay_date** | **datetime** | Дата дефолта | [optional] 
**real_pay_date** | **datetime** | Дата реального исполнения обязательства(заполняется в случае технического дефолта) | [optional] 
**note** | **str** | Примечание | [optional] 
**id** | **int** | Идентификатор события | [optional] 
**issueruid** | **int** |  | [optional] 
**borroweruid** | **int** |  | [optional] 
**counter** | **int** | Общее количество записей в выборке | [optional] 
**rn** | **int** | Номер записи в выборке | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

