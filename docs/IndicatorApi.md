# swagger_client.IndicatorApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_indicator_constituents_post**](IndicatorApi.md#v2_indicator_constituents_post) | **POST** /v2/Indicator/Constituents | Выборка состава индексов
[**v2_indicator_list_post**](IndicatorApi.md#v2_indicator_list_post) | **POST** /v2/Indicator/List | Выборка справочника индикаторов
[**v2_indicator_mfb_indicative_risk_fond_post**](IndicatorApi.md#v2_indicator_mfb_indicative_risk_fond_post) | **POST** /v2/Indicator/MfbIndicativeRiskFond | Индикативные ставки риска, МФБ
[**v2_indicator_risk_free_post**](IndicatorApi.md#v2_indicator_risk_free_post) | **POST** /v2/Indicator/RiskFree | Значения безрисковых кривых на дату

# **v2_indicator_constituents_post**
> list[EfirDataHubModelsModelsIndicatorConstituentFields] v2_indicator_constituents_post(body=body)

Выборка состава индексов

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
api_instance = swagger_client.IndicatorApi(swagger_client.ApiClient(configuration))
body = swagger_client.IndicatorConstituentsBody() # IndicatorConstituentsBody |  (optional)

try:
    # Выборка состава индексов
    api_response = api_instance.v2_indicator_constituents_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorApi->v2_indicator_constituents_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IndicatorConstituentsBody**](IndicatorConstituentsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsIndicatorConstituentFields]**](EfirDataHubModelsModelsIndicatorConstituentFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_indicator_list_post**
> list[EfirDataHubModelsModelsIndicatorListFields] v2_indicator_list_post(body=body)

Выборка справочника индикаторов

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
api_instance = swagger_client.IndicatorApi(swagger_client.ApiClient(configuration))
body = swagger_client.IndicatorListBody() # IndicatorListBody |  (optional)

try:
    # Выборка справочника индикаторов
    api_response = api_instance.v2_indicator_list_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorApi->v2_indicator_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IndicatorListBody**](IndicatorListBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsIndicatorListFields]**](EfirDataHubModelsModelsIndicatorListFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_indicator_mfb_indicative_risk_fond_post**
> list[EfirDataHubModelsModelsIndicatorMfbIndicativeRiskFondFields] v2_indicator_mfb_indicative_risk_fond_post(body=body)

Индикативные ставки риска, МФБ

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
api_instance = swagger_client.IndicatorApi(swagger_client.ApiClient(configuration))
body = swagger_client.IndicatorMfbIndicativeRiskFondBody() # IndicatorMfbIndicativeRiskFondBody |  (optional)

try:
    # Индикативные ставки риска, МФБ
    api_response = api_instance.v2_indicator_mfb_indicative_risk_fond_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorApi->v2_indicator_mfb_indicative_risk_fond_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IndicatorMfbIndicativeRiskFondBody**](IndicatorMfbIndicativeRiskFondBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsIndicatorMfbIndicativeRiskFondFields]**](EfirDataHubModelsModelsIndicatorMfbIndicativeRiskFondFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_indicator_risk_free_post**
> list[EfirDataHubModelsModelsIndicatorRiskFreeFields] v2_indicator_risk_free_post(body=body)

Значения безрисковых кривых на дату

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
api_instance = swagger_client.IndicatorApi(swagger_client.ApiClient(configuration))
body = swagger_client.IndicatorRiskFreeBody() # IndicatorRiskFreeBody |  (optional)

try:
    # Значения безрисковых кривых на дату
    api_response = api_instance.v2_indicator_risk_free_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorApi->v2_indicator_risk_free_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IndicatorRiskFreeBody**](IndicatorRiskFreeBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsIndicatorRiskFreeFields]**](EfirDataHubModelsModelsIndicatorRiskFreeFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

