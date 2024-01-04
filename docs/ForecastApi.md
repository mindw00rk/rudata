# swagger_client.ForecastApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_forecast_analysts_post**](ForecastApi.md#v2_forecast_analysts_post) | **POST** /v2/Forecast/Analysts | Получить список аналитиков.
[**v2_forecast_emitents_post**](ForecastApi.md#v2_forecast_emitents_post) | **POST** /v2/Forecast/Emitents | Получить список анализируемых эмитентов.
[**v2_forecast_market_makers_post**](ForecastApi.md#v2_forecast_market_makers_post) | **POST** /v2/Forecast/MarketMakers | Получить список маркетмейкеров (инвесткомпаний), предоставляющих прогнозы и рекомендации.
[**v2_forecast_price_consensus_post**](ForecastApi.md#v2_forecast_price_consensus_post) | **POST** /v2/Forecast/PriceConsensus | Получить текущий консенсус-прогноз по ценам и консенсус-рекомендации.
[**v2_forecast_securities_post**](ForecastApi.md#v2_forecast_securities_post) | **POST** /v2/Forecast/Securities | Получить список ценных бумаг (акции и депозитарные расписки), по которым предоставляются прогнозы и рекомендации.
[**v2_forecast_target_prices_post**](ForecastApi.md#v2_forecast_target_prices_post) | **POST** /v2/Forecast/TargetPrices | Получить текущие прогнозы по ценам и рекомендации.

# **v2_forecast_analysts_post**
> list[EfirDataHubModelsModelsForecastAnalystsFields] v2_forecast_analysts_post(body=body)

Получить список аналитиков.

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
api_instance = swagger_client.ForecastApi(swagger_client.ApiClient(configuration))
body = swagger_client.ForecastAnalystsBody() # ForecastAnalystsBody |  (optional)

try:
    # Получить список аналитиков.
    api_response = api_instance.v2_forecast_analysts_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForecastApi->v2_forecast_analysts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ForecastAnalystsBody**](ForecastAnalystsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsForecastAnalystsFields]**](EfirDataHubModelsModelsForecastAnalystsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_forecast_emitents_post**
> list[EfirDataHubModelsModelsForecastEmitentsFields] v2_forecast_emitents_post(body=body)

Получить список анализируемых эмитентов.

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
api_instance = swagger_client.ForecastApi(swagger_client.ApiClient(configuration))
body = swagger_client.ForecastEmitentsBody() # ForecastEmitentsBody |  (optional)

try:
    # Получить список анализируемых эмитентов.
    api_response = api_instance.v2_forecast_emitents_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForecastApi->v2_forecast_emitents_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ForecastEmitentsBody**](ForecastEmitentsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsForecastEmitentsFields]**](EfirDataHubModelsModelsForecastEmitentsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_forecast_market_makers_post**
> list[EfirDataHubModelsModelsForecastMarketMakersFields] v2_forecast_market_makers_post(body=body)

Получить список маркетмейкеров (инвесткомпаний), предоставляющих прогнозы и рекомендации.

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
api_instance = swagger_client.ForecastApi(swagger_client.ApiClient(configuration))
body = swagger_client.ForecastMarketMakersBody() # ForecastMarketMakersBody |  (optional)

try:
    # Получить список маркетмейкеров (инвесткомпаний), предоставляющих прогнозы и рекомендации.
    api_response = api_instance.v2_forecast_market_makers_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForecastApi->v2_forecast_market_makers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ForecastMarketMakersBody**](ForecastMarketMakersBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsForecastMarketMakersFields]**](EfirDataHubModelsModelsForecastMarketMakersFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_forecast_price_consensus_post**
> list[EfirDataHubModelsModelsForecastPriceConsensusFields] v2_forecast_price_consensus_post(body=body)

Получить текущий консенсус-прогноз по ценам и консенсус-рекомендации.

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
api_instance = swagger_client.ForecastApi(swagger_client.ApiClient(configuration))
body = swagger_client.ForecastPriceConsensusBody() # ForecastPriceConsensusBody |  (optional)

try:
    # Получить текущий консенсус-прогноз по ценам и консенсус-рекомендации.
    api_response = api_instance.v2_forecast_price_consensus_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForecastApi->v2_forecast_price_consensus_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ForecastPriceConsensusBody**](ForecastPriceConsensusBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsForecastPriceConsensusFields]**](EfirDataHubModelsModelsForecastPriceConsensusFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_forecast_securities_post**
> list[EfirDataHubModelsModelsForecastSecuritiesFields] v2_forecast_securities_post(body=body)

Получить список ценных бумаг (акции и депозитарные расписки), по которым предоставляются прогнозы и рекомендации.

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
api_instance = swagger_client.ForecastApi(swagger_client.ApiClient(configuration))
body = swagger_client.ForecastSecuritiesBody() # ForecastSecuritiesBody |  (optional)

try:
    # Получить список ценных бумаг (акции и депозитарные расписки), по которым предоставляются прогнозы и рекомендации.
    api_response = api_instance.v2_forecast_securities_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForecastApi->v2_forecast_securities_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ForecastSecuritiesBody**](ForecastSecuritiesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsForecastSecuritiesFields]**](EfirDataHubModelsModelsForecastSecuritiesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_forecast_target_prices_post**
> list[EfirDataHubModelsModelsForecastTargetPricesFields] v2_forecast_target_prices_post(body=body)

Получить текущие прогнозы по ценам и рекомендации.

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
api_instance = swagger_client.ForecastApi(swagger_client.ApiClient(configuration))
body = swagger_client.ForecastTargetPricesBody() # ForecastTargetPricesBody |  (optional)

try:
    # Получить текущие прогнозы по ценам и рекомендации.
    api_response = api_instance.v2_forecast_target_prices_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForecastApi->v2_forecast_target_prices_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ForecastTargetPricesBody**](ForecastTargetPricesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsForecastTargetPricesFields]**](EfirDataHubModelsModelsForecastTargetPricesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

