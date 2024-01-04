# EfirDataHubModelsRequestsV2ArchiveHistoryRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iss_id** | **int** | Идентификатор инструмента. Должен быть задан этот параметр или isin. | [optional] 
**isin** | **str** | ISIN инструмента. Должен быть задан этот параметр или issId. | [optional] 
**date_from** | **datetime** | Дата начала периода | 
**date_to** | **datetime** | Дата окончания периода | 
**step** | **str** | Шаг 5 – 5-минутки; 30 – получасовики; 60 – часовики; 1440 – EndOfDay | 
**row_num** | **int** | Макимальное возвращаемое количество записей. | [optional] 
**fields** | **list[str]** | Список кодовых наименований полей, колонка name из выходной таблицы метода /Info/Fields. По умолчанию выводятся все доступные поля. | [optional] 
**official** | **bool** | Запрос официальных итогов:  - true – запрашивать официальные итоги   - false – запрашивать неофициальные итоги | [optional] 
**sort** | **str** | Сортировка по указанному полю,  в виде FIELD&#x3D;[A|D], например \&quot;TIME&#x3D;D\&quot; - сортировка по убыванию значений поля TIME.  По умолчанию TIME&#x3D;A | [optional] 
**trade_site** | **str** | Идентификатор ID из справочника «Торговые площадки» или код режима торгов МБ. Используется для уточнения указанного Isin | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

