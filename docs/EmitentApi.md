# swagger_client.EmitentApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_emitent_bankrupt_list_post**](EmitentApi.md#v2_emitent_bankrupt_list_post) | **POST** /v2/Emitent/BankruptList | Возвращает сведения о банкротстве запрашиваемой компании
[**v2_emitent_calendar_post**](EmitentApi.md#v2_emitent_calendar_post) | **POST** /v2/Emitent/Calendar | Календари событий эмитентов
[**v2_emitent_classification_post**](EmitentApi.md#v2_emitent_classification_post) | **POST** /v2/Emitent/Classification | Получить классификацию эмитентов.
[**v2_emitent_code_get**](EmitentApi.md#v2_emitent_code_get) | **GET** /v2/Emitent/{code} | Получить краткий справочник по эмитенту.
[**v2_emitent_code_msfo_report_list_get**](EmitentApi.md#v2_emitent_code_msfo_report_list_get) | **GET** /v2/Emitent/{code}/MSFOReportList | Список доступных отчетов по МСФО
[**v2_emitent_code_msfo_report_post**](EmitentApi.md#v2_emitent_code_msfo_report_post) | **POST** /v2/Emitent/{code}/MSFOReport | Отчет по МСФО
[**v2_emitent_code_rsbu_report_list_get**](EmitentApi.md#v2_emitent_code_rsbu_report_list_get) | **GET** /v2/Emitent/{code}/RSBUReportList | Список доступных отчетов по РСБУ
[**v2_emitent_code_rsbu_report_post**](EmitentApi.md#v2_emitent_code_rsbu_report_post) | **POST** /v2/Emitent/{code}/RSBUReport | Отчет по РСБУ
[**v2_emitent_companies_post**](EmitentApi.md#v2_emitent_companies_post) | **POST** /v2/Emitent/Companies | Список компаний, поддерживаемых в методах сервиса Emitent
[**v2_emitent_company_groups_by_inclusions_post**](EmitentApi.md#v2_emitent_company_groups_by_inclusions_post) | **POST** /v2/Emitent/CompanyGroupsByInclusions | Возвращает информацию о принадлежности компаний к группам компаний
[**v2_emitent_company_groups_members_post**](EmitentApi.md#v2_emitent_company_groups_members_post) | **POST** /v2/Emitent/CompanyGroupsMembers | Возвращает полные описания групп по ид групп
[**v2_emitent_company_traffic_light_scoring_post**](EmitentApi.md#v2_emitent_company_traffic_light_scoring_post) | **POST** /v2/Emitent/CompanyTrafficLightScoring | Возвращает показатели кредитной оценки эмитентов по шкале \&quot;светофора\&quot; (1-6), актуальные на заданную дату
[**v2_emitent_encumbrance_list_post**](EmitentApi.md#v2_emitent_encumbrance_list_post) | **POST** /v2/Emitent/EncumbranceList | Возвращает данные об обременениях имущества компаний
[**v2_emitent_find_code_get**](EmitentApi.md#v2_emitent_find_code_get) | **GET** /v2/Emitent/Find/{code} | Поиск эмитента по коду (fininstId, ИНН, ОГРН, shortname)
[**v2_emitent_find_post**](EmitentApi.md#v2_emitent_find_post) | **POST** /v2/Emitent/Find | Поиск эмитента по списку кодов (fininstId, ИНН, ОГРН, shortname)
[**v2_emitent_kmv_emitent_dates_post**](EmitentApi.md#v2_emitent_kmv_emitent_dates_post) | **POST** /v2/Emitent/KMVEmitentDates | Возвращает перечень дат, для которых есть значения KMV PD для указанных эмитентов
[**v2_emitent_kmv_emitents_get**](EmitentApi.md#v2_emitent_kmv_emitents_get) | **GET** /v2/Emitent/KMVEmitents | Возвращает перечень эмитентов, для которых когда-либо было рассчитано значение KMV PD
[**v2_emitent_kmvpd_post**](EmitentApi.md#v2_emitent_kmvpd_post) | **POST** /v2/Emitent/KMVPD | Возвращает значения PIT KMV PD для указанных эмитентов на дату.
[**v2_emitent_list_ext_post**](EmitentApi.md#v2_emitent_list_ext_post) | **POST** /v2/Emitent/ListExt | Получить расширенный справочник по эмитентам.
[**v2_emitent_list_post**](EmitentApi.md#v2_emitent_list_post) | **POST** /v2/Emitent/List | Получить краткий справочник по эмитентам.
[**v2_emitent_multipliers_list_get**](EmitentApi.md#v2_emitent_multipliers_list_get) | **GET** /v2/Emitent/MultipliersList | Справочные данные мультипликаторов
[**v2_emitent_multipliers_post**](EmitentApi.md#v2_emitent_multipliers_post) | **POST** /v2/Emitent/Multipliers | Данные мультипликаторов по российской компании за интересующий период
[**v2_emitent_multipliers_trade_statistics_post**](EmitentApi.md#v2_emitent_multipliers_trade_statistics_post) | **POST** /v2/Emitent/MultipliersTradeStatistics | Торговая статистика, участвовавшая в расчёте мультипликаторов за интересующий период
[**v2_emitent_pd_multipliers_post**](EmitentApi.md#v2_emitent_pd_multipliers_post) | **POST** /v2/Emitent/PDMultipliers | Возвращает прогнозные мультипликаторы для PD
[**v2_emitent_pit_coefficient_post**](EmitentApi.md#v2_emitent_pit_coefficient_post) | **POST** /v2/Emitent/PITCoefficient | Возвращает значение коэффициента коррекции скоринговой величины PD ( (probability of default)
[**v2_emitent_profile_post**](EmitentApi.md#v2_emitent_profile_post) | **POST** /v2/Emitent/Profile | Возвращает описание деятельности компании, планы и пр.
[**v2_emitent_scoring_coeff_weights_post**](EmitentApi.md#v2_emitent_scoring_coeff_weights_post) | **POST** /v2/Emitent/ScoringCoeffWeights | Возвращает веса для коэффициентов скоринговой модели раздельно по типам отчетности
[**v2_emitent_scoring_ext_fields_get**](EmitentApi.md#v2_emitent_scoring_ext_fields_get) | **GET** /v2/Emitent/ScoringExtFields | Возвращает описания полей которые возвращает метод /Emitent/ScoringExt
[**v2_emitent_scoring_ext_history_post**](EmitentApi.md#v2_emitent_scoring_ext_history_post) | **POST** /v2/Emitent/ScoringExtHistory | Возвращает историю расширенных скорингов для списка компаний
[**v2_emitent_scoring_ext_post**](EmitentApi.md#v2_emitent_scoring_ext_post) | **POST** /v2/Emitent/ScoringExt | Возвращает расширенные скоринговые значения по компании за период отчетности
[**v2_emitent_scoring_ext_stats_post**](EmitentApi.md#v2_emitent_scoring_ext_stats_post) | **POST** /v2/Emitent/ScoringExtStats | Возвращает статистики по расширенным скорингам
[**v2_emitent_scoring_history_post**](EmitentApi.md#v2_emitent_scoring_history_post) | **POST** /v2/Emitent/ScoringHistory | Возвращает историю скорингов для списка компаний
[**v2_emitent_scoring_post**](EmitentApi.md#v2_emitent_scoring_post) | **POST** /v2/Emitent/Scoring | Скоринг компаний
[**v2_emitent_scoring_scale_post**](EmitentApi.md#v2_emitent_scoring_scale_post) | **POST** /v2/Emitent/ScoringScale | Возвращает описание рейтинговой шкалы - глобальной или национальной
[**v2_emitent_scoring_sector_weights_post**](EmitentApi.md#v2_emitent_scoring_sector_weights_post) | **POST** /v2/Emitent/ScoringSectorWeights | Возвращает веса скоринговой модели для для групп секторов экономики
[**v2_emitent_scoring_slopes_post**](EmitentApi.md#v2_emitent_scoring_slopes_post) | **POST** /v2/Emitent/ScoringSlopes | Возвращает значение свободного члена регрессии для скоринговой модели по типу отчетности
[**v2_emitent_scoring_stats_post**](EmitentApi.md#v2_emitent_scoring_stats_post) | **POST** /v2/Emitent/ScoringStats | Возвращает статистики по скорингам
[**v2_emitent_scoring_transformants_post**](EmitentApi.md#v2_emitent_scoring_transformants_post) | **POST** /v2/Emitent/ScoringTransformants | Возвращает трансформанты для коэффициента скоринговой модели на дату

# **v2_emitent_bankrupt_list_post**
> list[EfirDataHubModelsModelsEmitentBankruptListFields] v2_emitent_bankrupt_list_post(body=body)

Возвращает сведения о банкротстве запрашиваемой компании

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentBankruptListBody() # EmitentBankruptListBody |  (optional)

try:
    # Возвращает сведения о банкротстве запрашиваемой компании
    api_response = api_instance.v2_emitent_bankrupt_list_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_bankrupt_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentBankruptListBody**](EmitentBankruptListBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentBankruptListFields]**](EfirDataHubModelsModelsEmitentBankruptListFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_calendar_post**
> list[EfirDataHubModelsModelsEmitentCalendarFields] v2_emitent_calendar_post(body=body)

Календари событий эмитентов

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentCalendarBody() # EmitentCalendarBody |  (optional)

try:
    # Календари событий эмитентов
    api_response = api_instance.v2_emitent_calendar_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_calendar_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentCalendarBody**](EmitentCalendarBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentCalendarFields]**](EfirDataHubModelsModelsEmitentCalendarFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_classification_post**
> list[EfirDataHubModelsModelsInfoEmitentClassificationFields] v2_emitent_classification_post(body=body)

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentClassificationBody() # EmitentClassificationBody |  (optional)

try:
    # Получить классификацию эмитентов.
    api_response = api_instance.v2_emitent_classification_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_classification_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentClassificationBody**](EmitentClassificationBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoEmitentClassificationFields]**](EfirDataHubModelsModelsInfoEmitentClassificationFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_code_get**
> EfirDataHubModelsModelsInfoEmitentsFields v2_emitent_code_get(code)

Получить краткий справочник по эмитенту.

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
code = 'code_example' # str | 

try:
    # Получить краткий справочник по эмитенту.
    api_response = api_instance.v2_emitent_code_get(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 

### Return type

[**EfirDataHubModelsModelsInfoEmitentsFields**](EfirDataHubModelsModelsInfoEmitentsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_code_msfo_report_list_get**
> list[EfirDataHubModelsModelsEmitentMsfoReportListFields] v2_emitent_code_msfo_report_list_get(code)

Список доступных отчетов по МСФО

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
code = 'code_example' # str | Один из идентификаторов компании: FininstId, ИНН, ОГРН

try:
    # Список доступных отчетов по МСФО
    api_response = api_instance.v2_emitent_code_msfo_report_list_get(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_code_msfo_report_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Один из идентификаторов компании: FininstId, ИНН, ОГРН | 

### Return type

[**list[EfirDataHubModelsModelsEmitentMsfoReportListFields]**](EfirDataHubModelsModelsEmitentMsfoReportListFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_code_msfo_report_post**
> list[EfirDataHubModelsModelsEmitentMsfoReportFields] v2_emitent_code_msfo_report_post(code, body=body)

Отчет по МСФО

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
code = 'code_example' # str | Один из идентификаторов компании: FininstId, ИНН, ОГРН
body = swagger_client.CodeMSFOReportBody() # CodeMSFOReportBody |  (optional)

try:
    # Отчет по МСФО
    api_response = api_instance.v2_emitent_code_msfo_report_post(code, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_code_msfo_report_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Один из идентификаторов компании: FininstId, ИНН, ОГРН | 
 **body** | [**CodeMSFOReportBody**](CodeMSFOReportBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentMsfoReportFields]**](EfirDataHubModelsModelsEmitentMsfoReportFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_code_rsbu_report_list_get**
> list[EfirDataHubModelsModelsEmitentRsbuReportListFields] v2_emitent_code_rsbu_report_list_get(code)

Список доступных отчетов по РСБУ

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
code = 'code_example' # str | Один из идентификаторов компании: FininstId, ИНН, ОГРН

try:
    # Список доступных отчетов по РСБУ
    api_response = api_instance.v2_emitent_code_rsbu_report_list_get(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_code_rsbu_report_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Один из идентификаторов компании: FininstId, ИНН, ОГРН | 

### Return type

[**list[EfirDataHubModelsModelsEmitentRsbuReportListFields]**](EfirDataHubModelsModelsEmitentRsbuReportListFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_code_rsbu_report_post**
> list[EfirDataHubModelsModelsEmitentRsbuReportFields] v2_emitent_code_rsbu_report_post(code, body=body)

Отчет по РСБУ

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
code = 'code_example' # str | Один из идентификаторов компании: FininstId, ИНН, ОГРН
body = swagger_client.CodeRSBUReportBody() # CodeRSBUReportBody |  (optional)

try:
    # Отчет по РСБУ
    api_response = api_instance.v2_emitent_code_rsbu_report_post(code, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_code_rsbu_report_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Один из идентификаторов компании: FininstId, ИНН, ОГРН | 
 **body** | [**CodeRSBUReportBody**](CodeRSBUReportBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentRsbuReportFields]**](EfirDataHubModelsModelsEmitentRsbuReportFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_companies_post**
> list[EfirDataHubModelsModelsEmitentCompaniesFields] v2_emitent_companies_post(body=body)

Список компаний, поддерживаемых в методах сервиса Emitent

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentCompaniesBody() # EmitentCompaniesBody |  (optional)

try:
    # Список компаний, поддерживаемых в методах сервиса Emitent
    api_response = api_instance.v2_emitent_companies_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_companies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentCompaniesBody**](EmitentCompaniesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentCompaniesFields]**](EfirDataHubModelsModelsEmitentCompaniesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_company_groups_by_inclusions_post**
> list[EfirDataHubModelsModelsEmitentCompanyGroupsByInclusionsFields] v2_emitent_company_groups_by_inclusions_post(body=body)

Возвращает информацию о принадлежности компаний к группам компаний

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentCompanyGroupsByInclusionsBody() # EmitentCompanyGroupsByInclusionsBody |  (optional)

try:
    # Возвращает информацию о принадлежности компаний к группам компаний
    api_response = api_instance.v2_emitent_company_groups_by_inclusions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_company_groups_by_inclusions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentCompanyGroupsByInclusionsBody**](EmitentCompanyGroupsByInclusionsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentCompanyGroupsByInclusionsFields]**](EfirDataHubModelsModelsEmitentCompanyGroupsByInclusionsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_company_groups_members_post**
> list[EfirDataHubModelsModelsEmitentCompanyGroupsMembersFields] v2_emitent_company_groups_members_post(body=body)

Возвращает полные описания групп по ид групп

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentCompanyGroupsMembersBody() # EmitentCompanyGroupsMembersBody |  (optional)

try:
    # Возвращает полные описания групп по ид групп
    api_response = api_instance.v2_emitent_company_groups_members_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_company_groups_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentCompanyGroupsMembersBody**](EmitentCompanyGroupsMembersBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentCompanyGroupsMembersFields]**](EfirDataHubModelsModelsEmitentCompanyGroupsMembersFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_company_traffic_light_scoring_post**
> list[EfirDataHubModelsModelsEmitentCompanyTrafficLightScoringFields] v2_emitent_company_traffic_light_scoring_post(body=body)

Возвращает показатели кредитной оценки эмитентов по шкале \"светофора\" (1-6), актуальные на заданную дату

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentCompanyTrafficLightScoringBody() # EmitentCompanyTrafficLightScoringBody |  (optional)

try:
    # Возвращает показатели кредитной оценки эмитентов по шкале \"светофора\" (1-6), актуальные на заданную дату
    api_response = api_instance.v2_emitent_company_traffic_light_scoring_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_company_traffic_light_scoring_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentCompanyTrafficLightScoringBody**](EmitentCompanyTrafficLightScoringBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentCompanyTrafficLightScoringFields]**](EfirDataHubModelsModelsEmitentCompanyTrafficLightScoringFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_encumbrance_list_post**
> list[EfirDataHubModelsModelsEmitentEncumbranceListFields] v2_emitent_encumbrance_list_post(body=body)

Возвращает данные об обременениях имущества компаний

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentEncumbranceListBody() # EmitentEncumbranceListBody |  (optional)

try:
    # Возвращает данные об обременениях имущества компаний
    api_response = api_instance.v2_emitent_encumbrance_list_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_encumbrance_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentEncumbranceListBody**](EmitentEncumbranceListBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentEncumbranceListFields]**](EfirDataHubModelsModelsEmitentEncumbranceListFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_find_code_get**
> EfirDataHubModelsModelsEmitentEmitentShortInfoFields v2_emitent_find_code_get(code)

Поиск эмитента по коду (fininstId, ИНН, ОГРН, shortname)

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
code = 'code_example' # str | 

try:
    # Поиск эмитента по коду (fininstId, ИНН, ОГРН, shortname)
    api_response = api_instance.v2_emitent_find_code_get(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_find_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 

### Return type

[**EfirDataHubModelsModelsEmitentEmitentShortInfoFields**](EfirDataHubModelsModelsEmitentEmitentShortInfoFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_find_post**
> list[EfirDataHubModelsModelsEmitentEmitentShortInfoFields] v2_emitent_find_post(body=body)

Поиск эмитента по списку кодов (fininstId, ИНН, ОГРН, shortname)

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentFindBody() # EmitentFindBody |  (optional)

try:
    # Поиск эмитента по списку кодов (fininstId, ИНН, ОГРН, shortname)
    api_response = api_instance.v2_emitent_find_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_find_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentFindBody**](EmitentFindBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentEmitentShortInfoFields]**](EfirDataHubModelsModelsEmitentEmitentShortInfoFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_kmv_emitent_dates_post**
> list[EfirDataHubModelsModelsEmitentKmvEmitentDatesFields] v2_emitent_kmv_emitent_dates_post(body=body)

Возвращает перечень дат, для которых есть значения KMV PD для указанных эмитентов

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentKMVEmitentDatesBody() # EmitentKMVEmitentDatesBody |  (optional)

try:
    # Возвращает перечень дат, для которых есть значения KMV PD для указанных эмитентов
    api_response = api_instance.v2_emitent_kmv_emitent_dates_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_kmv_emitent_dates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentKMVEmitentDatesBody**](EmitentKMVEmitentDatesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentKmvEmitentDatesFields]**](EfirDataHubModelsModelsEmitentKmvEmitentDatesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_kmv_emitents_get**
> list[int] v2_emitent_kmv_emitents_get()

Возвращает перечень эмитентов, для которых когда-либо было рассчитано значение KMV PD

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))

try:
    # Возвращает перечень эмитентов, для которых когда-либо было рассчитано значение KMV PD
    api_response = api_instance.v2_emitent_kmv_emitents_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_kmv_emitents_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[int]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_kmvpd_post**
> list[EfirDataHubModelsModelsEmitentKmvPdFields] v2_emitent_kmvpd_post(body=body)

Возвращает значения PIT KMV PD для указанных эмитентов на дату.

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentKMVPDBody() # EmitentKMVPDBody |  (optional)

try:
    # Возвращает значения PIT KMV PD для указанных эмитентов на дату.
    api_response = api_instance.v2_emitent_kmvpd_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_kmvpd_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentKMVPDBody**](EmitentKMVPDBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentKmvPdFields]**](EfirDataHubModelsModelsEmitentKmvPdFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_list_ext_post**
> list[EfirDataHubModelsModelsInfoEmitentsExtFields] v2_emitent_list_ext_post(body=body)

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentListExtBody() # EmitentListExtBody |  (optional)

try:
    # Получить расширенный справочник по эмитентам.
    api_response = api_instance.v2_emitent_list_ext_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_list_ext_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentListExtBody**](EmitentListExtBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoEmitentsExtFields]**](EfirDataHubModelsModelsInfoEmitentsExtFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_list_post**
> list[EfirDataHubModelsModelsInfoEmitentsFields] v2_emitent_list_post(body=body)

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentListBody() # EmitentListBody |  (optional)

try:
    # Получить краткий справочник по эмитентам.
    api_response = api_instance.v2_emitent_list_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentListBody**](EmitentListBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoEmitentsFields]**](EfirDataHubModelsModelsInfoEmitentsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_multipliers_list_get**
> list[EfirDataHubModelsModelsEmitentMultipliersListFields] v2_emitent_multipliers_list_get()

Справочные данные мультипликаторов

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))

try:
    # Справочные данные мультипликаторов
    api_response = api_instance.v2_emitent_multipliers_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_multipliers_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EfirDataHubModelsModelsEmitentMultipliersListFields]**](EfirDataHubModelsModelsEmitentMultipliersListFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_multipliers_post**
> list[EfirDataHubModelsModelsEmitentMultipliersFields] v2_emitent_multipliers_post(body=body)

Данные мультипликаторов по российской компании за интересующий период

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentMultipliersBody() # EmitentMultipliersBody |  (optional)

try:
    # Данные мультипликаторов по российской компании за интересующий период
    api_response = api_instance.v2_emitent_multipliers_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_multipliers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentMultipliersBody**](EmitentMultipliersBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentMultipliersFields]**](EfirDataHubModelsModelsEmitentMultipliersFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_multipliers_trade_statistics_post**
> list[EfirDataHubModelsModelsEmitentMultipliersTradeStatisticsFields] v2_emitent_multipliers_trade_statistics_post(body=body)

Торговая статистика, участвовавшая в расчёте мультипликаторов за интересующий период

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentMultipliersTradeStatisticsBody() # EmitentMultipliersTradeStatisticsBody |  (optional)

try:
    # Торговая статистика, участвовавшая в расчёте мультипликаторов за интересующий период
    api_response = api_instance.v2_emitent_multipliers_trade_statistics_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_multipliers_trade_statistics_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentMultipliersTradeStatisticsBody**](EmitentMultipliersTradeStatisticsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentMultipliersTradeStatisticsFields]**](EfirDataHubModelsModelsEmitentMultipliersTradeStatisticsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_pd_multipliers_post**
> list[EfirDataHubModelsModelsEmitentPDMultipliersFields] v2_emitent_pd_multipliers_post(body=body)

Возвращает прогнозные мультипликаторы для PD

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentPDMultipliersBody() # EmitentPDMultipliersBody |  (optional)

try:
    # Возвращает прогнозные мультипликаторы для PD
    api_response = api_instance.v2_emitent_pd_multipliers_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_pd_multipliers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentPDMultipliersBody**](EmitentPDMultipliersBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentPDMultipliersFields]**](EfirDataHubModelsModelsEmitentPDMultipliersFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_pit_coefficient_post**
> EfirDataHubModelsModelsEmitentPitCoefficientResponse v2_emitent_pit_coefficient_post(body=body)

Возвращает значение коэффициента коррекции скоринговой величины PD ( (probability of default)

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentPITCoefficientBody() # EmitentPITCoefficientBody |  (optional)

try:
    # Возвращает значение коэффициента коррекции скоринговой величины PD ( (probability of default)
    api_response = api_instance.v2_emitent_pit_coefficient_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_pit_coefficient_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentPITCoefficientBody**](EmitentPITCoefficientBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsEmitentPitCoefficientResponse**](EfirDataHubModelsModelsEmitentPitCoefficientResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_profile_post**
> list[EfirDataHubModelsModelsEmitentProfileFields] v2_emitent_profile_post(body=body)

Возвращает описание деятельности компании, планы и пр.

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentProfileBody() # EmitentProfileBody |  (optional)

try:
    # Возвращает описание деятельности компании, планы и пр.
    api_response = api_instance.v2_emitent_profile_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_profile_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentProfileBody**](EmitentProfileBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentProfileFields]**](EfirDataHubModelsModelsEmitentProfileFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_scoring_coeff_weights_post**
> list[EfirDataHubModelsModelsEmitentScoringCoeffWeightsFields] v2_emitent_scoring_coeff_weights_post(body=body)

Возвращает веса для коэффициентов скоринговой модели раздельно по типам отчетности

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentScoringCoeffWeightsBody() # EmitentScoringCoeffWeightsBody |  (optional)

try:
    # Возвращает веса для коэффициентов скоринговой модели раздельно по типам отчетности
    api_response = api_instance.v2_emitent_scoring_coeff_weights_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_scoring_coeff_weights_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentScoringCoeffWeightsBody**](EmitentScoringCoeffWeightsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentScoringCoeffWeightsFields]**](EfirDataHubModelsModelsEmitentScoringCoeffWeightsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_scoring_ext_fields_get**
> list[EfirDataHubModelsModelsEmitentScoringExtFieldsFields] v2_emitent_scoring_ext_fields_get()

Возвращает описания полей которые возвращает метод /Emitent/ScoringExt

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))

try:
    # Возвращает описания полей которые возвращает метод /Emitent/ScoringExt
    api_response = api_instance.v2_emitent_scoring_ext_fields_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_scoring_ext_fields_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EfirDataHubModelsModelsEmitentScoringExtFieldsFields]**](EfirDataHubModelsModelsEmitentScoringExtFieldsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_scoring_ext_history_post**
> list[EfirDataHubModelsModelsEmitentScoringExtHistoryFields] v2_emitent_scoring_ext_history_post(body=body)

Возвращает историю расширенных скорингов для списка компаний

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentScoringExtHistoryBody() # EmitentScoringExtHistoryBody |  (optional)

try:
    # Возвращает историю расширенных скорингов для списка компаний
    api_response = api_instance.v2_emitent_scoring_ext_history_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_scoring_ext_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentScoringExtHistoryBody**](EmitentScoringExtHistoryBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentScoringExtHistoryFields]**](EfirDataHubModelsModelsEmitentScoringExtHistoryFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_scoring_ext_post**
> list[EfirDataHubModelsModelsEmitentScoringExtFields] v2_emitent_scoring_ext_post(body=body)

Возвращает расширенные скоринговые значения по компании за период отчетности

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentScoringExtBody() # EmitentScoringExtBody |  (optional)

try:
    # Возвращает расширенные скоринговые значения по компании за период отчетности
    api_response = api_instance.v2_emitent_scoring_ext_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_scoring_ext_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentScoringExtBody**](EmitentScoringExtBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentScoringExtFields]**](EfirDataHubModelsModelsEmitentScoringExtFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_scoring_ext_stats_post**
> list[EfirDataHubModelsModelsEmitentScoringExtStatsFields] v2_emitent_scoring_ext_stats_post(body=body)

Возвращает статистики по расширенным скорингам

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentScoringExtStatsBody() # EmitentScoringExtStatsBody |  (optional)

try:
    # Возвращает статистики по расширенным скорингам
    api_response = api_instance.v2_emitent_scoring_ext_stats_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_scoring_ext_stats_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentScoringExtStatsBody**](EmitentScoringExtStatsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentScoringExtStatsFields]**](EfirDataHubModelsModelsEmitentScoringExtStatsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_scoring_history_post**
> list[EfirDataHubModelsModelsEmitentScoringHistoryFields] v2_emitent_scoring_history_post(body=body)

Возвращает историю скорингов для списка компаний

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentScoringHistoryBody() # EmitentScoringHistoryBody |  (optional)

try:
    # Возвращает историю скорингов для списка компаний
    api_response = api_instance.v2_emitent_scoring_history_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_scoring_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentScoringHistoryBody**](EmitentScoringHistoryBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentScoringHistoryFields]**](EfirDataHubModelsModelsEmitentScoringHistoryFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_scoring_post**
> list[EfirDataHubModelsModelsEmitentScoringFields] v2_emitent_scoring_post(body=body)

Скоринг компаний

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentScoringBody() # EmitentScoringBody |  (optional)

try:
    # Скоринг компаний
    api_response = api_instance.v2_emitent_scoring_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_scoring_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentScoringBody**](EmitentScoringBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentScoringFields]**](EfirDataHubModelsModelsEmitentScoringFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_scoring_scale_post**
> list[EfirDataHubModelsModelsEmitentScoringScaleFields] v2_emitent_scoring_scale_post(body=body)

Возвращает описание рейтинговой шкалы - глобальной или национальной

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentScoringScaleBody() # EmitentScoringScaleBody |  (optional)

try:
    # Возвращает описание рейтинговой шкалы - глобальной или национальной
    api_response = api_instance.v2_emitent_scoring_scale_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_scoring_scale_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentScoringScaleBody**](EmitentScoringScaleBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentScoringScaleFields]**](EfirDataHubModelsModelsEmitentScoringScaleFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_scoring_sector_weights_post**
> list[EfirDataHubModelsModelsEmitentScoringSectorWeightsFields] v2_emitent_scoring_sector_weights_post(body=body)

Возвращает веса скоринговой модели для для групп секторов экономики

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentScoringSectorWeightsBody() # EmitentScoringSectorWeightsBody |  (optional)

try:
    # Возвращает веса скоринговой модели для для групп секторов экономики
    api_response = api_instance.v2_emitent_scoring_sector_weights_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_scoring_sector_weights_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentScoringSectorWeightsBody**](EmitentScoringSectorWeightsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentScoringSectorWeightsFields]**](EfirDataHubModelsModelsEmitentScoringSectorWeightsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_scoring_slopes_post**
> EfirDataHubModelsModelsEmitentScoringSlopesResponse v2_emitent_scoring_slopes_post(body=body)

Возвращает значение свободного члена регрессии для скоринговой модели по типу отчетности

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentScoringSlopesBody() # EmitentScoringSlopesBody |  (optional)

try:
    # Возвращает значение свободного члена регрессии для скоринговой модели по типу отчетности
    api_response = api_instance.v2_emitent_scoring_slopes_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_scoring_slopes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentScoringSlopesBody**](EmitentScoringSlopesBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsEmitentScoringSlopesResponse**](EfirDataHubModelsModelsEmitentScoringSlopesResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_scoring_stats_post**
> list[EfirDataHubModelsModelsEmitentScoringStatsFields] v2_emitent_scoring_stats_post(body=body)

Возвращает статистики по скорингам

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentScoringStatsBody() # EmitentScoringStatsBody |  (optional)

try:
    # Возвращает статистики по скорингам
    api_response = api_instance.v2_emitent_scoring_stats_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_scoring_stats_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentScoringStatsBody**](EmitentScoringStatsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentScoringStatsFields]**](EfirDataHubModelsModelsEmitentScoringStatsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_emitent_scoring_transformants_post**
> EfirDataHubModelsModelsEmitentScoringTransformantsResponse v2_emitent_scoring_transformants_post(body=body)

Возвращает трансформанты для коэффициента скоринговой модели на дату

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
api_instance = swagger_client.EmitentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmitentScoringTransformantsBody() # EmitentScoringTransformantsBody |  (optional)

try:
    # Возвращает трансформанты для коэффициента скоринговой модели на дату
    api_response = api_instance.v2_emitent_scoring_transformants_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmitentApi->v2_emitent_scoring_transformants_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmitentScoringTransformantsBody**](EmitentScoringTransformantsBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsEmitentScoringTransformantsResponse**](EfirDataHubModelsModelsEmitentScoringTransformantsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

