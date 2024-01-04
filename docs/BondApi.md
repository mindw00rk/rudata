# swagger_client.BondApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_bond_amortizations_ext_post**](BondApi.md#v2_bond_amortizations_ext_post) | **POST** /v2/Bond/AmortizationsExt | Получить расширенный план погашения выпусков с амортизацией долга.
[**v2_bond_amortizations_post**](BondApi.md#v2_bond_amortizations_post) | **POST** /v2/Bond/Amortizations | Получить план погашения выпусков с амортизацией долга.
[**v2_bond_auction_data_post**](BondApi.md#v2_bond_auction_data_post) | **POST** /v2/Bond/AuctionData | Получить данные по первичным размещениям.
[**v2_bond_calculate_bond_ex_post**](BondApi.md#v2_bond_calculate_bond_ex_post) | **POST** /v2/Bond/CalculateBondEx | Произвести вычисления доходностей и других параметров облигаций. Является аналогом метода CalculateBond с дополнительными полями входного параметра couponForecast и couponBinding.
[**v2_bond_calculate_bond_multi_post**](BondApi.md#v2_bond_calculate_bond_multi_post) | **POST** /v2/Bond/CalculateBondMulti | Аналог CalcucalteBondEx для списка инструментов
[**v2_bond_calculate_bond_post**](BondApi.md#v2_bond_calculate_bond_post) | **POST** /v2/Bond/CalculateBond | Произвести вычисления доходностей и других параметров облигаций.
[**v2_bond_calculate_post**](BondApi.md#v2_bond_calculate_post) | **POST** /v2/Bond/Calculate | Calculate bond yields, durations, face value
[**v2_bond_classification_post**](BondApi.md#v2_bond_classification_post) | **POST** /v2/Bond/Classification | Получить классификацию выпуска.
[**v2_bond_common_data_ext_post**](BondApi.md#v2_bond_common_data_ext_post) | **POST** /v2/Bond/CommonDataExt | Получить расширенные общие данные по выпуску.
[**v2_bond_common_data_post**](BondApi.md#v2_bond_common_data_post) | **POST** /v2/Bond/CommonData | Получить общие данные по выпуску.
[**v2_bond_convertation_post**](BondApi.md#v2_bond_convertation_post) | **POST** /v2/Bond/Convertation | Получить данные по конвертациям облигаций в другие инструменты.
[**v2_bond_coupons_ext_post**](BondApi.md#v2_bond_coupons_ext_post) | **POST** /v2/Bond/CouponsExt | Получить расширенные данные по купонам.
[**v2_bond_coupons_post**](BondApi.md#v2_bond_coupons_post) | **POST** /v2/Bond/Coupons | Получить данные по купонам.
[**v2_bond_covenants_post**](BondApi.md#v2_bond_covenants_post) | **POST** /v2/Bond/Covenants | Возвращает список ковенантов для массива бумаг
[**v2_bond_date_options_fields_post**](BondApi.md#v2_bond_date_options_fields_post) | **POST** /v2/Bond/DateOptionsFields | Получить справочник полей для метода DateOptionsTable.
[**v2_bond_date_options_post**](BondApi.md#v2_bond_date_options_post) | **POST** /v2/Bond/DateOptions | Получить параметры облигации, зависимые от даты.
[**v2_bond_date_options_table_post**](BondApi.md#v2_bond_date_options_table_post) | **POST** /v2/Bond/DateOptionsTable | Получить параметры облигации, зависимые от даты, в табличном виде.
[**v2_bond_default_events_post**](BondApi.md#v2_bond_default_events_post) | **POST** /v2/Bond/DefaultEvents | Получить данные по дефолтам по облигациям.
[**v2_bond_defaults_table_post**](BondApi.md#v2_bond_defaults_table_post) | **POST** /v2/Bond/DefaultsTable | Получить список произошедших дефолтов.
[**v2_bond_emission_docs_post**](BondApi.md#v2_bond_emission_docs_post) | **POST** /v2/Bond/EmissionDocs | Получить ссылки на документы эмиссий.
[**v2_bond_fintool_id_amortizations_post**](BondApi.md#v2_bond_fintool_id_amortizations_post) | **POST** /v2/Bond/{fintoolId}/Amortizations | Получить план погашения выпусков с амортизацией долга.
[**v2_bond_fintool_id_coupons_post**](BondApi.md#v2_bond_fintool_id_coupons_post) | **POST** /v2/Bond/{fintoolId}/Coupons | Получить данные по купонам.
[**v2_bond_fintool_id_covenant_info_post**](BondApi.md#v2_bond_fintool_id_covenant_info_post) | **POST** /v2/Bond/{fintoolId}/CovenantInfo | Возвращает список ковенантов для указанного fintoolId облигации
[**v2_bond_fintool_id_offers_post**](BondApi.md#v2_bond_fintool_id_offers_post) | **POST** /v2/Bond/{fintoolId}/Offers | Получить данные по досрочным выкупам/офертам.
[**v2_bond_floater_data_post**](BondApi.md#v2_bond_floater_data_post) | **POST** /v2/Bond/FloaterData | Возвращает описания правил расчета ставок для бумаг с плавающей купонной ставкой
[**v2_bond_g_curve_ofz_post**](BondApi.md#v2_bond_g_curve_ofz_post) | **POST** /v2/Bond/g-curve-ofz | Параметры кривой бескупонной доходности государственных облигаций
[**v2_bond_list_bond_types_post**](BondApi.md#v2_bond_list_bond_types_post) | **POST** /v2/Bond/ListBondTypes | Получить справочник типов облигаций.
[**v2_bond_list_org_roles_post**](BondApi.md#v2_bond_list_org_roles_post) | **POST** /v2/Bond/ListOrgRoles | Получить справочник ролей организаций.
[**v2_bond_list_type_groups_post**](BondApi.md#v2_bond_list_type_groups_post) | **POST** /v2/Bond/ListTypeGroups | Получить категории типов облигаций.
[**v2_bond_offerors_guarants_post**](BondApi.md#v2_bond_offerors_guarants_post) | **POST** /v2/Bond/OfferorsGuarants | Возвращает список гарантов/оферентов для инструмента
[**v2_bond_offers_post**](BondApi.md#v2_bond_offers_post) | **POST** /v2/Bond/Offers | Получить данные по досрочным выкупам/офертам.
[**v2_bond_organizers_post**](BondApi.md#v2_bond_organizers_post) | **POST** /v2/Bond/Organizers | Получить роли организаторов выпуска.
[**v2_bond_programs_post**](BondApi.md#v2_bond_programs_post) | **POST** /v2/Bond/Programs | Получить данные по программам выпуска облигаций.
[**v2_bond_risk_data_post**](BondApi.md#v2_bond_risk_data_post) | **POST** /v2/Bond/RiskData | Получить данные, необходимые для расчёта рисков по выпуску.
[**v2_bond_time_table_field_groups_post**](BondApi.md#v2_bond_time_table_field_groups_post) | **POST** /v2/Bond/TimeTableFieldGroups | Получить справочник групп полей (см. метод TimeTableFields).
[**v2_bond_time_table_fields_post**](BondApi.md#v2_bond_time_table_fields_post) | **POST** /v2/Bond/TimeTableFields | Получить справочник полей для использования в календаре событий (см. метод TimeTable).
[**v2_bond_time_table_post**](BondApi.md#v2_bond_time_table_post) | **POST** /v2/Bond/TimeTable | Получить календарь событий.
[**v2_bond_traffic_light_scoring_post**](BondApi.md#v2_bond_traffic_light_scoring_post) | **POST** /v2/Bond/TrafficLightScoring | Возвращает показатели кредитной оценки облигаций российских эмитентов или евробондов российских компаний  по шкале \&quot;светофора\&quot; (1-6), актуальные на заданную дату

# **v2_bond_amortizations_ext_post**
> list[EfirDataHubModelsModelsBondAmortizationsExtFields] v2_bond_amortizations_ext_post(body=body)

Получить расширенный план погашения выпусков с амортизацией долга.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondAmortizationsExtBody() # BondAmortizationsExtBody |  (optional)

try:
    # Получить расширенный план погашения выпусков с амортизацией долга.
    api_response = api_instance.v2_bond_amortizations_ext_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_amortizations_ext_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondAmortizationsExtBody**](BondAmortizationsExtBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondAmortizationsExtFields]**](EfirDataHubModelsModelsBondAmortizationsExtFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_amortizations_post**
> list[EfirDataHubModelsModelsBondAmortizationsFields] v2_bond_amortizations_post(body=body)

Получить план погашения выпусков с амортизацией долга.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondAmortizationsBody() # BondAmortizationsBody |  (optional)

try:
    # Получить план погашения выпусков с амортизацией долга.
    api_response = api_instance.v2_bond_amortizations_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_amortizations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondAmortizationsBody**](BondAmortizationsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondAmortizationsFields]**](EfirDataHubModelsModelsBondAmortizationsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_auction_data_post**
> list[EfirDataHubModelsModelsBondAuctionDataFields] v2_bond_auction_data_post(body=body)

Получить данные по первичным размещениям.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondAuctionDataBody() # BondAuctionDataBody |  (optional)

try:
    # Получить данные по первичным размещениям.
    api_response = api_instance.v2_bond_auction_data_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_auction_data_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondAuctionDataBody**](BondAuctionDataBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondAuctionDataFields]**](EfirDataHubModelsModelsBondAuctionDataFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_calculate_bond_ex_post**
> list[EfirDataHubModelsModelsBondCalculateBondFields] v2_bond_calculate_bond_ex_post(body=body)

Произвести вычисления доходностей и других параметров облигаций. Является аналогом метода CalculateBond с дополнительными полями входного параметра couponForecast и couponBinding.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondCalculateBondExBody() # BondCalculateBondExBody |  (optional)

try:
    # Произвести вычисления доходностей и других параметров облигаций. Является аналогом метода CalculateBond с дополнительными полями входного параметра couponForecast и couponBinding.
    api_response = api_instance.v2_bond_calculate_bond_ex_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_calculate_bond_ex_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondCalculateBondExBody**](BondCalculateBondExBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondCalculateBondFields]**](EfirDataHubModelsModelsBondCalculateBondFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_calculate_bond_multi_post**
> list[EfirDataHubModelsModelsBondCalculateBondMultiResponse] v2_bond_calculate_bond_multi_post(body=body)

Аналог CalcucalteBondEx для списка инструментов

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondCalculateBondMultiBody() # BondCalculateBondMultiBody |  (optional)

try:
    # Аналог CalcucalteBondEx для списка инструментов
    api_response = api_instance.v2_bond_calculate_bond_multi_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_calculate_bond_multi_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondCalculateBondMultiBody**](BondCalculateBondMultiBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondCalculateBondMultiResponse]**](EfirDataHubModelsModelsBondCalculateBondMultiResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_calculate_bond_post**
> list[EfirDataHubModelsModelsBondCalculateBondFields] v2_bond_calculate_bond_post(body=body)

Произвести вычисления доходностей и других параметров облигаций.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondCalculateBondBody() # BondCalculateBondBody |  (optional)

try:
    # Произвести вычисления доходностей и других параметров облигаций.
    api_response = api_instance.v2_bond_calculate_bond_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_calculate_bond_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondCalculateBondBody**](BondCalculateBondBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondCalculateBondFields]**](EfirDataHubModelsModelsBondCalculateBondFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_calculate_post**
> EfirDataHubModelsModelsBondCalculateResponse v2_bond_calculate_post(body=body)

Calculate bond yields, durations, face value

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondCalculateBody() # BondCalculateBody |  (optional)

try:
    # Calculate bond yields, durations, face value
    api_response = api_instance.v2_bond_calculate_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_calculate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondCalculateBody**](BondCalculateBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsBondCalculateResponse**](EfirDataHubModelsModelsBondCalculateResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_classification_post**
> list[EfirDataHubModelsModelsBondClassificationFields] v2_bond_classification_post(body=body)

Получить классификацию выпуска.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondClassificationBody() # BondClassificationBody |  (optional)

try:
    # Получить классификацию выпуска.
    api_response = api_instance.v2_bond_classification_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_classification_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondClassificationBody**](BondClassificationBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondClassificationFields]**](EfirDataHubModelsModelsBondClassificationFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_common_data_ext_post**
> list[EfirDataHubModelsModelsBondCommonDataExtFields] v2_bond_common_data_ext_post(body=body)

Получить расширенные общие данные по выпуску.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondCommonDataExtBody() # BondCommonDataExtBody |  (optional)

try:
    # Получить расширенные общие данные по выпуску.
    api_response = api_instance.v2_bond_common_data_ext_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_common_data_ext_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondCommonDataExtBody**](BondCommonDataExtBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondCommonDataExtFields]**](EfirDataHubModelsModelsBondCommonDataExtFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_common_data_post**
> list[EfirDataHubModelsModelsBondCommonDataFields] v2_bond_common_data_post(body=body)

Получить общие данные по выпуску.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondCommonDataBody() # BondCommonDataBody |  (optional)

try:
    # Получить общие данные по выпуску.
    api_response = api_instance.v2_bond_common_data_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_common_data_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondCommonDataBody**](BondCommonDataBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondCommonDataFields]**](EfirDataHubModelsModelsBondCommonDataFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_convertation_post**
> list[EfirDataHubModelsModelsBondConvertationFields] v2_bond_convertation_post(body=body)

Получить данные по конвертациям облигаций в другие инструменты.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondConvertationBody() # BondConvertationBody |  (optional)

try:
    # Получить данные по конвертациям облигаций в другие инструменты.
    api_response = api_instance.v2_bond_convertation_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_convertation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondConvertationBody**](BondConvertationBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondConvertationFields]**](EfirDataHubModelsModelsBondConvertationFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_coupons_ext_post**
> list[EfirDataHubModelsModelsBondCouponsExtFields] v2_bond_coupons_ext_post(body=body)

Получить расширенные данные по купонам.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondCouponsExtBody() # BondCouponsExtBody |  (optional)

try:
    # Получить расширенные данные по купонам.
    api_response = api_instance.v2_bond_coupons_ext_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_coupons_ext_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondCouponsExtBody**](BondCouponsExtBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondCouponsExtFields]**](EfirDataHubModelsModelsBondCouponsExtFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_coupons_post**
> list[EfirDataHubModelsModelsBondCouponsFields] v2_bond_coupons_post(body=body)

Получить данные по купонам.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondCouponsBody() # BondCouponsBody |  (optional)

try:
    # Получить данные по купонам.
    api_response = api_instance.v2_bond_coupons_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_coupons_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondCouponsBody**](BondCouponsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondCouponsFields]**](EfirDataHubModelsModelsBondCouponsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_covenants_post**
> list[EfirDataHubModelsModelsBondCovenantsFields] v2_bond_covenants_post(body=body)

Возвращает список ковенантов для массива бумаг

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondCovenantsBody() # BondCovenantsBody |  (optional)

try:
    # Возвращает список ковенантов для массива бумаг
    api_response = api_instance.v2_bond_covenants_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_covenants_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondCovenantsBody**](BondCovenantsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondCovenantsFields]**](EfirDataHubModelsModelsBondCovenantsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_date_options_fields_post**
> list[EfirDataHubModelsModelsBondDateOptionsFieldsFields] v2_bond_date_options_fields_post(body=body)

Получить справочник полей для метода DateOptionsTable.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondDateOptionsFieldsBody() # BondDateOptionsFieldsBody |  (optional)

try:
    # Получить справочник полей для метода DateOptionsTable.
    api_response = api_instance.v2_bond_date_options_fields_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_date_options_fields_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondDateOptionsFieldsBody**](BondDateOptionsFieldsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondDateOptionsFieldsFields]**](EfirDataHubModelsModelsBondDateOptionsFieldsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_date_options_post**
> EfirDataHubModelsModelsBondDateOptionsResponse v2_bond_date_options_post(body=body)

Получить параметры облигации, зависимые от даты.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondDateOptionsBody() # BondDateOptionsBody |  (optional)

try:
    # Получить параметры облигации, зависимые от даты.
    api_response = api_instance.v2_bond_date_options_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_date_options_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondDateOptionsBody**](BondDateOptionsBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsBondDateOptionsResponse**](EfirDataHubModelsModelsBondDateOptionsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_date_options_table_post**
> list[EfirDataHubModelsModelsBondDateOptionsTableFields] v2_bond_date_options_table_post(body=body)

Получить параметры облигации, зависимые от даты, в табличном виде.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondDateOptionsTableBody() # BondDateOptionsTableBody |  (optional)

try:
    # Получить параметры облигации, зависимые от даты, в табличном виде.
    api_response = api_instance.v2_bond_date_options_table_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_date_options_table_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondDateOptionsTableBody**](BondDateOptionsTableBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondDateOptionsTableFields]**](EfirDataHubModelsModelsBondDateOptionsTableFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_default_events_post**
> list[EfirDataHubModelsModelsBondDefaultEventsFields] v2_bond_default_events_post(body=body)

Получить данные по дефолтам по облигациям.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondDefaultEventsBody() # BondDefaultEventsBody |  (optional)

try:
    # Получить данные по дефолтам по облигациям.
    api_response = api_instance.v2_bond_default_events_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_default_events_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondDefaultEventsBody**](BondDefaultEventsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondDefaultEventsFields]**](EfirDataHubModelsModelsBondDefaultEventsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_defaults_table_post**
> list[EfirDataHubModelsModelsBondDefaultsTableFields] v2_bond_defaults_table_post(body=body)

Получить список произошедших дефолтов.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondDefaultsTableBody() # BondDefaultsTableBody |  (optional)

try:
    # Получить список произошедших дефолтов.
    api_response = api_instance.v2_bond_defaults_table_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_defaults_table_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondDefaultsTableBody**](BondDefaultsTableBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondDefaultsTableFields]**](EfirDataHubModelsModelsBondDefaultsTableFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_emission_docs_post**
> list[EfirDataHubModelsModelsBondEmissionDocsFields] v2_bond_emission_docs_post(body=body)

Получить ссылки на документы эмиссий.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondEmissionDocsBody() # BondEmissionDocsBody |  (optional)

try:
    # Получить ссылки на документы эмиссий.
    api_response = api_instance.v2_bond_emission_docs_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_emission_docs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondEmissionDocsBody**](BondEmissionDocsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondEmissionDocsFields]**](EfirDataHubModelsModelsBondEmissionDocsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_fintool_id_amortizations_post**
> list[EfirDataHubModelsModelsBondAmortizationsFields] v2_bond_fintool_id_amortizations_post(fintool_id, body=body)

Получить план погашения выпусков с амортизацией долга.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
fintool_id = 789 # int | Идентификатор финансового инструмента в базе Интерфакс
body = swagger_client.FintoolIdAmortizationsBody() # FintoolIdAmortizationsBody | Параметры запроса (optional)

try:
    # Получить план погашения выпусков с амортизацией долга.
    api_response = api_instance.v2_bond_fintool_id_amortizations_post(fintool_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_fintool_id_amortizations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fintool_id** | **int**| Идентификатор финансового инструмента в базе Интерфакс | 
 **body** | [**FintoolIdAmortizationsBody**](FintoolIdAmortizationsBody.md)| Параметры запроса | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondAmortizationsFields]**](EfirDataHubModelsModelsBondAmortizationsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_fintool_id_coupons_post**
> list[EfirDataHubModelsModelsBondCouponsFields] v2_bond_fintool_id_coupons_post(fintool_id, body=body)

Получить данные по купонам.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
fintool_id = 789 # int | Идентификатор финансового инструмента в базе Интерфакс
body = swagger_client.FintoolIdCouponsBody() # FintoolIdCouponsBody | Параметры запроса (optional)

try:
    # Получить данные по купонам.
    api_response = api_instance.v2_bond_fintool_id_coupons_post(fintool_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_fintool_id_coupons_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fintool_id** | **int**| Идентификатор финансового инструмента в базе Интерфакс | 
 **body** | [**FintoolIdCouponsBody**](FintoolIdCouponsBody.md)| Параметры запроса | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondCouponsFields]**](EfirDataHubModelsModelsBondCouponsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_fintool_id_covenant_info_post**
> list[EfirDataHubModelsModelsBondCovenantsInfoFields] v2_bond_fintool_id_covenant_info_post(fintool_id)

Возвращает список ковенантов для указанного fintoolId облигации

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
fintool_id = 789 # int | 

try:
    # Возвращает список ковенантов для указанного fintoolId облигации
    api_response = api_instance.v2_bond_fintool_id_covenant_info_post(fintool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_fintool_id_covenant_info_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fintool_id** | **int**|  | 

### Return type

[**list[EfirDataHubModelsModelsBondCovenantsInfoFields]**](EfirDataHubModelsModelsBondCovenantsInfoFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_fintool_id_offers_post**
> list[EfirDataHubModelsModelsBondOffersFields] v2_bond_fintool_id_offers_post(fintool_id, body=body)

Получить данные по досрочным выкупам/офертам.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
fintool_id = 789 # int | Идентификатор финансового инструмента в базе Интерфакс
body = swagger_client.FintoolIdOffersBody() # FintoolIdOffersBody | Параметры запроса (optional)

try:
    # Получить данные по досрочным выкупам/офертам.
    api_response = api_instance.v2_bond_fintool_id_offers_post(fintool_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_fintool_id_offers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fintool_id** | **int**| Идентификатор финансового инструмента в базе Интерфакс | 
 **body** | [**FintoolIdOffersBody**](FintoolIdOffersBody.md)| Параметры запроса | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondOffersFields]**](EfirDataHubModelsModelsBondOffersFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_floater_data_post**
> list[EfirDataHubModelsModelsBondFloaterDataFields] v2_bond_floater_data_post(body=body)

Возвращает описания правил расчета ставок для бумаг с плавающей купонной ставкой

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondFloaterDataBody() # BondFloaterDataBody |  (optional)

try:
    # Возвращает описания правил расчета ставок для бумаг с плавающей купонной ставкой
    api_response = api_instance.v2_bond_floater_data_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_floater_data_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondFloaterDataBody**](BondFloaterDataBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondFloaterDataFields]**](EfirDataHubModelsModelsBondFloaterDataFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_g_curve_ofz_post**
> EfirDataHubModelsModelsRuDataGCurveOFZResponse v2_bond_g_curve_ofz_post(body=body)

Параметры кривой бескупонной доходности государственных облигаций

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondGcurveofzBody() # BondGcurveofzBody |  (optional)

try:
    # Параметры кривой бескупонной доходности государственных облигаций
    api_response = api_instance.v2_bond_g_curve_ofz_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_g_curve_ofz_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondGcurveofzBody**](BondGcurveofzBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsRuDataGCurveOFZResponse**](EfirDataHubModelsModelsRuDataGCurveOFZResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_list_bond_types_post**
> list[EfirDataHubModelsModelsBondListBondTypesFields] v2_bond_list_bond_types_post(body=body)

Получить справочник типов облигаций.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondListBondTypesBody() # BondListBondTypesBody |  (optional)

try:
    # Получить справочник типов облигаций.
    api_response = api_instance.v2_bond_list_bond_types_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_list_bond_types_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondListBondTypesBody**](BondListBondTypesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondListBondTypesFields]**](EfirDataHubModelsModelsBondListBondTypesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_list_org_roles_post**
> list[EfirDataHubModelsModelsBondListOrgRolesFields] v2_bond_list_org_roles_post(body=body)

Получить справочник ролей организаций.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondListOrgRolesBody() # BondListOrgRolesBody |  (optional)

try:
    # Получить справочник ролей организаций.
    api_response = api_instance.v2_bond_list_org_roles_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_list_org_roles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondListOrgRolesBody**](BondListOrgRolesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondListOrgRolesFields]**](EfirDataHubModelsModelsBondListOrgRolesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_list_type_groups_post**
> list[EfirDataHubModelsModelsBondListTypeGroupsFields] v2_bond_list_type_groups_post(body=body)

Получить категории типов облигаций.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondListTypeGroupsBody() # BondListTypeGroupsBody |  (optional)

try:
    # Получить категории типов облигаций.
    api_response = api_instance.v2_bond_list_type_groups_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_list_type_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondListTypeGroupsBody**](BondListTypeGroupsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondListTypeGroupsFields]**](EfirDataHubModelsModelsBondListTypeGroupsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_offerors_guarants_post**
> list[EfirDataHubModelsModelsBondOfferorsGuarantsFields] v2_bond_offerors_guarants_post(body=body)

Возвращает список гарантов/оферентов для инструмента

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondOfferorsGuarantsBody() # BondOfferorsGuarantsBody |  (optional)

try:
    # Возвращает список гарантов/оферентов для инструмента
    api_response = api_instance.v2_bond_offerors_guarants_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_offerors_guarants_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondOfferorsGuarantsBody**](BondOfferorsGuarantsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondOfferorsGuarantsFields]**](EfirDataHubModelsModelsBondOfferorsGuarantsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_offers_post**
> list[EfirDataHubModelsModelsBondOffersFields] v2_bond_offers_post(body=body)

Получить данные по досрочным выкупам/офертам.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondOffersBody() # BondOffersBody |  (optional)

try:
    # Получить данные по досрочным выкупам/офертам.
    api_response = api_instance.v2_bond_offers_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_offers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondOffersBody**](BondOffersBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondOffersFields]**](EfirDataHubModelsModelsBondOffersFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_organizers_post**
> list[EfirDataHubModelsModelsBondOrganizersFields] v2_bond_organizers_post(body=body)

Получить роли организаторов выпуска.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondOrganizersBody() # BondOrganizersBody |  (optional)

try:
    # Получить роли организаторов выпуска.
    api_response = api_instance.v2_bond_organizers_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_organizers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondOrganizersBody**](BondOrganizersBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondOrganizersFields]**](EfirDataHubModelsModelsBondOrganizersFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_programs_post**
> list[EfirDataHubModelsModelsBondProgramsFields] v2_bond_programs_post(body=body)

Получить данные по программам выпуска облигаций.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondProgramsBody() # BondProgramsBody |  (optional)

try:
    # Получить данные по программам выпуска облигаций.
    api_response = api_instance.v2_bond_programs_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_programs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondProgramsBody**](BondProgramsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondProgramsFields]**](EfirDataHubModelsModelsBondProgramsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_risk_data_post**
> list[EfirDataHubModelsModelsBondRiskDataFields] v2_bond_risk_data_post(body=body)

Получить данные, необходимые для расчёта рисков по выпуску.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondRiskDataBody() # BondRiskDataBody |  (optional)

try:
    # Получить данные, необходимые для расчёта рисков по выпуску.
    api_response = api_instance.v2_bond_risk_data_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_risk_data_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondRiskDataBody**](BondRiskDataBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondRiskDataFields]**](EfirDataHubModelsModelsBondRiskDataFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_time_table_field_groups_post**
> list[EfirDataHubModelsModelsBondTimeTableFieldGroupsFields] v2_bond_time_table_field_groups_post(body=body)

Получить справочник групп полей (см. метод TimeTableFields).

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondTimeTableFieldGroupsBody() # BondTimeTableFieldGroupsBody |  (optional)

try:
    # Получить справочник групп полей (см. метод TimeTableFields).
    api_response = api_instance.v2_bond_time_table_field_groups_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_time_table_field_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondTimeTableFieldGroupsBody**](BondTimeTableFieldGroupsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondTimeTableFieldGroupsFields]**](EfirDataHubModelsModelsBondTimeTableFieldGroupsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_time_table_fields_post**
> list[EfirDataHubModelsModelsBondTimeTableFieldsFields] v2_bond_time_table_fields_post(body=body)

Получить справочник полей для использования в календаре событий (см. метод TimeTable).

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondTimeTableFieldsBody() # BondTimeTableFieldsBody |  (optional)

try:
    # Получить справочник полей для использования в календаре событий (см. метод TimeTable).
    api_response = api_instance.v2_bond_time_table_fields_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_time_table_fields_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondTimeTableFieldsBody**](BondTimeTableFieldsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondTimeTableFieldsFields]**](EfirDataHubModelsModelsBondTimeTableFieldsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_time_table_post**
> EfirDataHubModelsModelsBondTimeTableResponse v2_bond_time_table_post(body=body)

Получить календарь событий.

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondTimeTableBody() # BondTimeTableBody |  (optional)

try:
    # Получить календарь событий.
    api_response = api_instance.v2_bond_time_table_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_time_table_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondTimeTableBody**](BondTimeTableBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsBondTimeTableResponse**](EfirDataHubModelsModelsBondTimeTableResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_bond_traffic_light_scoring_post**
> list[EfirDataHubModelsModelsBondTrafficLightScoringFields] v2_bond_traffic_light_scoring_post(body=body)

Возвращает показатели кредитной оценки облигаций российских эмитентов или евробондов российских компаний  по шкале \"светофора\" (1-6), актуальные на заданную дату

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
api_instance = swagger_client.BondApi(swagger_client.ApiClient(configuration))
body = swagger_client.BondTrafficLightScoringBody() # BondTrafficLightScoringBody |  (optional)

try:
    # Возвращает показатели кредитной оценки облигаций российских эмитентов или евробондов российских компаний  по шкале \"светофора\" (1-6), актуальные на заданную дату
    api_response = api_instance.v2_bond_traffic_light_scoring_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->v2_bond_traffic_light_scoring_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondTrafficLightScoringBody**](BondTrafficLightScoringBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondTrafficLightScoringFields]**](EfirDataHubModelsModelsBondTrafficLightScoringFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

