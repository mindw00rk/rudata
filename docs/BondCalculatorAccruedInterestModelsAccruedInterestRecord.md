# BondCalculatorAccruedInterestModelsAccruedInterestRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fintool_id** | **int** | Идентификатор инструмента в базе Интерфакс | [optional] 
**shift_days** | **int** | Число дней смещения | [optional] 
**shift_type_source** | **AllOfBondCalculatorAccruedInterestModelsAccruedInterestRecordShiftTypeSource** | Тип календаря:  - calendar - календарные дни;  - workdays - рабочие дни.  0 &#x3D; Calendar  1 &#x3D; Workdays | [optional] 
**type_currency** | **str** | Код или источник валюты:  - facevalue - используется календарь страны выпуска;  - jurisdiction - используется календарь страны-эмитента валюты номинала инструмента;  - 3-буквенный код валюты ОКВ. | [optional] 
**_date** | **datetime** | Дата, на которую рассчитаны показатели | [optional] 
**accrued_interest** | **float** | НКД в валюте номинала | [optional] 
**accrued_interest_pct** | **float** | НКД в процентах от номинала | [optional] 
**current_face_value** | **float** | Текущий номинал в валюте номинала | [optional] 
**current_face_value_pct** | **float** | Текущий номинал в процентах от номинала | [optional] 
**calculation_type** | **AllOfBondCalculatorAccruedInterestModelsAccruedInterestRecordCalculationType** | Способ вычисления НКД:  - typical - типовой случай;  - null - при ошибке.  0 &#x3D; Typical | [optional] 
**error** | **str** | Текст ошибки при наличии, в остальных случаях null. | [optional] 
**face_value_currency** | **str** | Код валюты номинала по ОКВ | [optional] 
**accrued_interest_currency** | **str** | Код валюты НКД (купонной выплаты) по ОКВ | [optional] 
**face_value_last_known_date** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

