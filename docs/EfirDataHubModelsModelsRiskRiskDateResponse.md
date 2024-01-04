# EfirDataHubModelsModelsRiskRiskDateResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_date** | **datetime** | Дата для вычисления группы срочности | [optional] 
**rule** | **str** | Идентификатор правила:  - POSITION_MATURITY - срок договора  - ISSUE_MATURITY – погашение  - ISSUE_OFFER - оферта  - ISSUE_RATE – купон  - ISSUE_DIVIDEND – дивиденды  - AMORTISATION - амортизация  - ISSUE_FLOATINGRATE - ставка  - AVERAGE_FLOATINGRATE - средняя RUONIA  - MBD_CBRF - непрерывная КС  - OVERDUE - истечение | [optional] 
**has_amortisations** | **bool** | Наличие амортизации | [optional] 
**error** | **str** | Текст ошибки, если она есть | [optional] 
**timing_group_id** | **int** | Идентификатор группы срочности | [optional] 
**timing_group_name** | **str** | Наименование группы срочности | [optional] 
**rule_name** | **str** | Наименование правила | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

