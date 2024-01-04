# EfirDataHubModelsRequestsV2RiskFairValueRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Обязательный параметр. Инструмент задается числовым или строковым кодом – это может быть ID_ISS, ISIN, TradeCode, EfirCode | 
**_date** | **datetime** | Обязательный параметр. Дата расчета текущей справедливой стоимости (ТСС). Может задаваться ячейкой с датой либо строкой в формате \&quot;DD.MM.YYYY\&quot;. | 
**price_type** | **str** | Тип цены  Any или пустое значение - по умолчанию  Market – рыночная  Close – цена закрытия  AvgPrice – средневзвешенная | [optional] 
**is_close_register** | **bool** | true – учитывать даты закрытия реестра перед выплатой купона/амортизации.  false – (по умолчанию) не учитывать даты закрытия реестра. В этом случае будут использоваться, соответственно,  даты начала и конца купонного периода, а также дата амортизации. | [optional] 
**is_percent** | **bool** | true – функция возвращает справедливую стоимость в процентах к номиналу. Применимо только к облигациям.  false – (по умолчанию) функция возвращает справедливую стоимость в валюте номинала. | [optional] 
**ignore_accrued_int** | **bool** | true – не учитывать НКД для облигаций;  false – (по умолчанию) учитывать НКД для облигаций. | [optional] 
**depth** | **int** | Глубина поиска, выраженная в днях.  Значение по умолчанию: 90. Если Depth&#x3D;0, поиск цены будет идти только в рамках указанной даты | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
