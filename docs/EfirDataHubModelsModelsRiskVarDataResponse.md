# EfirDataHubModelsModelsRiskVarDataResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_rf** | **int** | Тип фактора риска инструмента (0 – облигации, 1 – валюты, 2 - акции) | [optional] 
**rf** | **int** | Фактор риска инструмента | [optional] 
**cur** | **str** | Код валюты. Если входной инструмент – валюта, то CUR &#x3D; ID. | [optional] 
**type_rfc** | **int** | Тип фактора риска валюты (0-2) | [optional] 
**rfc** | **int** | Фактор риска валюты (1-29) | [optional] 
**r_o_isin** | **float** | Множитель риска по инструменту | [optional] 
**r_o_cur** | **float** | Множитель риска по валюте | [optional] 
**sigma_rf** | **float** | Волатильность фактора риска инструмента | [optional] 
**sigma_rfc** | **float** | Волатильность фактора риска валюты | [optional] 
**cor_rf_rfc** | **float** | Коэффициент корреляции между факторами риска инструмента и валюты(из корреляционной матрицы) | [optional] 
**va_r_mult** | **float** | Множитель VaR с учетом временного горизонта прогноза | [optional] 
**e_s_mult** | **float** | Множитель ES с учетом временного горизонта прогноза | [optional] 
**unit_isin** | **float** | Множитель риска на единицу позиции (составляющая по инструменту) | [optional] 
**unit_cur** | **float** | Множитель риска на единицу позиции (составляющая по валюте) | [optional] 
**error** | **str** | Текст ошибки, если она произошла | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

