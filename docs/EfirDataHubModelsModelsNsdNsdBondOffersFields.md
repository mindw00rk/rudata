# EfirDataHubModelsModelsNsdNsdBondOffersFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code_nsd** | **str** | Идентификатор выпуска в базе НРД | [optional] 
**payment_currency** | **str** | Валюта выплаты | [optional] 
**payment_date_calc** | **datetime** | Расчетная дата погашения | [optional] 
**payment_date_fact** | **datetime** | Дата фактической выплаты | [optional] 
**payment_date_plan** | **datetime** | Реальная дата погашения | [optional] 
**payment_size_cur** | **float** | Погашение на одну облигацию в валюте выплаты | [optional] 
**payment_size_percent** | **float** | Объем выплат, проценты | [optional] 
**pp_number** | **int** | Номер оферты (null для окончательного погашения) | [optional] 
**record_date_plan** | **datetime** | Дата фиксации списка | [optional] 
**id_fintool** | **int** | Идентификатор выпуска в базе Интерфакс (синоним fintoolid) | [optional] 
**action_id** | **int** | Референс КД | [optional] 
**action_type_code** | **str** | Тип погашения | [optional] 
**record_date_calc** | **datetime** | Дата фиксации расчетная | [optional] 
**lock_date_calc** | **datetime** | Дата блокировки расчетная | [optional] 
**lock_date_plan** | **datetime** | Дата блокировки плановая | [optional] 
**unlock_date_calc** | **datetime** | Дата разблокировки расчетная | [optional] 
**unlock_date_plan** | **datetime** | Дата разблокировки плановая | [optional] 
**action_status_mn** | **str** | Состояние КД | [optional] 
**update_date** | **datetime** | Дата/время последнего изменения записи | [optional] 
**nrd_sec_id** | **int** | Идентификатор бумаги в базе НРД | [optional] 
**counter** | **int** | Общее количество записей в выборке | [optional] 
**rn** | **int** | Номер записи в выборке | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

