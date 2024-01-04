# EfirDataHubModelsRequestsV2RatingCompanyRatingsAggRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **list[str]** | Список идентификаторов компаний/стран (Обязательный) | 
**id_types** | **list[str]** | Тип идентификатора компании/страны. (Необязательный) Возможные значения:  \&quot;OKPO\&quot; - ОКПО  \&quot;OGRN\&quot; - ОГРН  \&quot;INN\&quot; - ИНН для российских компаний, TIN для остальных  \&quot;TIN\&quot; - TIN (США)  \&quot;LEI_CODE\&quot; - LEI-код  \&quot;SWIFT\&quot; - Код SWIFT  \&quot;ISSUER_NRD\&quot; - Идентификатор эмитента в базе НРД  \&quot;FININSTID\&quot; - Идентификатор эмитента в базе Интерфакс  \&quot;SPARKID\&quot; - Идентификатор эмитента в базе СПАРК  \&quot;A2\&quot; - Идентификатор страны A2 по ISO 3166-1 Alpha-2  \&quot;A3\&quot; - Идентификатор страны A3 по ISO 3166-1 Alpha-3 | [optional] 
**company_name** | **str** | Тип наименования компании, выводимого в поле company_name. (Необязательный) Возможные значения:  \&quot;SHORTNAME_RUS\&quot;  \&quot;FULLNAME_RUS\&quot;  \&quot;SHORTNAME_ENG\&quot;  \&quot;FULLNAME_ENG\&quot;  \&quot;SHORTNAME_RUS_NRD\&quot;  \&quot;FULLNAME_RUS_NRD\&quot;  \&quot;SHORTNAME_ENG_NRD\&quot;  \&quot;FULLNAME_ENG_NRD\&quot;  \&quot;SHORTNAME_RUS_SPARK\&quot;  \&quot;FULLNAME_RUS_SPARK\&quot;  \&quot;SHORTNAME_ENG_SPARK\&quot;  \&quot;FULLNAME_ENG_SPARK\&quot; | [optional] 
**agg_type** | **str** | Идентификатор типа агрегата. (Необязательный) Допустимые значения: MIN, MAX. По умолчанию MAX. | [optional] 
**using_type** | **str** | (Необязательный, действует только на российские компании)   Вариант использования иностранных и российских рейтингов. Допустимые значения: Rus/Big3/Composite.   По умолчанию Rus – используются только российские рейтинги.   Big3 – используются только иностранные рейтинги.   Composite – при отсутствии российских рейтингов у российской компании использовать рейтинги иностранных рейтинговых агентств, но значение приводить к шкале для российских субъектов по таблице соответствия. | [optional] 
**priority_ra** | **str** | (Необязательный, действует только на российские компании)   Приоритетное российское рейтинговое агентство. Допустимые значения: AKRA/MAX.   По умолчанию AKRA – при прочих равных показываем рейтинги АКРА. RAEX показываем, только если рейтингов от АКРА нет совсем.   MAX – показываем АКРА, RAEX показываем, только если он лучше. | [optional] 
**_date** | **datetime** | (Необязательный) Дата рейтингов. Если не задано, используется текущая дата. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

