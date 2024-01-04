# swagger_client.RuPriceApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_ru_price_history_column_groups_post**](RuPriceApi.md#v2_ru_price_history_column_groups_post) | **POST** /v2/RUPrice/HistoryColumnGroups | Метод возвращает справочник групп полей для метода HistoryColumns.
[**v2_ru_price_history_columns_post**](RuPriceApi.md#v2_ru_price_history_columns_post) | **POST** /v2/RUPrice/HistoryColumns | Метод возвращает список полей в терминологии, принятой в системе ЭФИР.
[**v2_ru_price_history_post**](RuPriceApi.md#v2_ru_price_history_post) | **POST** /v2/RUPrice/History | Позволяет получить таблицу с историческими данными по одному или нескольким инструментам за заданный период времени.
[**v2_ru_price_securities_post**](RuPriceApi.md#v2_ru_price_securities_post) | **POST** /v2/RUPrice/Securities | Справочник бумаг Ценового центра.

# **v2_ru_price_history_column_groups_post**
> list[EfirDataHubModelsModelsRUPriceHistoryColumnGroupsFields] v2_ru_price_history_column_groups_post()

Метод возвращает справочник групп полей для метода HistoryColumns.

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
api_instance = swagger_client.RuPriceApi(swagger_client.ApiClient(configuration))

try:
    # Метод возвращает справочник групп полей для метода HistoryColumns.
    api_response = api_instance.v2_ru_price_history_column_groups_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuPriceApi->v2_ru_price_history_column_groups_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EfirDataHubModelsModelsRUPriceHistoryColumnGroupsFields]**](EfirDataHubModelsModelsRUPriceHistoryColumnGroupsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_ru_price_history_columns_post**
> list[EfirDataHubModelsModelsRUPriceHistoryColumnsFields] v2_ru_price_history_columns_post(body=body)

Метод возвращает список полей в терминологии, принятой в системе ЭФИР.

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
api_instance = swagger_client.RuPriceApi(swagger_client.ApiClient(configuration))
body = swagger_client.RUPriceHistoryColumnsBody() # RUPriceHistoryColumnsBody |  (optional)

try:
    # Метод возвращает список полей в терминологии, принятой в системе ЭФИР.
    api_response = api_instance.v2_ru_price_history_columns_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuPriceApi->v2_ru_price_history_columns_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RUPriceHistoryColumnsBody**](RUPriceHistoryColumnsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRUPriceHistoryColumnsFields]**](EfirDataHubModelsModelsRUPriceHistoryColumnsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_ru_price_history_post**
> list[EfirDataHubModelsModelsRUPriceHistoryFields] v2_ru_price_history_post(body=body)

Позволяет получить таблицу с историческими данными по одному или нескольким инструментам за заданный период времени.

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
api_instance = swagger_client.RuPriceApi(swagger_client.ApiClient(configuration))
body = swagger_client.RUPriceHistoryBody() # RUPriceHistoryBody |  (optional)

try:
    # Позволяет получить таблицу с историческими данными по одному или нескольким инструментам за заданный период времени.
    api_response = api_instance.v2_ru_price_history_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuPriceApi->v2_ru_price_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RUPriceHistoryBody**](RUPriceHistoryBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRUPriceHistoryFields]**](EfirDataHubModelsModelsRUPriceHistoryFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_ru_price_securities_post**
> list[EfirDataHubModelsModelsRUPriceSecuritiesFields] v2_ru_price_securities_post(body=body)

Справочник бумаг Ценового центра.

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
api_instance = swagger_client.RuPriceApi(swagger_client.ApiClient(configuration))
body = swagger_client.RUPriceSecuritiesBody() # RUPriceSecuritiesBody |  (optional)

try:
    # Справочник бумаг Ценового центра.
    api_response = api_instance.v2_ru_price_securities_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuPriceApi->v2_ru_price_securities_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RUPriceSecuritiesBody**](RUPriceSecuritiesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRUPriceSecuritiesFields]**](EfirDataHubModelsModelsRUPriceSecuritiesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

