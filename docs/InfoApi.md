# swagger_client.InfoApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_info_bank_branches_post**](InfoApi.md#v2_info_bank_branches_post) | **POST** /v2/Info/BankBranches | Получить список отделений банков.
[**v2_info_calendar_post**](InfoApi.md#v2_info_calendar_post) | **POST** /v2/Info/Calendar | Возвращает календарь событий по инструментам за период.
[**v2_info_calendar_v2_post**](InfoApi.md#v2_info_calendar_v2_post) | **POST** /v2/Info/CalendarV2 | Возвращает календарь событий по инструментам за период
[**v2_info_classification_codes_post**](InfoApi.md#v2_info_classification_codes_post) | **POST** /v2/Info/ClassificationCodes | Получить структуру «Группы классификаторов» / «Классификаторы» для инструментов и/или эмитентов.
[**v2_info_classification_post**](InfoApi.md#v2_info_classification_post) | **POST** /v2/Info/Classification | Классификатор финансовых инструментов.
[**v2_info_country_classification_post**](InfoApi.md#v2_info_country_classification_post) | **POST** /v2/Info/CountryClassification | Получить классификацию стран
[**v2_info_currencies_post**](InfoApi.md#v2_info_currencies_post) | **POST** /v2/Info/Currencies | Получить справочник валют.
[**v2_info_currency_codes_post**](InfoApi.md#v2_info_currency_codes_post) | **POST** /v2/Info/CurrencyCodes | Получить коды валют по различным классификаторам.
[**v2_info_deleted_securities_post**](InfoApi.md#v2_info_deleted_securities_post) | **POST** /v2/Info/DeletedSecurities | Получить список удаленных из базы инструментов.
[**v2_info_emission_docs_post**](InfoApi.md#v2_info_emission_docs_post) | **POST** /v2/Info/EmissionDocs | Получить ссылки на документы эмиссий.
[**v2_info_emitent_category_value_post**](InfoApi.md#v2_info_emitent_category_value_post) | **POST** /v2/Info/emitent-category-value | Метод для получения компаний и их категорий
[**v2_info_emitent_classification_post**](InfoApi.md#v2_info_emitent_classification_post) | **POST** /v2/Info/EmitentClassification | Получить классификацию эмитентов.
[**v2_info_emitent_docs_post**](InfoApi.md#v2_info_emitent_docs_post) | **POST** /v2/Info/EmitentDocs | Получить информационные материалы по эмитентам
[**v2_info_emitents_ext_post**](InfoApi.md#v2_info_emitents_ext_post) | **POST** /v2/Info/EmitentsExt | Получить расширенный справочник по эмитентам.
[**v2_info_emitents_id_post**](InfoApi.md#v2_info_emitents_id_post) | **POST** /v2/Info/Emitents/{id} | Получить краткий справочник по эмитентам.
[**v2_info_emitents_post**](InfoApi.md#v2_info_emitents_post) | **POST** /v2/Info/Emitents | Получить краткий справочник по эмитентам.
[**v2_info_enum_values_post**](InfoApi.md#v2_info_enum_values_post) | **POST** /v2/Info/EnumValues | Списки значений выходных полей с перечислениями в методах Securities и FintoolReferenceData.
[**v2_info_enums_post**](InfoApi.md#v2_info_enums_post) | **POST** /v2/Info/Enums | Списки выходных полей с перечислениями в методах Securities и FintoolReferenceData.
[**v2_info_exchange_tree_post**](InfoApi.md#v2_info_exchange_tree_post) | **POST** /v2/Info/ExchangeTree | Получить иерархию торговых площадок/источников, используемых Интерфакс.
[**v2_info_fields_post**](InfoApi.md#v2_info_fields_post) | **POST** /v2/Info/Fields | Получить справочник по полям данных для торговых инструментов.
[**v2_info_fintool_category_value_post**](InfoApi.md#v2_info_fintool_category_value_post) | **POST** /v2/Info/fintool-category-value | Метод для получения инструментов и их категорий
[**v2_info_fintool_classification_post**](InfoApi.md#v2_info_fintool_classification_post) | **POST** /v2/Info/FintoolClassification | Получить классификацию инструментов.
[**v2_info_fintool_convertation_post**](InfoApi.md#v2_info_fintool_convertation_post) | **POST** /v2/Info/FintoolConvertation | Получить данные по конвертациям инструментов (кроме облигаций) в другие инструменты.
[**v2_info_fintool_fields_ext_post**](InfoApi.md#v2_info_fintool_fields_ext_post) | **POST** /v2/Info/FintoolFieldsExt | Получить справочник по полям данных для финансовых инструментов (метод служебный, только для внутреннего использования).
[**v2_info_fintool_fields_post**](InfoApi.md#v2_info_fintool_fields_post) | **POST** /v2/Info/FintoolFields | Получить справочник по полям данных для финансовых инструментов.
[**v2_info_fintool_listing_post**](InfoApi.md#v2_info_fintool_listing_post) | **POST** /v2/Info/FintoolListing | Уровень листинга и суммарные объемы торгов (метод служебный, только для внутреннего использования).
[**v2_info_fintool_ref_data_list_post**](InfoApi.md#v2_info_fintool_ref_data_list_post) | **POST** /v2/Info/FintoolRefData/list | Get fintool reference data
[**v2_info_fintool_reference_data_id_post**](InfoApi.md#v2_info_fintool_reference_data_id_post) | **POST** /v2/Info/FintoolReferenceData/{id} | Получить расширенный справочник по финансовому инструменту.
[**v2_info_fintool_reference_data_post**](InfoApi.md#v2_info_fintool_reference_data_post) | **POST** /v2/Info/FintoolReferenceData | Получить расширенный справочник по финансовым инструментам.
[**v2_info_holidays_post**](InfoApi.md#v2_info_holidays_post) | **POST** /v2/Info/Holidays | Возвращает даты неторговых дней
[**v2_info_ifx_fintool_ref_data_post**](InfoApi.md#v2_info_ifx_fintool_ref_data_post) | **POST** /v2/Info/IFXFintoolRefData | Получить справочник Интерфакс по финансовым инструментам.
[**v2_info_instruments_post**](InfoApi.md#v2_info_instruments_post) | **POST** /v2/Info/Instruments | Получить краткий справочник по торговым инструментам.
[**v2_info_list_org_roles_post**](InfoApi.md#v2_info_list_org_roles_post) | **POST** /v2/Info/ListOrgRoles | Получить справочник ролей организаций
[**v2_info_money_flow_post**](InfoApi.md#v2_info_money_flow_post) | **POST** /v2/Info/MoneyFlow | Поток платежей по ценной бумаге в валюте номинала.
[**v2_info_organizers_by_fininst_id_post**](InfoApi.md#v2_info_organizers_by_fininst_id_post) | **POST** /v2/Info/OrganizersByFininstId | Получить роли организаторов выпуска по списку FininstId
[**v2_info_organizers_by_fintool_id_post**](InfoApi.md#v2_info_organizers_by_fintool_id_post) | **POST** /v2/Info/OrganizersByFintoolId | Получить роли организаторов выпуска по списку FintoolId
[**v2_info_organizers_post**](InfoApi.md#v2_info_organizers_post) | **POST** /v2/Info/Organizers | Получить роли организаторов выпуска
[**v2_info_prof_participants_post**](InfoApi.md#v2_info_prof_participants_post) | **POST** /v2/Info/ProfParticipants | Получить реквизиты профессиональных участников финансового рынка по версии ЦБ.
[**v2_info_residual_face_value_post**](InfoApi.md#v2_info_residual_face_value_post) | **POST** /v2/Info/ResidualFaceValue | Получить величину остаточного номинала на заданную дату.
[**v2_info_securities_post**](InfoApi.md#v2_info_securities_post) | **POST** /v2/Info/Securities | Получить краткий справочник по финансовым инструментам. Для акций метод возвращает только основные выпуски (по колонке SecurityKind).   Для получения данных по дополнительным выпускам необходимо использовать метод FintoolRefrenceData.
[**v2_info_share_dividend_id_post**](InfoApi.md#v2_info_share_dividend_id_post) | **POST** /v2/Info/ShareDividend/{id} | Информация по дивидендам
[**v2_info_share_dividend_post**](InfoApi.md#v2_info_share_dividend_post) | **POST** /v2/Info/ShareDividend | Информация по дивидендам
[**v2_info_type_tree_post**](InfoApi.md#v2_info_type_tree_post) | **POST** /v2/Info/TypeTree | Get information about tree of instrument types

# **v2_info_bank_branches_post**
> list[EfirDataHubModelsModelsInfoBankBranchesFields] v2_info_bank_branches_post(body=body)

Получить список отделений банков.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoBankBranchesBody() # InfoBankBranchesBody |  (optional)

try:
    # Получить список отделений банков.
    api_response = api_instance.v2_info_bank_branches_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_bank_branches_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoBankBranchesBody**](InfoBankBranchesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoBankBranchesFields]**](EfirDataHubModelsModelsInfoBankBranchesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_calendar_post**
> EfirDataHubModelsModelsBondTimeTableResponse v2_info_calendar_post(body=body)

Возвращает календарь событий по инструментам за период.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoCalendarBody() # InfoCalendarBody |  (optional)

try:
    # Возвращает календарь событий по инструментам за период.
    api_response = api_instance.v2_info_calendar_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_calendar_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoCalendarBody**](InfoCalendarBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsBondTimeTableResponse**](EfirDataHubModelsModelsBondTimeTableResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_calendar_v2_post**
> list[EfirDataHubModelsModelsBondTimeTableV2Fields] v2_info_calendar_v2_post(body=body)

Возвращает календарь событий по инструментам за период

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoCalendarV2Body() # InfoCalendarV2Body |  (optional)

try:
    # Возвращает календарь событий по инструментам за период
    api_response = api_instance.v2_info_calendar_v2_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_calendar_v2_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoCalendarV2Body**](InfoCalendarV2Body.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsBondTimeTableV2Fields]**](EfirDataHubModelsModelsBondTimeTableV2Fields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_classification_codes_post**
> EfirDataHubModelsModelsInfoClassificationCodesResponse v2_info_classification_codes_post(body=body)

Получить структуру «Группы классификаторов» / «Классификаторы» для инструментов и/или эмитентов.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoClassificationCodesBody() # InfoClassificationCodesBody |  (optional)

try:
    # Получить структуру «Группы классификаторов» / «Классификаторы» для инструментов и/или эмитентов.
    api_response = api_instance.v2_info_classification_codes_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_classification_codes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoClassificationCodesBody**](InfoClassificationCodesBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsInfoClassificationCodesResponse**](EfirDataHubModelsModelsInfoClassificationCodesResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_classification_post**
> list[EfirDataHubModelsModelsInfoClassificationFields] v2_info_classification_post(body=body)

Классификатор финансовых инструментов.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoClassificationBody() # InfoClassificationBody |  (optional)

try:
    # Классификатор финансовых инструментов.
    api_response = api_instance.v2_info_classification_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_classification_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoClassificationBody**](InfoClassificationBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoClassificationFields]**](EfirDataHubModelsModelsInfoClassificationFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_country_classification_post**
> list[EfirDataHubModelsModelsInfoCountryClassificationFields] v2_info_country_classification_post(body=body)

Получить классификацию стран

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoCountryClassificationBody() # InfoCountryClassificationBody |  (optional)

try:
    # Получить классификацию стран
    api_response = api_instance.v2_info_country_classification_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_country_classification_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoCountryClassificationBody**](InfoCountryClassificationBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoCountryClassificationFields]**](EfirDataHubModelsModelsInfoCountryClassificationFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_currencies_post**
> EfirDataHubModelsModelsInfoCurrenciesWithKkvFields v2_info_currencies_post(body=body)

Получить справочник валют.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoCurrenciesBody() # InfoCurrenciesBody |  (optional)

try:
    # Получить справочник валют.
    api_response = api_instance.v2_info_currencies_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_currencies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoCurrenciesBody**](InfoCurrenciesBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsInfoCurrenciesWithKkvFields**](EfirDataHubModelsModelsInfoCurrenciesWithKkvFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_currency_codes_post**
> list[EfirDataHubModelsModelsInfoCurrencyCodesFields] v2_info_currency_codes_post(body=body)

Получить коды валют по различным классификаторам.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoCurrencyCodesBody() # InfoCurrencyCodesBody |  (optional)

try:
    # Получить коды валют по различным классификаторам.
    api_response = api_instance.v2_info_currency_codes_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_currency_codes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoCurrencyCodesBody**](InfoCurrencyCodesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoCurrencyCodesFields]**](EfirDataHubModelsModelsInfoCurrencyCodesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_deleted_securities_post**
> list[EfirDataHubModelsModelsInfoDeletedSecuritiesFields] v2_info_deleted_securities_post(body=body)

Получить список удаленных из базы инструментов.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoDeletedSecuritiesBody() # InfoDeletedSecuritiesBody |  (optional)

try:
    # Получить список удаленных из базы инструментов.
    api_response = api_instance.v2_info_deleted_securities_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_deleted_securities_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoDeletedSecuritiesBody**](InfoDeletedSecuritiesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoDeletedSecuritiesFields]**](EfirDataHubModelsModelsInfoDeletedSecuritiesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_emission_docs_post**
> EfirDataHubModelsModelsInfoEmissionDocsResponse v2_info_emission_docs_post(body=body)

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoEmissionDocsBody() # InfoEmissionDocsBody |  (optional)

try:
    # Получить ссылки на документы эмиссий.
    api_response = api_instance.v2_info_emission_docs_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_emission_docs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoEmissionDocsBody**](InfoEmissionDocsBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsInfoEmissionDocsResponse**](EfirDataHubModelsModelsInfoEmissionDocsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_emitent_category_value_post**
> list[EfirDataHubModelsModelsDictionaryEmitentCategoryValueFields] v2_info_emitent_category_value_post(body=body)

Метод для получения компаний и их категорий

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoEmitentcategoryvalueBody() # InfoEmitentcategoryvalueBody |  (optional)

try:
    # Метод для получения компаний и их категорий
    api_response = api_instance.v2_info_emitent_category_value_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_emitent_category_value_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoEmitentcategoryvalueBody**](InfoEmitentcategoryvalueBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsDictionaryEmitentCategoryValueFields]**](EfirDataHubModelsModelsDictionaryEmitentCategoryValueFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_emitent_classification_post**
> list[EfirDataHubModelsModelsInfoEmitentClassificationFields] v2_info_emitent_classification_post(body=body)

Получить классификацию эмитентов.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoEmitentClassificationBody() # InfoEmitentClassificationBody |  (optional)

try:
    # Получить классификацию эмитентов.
    api_response = api_instance.v2_info_emitent_classification_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_emitent_classification_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoEmitentClassificationBody**](InfoEmitentClassificationBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoEmitentClassificationFields]**](EfirDataHubModelsModelsInfoEmitentClassificationFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_emitent_docs_post**
> list[EfirDataHubModelsModelsInfoEmitentDocsFields] v2_info_emitent_docs_post(body=body)

Получить информационные материалы по эмитентам

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoEmitentDocsBody() # InfoEmitentDocsBody |  (optional)

try:
    # Получить информационные материалы по эмитентам
    api_response = api_instance.v2_info_emitent_docs_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_emitent_docs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoEmitentDocsBody**](InfoEmitentDocsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoEmitentDocsFields]**](EfirDataHubModelsModelsInfoEmitentDocsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_emitents_ext_post**
> list[EfirDataHubModelsModelsInfoEmitentsExtFields] v2_info_emitents_ext_post(body=body)

Получить расширенный справочник по эмитентам.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoEmitentsExtBody() # InfoEmitentsExtBody |  (optional)

try:
    # Получить расширенный справочник по эмитентам.
    api_response = api_instance.v2_info_emitents_ext_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_emitents_ext_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoEmitentsExtBody**](InfoEmitentsExtBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoEmitentsExtFields]**](EfirDataHubModelsModelsInfoEmitentsExtFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_emitents_id_post**
> EfirDataHubModelsModelsInfoEmitentsFields v2_info_emitents_id_post(id)

Получить краткий справочник по эмитентам.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Получить краткий справочник по эмитентам.
    api_response = api_instance.v2_info_emitents_id_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_emitents_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**EfirDataHubModelsModelsInfoEmitentsFields**](EfirDataHubModelsModelsInfoEmitentsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_emitents_post**
> list[EfirDataHubModelsModelsInfoEmitentsFields] v2_info_emitents_post(body=body)

Получить краткий справочник по эмитентам.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoEmitentsBody() # InfoEmitentsBody |  (optional)

try:
    # Получить краткий справочник по эмитентам.
    api_response = api_instance.v2_info_emitents_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_emitents_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoEmitentsBody**](InfoEmitentsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoEmitentsFields]**](EfirDataHubModelsModelsInfoEmitentsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_enum_values_post**
> list[EfirDataHubModelsModelsInfoEnumValuesFields] v2_info_enum_values_post(body=body)

Списки значений выходных полей с перечислениями в методах Securities и FintoolReferenceData.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoEnumValuesBody() # InfoEnumValuesBody |  (optional)

try:
    # Списки значений выходных полей с перечислениями в методах Securities и FintoolReferenceData.
    api_response = api_instance.v2_info_enum_values_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_enum_values_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoEnumValuesBody**](InfoEnumValuesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoEnumValuesFields]**](EfirDataHubModelsModelsInfoEnumValuesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_enums_post**
> list[EfirDataHubModelsModelsInfoEnumsFields] v2_info_enums_post(body=body)

Списки выходных полей с перечислениями в методах Securities и FintoolReferenceData.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoEnumsBody() # InfoEnumsBody |  (optional)

try:
    # Списки выходных полей с перечислениями в методах Securities и FintoolReferenceData.
    api_response = api_instance.v2_info_enums_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_enums_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoEnumsBody**](InfoEnumsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoEnumsFields]**](EfirDataHubModelsModelsInfoEnumsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_exchange_tree_post**
> list[EfirDataHubModelsModelsInfoExchangeTreeFields] v2_info_exchange_tree_post(body=body)

Получить иерархию торговых площадок/источников, используемых Интерфакс.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoExchangeTreeBody() # InfoExchangeTreeBody |  (optional)

try:
    # Получить иерархию торговых площадок/источников, используемых Интерфакс.
    api_response = api_instance.v2_info_exchange_tree_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_exchange_tree_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoExchangeTreeBody**](InfoExchangeTreeBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoExchangeTreeFields]**](EfirDataHubModelsModelsInfoExchangeTreeFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_fields_post**
> list[EfirDataHubModelsModelsInfoFieldsFields] v2_info_fields_post(body=body)

Получить справочник по полям данных для торговых инструментов.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoFieldsBody() # InfoFieldsBody |  (optional)

try:
    # Получить справочник по полям данных для торговых инструментов.
    api_response = api_instance.v2_info_fields_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_fields_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoFieldsBody**](InfoFieldsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoFieldsFields]**](EfirDataHubModelsModelsInfoFieldsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_fintool_category_value_post**
> list[EfirDataHubModelsModelsDictionaryFintoolCategoryValueFields] v2_info_fintool_category_value_post(body=body)

Метод для получения инструментов и их категорий

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoFintoolcategoryvalueBody() # InfoFintoolcategoryvalueBody |  (optional)

try:
    # Метод для получения инструментов и их категорий
    api_response = api_instance.v2_info_fintool_category_value_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_fintool_category_value_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoFintoolcategoryvalueBody**](InfoFintoolcategoryvalueBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsDictionaryFintoolCategoryValueFields]**](EfirDataHubModelsModelsDictionaryFintoolCategoryValueFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_fintool_classification_post**
> list[EfirDataHubModelsModelsInfoFintoolClassificationFields] v2_info_fintool_classification_post(body=body)

Получить классификацию инструментов.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoFintoolClassificationBody() # InfoFintoolClassificationBody |  (optional)

try:
    # Получить классификацию инструментов.
    api_response = api_instance.v2_info_fintool_classification_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_fintool_classification_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoFintoolClassificationBody**](InfoFintoolClassificationBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoFintoolClassificationFields]**](EfirDataHubModelsModelsInfoFintoolClassificationFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_fintool_convertation_post**
> list[EfirDataHubModelsModelsInfoFintoolConvertationFields] v2_info_fintool_convertation_post(body=body)

Получить данные по конвертациям инструментов (кроме облигаций) в другие инструменты.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoFintoolConvertationBody() # InfoFintoolConvertationBody |  (optional)

try:
    # Получить данные по конвертациям инструментов (кроме облигаций) в другие инструменты.
    api_response = api_instance.v2_info_fintool_convertation_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_fintool_convertation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoFintoolConvertationBody**](InfoFintoolConvertationBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoFintoolConvertationFields]**](EfirDataHubModelsModelsInfoFintoolConvertationFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_fintool_fields_ext_post**
> list[EfirDataHubModelsModelsInfoFintoolFieldsExtFields] v2_info_fintool_fields_ext_post(body=body)

Получить справочник по полям данных для финансовых инструментов (метод служебный, только для внутреннего использования).

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoFintoolFieldsExtBody() # InfoFintoolFieldsExtBody |  (optional)

try:
    # Получить справочник по полям данных для финансовых инструментов (метод служебный, только для внутреннего использования).
    api_response = api_instance.v2_info_fintool_fields_ext_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_fintool_fields_ext_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoFintoolFieldsExtBody**](InfoFintoolFieldsExtBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoFintoolFieldsExtFields]**](EfirDataHubModelsModelsInfoFintoolFieldsExtFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_fintool_fields_post**
> list[EfirDataHubModelsModelsInfoFintoolFieldsFields] v2_info_fintool_fields_post(body=body)

Получить справочник по полям данных для финансовых инструментов.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoFintoolFieldsBody() # InfoFintoolFieldsBody |  (optional)

try:
    # Получить справочник по полям данных для финансовых инструментов.
    api_response = api_instance.v2_info_fintool_fields_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_fintool_fields_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoFintoolFieldsBody**](InfoFintoolFieldsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoFintoolFieldsFields]**](EfirDataHubModelsModelsInfoFintoolFieldsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_fintool_listing_post**
> list[EfirDataHubModelsModelsInfoFintoolListingFields] v2_info_fintool_listing_post(body=body)

Уровень листинга и суммарные объемы торгов (метод служебный, только для внутреннего использования).

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoFintoolListingBody() # InfoFintoolListingBody |  (optional)

try:
    # Уровень листинга и суммарные объемы торгов (метод служебный, только для внутреннего использования).
    api_response = api_instance.v2_info_fintool_listing_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_fintool_listing_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoFintoolListingBody**](InfoFintoolListingBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoFintoolListingFields]**](EfirDataHubModelsModelsInfoFintoolListingFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_fintool_ref_data_list_post**
> list[EfirDataHubModelsModelsInfoFintoolReferenceDataFields] v2_info_fintool_ref_data_list_post(body=body)

Get fintool reference data

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.FintoolRefDataListBody() # FintoolRefDataListBody |  (optional)

try:
    # Get fintool reference data
    api_response = api_instance.v2_info_fintool_ref_data_list_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_fintool_ref_data_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FintoolRefDataListBody**](FintoolRefDataListBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoFintoolReferenceDataFields]**](EfirDataHubModelsModelsInfoFintoolReferenceDataFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_fintool_reference_data_id_post**
> EfirDataHubModelsModelsInfoFintoolReferenceDataFields v2_info_fintool_reference_data_id_post(id, body=body)

Получить расширенный справочник по финансовому инструменту.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
id = 789 # int | Идентификатор финансового инструмента в базе Интерфакс
body = swagger_client.FintoolReferenceDataIdBody() # FintoolReferenceDataIdBody | Параметры запроса (optional)

try:
    # Получить расширенный справочник по финансовому инструменту.
    api_response = api_instance.v2_info_fintool_reference_data_id_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_fintool_reference_data_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Идентификатор финансового инструмента в базе Интерфакс | 
 **body** | [**FintoolReferenceDataIdBody**](FintoolReferenceDataIdBody.md)| Параметры запроса | [optional] 

### Return type

[**EfirDataHubModelsModelsInfoFintoolReferenceDataFields**](EfirDataHubModelsModelsInfoFintoolReferenceDataFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_fintool_reference_data_post**
> list[EfirDataHubModelsModelsInfoFintoolReferenceDataFields] v2_info_fintool_reference_data_post(body=body)

Получить расширенный справочник по финансовым инструментам.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoFintoolReferenceDataBody() # InfoFintoolReferenceDataBody |  (optional)

try:
    # Получить расширенный справочник по финансовым инструментам.
    api_response = api_instance.v2_info_fintool_reference_data_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_fintool_reference_data_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoFintoolReferenceDataBody**](InfoFintoolReferenceDataBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoFintoolReferenceDataFields]**](EfirDataHubModelsModelsInfoFintoolReferenceDataFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_holidays_post**
> list[EfirDataHubModelsModelsInfoHolidaysFields] v2_info_holidays_post(body=body)

Возвращает даты неторговых дней

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoHolidaysBody() # InfoHolidaysBody |  (optional)

try:
    # Возвращает даты неторговых дней
    api_response = api_instance.v2_info_holidays_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_holidays_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoHolidaysBody**](InfoHolidaysBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoHolidaysFields]**](EfirDataHubModelsModelsInfoHolidaysFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_ifx_fintool_ref_data_post**
> list[EfirDataHubModelsModelsInfoIFXFintoolRefDataFields] v2_info_ifx_fintool_ref_data_post(body=body)

Получить справочник Интерфакс по финансовым инструментам.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoIFXFintoolRefDataBody() # InfoIFXFintoolRefDataBody |  (optional)

try:
    # Получить справочник Интерфакс по финансовым инструментам.
    api_response = api_instance.v2_info_ifx_fintool_ref_data_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_ifx_fintool_ref_data_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoIFXFintoolRefDataBody**](InfoIFXFintoolRefDataBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoIFXFintoolRefDataFields]**](EfirDataHubModelsModelsInfoIFXFintoolRefDataFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_instruments_post**
> list[EfirDataHubModelsModelsInfoInstrumentsFields] v2_info_instruments_post(body=body)

Получить краткий справочник по торговым инструментам.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoInstrumentsBody() # InfoInstrumentsBody |  (optional)

try:
    # Получить краткий справочник по торговым инструментам.
    api_response = api_instance.v2_info_instruments_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_instruments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoInstrumentsBody**](InfoInstrumentsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoInstrumentsFields]**](EfirDataHubModelsModelsInfoInstrumentsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_list_org_roles_post**
> list[EfirDataHubModelsModelsInfoListOrgRolesFields] v2_info_list_org_roles_post(body=body)

Получить справочник ролей организаций

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoListOrgRolesBody() # InfoListOrgRolesBody |  (optional)

try:
    # Получить справочник ролей организаций
    api_response = api_instance.v2_info_list_org_roles_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_list_org_roles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoListOrgRolesBody**](InfoListOrgRolesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoListOrgRolesFields]**](EfirDataHubModelsModelsInfoListOrgRolesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_money_flow_post**
> EfirDataHubModelsModelsInfoMoneyFlowResponse v2_info_money_flow_post(body=body)

Поток платежей по ценной бумаге в валюте номинала.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoMoneyFlowBody() # InfoMoneyFlowBody |  (optional)

try:
    # Поток платежей по ценной бумаге в валюте номинала.
    api_response = api_instance.v2_info_money_flow_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_money_flow_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoMoneyFlowBody**](InfoMoneyFlowBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsInfoMoneyFlowResponse**](EfirDataHubModelsModelsInfoMoneyFlowResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_organizers_by_fininst_id_post**
> list[EfirDataHubModelsModelsInfoOrganizersByFininstIdFields] v2_info_organizers_by_fininst_id_post(body=body)

Получить роли организаторов выпуска по списку FininstId

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoOrganizersByFininstIdBody() # InfoOrganizersByFininstIdBody |  (optional)

try:
    # Получить роли организаторов выпуска по списку FininstId
    api_response = api_instance.v2_info_organizers_by_fininst_id_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_organizers_by_fininst_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoOrganizersByFininstIdBody**](InfoOrganizersByFininstIdBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoOrganizersByFininstIdFields]**](EfirDataHubModelsModelsInfoOrganizersByFininstIdFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_organizers_by_fintool_id_post**
> list[EfirDataHubModelsModelsInfoOrganizersFields] v2_info_organizers_by_fintool_id_post(body=body)

Получить роли организаторов выпуска по списку FintoolId

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoOrganizersByFintoolIdBody() # InfoOrganizersByFintoolIdBody |  (optional)

try:
    # Получить роли организаторов выпуска по списку FintoolId
    api_response = api_instance.v2_info_organizers_by_fintool_id_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_organizers_by_fintool_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoOrganizersByFintoolIdBody**](InfoOrganizersByFintoolIdBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoOrganizersFields]**](EfirDataHubModelsModelsInfoOrganizersFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_organizers_post**
> list[EfirDataHubModelsModelsInfoOrganizersFields] v2_info_organizers_post(body=body)

Получить роли организаторов выпуска

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoOrganizersBody() # InfoOrganizersBody |  (optional)

try:
    # Получить роли организаторов выпуска
    api_response = api_instance.v2_info_organizers_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_organizers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoOrganizersBody**](InfoOrganizersBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoOrganizersFields]**](EfirDataHubModelsModelsInfoOrganizersFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_prof_participants_post**
> list[EfirDataHubModelsModelsInfoProfParticipantsFields] v2_info_prof_participants_post(body=body)

Получить реквизиты профессиональных участников финансового рынка по версии ЦБ.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoProfParticipantsBody() # InfoProfParticipantsBody |  (optional)

try:
    # Получить реквизиты профессиональных участников финансового рынка по версии ЦБ.
    api_response = api_instance.v2_info_prof_participants_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_prof_participants_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoProfParticipantsBody**](InfoProfParticipantsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoProfParticipantsFields]**](EfirDataHubModelsModelsInfoProfParticipantsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_residual_face_value_post**
> EfirDataHubModelsModelsInfoResidualFaceValueResponse v2_info_residual_face_value_post(body=body)

Получить величину остаточного номинала на заданную дату.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoResidualFaceValueBody() # InfoResidualFaceValueBody |  (optional)

try:
    # Получить величину остаточного номинала на заданную дату.
    api_response = api_instance.v2_info_residual_face_value_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_residual_face_value_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoResidualFaceValueBody**](InfoResidualFaceValueBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsInfoResidualFaceValueResponse**](EfirDataHubModelsModelsInfoResidualFaceValueResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_securities_post**
> list[EfirDataHubModelsModelsInfoSecuritiesFields] v2_info_securities_post(body=body)

Получить краткий справочник по финансовым инструментам. Для акций метод возвращает только основные выпуски (по колонке SecurityKind).   Для получения данных по дополнительным выпускам необходимо использовать метод FintoolRefrenceData.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoSecuritiesBody() # InfoSecuritiesBody |  (optional)

try:
    # Получить краткий справочник по финансовым инструментам. Для акций метод возвращает только основные выпуски (по колонке SecurityKind).   Для получения данных по дополнительным выпускам необходимо использовать метод FintoolRefrenceData.
    api_response = api_instance.v2_info_securities_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_securities_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoSecuritiesBody**](InfoSecuritiesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoSecuritiesFields]**](EfirDataHubModelsModelsInfoSecuritiesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_share_dividend_id_post**
> list[EfirDataHubModelsModelsInfoShareDividendFields] v2_info_share_dividend_id_post(id, body=body)

Информация по дивидендам

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
id = 789 # int | Идентификатор финансового инструмента в базе Интерфакс
body = swagger_client.ShareDividendIdBody() # ShareDividendIdBody | Параметры запроса (optional)

try:
    # Информация по дивидендам
    api_response = api_instance.v2_info_share_dividend_id_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_share_dividend_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Идентификатор финансового инструмента в базе Интерфакс | 
 **body** | [**ShareDividendIdBody**](ShareDividendIdBody.md)| Параметры запроса | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoShareDividendFields]**](EfirDataHubModelsModelsInfoShareDividendFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_share_dividend_post**
> list[EfirDataHubModelsModelsInfoShareDividendFields] v2_info_share_dividend_post(body=body)

Информация по дивидендам

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoShareDividendBody() # InfoShareDividendBody |  (optional)

try:
    # Информация по дивидендам
    api_response = api_instance.v2_info_share_dividend_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_share_dividend_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoShareDividendBody**](InfoShareDividendBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoShareDividendFields]**](EfirDataHubModelsModelsInfoShareDividendFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_info_type_tree_post**
> list[EfirDataHubModelsModelsInfoTypeTreeFields] v2_info_type_tree_post(body=body)

Get information about tree of instrument types

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoTypeTreeBody() # InfoTypeTreeBody |  (optional)

try:
    # Get information about tree of instrument types
    api_response = api_instance.v2_info_type_tree_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->v2_info_type_tree_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoTypeTreeBody**](InfoTypeTreeBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoTypeTreeFields]**](EfirDataHubModelsModelsInfoTypeTreeFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

