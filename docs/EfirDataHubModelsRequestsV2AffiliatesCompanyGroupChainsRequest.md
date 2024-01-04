# EfirDataHubModelsRequestsV2AffiliatesCompanyGroupChainsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_inns** | **list[str]** | Массив ИНН компаний, обязательный, не более 100 шт | [optional] 
**actual_date** | **datetime** | Дата актуальности. Необязательный, по умолчанию текущая дата | [optional] 
**stop_when** | **AllOfEfirDataHubModelsRequestsV2AffiliatesCompanyGroupChainsRequestStopWhen** | Условие окончания построения цепочки связей:  1 - до головной компании группы,  2 - до ближайшего эмитента.  Необязательный, по умолчанию 1.  1 &#x3D; GroupRoot  2 &#x3D; NearestIssuer | [optional] 
**min_share_part** | **int** | Минимальное значение доли владения. Необязательный, по умолчанию 20. | [optional] 
**use_management_relations** | **bool** | Использовать связи управления. Необязательный, по умолчанию true. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

