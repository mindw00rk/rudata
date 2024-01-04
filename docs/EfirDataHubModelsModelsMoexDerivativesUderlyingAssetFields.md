# EfirDataHubModelsModelsMoexDerivativesUderlyingAssetFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basset_group_id** | **int** | Идентификатор группы базового актива | [optional] 
**basset_group_name** | **str** | Наименование группы базового актива | [optional] 
**basset_code** | **str** | Короткий код базового актива | [optional] 
**basset_name** | **str** | Наименование базового актива | [optional] 
**basset_fintoolid** | **int** | Идентификатор базового актива в БД Интерфакс  Для товаров, валюты, индексов, процентных ставок, валютных пар описание базового актива может быть получено с помощью метода Indicator/List  Для акций и паев ИФ см. Info/FintoolReferenceData. | [optional] 
**bcontract_ticker** | **str** | Тикер базового контракта | [optional] 
**bcontract_fintoolid** | **int** | Идентификатор базового контракта в БД Интерфакс | [optional] 
**bcontract_name** | **str** | Наименование базового контракта | [optional] 
**o_sh_minstartdate** | **datetime** | Минимальная дата начала обращения опционов на акции | [optional] 
**o_sh_maxenddate** | **datetime** | Максимальная дата окончания обращения опционов на акции | [optional] 
**o_fut_minstartdate** | **datetime** | Минимальная дата начала обращения опционов на фьючерсы | [optional] 
**o_fut_maxenddate** | **datetime** | Максимальная дата окончания обращения опционов на фьючерсы | [optional] 
**basset_neg_strike** | **bool** | Наличие отрицательного страйка | [optional] 
**has_futures** | **bool** | Наличие фьючерсов для базового контракта | [optional] 
**fut_min_exp_date** | **datetime** | Минимальная дата экспирации фьючерсов | [optional] 
**fut_max_exp_date** | **datetime** | Максимальная дата экспирации фьючерсов | [optional] 
**spread_min_exp_date** | **datetime** | Минимальная дата экспирации спредов | [optional] 
**spread_max_exp_date** | **datetime** | Максимальная дата экспирации спредов | [optional] 
**counter** | **int** | Общее количество записей в выборке | [optional] 
**rn** | **int** | Номер записи в выборке | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

