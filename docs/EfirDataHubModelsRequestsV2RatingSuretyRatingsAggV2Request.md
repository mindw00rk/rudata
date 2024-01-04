# EfirDataHubModelsRequestsV2RatingSuretyRatingsAggV2Request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **list[str]** | (обязательный) Список идентификаторов инструментов (ISIN, регистрационный номер, код НРД, ISIN144a). FINTOOLID не поддерживается. | 
**agg_type** | **str** | (необязательный) Идентификатор типа агрегата. Допустимые значения:  - MAX (по умолчанию),  - MIN. | [optional] 
**company_name** | **str** | (необязательный) Тип наименования компании, выводимого в поле company_name. Возможные значения:  - SHORTNAME_RUS  - FULLNAME_RUS  - SHORTNAME_ENG  - FULLNAME_ENG  - SHORTNAME_RUS_NRD  - FULLNAME_RUS_NRD  - SHORTNAME_ENG_NRD  - FULLNAME_ENG_NRD  - SHORTNAME_RUS_SPARK  - FULLNAME_RUS_SPARK  - SHORTNAME_ENG_SPARK  - FULLNAME_ENG_SPARK | [optional] 
**_date** | **datetime** | (необязательный) Дата рейтингов. Если не задано, используется текущая дата. | [optional] 
**using_type** | **str** | (Необязательный, действует только на российские компании)   Вариант использования иностранных и российских рейтингов. Допустимые значения:  - Rus – По умолчанию. Используются только российские рейтинги.   - Big3 – используются только иностранные рейтинги.   - Composite – при отсутствии российских рейтингов у российской компании использовать рейтинги иностранных рейтинговых агентств, но значение приводить к шкале для российских субъектов по таблице соответствия. | [optional] 
**priority_ra** | **str** | (Необязательный, действует только на российские компании)   Приоритетное российское рейтинговое агентство. Допустимые значения:  - AKRA – По умолчанию. При прочих равных показываем рейтинги АКРА. RAEX показываем, только если рейтингов от АКРА нет совсем.   - MAX – показываем АКРА, RAEX показываем, только если он лучше. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

