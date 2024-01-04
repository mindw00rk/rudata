# EfirDataHubModelsRequestsV2BondDateOptionsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | ISIN, либо регистрационный номер, либо торговый код ID_ISS | 
**_date** | **datetime** | Дата определения параметров; если не указана, возвращаются параметры на текущую дату. | [optional] 
**is_close_register** | **bool** | True указывает на то, что при расчете НКД по амортизируемым бумагам, текущий номинал бумаги будет определяться по датам закрытия реестра, а не по датам непосредственно амортизационных выплат. | [optional] 
**coupon_forecast** | **str** | Пользовательские значения доходности для неизвестных купонов. Разделитель «;». | [optional] 
**coupon_binding** | **str** | Даты пользовательских купонов, заданных в параметре couponForecast. Разделитель «;». | [optional] 
**use_fix_date** | **bool** | True - использовать дату фиксации для определения купонного периода, актуального на дату расчета  Если не указано - false | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

