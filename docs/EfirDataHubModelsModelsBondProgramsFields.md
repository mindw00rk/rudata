# EfirDataHubModelsModelsBondProgramsFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Идентификатор программы (id_fintool) | [optional] 
**shortname_rus** | **str** | Краткое название программы | [optional] 
**fullname_rus** | **str** | Полное название программы | [optional] 
**fininstid** | **int** | Идентификатор эмитента в базе Интерфакс | [optional] 
**okpo** | **str** | ОКПО эмитента | [optional] 
**status** | **str** | Статус программы | [optional] 
**country** | **str** | Двухбуквенный код страны в соответствии с ОКСМ | [optional] 
**reg_code** | **str** | Регистрационный номер программы | [optional] 
**reg_date** | **datetime** | Дата регистрации | [optional] 
**reg_org** | **str** | Регистратор(ФСФР, ЦБ, МосБиржа и т.п.) | [optional] 
**facevalue** | **float** | Номинал | [optional] 
**facevalue_currency** | **str** | Валюта номинала | [optional] 
**issue_vol** | **float** | Объем программы(в штуках) | [optional] 
**issue_val** | **float** | Размер программы(в деньгах) | [optional] 
**begdist_date** | **datetime** | Дата начала размещения | [optional] 
**enddist_date** | **datetime** | Дата окончания размещения | [optional] 
**market_vol** | **float** | Объем в обращении(в штуках) | [optional] 
**market_val** | **float** | Объем в обращении(в деньгах) | [optional] 
**guaranteed** | **int** | Признак наличия гарантии по программе | [optional] 
**guaranteed_val** | **float** | Гарантированная сумма | [optional] 
**coverage_val** | **float** | Объем ипотечного/иного покрытия по программе | [optional] 
**have_regress** | **int** | Признак наличия полного регресса по программе | [optional] 
**emitent_take_risk** | **int** | Эмитент принимает на себя часть кредитного риска через сохранение доли в секьюритизируемых активах | [optional] 
**debt_cost_ratio** | **float** | Средняя величина соотношения суммы основного долга по ссудам к текущей(справедливой) стоимости предметов залога на момент выпуска программы | [optional] 
**note** | **str** | Примечание | [optional] 
**counter** | **int** | Общее количество записей в выборке | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

