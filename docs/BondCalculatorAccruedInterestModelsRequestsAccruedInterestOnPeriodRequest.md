# BondCalculatorAccruedInterestModelsRequestsAccruedInterestOnPeriodRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_period_date** | **datetime** | Последняя дата периода расчета. | [optional] 
**fintool_ids** | **list[int]** | Идентификаторы инструментов в базе Интерфакс. Максимальное число элементов 100. | [optional] 
**cash_flow_calc_date** | **datetime** | Дата расчета. Необязательный. По умолчанию используется текущая дата. | [optional] 
**shift_days** | **int** | Число дней смещения, число от 0 до 31 включительно. | [optional] 
**shift_type_source** | **AllOfBondCalculatorAccruedInterestModelsRequestsAccruedInterestOnPeriodRequestShiftTypeSource** | Тип смещения  - calendar - календарные дни (по умолчаню);  - workdays - рабочие дни.  0 &#x3D; Calendar  1 &#x3D; Workdays | [optional] 
**type_currency** | **str** | Источник валюты для определения календаря рабочих дней:  - facevalue - используется календарь страны эмитента валюты номинала инструмента;  - jurisdiction - используется календарь страны выпуска;  - 3-буквенный код валюты ОКВ, например, USD. | [optional] 
**use_rounding** | **bool** | Производить ли округление до знака купона:  - true - да, производить до знака купона (по умолчанию),  - false - не производить. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

