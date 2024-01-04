# swagger_client.ArchiveApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_archive_bond_yields_post**](ArchiveApi.md#v2_archive_bond_yields_post) | **POST** /v2/Archive/BondYields | Получить доходности и другие рыночные показатели облигации на заданную дату.
[**v2_archive_cash_currency_rate_post**](ArchiveApi.md#v2_archive_cash_currency_rate_post) | **POST** /v2/Archive/CashCurrencyRate | Получить данные о курсах наличной валюты за указанную дату.
[**v2_archive_currency_rate_history_post**](ArchiveApi.md#v2_archive_currency_rate_history_post) | **POST** /v2/Archive/CurrencyRateHistory | История курсов валют за период
[**v2_archive_currency_rate_post**](ArchiveApi.md#v2_archive_currency_rate_post) | **POST** /v2/Archive/CurrencyRate | Получить кросс-курс двух валют.
[**v2_archive_end_of_day_on_exchanges_post**](ArchiveApi.md#v2_archive_end_of_day_on_exchanges_post) | **POST** /v2/Archive/EndOfDayOnExchanges | Итоги торгов по инструментам за период на различных площадках.
[**v2_archive_end_of_day_post**](ArchiveApi.md#v2_archive_end_of_day_post) | **POST** /v2/Archive/EndOfDay | Получить данные по результатам торгов на заданную дату.
[**v2_archive_history_official_post**](ArchiveApi.md#v2_archive_history_official_post) | **POST** /v2/Archive/HistoryOfficial | Официальные итоги торгов по инструменту
[**v2_archive_history_post**](ArchiveApi.md#v2_archive_history_post) | **POST** /v2/Archive/History | Получить данные о торгах за указанный период.
[**v2_archive_moex_current_snapshot_post**](ArchiveApi.md#v2_archive_moex_current_snapshot_post) | **POST** /v2/Archive/MoexCurrentSnapshot | Метод возвращает срез текущего состояния торгов из основных режимов торгов по акциям, облигациям, фьючерсам, валюте и индексам
[**v2_archive_moex_trade_history_post**](ArchiveApi.md#v2_archive_moex_trade_history_post) | **POST** /v2/Archive/MoexTradeHistory | Реестр сделок на Московской бирже (облигации).
[**v2_archive_multi_history_post**](ArchiveApi.md#v2_archive_multi_history_post) | **POST** /v2/Archive/MultiHistory | Получить данные о торгах за указанный период.
[**v2_archive_snapshot_on_exchanges_post**](ArchiveApi.md#v2_archive_snapshot_on_exchanges_post) | **POST** /v2/Archive/SnapshotOnExchanges | Итоги торгов по инструментам за период с почасовыми срезами. Данные Московской биржи не поддерживаются
[**v2_archive_spbex_index_history_post**](ArchiveApi.md#v2_archive_spbex_index_history_post) | **POST** /v2/Archive/SPBEXIndexHistory | Возвращает расширенные данные по индексам СПБ

# **v2_archive_bond_yields_post**
> list[EfirDataHubModelsModelsArchiveBondYieldsFields] v2_archive_bond_yields_post(body=body)

Получить доходности и другие рыночные показатели облигации на заданную дату.

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
api_instance = swagger_client.ArchiveApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArchiveBondYieldsBody() # ArchiveBondYieldsBody |  (optional)

try:
    # Получить доходности и другие рыночные показатели облигации на заданную дату.
    api_response = api_instance.v2_archive_bond_yields_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->v2_archive_bond_yields_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArchiveBondYieldsBody**](ArchiveBondYieldsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsArchiveBondYieldsFields]**](EfirDataHubModelsModelsArchiveBondYieldsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_archive_cash_currency_rate_post**
> list[EfirDataHubModelsModelsArchiveCashCurrencyRateFields] v2_archive_cash_currency_rate_post(body=body)

Получить данные о курсах наличной валюты за указанную дату.

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
api_instance = swagger_client.ArchiveApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArchiveCashCurrencyRateBody() # ArchiveCashCurrencyRateBody |  (optional)

try:
    # Получить данные о курсах наличной валюты за указанную дату.
    api_response = api_instance.v2_archive_cash_currency_rate_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->v2_archive_cash_currency_rate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArchiveCashCurrencyRateBody**](ArchiveCashCurrencyRateBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsArchiveCashCurrencyRateFields]**](EfirDataHubModelsModelsArchiveCashCurrencyRateFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_archive_currency_rate_history_post**
> list[EfirDataHubModelsModelsArchiveCurrencyRateHistoryFields] v2_archive_currency_rate_history_post(body=body)

История курсов валют за период

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
api_instance = swagger_client.ArchiveApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArchiveCurrencyRateHistoryBody() # ArchiveCurrencyRateHistoryBody |  (optional)

try:
    # История курсов валют за период
    api_response = api_instance.v2_archive_currency_rate_history_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->v2_archive_currency_rate_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArchiveCurrencyRateHistoryBody**](ArchiveCurrencyRateHistoryBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsArchiveCurrencyRateHistoryFields]**](EfirDataHubModelsModelsArchiveCurrencyRateHistoryFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_archive_currency_rate_post**
> EfirDataHubModelsModelsArchiveCurrencyRateResponse v2_archive_currency_rate_post(body=body)

Получить кросс-курс двух валют.

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
api_instance = swagger_client.ArchiveApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArchiveCurrencyRateBody() # ArchiveCurrencyRateBody |  (optional)

try:
    # Получить кросс-курс двух валют.
    api_response = api_instance.v2_archive_currency_rate_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->v2_archive_currency_rate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArchiveCurrencyRateBody**](ArchiveCurrencyRateBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsArchiveCurrencyRateResponse**](EfirDataHubModelsModelsArchiveCurrencyRateResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_archive_end_of_day_on_exchanges_post**
> list[EfirDataHubModelsModelsArchiveEndOfDayOnExchangeFields] v2_archive_end_of_day_on_exchanges_post(body=body)

Итоги торгов по инструментам за период на различных площадках.

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
api_instance = swagger_client.ArchiveApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArchiveEndOfDayOnExchangesBody() # ArchiveEndOfDayOnExchangesBody |  (optional)

try:
    # Итоги торгов по инструментам за период на различных площадках.
    api_response = api_instance.v2_archive_end_of_day_on_exchanges_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->v2_archive_end_of_day_on_exchanges_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArchiveEndOfDayOnExchangesBody**](ArchiveEndOfDayOnExchangesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsArchiveEndOfDayOnExchangeFields]**](EfirDataHubModelsModelsArchiveEndOfDayOnExchangeFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_archive_end_of_day_post**
> list[EfirDataHubModelsModelsArchiveHistoryFullFields] v2_archive_end_of_day_post(body=body)

Получить данные по результатам торгов на заданную дату.

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
api_instance = swagger_client.ArchiveApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArchiveEndOfDayBody() # ArchiveEndOfDayBody |  (optional)

try:
    # Получить данные по результатам торгов на заданную дату.
    api_response = api_instance.v2_archive_end_of_day_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->v2_archive_end_of_day_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArchiveEndOfDayBody**](ArchiveEndOfDayBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsArchiveHistoryFullFields]**](EfirDataHubModelsModelsArchiveHistoryFullFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_archive_history_official_post**
> list[EfirDataHubModelsModelsArchiveHistoryOfficialFullFieldsV2] v2_archive_history_official_post(body=body)

Официальные итоги торгов по инструменту

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
api_instance = swagger_client.ArchiveApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArchiveHistoryOfficialBody() # ArchiveHistoryOfficialBody |  (optional)

try:
    # Официальные итоги торгов по инструменту
    api_response = api_instance.v2_archive_history_official_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->v2_archive_history_official_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArchiveHistoryOfficialBody**](ArchiveHistoryOfficialBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsArchiveHistoryOfficialFullFieldsV2]**](EfirDataHubModelsModelsArchiveHistoryOfficialFullFieldsV2.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_archive_history_post**
> EfirDataHubModelsModelsArchiveHistoryFullFields v2_archive_history_post(body=body)

Получить данные о торгах за указанный период.

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
api_instance = swagger_client.ArchiveApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArchiveHistoryBody() # ArchiveHistoryBody |  (optional)

try:
    # Получить данные о торгах за указанный период.
    api_response = api_instance.v2_archive_history_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->v2_archive_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArchiveHistoryBody**](ArchiveHistoryBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsArchiveHistoryFullFields**](EfirDataHubModelsModelsArchiveHistoryFullFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_archive_moex_current_snapshot_post**
> list[EfirDataHubModelsModelsArchiveHistoryOfficialFullFields] v2_archive_moex_current_snapshot_post(body=body)

Метод возвращает срез текущего состояния торгов из основных режимов торгов по акциям, облигациям, фьючерсам, валюте и индексам

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
api_instance = swagger_client.ArchiveApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArchiveMoexCurrentSnapshotBody() # ArchiveMoexCurrentSnapshotBody |  (optional)

try:
    # Метод возвращает срез текущего состояния торгов из основных режимов торгов по акциям, облигациям, фьючерсам, валюте и индексам
    api_response = api_instance.v2_archive_moex_current_snapshot_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->v2_archive_moex_current_snapshot_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArchiveMoexCurrentSnapshotBody**](ArchiveMoexCurrentSnapshotBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsArchiveHistoryOfficialFullFields]**](EfirDataHubModelsModelsArchiveHistoryOfficialFullFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_archive_moex_trade_history_post**
> list[EfirDataHubModelsModelsArchiveMoexTradeHistoryFields] v2_archive_moex_trade_history_post(body=body)

Реестр сделок на Московской бирже (облигации).

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
api_instance = swagger_client.ArchiveApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArchiveMoexTradeHistoryBody() # ArchiveMoexTradeHistoryBody |  (optional)

try:
    # Реестр сделок на Московской бирже (облигации).
    api_response = api_instance.v2_archive_moex_trade_history_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->v2_archive_moex_trade_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArchiveMoexTradeHistoryBody**](ArchiveMoexTradeHistoryBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsArchiveMoexTradeHistoryFields]**](EfirDataHubModelsModelsArchiveMoexTradeHistoryFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_archive_multi_history_post**
> list[EfirDataHubModelsModelsArchiveMultiHistoryGroup] v2_archive_multi_history_post(body=body)

Получить данные о торгах за указанный период.

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
api_instance = swagger_client.ArchiveApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArchiveMultiHistoryBody() # ArchiveMultiHistoryBody |  (optional)

try:
    # Получить данные о торгах за указанный период.
    api_response = api_instance.v2_archive_multi_history_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->v2_archive_multi_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArchiveMultiHistoryBody**](ArchiveMultiHistoryBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsArchiveMultiHistoryGroup]**](EfirDataHubModelsModelsArchiveMultiHistoryGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_archive_snapshot_on_exchanges_post**
> list[EfirDataHubModelsModelsArchiveEndOfDayOnExchangeFields] v2_archive_snapshot_on_exchanges_post(body=body)

Итоги торгов по инструментам за период с почасовыми срезами. Данные Московской биржи не поддерживаются

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
api_instance = swagger_client.ArchiveApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArchiveSnapshotOnExchangesBody() # ArchiveSnapshotOnExchangesBody |  (optional)

try:
    # Итоги торгов по инструментам за период с почасовыми срезами. Данные Московской биржи не поддерживаются
    api_response = api_instance.v2_archive_snapshot_on_exchanges_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->v2_archive_snapshot_on_exchanges_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArchiveSnapshotOnExchangesBody**](ArchiveSnapshotOnExchangesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsArchiveEndOfDayOnExchangeFields]**](EfirDataHubModelsModelsArchiveEndOfDayOnExchangeFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_archive_spbex_index_history_post**
> list[EfirDataHubModelsModelsArchiveSpbexIndexHistoryFields] v2_archive_spbex_index_history_post(body=body)

Возвращает расширенные данные по индексам СПБ

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
api_instance = swagger_client.ArchiveApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArchiveSPBEXIndexHistoryBody() # ArchiveSPBEXIndexHistoryBody |  (optional)

try:
    # Возвращает расширенные данные по индексам СПБ
    api_response = api_instance.v2_archive_spbex_index_history_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->v2_archive_spbex_index_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArchiveSPBEXIndexHistoryBody**](ArchiveSPBEXIndexHistoryBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsArchiveSpbexIndexHistoryFields]**](EfirDataHubModelsModelsArchiveSpbexIndexHistoryFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

