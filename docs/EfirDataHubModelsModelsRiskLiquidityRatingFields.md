# EfirDataHubModelsModelsRiskLiquidityRatingFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Идентификатор инструмента | [optional] 
**isincode** | **str** | ISIN-код выпуска облигаций, присваивается НДЦ | [optional] 
**regcode** | **str** | Регистрационный номер выпуска облигаций | [optional] 
**nrdcode** | **str** | Код НРД выпуска облигаций, присваивается НРД | [optional] 
**nickname** | **str** | Краткое название облигации на русском языке | [optional] 
**fullname** | **str** | Полное название выпуска облигации на русском языке | [optional] 
**liqrt** | **str** | Рейтинг ликвидности: L1 … L7 | [optional] 
**mdepthcoef** | **float** | Коэффициент \&quot;глубины\&quot; рынка | [optional] 
**omegabid** | **float** | Значение экспоненциального среднего от логарифма объема, который нужно купить/продать для сдвига цены на минимальный шаг, при коэффициенте усреднения 0.94 | [optional] 
**gammabid** | **float** | Значение экспоненциального среднего стандартной ошибки модели при коэффициенте усреднения 0.94 | [optional] 
**hhi** | **float** | Индекс Херфиндаля-Хиршмана для структуры владения облигацией | [optional] 
**ind_liq** | **float** | Индекс ликвидности, показывающий средний уровень значения индекса Херфиндаля-Хиршмана в портфеле «типичного» инвестора данной облигации | [optional] 
**ind_unliq** | **float** | Индекс ликвидности, показывающий средний уровень для неликвидных бумаг в портфеле «типичного» инвестора данной облигации | [optional] 
**activ_m2** | **float** | Активность торгов | [optional] 
**summarketvol** | **float** | Объём выпуска в валюте номинала на указанную дату | [optional] 
**theta** | **float** | Доверительная вероятность, константа, равна 0.95 | [optional] 
**mu** | **float** | Допустимая погрешность оценки цены (μ), константа, равна 1.5 | [optional] 
**nickname_eng** | **str** | Краткое название облигации на английском языке | [optional] 
**fullname_eng** | **str** | Полное название выпуска облигации на английском языке | [optional] 
**dt** | **datetime** | Дата расчета | [optional] 
**fintoolid** | **int** | Идентификатор текущего инструмента в базе ФинМаркет | [optional] 
**sigmabid** | **float** |  | [optional] 
**mubid** | **float** |  | [optional] 
**issue_vol** | **float** |  | [optional] 
**activ_m3** | **float** |  | [optional] 
**duration** | **float** |  | [optional] 
**omega** | **float** |  | [optional] 
**nrd_trueprice_pct** | **float** |  | [optional] 
**k_theta** | **float** |  | [optional] 
**fintool_type** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**method_id** | **float** |  | [optional] 
**ro** | **float** |  | [optional] 
**vol_max** | **float** |  | [optional] 
**l_date** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

