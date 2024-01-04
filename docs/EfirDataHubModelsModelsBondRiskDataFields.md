# EfirDataHubModelsModelsBondRiskDataFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_fintool** | **int** | Идентификатор облигации | [optional] 
**oecd** | **str** | Значение уровня риска в стране эмитента, по данным классификации ОЭСР | [optional] 
**jurisdiction** | **str** | Название страны, в которой зарегистрирован эмитент выпуска | [optional] 
**currency** | **str** | Трехбуквенное стандартное обозначение валюты страны, в которой зарегистрирован эмитент выпуска | [optional] 
**government** | **int** | Признак, что эмитент правительство или ЦБ страны(0/1) | [optional] 
**bank** | **int** | Признак, что эмитент – банк(0/1) | [optional] 
**name_government** | **int** | Признак, что эмитент имеет право осуществлять эмиссии от имени государства(0/1) | [optional] 
**cis** | **int** | Признак, что страна входит в СНГ(за исключением России) (0/1) | [optional] 
**srf** | **int** | Признак, что эмитент субъект РФ или муниципальное объединение(0/1) | [optional] 
**ifo** | **int** | Признак, что эмитент – международная банковская организация(0/1) | [optional] 
**investmentrating** | **float** | Признак низкого риска инвестирования(0/1) | [optional] 
**isregion** | **float** | Выпуск субъекта федерации: 0 – муниципальный выпуск; 1 – выпуск субъекта федерации; пусто – другое. | [optional] 
**fininstid** | **int** | Идентификатор эмитента в базе Интерфакс | [optional] 
**jurisdiction_oksm** | **str** | Двухбуквенный код страны в соответствии с ОКСМ | [optional] 
**counter** | **int** | Общее количество записей в выборке | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

