# swagger_client.MifidApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_mifid_trade_filters_post**](MifidApi.md#v2_mifid_trade_filters_post) | **POST** /v2/Mifid/TradeFilters | Возвращает характеристики фильтров
[**v2_mifid_trade_stat_start_dates_post**](MifidApi.md#v2_mifid_trade_stat_start_dates_post) | **POST** /v2/Mifid/TradeStatStartDates | Получить перечень бумаг с указанием самых ранних торговых дней, по которым есть статистика.  Также указаны минимальные даты формирования статистики.
[**v2_mifid_trade_stats_aggregated_post**](MifidApi.md#v2_mifid_trade_stats_aggregated_post) | **POST** /v2/Mifid/TradeStatsAggregated | Статистика по сделкам - агрегированная за период
[**v2_mifid_trade_stats_by_days_post**](MifidApi.md#v2_mifid_trade_stats_by_days_post) | **POST** /v2/Mifid/TradeStatsByDays | Статистика по сделкам - агрегированная по дням за период

# **v2_mifid_trade_filters_post**
> list[EfirDataHubModelsModelsMifidTradeFiltersFields] v2_mifid_trade_filters_post(body=body)

Возвращает характеристики фильтров

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MifidApi(swagger_client.ApiClient(configuration))
body = swagger_client.MifidTradeFiltersBody() # MifidTradeFiltersBody |  (optional)

try:
    # Возвращает характеристики фильтров
    api_response = api_instance.v2_mifid_trade_filters_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MifidApi->v2_mifid_trade_filters_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MifidTradeFiltersBody**](MifidTradeFiltersBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsMifidTradeFiltersFields]**](EfirDataHubModelsModelsMifidTradeFiltersFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_mifid_trade_stat_start_dates_post**
> list[EfirDataHubModelsModelsMifidTradeStatStartDatesFields] v2_mifid_trade_stat_start_dates_post(body=body)

Получить перечень бумаг с указанием самых ранних торговых дней, по которым есть статистика.  Также указаны минимальные даты формирования статистики.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MifidApi(swagger_client.ApiClient(configuration))
body = swagger_client.MifidTradeStatStartDatesBody() # MifidTradeStatStartDatesBody |  (optional)

try:
    # Получить перечень бумаг с указанием самых ранних торговых дней, по которым есть статистика.  Также указаны минимальные даты формирования статистики.
    api_response = api_instance.v2_mifid_trade_stat_start_dates_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MifidApi->v2_mifid_trade_stat_start_dates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MifidTradeStatStartDatesBody**](MifidTradeStatStartDatesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsMifidTradeStatStartDatesFields]**](EfirDataHubModelsModelsMifidTradeStatStartDatesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_mifid_trade_stats_aggregated_post**
> list[EfirDataHubModelsModelsMifidTradeStatsAggregatedFields] v2_mifid_trade_stats_aggregated_post(body=body)

Статистика по сделкам - агрегированная за период

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MifidApi(swagger_client.ApiClient(configuration))
body = swagger_client.MifidTradeStatsAggregatedBody() # MifidTradeStatsAggregatedBody |  (optional)

try:
    # Статистика по сделкам - агрегированная за период
    api_response = api_instance.v2_mifid_trade_stats_aggregated_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MifidApi->v2_mifid_trade_stats_aggregated_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MifidTradeStatsAggregatedBody**](MifidTradeStatsAggregatedBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsMifidTradeStatsAggregatedFields]**](EfirDataHubModelsModelsMifidTradeStatsAggregatedFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_mifid_trade_stats_by_days_post**
> list[EfirDataHubModelsModelsMifidTradeStatsByDaysFields] v2_mifid_trade_stats_by_days_post(body=body)

Статистика по сделкам - агрегированная по дням за период

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MifidApi(swagger_client.ApiClient(configuration))
body = swagger_client.MifidTradeStatsByDaysBody() # MifidTradeStatsByDaysBody |  (optional)

try:
    # Статистика по сделкам - агрегированная по дням за период
    api_response = api_instance.v2_mifid_trade_stats_by_days_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MifidApi->v2_mifid_trade_stats_by_days_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MifidTradeStatsByDaysBody**](MifidTradeStatsByDaysBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsMifidTradeStatsByDaysFields]**](EfirDataHubModelsModelsMifidTradeStatsByDaysFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

