# EfirDataHubModelsModelsRatingRatingAggSecurityByRoleFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fintool_id** | **int** | Идентификатор инструмента в базе Интерфакс | [optional] 
**role_code** | **AllOfEfirDataHubModelsModelsRatingRatingAggSecurityByRoleFieldsRoleCode** | Код группы ролей (одно из значений issuer, surety, offeror, borrower)  0 &#x3D; Unknown  1 &#x3D; Issuer  2 &#x3D; Surety  3 &#x3D; Offeror  4 &#x3D; Borrower | [optional] 
**fininst_id** | **int** | Идентификатор компании в базе Интерфакс | [optional] 
**aggregated_rating_level** | **int** | Уровень рейтинга по итоговой шкале | [optional] 
**rating_code** | **str** | Код лучшего рейтинга или null при отсутствии рейтинга | [optional] 
**rating_id** | **int** | Идентификатор лучшего рейтинга или null при отсутствии рейтинга | [optional] 
**rating_agency_id** | **int** | Идентификатор агентства, присвоившего лучший рейтинг, или null при отсутствии рейтинга | [optional] 
**rating_scale_id** | **int** | Идентификатор шкалы лучшего рейтинга или null при отсутствии рейтинга | [optional] 
**rating_value** | **str** | Значение лучшего рейтинга или null при отсутствии рейтинга | [optional] 
**rating_date** | **datetime** | Дата присвоения значения лучшего рейтинга или null при отсутствии рейтинга | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

