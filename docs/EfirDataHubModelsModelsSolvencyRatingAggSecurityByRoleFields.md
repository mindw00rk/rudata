# EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fintool_id** | **int** | Идентификатор инструмента в базе Интерфакс | [optional] 
**role_code** | **str** | Код роли (всегда surety - гарант/поручитель) | [optional] 
**surety_fininst_id** | **int** | Идентификатор гаранта/поручителя в базе Интерфакс | [optional] 
**surety_aggregated_rating_level** | **int** | Уровень рейтинга гаранта/поручителя по итоговой шкале | [optional] 
**surety_rating_code** | **str** | Код лучшего рейтинга гаранта/поручителя или null при отсутствии рейтинга | [optional] 
**surety_rating_id** | **int** | Идентификатор лучшего рейтинга гаранта/поручителя или null при отсутствии рейтинга | [optional] 
**surety_rating_agency_id** | **int** | Идентификатор агентства, присвоившего лучший рейтинг гаранта/поручителя, или null при отсутствии рейтинга | [optional] 
**surety_rating_scale_id** | **int** | Идентификатор шкалы лучшего рейтинга гаранта/поручителя или null при отсутствии рейтинга | [optional] 
**surety_rating_value** | **str** | Значение лучшего рейтинга гаранта/поручителя или null при отсутствии рейтинга | [optional] 
**surety_rating_date** | **datetime** | Дата присвоения значения лучшего рейтинга гаранта/поручителя или null при отсутствии рейтинга | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

