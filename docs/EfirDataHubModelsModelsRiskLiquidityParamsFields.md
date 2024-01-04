# EfirDataHubModelsModelsRiskLiquidityParamsFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Идентификатор торгового инструмента. См. метод /Info/Securities. | [optional] 
**operation** | **float** | Направление операции. Равно входному параметру operation. | [optional] 
**omega** | **float** | Экспоненциальное среднее логарифма объема, который надо купить/продать для сдвига цены на минимальный шаг | [optional] 
**ro** | **float** | Экспоненциальное среднее разности между оценкой лучшей цены покупки/продажи, рассчитанной по модели, и фактическим значением лучшей цены | [optional] 
**gamma** | **float** | Экспоненциальное среднее стандартной ошибки модели | [optional] 
**volmax** | **float** | Максимальный объем покупки/продажи, для которого применима модель оценки сдвига цены | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

