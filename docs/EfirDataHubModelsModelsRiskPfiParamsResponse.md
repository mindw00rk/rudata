# EfirDataHubModelsModelsRiskPfiParamsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isin_base** | **str** | ISIN базового актива | [optional] 
**currency_code** | **str** | Трехбуквенный код валюты | [optional] 
**lot_size** | **int** | Размер лота | [optional] 
**expiration_date** | **str** | Дата экспирации типа String | [optional] 
**expiration_date_dt** | **datetime** | Дата экспирации типа DateTime | [optional] 
**currency_rate** | **float** | Курс валюты к рублю | [optional] 
**price** | **float** | Цена базового актива | [optional] 
**point** | **float** | Стоимость одного пункта цены контракта в валюте контракта | [optional] 
**error** | **str** | Текст ошибки, если она есть | [optional] 
**nominal** | **float** | Номинал ПФИ | [optional] 
**market_price** | **float** | Рыночная цена | [optional] 
**accrued_interest** | **float** | НКД облигации, наилучшей к поставке на дату расчета в процентах от номинала. | [optional] 
**delivery_ai** | **float** | НКД облигации, наилучшей к поставке на дату экспирации фьючерса.Процент от номинала бонда в процентах от номинала. | [optional] 
**conversion_factor** | **float** | Конверсионный коэффициент облигации, наилучшей к поставке. | [optional] 
**instrument_type** | **int** | Тип ПФИ:  0 – фьючерс на акции или индекс  1 – фьючерс на корзину облигаций  2 – товарный контракт  3 – валютный контракт  4 – фьючерс на процентную ставку | [optional] 
**isin_base_rate** | **float** | Курс базового актива для валютных контрактов | [optional] 
**rate_period** | **str** | Дата для фьючерсов на процентную ставку | [optional] 
**quotation_price** | **float** | Котировка ПФИ | [optional] 
**basic_asset_code** | **str** | Код базового актива | [optional] 
**risk_type** | **str** | Тип риска | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

