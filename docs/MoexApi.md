# swagger_client.MoexApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_moex_boards_post**](MoexApi.md#v2_moex_boards_post) | **POST** /v2/Moex/Boards | Получить справочник подсистем (engines), рынков (markets), групп режимов (board groups) и режимов торгов (boards) со всеми взаимосвязями между собой – всё дерево за один вызов. Входных параметров нет.
[**v2_moex_derivatives_uderlying_assets_post**](MoexApi.md#v2_moex_derivatives_uderlying_assets_post) | **POST** /v2/Moex/derivatives-uderlying-assets | Возвращает описание базовых активов производных финансовых инструментов
[**v2_moex_dividend_yield_post**](MoexApi.md#v2_moex_dividend_yield_post) | **POST** /v2/Moex/DividendYield | Возвращает сведения о дивидендной доходности, получаемые с Московской Биржи
[**v2_moex_futures_columns_post**](MoexApi.md#v2_moex_futures_columns_post) | **POST** /v2/Moex/FuturesColumns | Получить описание полей в справочнике фьючерсов, см. метод Futures. Входных параметров нет.
[**v2_moex_futures_post**](MoexApi.md#v2_moex_futures_post) | **POST** /v2/Moex/Futures | Получить описания фьючерсов.
[**v2_moex_history_columns_post**](MoexApi.md#v2_moex_history_columns_post) | **POST** /v2/Moex/HistoryColumns | Получить описания колонок в исторических данных по инструментам, см. метод History.
[**v2_moex_history_post**](MoexApi.md#v2_moex_history_post) | **POST** /v2/Moex/History | Получить официальные итоги по набору конкретных инструментов или по всем инструментам заданного рынка, группы режимов или одного режима торгов.  В зависимости от комбинации входных параметров engine и market возвращаются следующие типы ответов:  \&quot;stock\&quot;, \&quot;bonds\&quot; HistoryStockBondsFields  \&quot;stock\&quot;, \&quot;ccp\&quot; HistoryStockCcpFields  \&quot;stock\&quot;, \&quot;index\&quot; HistoryStockIndexFields  \&quot;stock\&quot;, \&quot;ndm\&quot; HistoryStockNdmFields  \&quot;stock\&quot;, \&quot;foreignndm\&quot; HistoryStockNdmFields  \&quot;stock\&quot;, \&quot;otc\&quot; HistoryStockSharesFields  \&quot;stock\&quot;, \&quot;qnv\&quot; HistoryStockQnvFields  \&quot;stock\&quot;, \&quot;repo\&quot; HistoryStockRepoFields  \&quot;stock\&quot;, \&quot;gcc\&quot; HistoryStockRepoFields  \&quot;stock\&quot;, \&quot;shares\&quot; HistoryStockSharesFields  \&quot;stock\&quot;, \&quot;foreignshares\&quot; HistoryStockSharesFields  \&quot;futures\&quot;, \&quot;options\&quot; HistoryFuturesOptionsFields  \&quot;futures\&quot;, \&quot;forts\&quot; HistoryFuturesFortsFields  \&quot;currency\&quot;, \&quot;futures\&quot; HistoryCurrencyFuturesFields  \&quot;currency\&quot;, \&quot;selt\&quot; HistoryCurrencySeltFields
[**v2_moex_limitval_currency_post**](MoexApi.md#v2_moex_limitval_currency_post) | **POST** /v2/Moex/Limitval-Currency | Возвращает лимиты концентрации Валютного рынка
[**v2_moex_limitval_stock_post**](MoexApi.md#v2_moex_limitval_stock_post) | **POST** /v2/Moex/Limitval-Stock | Возвращает лимиты концентрации Фондового рынка
[**v2_moex_ncc_indicative_risk_currency_post**](MoexApi.md#v2_moex_ncc_indicative_risk_currency_post) | **POST** /v2/Moex/NccIndicativeRiskCurrency | Индикативные ставки риска валютного рынка, НКЦ
[**v2_moex_ncc_indicative_risk_fond_post**](MoexApi.md#v2_moex_ncc_indicative_risk_fond_post) | **POST** /v2/Moex/NccIndicativeRiskFond | Индикативные ставки риска фондового рынка, НКЦ
[**v2_moex_ncc_indicative_risk_futures_post**](MoexApi.md#v2_moex_ncc_indicative_risk_futures_post) | **POST** /v2/Moex/NccIndicativeRiskFutures | Индикативные ставки риска срочного рынка, НКЦ
[**v2_moex_ncc_market_risk_currency_post**](MoexApi.md#v2_moex_ncc_market_risk_currency_post) | **POST** /v2/Moex/NccMarketRiskCurrency | Динамические риск-параметры рыночных рисков на валютном рынке, НКЦ
[**v2_moex_ncc_market_risk_fond_post**](MoexApi.md#v2_moex_ncc_market_risk_fond_post) | **POST** /v2/Moex/NccMarketRiskFond | Динамические риск-параметры рыночных рисков на фондовом рынке, НКЦ
[**v2_moex_ncc_percent_risk_currency_post**](MoexApi.md#v2_moex_ncc_percent_risk_currency_post) | **POST** /v2/Moex/NccPercentRiskCurrency | Возвращает динамические риск-параметры процентных рисков на валютном рынке
[**v2_moex_ncc_percent_risk_fond_post**](MoexApi.md#v2_moex_ncc_percent_risk_fond_post) | **POST** /v2/Moex/NccPercentRiskFond | Возвращает динамические риск-параметры процентных рисков на рынке акций и облигаций
[**v2_moex_option_columns_post**](MoexApi.md#v2_moex_option_columns_post) | **POST** /v2/Moex/OptionColumns | Получить описание полей в справочнике опционов, см. метод Options. Входных параметров нет.
[**v2_moex_options_post**](MoexApi.md#v2_moex_options_post) | **POST** /v2/Moex/Options | Получить описания опционов.
[**v2_moex_sec_columns_post**](MoexApi.md#v2_moex_sec_columns_post) | **POST** /v2/Moex/SecColumns | Получить описание полей в справочнике торговых инструментов, см. метод Securities. Входных параметров нет.
[**v2_moex_securities_post**](MoexApi.md#v2_moex_securities_post) | **POST** /v2/Moex/Securities | Получить список торгуемых инструментов.
[**v2_moex_stock_boards_post**](MoexApi.md#v2_moex_stock_boards_post) | **POST** /v2/Moex/StockBoards | Возвращает описание режимов торгов (boards) ценных бумаг фондового рынка
[**v2_moex_stocks_post**](MoexApi.md#v2_moex_stocks_post) | **POST** /v2/Moex/Stocks | Возвращает краткое описание ценных бумаг фондового рынка

# **v2_moex_boards_post**
> EfirDataHubModelsModelsMoexBoardsResponse v2_moex_boards_post()

Получить справочник подсистем (engines), рынков (markets), групп режимов (board groups) и режимов торгов (boards) со всеми взаимосвязями между собой – всё дерево за один вызов. Входных параметров нет.

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
api_instance = swagger_client.MoexApi(swagger_client.ApiClient(configuration))

try:
    # Получить справочник подсистем (engines), рынков (markets), групп режимов (board groups) и режимов торгов (boards) со всеми взаимосвязями между собой – всё дерево за один вызов. Входных параметров нет.
    api_response = api_instance.v2_moex_boards_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoexApi->v2_moex_boards_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EfirDataHubModelsModelsMoexBoardsResponse**](EfirDataHubModelsModelsMoexBoardsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_moex_derivatives_uderlying_assets_post**
> list[EfirDataHubModelsModelsMoexDerivativesUderlyingAssetFields] v2_moex_derivatives_uderlying_assets_post(body=body)

Возвращает описание базовых активов производных финансовых инструментов

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
api_instance = swagger_client.MoexApi(swagger_client.ApiClient(configuration))
body = swagger_client.MoexDerivativesuderlyingassetsBody() # MoexDerivativesuderlyingassetsBody |  (optional)

try:
    # Возвращает описание базовых активов производных финансовых инструментов
    api_response = api_instance.v2_moex_derivatives_uderlying_assets_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoexApi->v2_moex_derivatives_uderlying_assets_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoexDerivativesuderlyingassetsBody**](MoexDerivativesuderlyingassetsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsMoexDerivativesUderlyingAssetFields]**](EfirDataHubModelsModelsMoexDerivativesUderlyingAssetFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_moex_dividend_yield_post**
> list[EfirDataHubModelsModelsMoexDividendYieldFields] v2_moex_dividend_yield_post(body=body)

Возвращает сведения о дивидендной доходности, получаемые с Московской Биржи

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
api_instance = swagger_client.MoexApi(swagger_client.ApiClient(configuration))
body = swagger_client.MoexDividendYieldBody() # MoexDividendYieldBody |  (optional)

try:
    # Возвращает сведения о дивидендной доходности, получаемые с Московской Биржи
    api_response = api_instance.v2_moex_dividend_yield_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoexApi->v2_moex_dividend_yield_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoexDividendYieldBody**](MoexDividendYieldBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsMoexDividendYieldFields]**](EfirDataHubModelsModelsMoexDividendYieldFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_moex_futures_columns_post**
> list[EfirDataHubModelsModelsMoexFuturesColumnsFields] v2_moex_futures_columns_post()

Получить описание полей в справочнике фьючерсов, см. метод Futures. Входных параметров нет.

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
api_instance = swagger_client.MoexApi(swagger_client.ApiClient(configuration))

try:
    # Получить описание полей в справочнике фьючерсов, см. метод Futures. Входных параметров нет.
    api_response = api_instance.v2_moex_futures_columns_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoexApi->v2_moex_futures_columns_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EfirDataHubModelsModelsMoexFuturesColumnsFields]**](EfirDataHubModelsModelsMoexFuturesColumnsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_moex_futures_post**
> list[EfirDataHubModelsModelsMoexFuturesFields] v2_moex_futures_post(body=body)

Получить описания фьючерсов.

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
api_instance = swagger_client.MoexApi(swagger_client.ApiClient(configuration))
body = swagger_client.MoexFuturesBody() # MoexFuturesBody |  (optional)

try:
    # Получить описания фьючерсов.
    api_response = api_instance.v2_moex_futures_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoexApi->v2_moex_futures_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoexFuturesBody**](MoexFuturesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsMoexFuturesFields]**](EfirDataHubModelsModelsMoexFuturesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_moex_history_columns_post**
> list[EfirDataHubModelsModelsMoexHistoryColumnsFields] v2_moex_history_columns_post(body=body)

Получить описания колонок в исторических данных по инструментам, см. метод History.

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
api_instance = swagger_client.MoexApi(swagger_client.ApiClient(configuration))
body = swagger_client.MoexHistoryColumnsBody() # MoexHistoryColumnsBody |  (optional)

try:
    # Получить описания колонок в исторических данных по инструментам, см. метод History.
    api_response = api_instance.v2_moex_history_columns_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoexApi->v2_moex_history_columns_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoexHistoryColumnsBody**](MoexHistoryColumnsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsMoexHistoryColumnsFields]**](EfirDataHubModelsModelsMoexHistoryColumnsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_moex_history_post**
> EfirDataHubModelsModelsMoexHistoryStockIndexFields v2_moex_history_post(body=body)

Получить официальные итоги по набору конкретных инструментов или по всем инструментам заданного рынка, группы режимов или одного режима торгов.  В зависимости от комбинации входных параметров engine и market возвращаются следующие типы ответов:  \"stock\", \"bonds\" HistoryStockBondsFields  \"stock\", \"ccp\" HistoryStockCcpFields  \"stock\", \"index\" HistoryStockIndexFields  \"stock\", \"ndm\" HistoryStockNdmFields  \"stock\", \"foreignndm\" HistoryStockNdmFields  \"stock\", \"otc\" HistoryStockSharesFields  \"stock\", \"qnv\" HistoryStockQnvFields  \"stock\", \"repo\" HistoryStockRepoFields  \"stock\", \"gcc\" HistoryStockRepoFields  \"stock\", \"shares\" HistoryStockSharesFields  \"stock\", \"foreignshares\" HistoryStockSharesFields  \"futures\", \"options\" HistoryFuturesOptionsFields  \"futures\", \"forts\" HistoryFuturesFortsFields  \"currency\", \"futures\" HistoryCurrencyFuturesFields  \"currency\", \"selt\" HistoryCurrencySeltFields

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
api_instance = swagger_client.MoexApi(swagger_client.ApiClient(configuration))
body = swagger_client.MoexHistoryBody() # MoexHistoryBody |  (optional)

try:
    # Получить официальные итоги по набору конкретных инструментов или по всем инструментам заданного рынка, группы режимов или одного режима торгов.  В зависимости от комбинации входных параметров engine и market возвращаются следующие типы ответов:  \"stock\", \"bonds\" HistoryStockBondsFields  \"stock\", \"ccp\" HistoryStockCcpFields  \"stock\", \"index\" HistoryStockIndexFields  \"stock\", \"ndm\" HistoryStockNdmFields  \"stock\", \"foreignndm\" HistoryStockNdmFields  \"stock\", \"otc\" HistoryStockSharesFields  \"stock\", \"qnv\" HistoryStockQnvFields  \"stock\", \"repo\" HistoryStockRepoFields  \"stock\", \"gcc\" HistoryStockRepoFields  \"stock\", \"shares\" HistoryStockSharesFields  \"stock\", \"foreignshares\" HistoryStockSharesFields  \"futures\", \"options\" HistoryFuturesOptionsFields  \"futures\", \"forts\" HistoryFuturesFortsFields  \"currency\", \"futures\" HistoryCurrencyFuturesFields  \"currency\", \"selt\" HistoryCurrencySeltFields
    api_response = api_instance.v2_moex_history_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoexApi->v2_moex_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoexHistoryBody**](MoexHistoryBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsMoexHistoryStockIndexFields**](EfirDataHubModelsModelsMoexHistoryStockIndexFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_moex_limitval_currency_post**
> list[EfirDataHubModelsModelsMoexLimitvalFields] v2_moex_limitval_currency_post(body=body)

Возвращает лимиты концентрации Валютного рынка

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
api_instance = swagger_client.MoexApi(swagger_client.ApiClient(configuration))
body = swagger_client.MoexLimitvalCurrencyBody() # MoexLimitvalCurrencyBody |  (optional)

try:
    # Возвращает лимиты концентрации Валютного рынка
    api_response = api_instance.v2_moex_limitval_currency_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoexApi->v2_moex_limitval_currency_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoexLimitvalCurrencyBody**](MoexLimitvalCurrencyBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsMoexLimitvalFields]**](EfirDataHubModelsModelsMoexLimitvalFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_moex_limitval_stock_post**
> list[EfirDataHubModelsModelsMoexLimitvalFields] v2_moex_limitval_stock_post(body=body)

Возвращает лимиты концентрации Фондового рынка

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
api_instance = swagger_client.MoexApi(swagger_client.ApiClient(configuration))
body = swagger_client.MoexLimitvalStockBody() # MoexLimitvalStockBody |  (optional)

try:
    # Возвращает лимиты концентрации Фондового рынка
    api_response = api_instance.v2_moex_limitval_stock_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoexApi->v2_moex_limitval_stock_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoexLimitvalStockBody**](MoexLimitvalStockBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsMoexLimitvalFields]**](EfirDataHubModelsModelsMoexLimitvalFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_moex_ncc_indicative_risk_currency_post**
> list[EfirDataHubModelsModelsMoexNccIndicativeRiskCurrencyFields] v2_moex_ncc_indicative_risk_currency_post(body=body)

Индикативные ставки риска валютного рынка, НКЦ

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
api_instance = swagger_client.MoexApi(swagger_client.ApiClient(configuration))
body = swagger_client.MoexNccIndicativeRiskCurrencyBody() # MoexNccIndicativeRiskCurrencyBody |  (optional)

try:
    # Индикативные ставки риска валютного рынка, НКЦ
    api_response = api_instance.v2_moex_ncc_indicative_risk_currency_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoexApi->v2_moex_ncc_indicative_risk_currency_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoexNccIndicativeRiskCurrencyBody**](MoexNccIndicativeRiskCurrencyBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsMoexNccIndicativeRiskCurrencyFields]**](EfirDataHubModelsModelsMoexNccIndicativeRiskCurrencyFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_moex_ncc_indicative_risk_fond_post**
> list[EfirDataHubModelsModelsMoexNccIndicativeRiskFondFields] v2_moex_ncc_indicative_risk_fond_post(body=body)

Индикативные ставки риска фондового рынка, НКЦ

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
api_instance = swagger_client.MoexApi(swagger_client.ApiClient(configuration))
body = swagger_client.MoexNccIndicativeRiskFondBody() # MoexNccIndicativeRiskFondBody |  (optional)

try:
    # Индикативные ставки риска фондового рынка, НКЦ
    api_response = api_instance.v2_moex_ncc_indicative_risk_fond_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoexApi->v2_moex_ncc_indicative_risk_fond_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoexNccIndicativeRiskFondBody**](MoexNccIndicativeRiskFondBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsMoexNccIndicativeRiskFondFields]**](EfirDataHubModelsModelsMoexNccIndicativeRiskFondFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_moex_ncc_indicative_risk_futures_post**
> list[EfirDataHubModelsModelsMoexNccIndicativeRiskFuturesFields] v2_moex_ncc_indicative_risk_futures_post(body=body)

Индикативные ставки риска срочного рынка, НКЦ

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
api_instance = swagger_client.MoexApi(swagger_client.ApiClient(configuration))
body = swagger_client.MoexNccIndicativeRiskFuturesBody() # MoexNccIndicativeRiskFuturesBody |  (optional)

try:
    # Индикативные ставки риска срочного рынка, НКЦ
    api_response = api_instance.v2_moex_ncc_indicative_risk_futures_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoexApi->v2_moex_ncc_indicative_risk_futures_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoexNccIndicativeRiskFuturesBody**](MoexNccIndicativeRiskFuturesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsMoexNccIndicativeRiskFuturesFields]**](EfirDataHubModelsModelsMoexNccIndicativeRiskFuturesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_moex_ncc_market_risk_currency_post**
> list[EfirDataHubModelsModelsMoexNccMarketRiskCurrencyFields] v2_moex_ncc_market_risk_currency_post(body=body)

Динамические риск-параметры рыночных рисков на валютном рынке, НКЦ

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
api_instance = swagger_client.MoexApi(swagger_client.ApiClient(configuration))
body = swagger_client.MoexNccMarketRiskCurrencyBody() # MoexNccMarketRiskCurrencyBody |  (optional)

try:
    # Динамические риск-параметры рыночных рисков на валютном рынке, НКЦ
    api_response = api_instance.v2_moex_ncc_market_risk_currency_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoexApi->v2_moex_ncc_market_risk_currency_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoexNccMarketRiskCurrencyBody**](MoexNccMarketRiskCurrencyBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsMoexNccMarketRiskCurrencyFields]**](EfirDataHubModelsModelsMoexNccMarketRiskCurrencyFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_moex_ncc_market_risk_fond_post**
> list[EfirDataHubModelsModelsMoexNccMarketRiskFondFields] v2_moex_ncc_market_risk_fond_post(body=body)

Динамические риск-параметры рыночных рисков на фондовом рынке, НКЦ

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
api_instance = swagger_client.MoexApi(swagger_client.ApiClient(configuration))
body = swagger_client.MoexNccMarketRiskFondBody() # MoexNccMarketRiskFondBody |  (optional)

try:
    # Динамические риск-параметры рыночных рисков на фондовом рынке, НКЦ
    api_response = api_instance.v2_moex_ncc_market_risk_fond_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoexApi->v2_moex_ncc_market_risk_fond_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoexNccMarketRiskFondBody**](MoexNccMarketRiskFondBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsMoexNccMarketRiskFondFields]**](EfirDataHubModelsModelsMoexNccMarketRiskFondFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_moex_ncc_percent_risk_currency_post**
> list[EfirDataHubModelsModelsMoexNccPercentRiskFields] v2_moex_ncc_percent_risk_currency_post(body=body)

Возвращает динамические риск-параметры процентных рисков на валютном рынке

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
api_instance = swagger_client.MoexApi(swagger_client.ApiClient(configuration))
body = swagger_client.MoexNccPercentRiskCurrencyBody() # MoexNccPercentRiskCurrencyBody |  (optional)

try:
    # Возвращает динамические риск-параметры процентных рисков на валютном рынке
    api_response = api_instance.v2_moex_ncc_percent_risk_currency_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoexApi->v2_moex_ncc_percent_risk_currency_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoexNccPercentRiskCurrencyBody**](MoexNccPercentRiskCurrencyBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsMoexNccPercentRiskFields]**](EfirDataHubModelsModelsMoexNccPercentRiskFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_moex_ncc_percent_risk_fond_post**
> list[EfirDataHubModelsModelsMoexNccPercentRiskFields] v2_moex_ncc_percent_risk_fond_post(body=body)

Возвращает динамические риск-параметры процентных рисков на рынке акций и облигаций

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
api_instance = swagger_client.MoexApi(swagger_client.ApiClient(configuration))
body = swagger_client.MoexNccPercentRiskFondBody() # MoexNccPercentRiskFondBody |  (optional)

try:
    # Возвращает динамические риск-параметры процентных рисков на рынке акций и облигаций
    api_response = api_instance.v2_moex_ncc_percent_risk_fond_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoexApi->v2_moex_ncc_percent_risk_fond_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoexNccPercentRiskFondBody**](MoexNccPercentRiskFondBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsMoexNccPercentRiskFields]**](EfirDataHubModelsModelsMoexNccPercentRiskFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_moex_option_columns_post**
> list[EfirDataHubModelsModelsMoexOptionColumnsFields] v2_moex_option_columns_post()

Получить описание полей в справочнике опционов, см. метод Options. Входных параметров нет.

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
api_instance = swagger_client.MoexApi(swagger_client.ApiClient(configuration))

try:
    # Получить описание полей в справочнике опционов, см. метод Options. Входных параметров нет.
    api_response = api_instance.v2_moex_option_columns_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoexApi->v2_moex_option_columns_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EfirDataHubModelsModelsMoexOptionColumnsFields]**](EfirDataHubModelsModelsMoexOptionColumnsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_moex_options_post**
> list[EfirDataHubModelsModelsMoexOptionsFields] v2_moex_options_post(body=body)

Получить описания опционов.

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
api_instance = swagger_client.MoexApi(swagger_client.ApiClient(configuration))
body = swagger_client.MoexOptionsBody() # MoexOptionsBody |  (optional)

try:
    # Получить описания опционов.
    api_response = api_instance.v2_moex_options_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoexApi->v2_moex_options_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoexOptionsBody**](MoexOptionsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsMoexOptionsFields]**](EfirDataHubModelsModelsMoexOptionsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_moex_sec_columns_post**
> list[EfirDataHubModelsModelsMoexSecColumnsFields] v2_moex_sec_columns_post()

Получить описание полей в справочнике торговых инструментов, см. метод Securities. Входных параметров нет.

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
api_instance = swagger_client.MoexApi(swagger_client.ApiClient(configuration))

try:
    # Получить описание полей в справочнике торговых инструментов, см. метод Securities. Входных параметров нет.
    api_response = api_instance.v2_moex_sec_columns_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoexApi->v2_moex_sec_columns_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EfirDataHubModelsModelsMoexSecColumnsFields]**](EfirDataHubModelsModelsMoexSecColumnsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_moex_securities_post**
> list[EfirDataHubModelsModelsMoexSecuritiesFields] v2_moex_securities_post(body=body)

Получить список торгуемых инструментов.

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
api_instance = swagger_client.MoexApi(swagger_client.ApiClient(configuration))
body = swagger_client.MoexSecuritiesBody() # MoexSecuritiesBody |  (optional)

try:
    # Получить список торгуемых инструментов.
    api_response = api_instance.v2_moex_securities_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoexApi->v2_moex_securities_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoexSecuritiesBody**](MoexSecuritiesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsMoexSecuritiesFields]**](EfirDataHubModelsModelsMoexSecuritiesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_moex_stock_boards_post**
> list[EfirDataHubModelsModelsMoexStockBoardsFields] v2_moex_stock_boards_post(body=body)

Возвращает описание режимов торгов (boards) ценных бумаг фондового рынка

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
api_instance = swagger_client.MoexApi(swagger_client.ApiClient(configuration))
body = swagger_client.MoexStockBoardsBody() # MoexStockBoardsBody |  (optional)

try:
    # Возвращает описание режимов торгов (boards) ценных бумаг фондового рынка
    api_response = api_instance.v2_moex_stock_boards_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoexApi->v2_moex_stock_boards_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoexStockBoardsBody**](MoexStockBoardsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsMoexStockBoardsFields]**](EfirDataHubModelsModelsMoexStockBoardsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_moex_stocks_post**
> list[EfirDataHubModelsModelsMoexStocksFields] v2_moex_stocks_post(body=body)

Возвращает краткое описание ценных бумаг фондового рынка

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
api_instance = swagger_client.MoexApi(swagger_client.ApiClient(configuration))
body = swagger_client.MoexStocksBody() # MoexStocksBody |  (optional)

try:
    # Возвращает краткое описание ценных бумаг фондового рынка
    api_response = api_instance.v2_moex_stocks_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoexApi->v2_moex_stocks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoexStocksBody**](MoexStocksBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsMoexStocksFields]**](EfirDataHubModelsModelsMoexStocksFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

