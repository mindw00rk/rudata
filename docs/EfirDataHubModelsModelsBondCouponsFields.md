# EfirDataHubModelsModelsBondCouponsFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_fintool** | **int** | Идентификатор облигации | [optional] 
**id_coupon** | **int** | Номер купонной выплаты | [optional] 
**begin_period** | **datetime** | Дата начала купона | [optional] 
**end_period** | **datetime** | Дата окончания купона | [optional] 
**coupon_period** | **int** | Количество дней в купонном периоде | [optional] 
**days_from_dist** | **int** | Количество дней от даты начала размещения до даты окончания купонного периода | [optional] 
**coupon_rate** | **float** | Ставка купона, процентов годовых | [optional] 
**pay_per_bond** | **float** | Выплата на одну облигацию | [optional] 
**coupon_val** | **float** | Выплаты на все облигации в обращении | [optional] 
**stop_trade_date** | **datetime** | Дата приостановки торгов в целях формирования списка владельцев облигаций для осуществления купонной выплаты | [optional] 
**pay_date** | **datetime** | Дата реальной выплаты купона | [optional] 
**coupon_rate_date** | **datetime** | Дата, не позже которой должна быть определена купонная ставка для будущих дат/дата определения купонной ставки для прошедших дат | [optional] 
**fix_date** | **datetime** | Дата фиксации списка | [optional] 
**update_date** | **datetime** | Дата/время последнего изменения записи | [optional] 
**pay_per_bond_frac** | **float** | Выплата на одну облигацию (без округл.) | [optional] 
**base_type_id** | **int** | ID типа базового индикатора | [optional] 
**base_type_name** | **str** | Название типа базового индикатора | [optional] 
**base_fintoolid** | **int** | ID базового инструмента в ФинМаркет | [optional] 
**rate_spread_pct** | **float** | Отличие ставки купона от ставки базового индикатора, в % | [optional] 
**period_from** | **datetime** | Дата начала действия ставки/правила | [optional] 
**period_to** | **datetime** | Дата окончания действия ставки/правила | [optional] 
**note** | **str** | Примечание | [optional] 
**counter** | **int** | Общее количество записей в выборке | [optional] 
**rn** | **int** | Номер записи в выборке | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

