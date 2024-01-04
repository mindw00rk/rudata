# swagger_client.ScoringApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_scoring_coeff_weights_post**](ScoringApi.md#v2_scoring_coeff_weights_post) | **POST** /v2/Scoring/CoeffWeights | Возвращает веса для коэффициентов скоринговой модели раздельно по типам отчетности
[**v2_scoring_company_main_owners_post**](ScoringApi.md#v2_scoring_company_main_owners_post) | **POST** /v2/Scoring/company-main-owners | Возвращает описание крупных акционеров компании
[**v2_scoring_company_owners_post**](ScoringApi.md#v2_scoring_company_owners_post) | **POST** /v2/Scoring/company-owners | Возвращает описание акционеров компании
[**v2_scoring_corrected_pd_post**](ScoringApi.md#v2_scoring_corrected_pd_post) | **POST** /v2/Scoring/corrected-pd | Возвращает скорректированный PD
[**v2_scoring_custom_report_scoring_msfo_ext_post**](ScoringApi.md#v2_scoring_custom_report_scoring_msfo_ext_post) | **POST** /v2/Scoring/CustomReportScoringMSFOExt | Возвращает расширенный скоринг по пользовательской отчётности типа МСФО
[**v2_scoring_custom_report_scoring_msfo_post**](ScoringApi.md#v2_scoring_custom_report_scoring_msfo_post) | **POST** /v2/Scoring/CustomReportScoringMSFO | Возвращает скоринг по пользовательской отчётности типа МСФО
[**v2_scoring_custom_report_scoring_rsbu_ext_post**](ScoringApi.md#v2_scoring_custom_report_scoring_rsbu_ext_post) | **POST** /v2/Scoring/CustomReportScoringRSBUExt | Возвращает расширенный скоринг по пользовательской отчётности типа РСБУ
[**v2_scoring_custom_report_scoring_rsbu_post**](ScoringApi.md#v2_scoring_custom_report_scoring_rsbu_post) | **POST** /v2/Scoring/CustomReportScoringRSBU | Возвращает скоринг по пользовательской отчётности типа РСБУ
[**v2_scoring_ext_fields_get**](ScoringApi.md#v2_scoring_ext_fields_get) | **GET** /v2/Scoring/ExtFields | Возвращает описания полей которые возвращает метод /Emitent/ScoringExt
[**v2_scoring_ext_history_post**](ScoringApi.md#v2_scoring_ext_history_post) | **POST** /v2/Scoring/ExtHistory | Возвращает историю расширенных скорингов для списка компаний
[**v2_scoring_ext_stats_post**](ScoringApi.md#v2_scoring_ext_stats_post) | **POST** /v2/Scoring/ExtStats | Возвращает статистики по расширенным скорингам
[**v2_scoring_history_post**](ScoringApi.md#v2_scoring_history_post) | **POST** /v2/Scoring/History | Возвращает историю скорингов для списка компаний
[**v2_scoring_rating_contribution_post**](ScoringApi.md#v2_scoring_rating_contribution_post) | **POST** /v2/Scoring/rating-contribution | Возвращает распределение долей владения по значениям рейтинга родительских компаний
[**v2_scoring_scale_post**](ScoringApi.md#v2_scoring_scale_post) | **POST** /v2/Scoring/Scale | Возвращает описание рейтинговой шкалы - глобальной или национальной
[**v2_scoring_scoring_ext_post**](ScoringApi.md#v2_scoring_scoring_ext_post) | **POST** /v2/Scoring/ScoringExt | Возвращает расширенные скоринговые значения по компании за период отчетности
[**v2_scoring_scoring_post**](ScoringApi.md#v2_scoring_scoring_post) | **POST** /v2/Scoring/Scoring | Скоринг компаний
[**v2_scoring_sector_weights_post**](ScoringApi.md#v2_scoring_sector_weights_post) | **POST** /v2/Scoring/SectorWeights | Возвращает веса скоринговой модели для для групп секторов экономики
[**v2_scoring_slopes_post**](ScoringApi.md#v2_scoring_slopes_post) | **POST** /v2/Scoring/Slopes | Возвращает значение свободного члена регрессии для скоринговой модели по типу отчетности
[**v2_scoring_stats_post**](ScoringApi.md#v2_scoring_stats_post) | **POST** /v2/Scoring/Stats | Возвращает статистики по скорингам
[**v2_scoring_transformants_post**](ScoringApi.md#v2_scoring_transformants_post) | **POST** /v2/Scoring/Transformants | Возвращает трансформанты для коэффициента скоринговой модели на дату

# **v2_scoring_coeff_weights_post**
> list[EfirDataHubModelsModelsEmitentScoringCoeffWeightsFields] v2_scoring_coeff_weights_post(body=body)

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
api_instance = swagger_client.ScoringApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScoringCoeffWeightsBody() # ScoringCoeffWeightsBody |  (optional)

try:
    # Возвращает веса для коэффициентов скоринговой модели раздельно по типам отчетности
    api_response = api_instance.v2_scoring_coeff_weights_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoringApi->v2_scoring_coeff_weights_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScoringCoeffWeightsBody**](ScoringCoeffWeightsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentScoringCoeffWeightsFields]**](EfirDataHubModelsModelsEmitentScoringCoeffWeightsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_scoring_company_main_owners_post**
> list[EfirDataHubModelsModelsScoringMainOwnerFields] v2_scoring_company_main_owners_post(body=body)

Возвращает описание крупных акционеров компании

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
api_instance = swagger_client.ScoringApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScoringCompanymainownersBody() # ScoringCompanymainownersBody |  (optional)

try:
    # Возвращает описание крупных акционеров компании
    api_response = api_instance.v2_scoring_company_main_owners_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoringApi->v2_scoring_company_main_owners_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScoringCompanymainownersBody**](ScoringCompanymainownersBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsScoringMainOwnerFields]**](EfirDataHubModelsModelsScoringMainOwnerFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_scoring_company_owners_post**
> list[EfirDataHubModelsModelsScoringOwnerFields] v2_scoring_company_owners_post(body=body)

Возвращает описание акционеров компании

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
api_instance = swagger_client.ScoringApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScoringCompanyownersBody() # ScoringCompanyownersBody |  (optional)

try:
    # Возвращает описание акционеров компании
    api_response = api_instance.v2_scoring_company_owners_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoringApi->v2_scoring_company_owners_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScoringCompanyownersBody**](ScoringCompanyownersBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsScoringOwnerFields]**](EfirDataHubModelsModelsScoringOwnerFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_scoring_corrected_pd_post**
> list[EfirDataHubModelsModelsScoringCompanyPDFields] v2_scoring_corrected_pd_post(body=body)

Возвращает скорректированный PD

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
api_instance = swagger_client.ScoringApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScoringCorrectedpdBody() # ScoringCorrectedpdBody |  (optional)

try:
    # Возвращает скорректированный PD
    api_response = api_instance.v2_scoring_corrected_pd_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoringApi->v2_scoring_corrected_pd_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScoringCorrectedpdBody**](ScoringCorrectedpdBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsScoringCompanyPDFields]**](EfirDataHubModelsModelsScoringCompanyPDFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_scoring_custom_report_scoring_msfo_ext_post**
> EfirDataHubModelsModelsEmitentScoringExtFields v2_scoring_custom_report_scoring_msfo_ext_post(body=body)

Возвращает расширенный скоринг по пользовательской отчётности типа МСФО

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
api_instance = swagger_client.ScoringApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScoringCustomReportScoringMSFOExtBody() # ScoringCustomReportScoringMSFOExtBody |  (optional)

try:
    # Возвращает расширенный скоринг по пользовательской отчётности типа МСФО
    api_response = api_instance.v2_scoring_custom_report_scoring_msfo_ext_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoringApi->v2_scoring_custom_report_scoring_msfo_ext_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScoringCustomReportScoringMSFOExtBody**](ScoringCustomReportScoringMSFOExtBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsEmitentScoringExtFields**](EfirDataHubModelsModelsEmitentScoringExtFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_scoring_custom_report_scoring_msfo_post**
> EfirDataHubModelsModelsEmitentScoringFields v2_scoring_custom_report_scoring_msfo_post(body=body)

Возвращает скоринг по пользовательской отчётности типа МСФО

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
api_instance = swagger_client.ScoringApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScoringCustomReportScoringMSFOBody() # ScoringCustomReportScoringMSFOBody |  (optional)

try:
    # Возвращает скоринг по пользовательской отчётности типа МСФО
    api_response = api_instance.v2_scoring_custom_report_scoring_msfo_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoringApi->v2_scoring_custom_report_scoring_msfo_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScoringCustomReportScoringMSFOBody**](ScoringCustomReportScoringMSFOBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsEmitentScoringFields**](EfirDataHubModelsModelsEmitentScoringFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_scoring_custom_report_scoring_rsbu_ext_post**
> EfirDataHubModelsModelsEmitentScoringExtFields v2_scoring_custom_report_scoring_rsbu_ext_post(body=body)

Возвращает расширенный скоринг по пользовательской отчётности типа РСБУ

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
api_instance = swagger_client.ScoringApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScoringCustomReportScoringRSBUExtBody() # ScoringCustomReportScoringRSBUExtBody |  (optional)

try:
    # Возвращает расширенный скоринг по пользовательской отчётности типа РСБУ
    api_response = api_instance.v2_scoring_custom_report_scoring_rsbu_ext_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoringApi->v2_scoring_custom_report_scoring_rsbu_ext_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScoringCustomReportScoringRSBUExtBody**](ScoringCustomReportScoringRSBUExtBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsEmitentScoringExtFields**](EfirDataHubModelsModelsEmitentScoringExtFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_scoring_custom_report_scoring_rsbu_post**
> EfirDataHubModelsModelsEmitentScoringFields v2_scoring_custom_report_scoring_rsbu_post(body=body)

Возвращает скоринг по пользовательской отчётности типа РСБУ

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
api_instance = swagger_client.ScoringApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScoringCustomReportScoringRSBUBody() # ScoringCustomReportScoringRSBUBody |  (optional)

try:
    # Возвращает скоринг по пользовательской отчётности типа РСБУ
    api_response = api_instance.v2_scoring_custom_report_scoring_rsbu_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoringApi->v2_scoring_custom_report_scoring_rsbu_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScoringCustomReportScoringRSBUBody**](ScoringCustomReportScoringRSBUBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsEmitentScoringFields**](EfirDataHubModelsModelsEmitentScoringFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_scoring_ext_fields_get**
> list[EfirDataHubModelsModelsEmitentScoringExtFieldsFields] v2_scoring_ext_fields_get()

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
api_instance = swagger_client.ScoringApi(swagger_client.ApiClient(configuration))

try:
    # Возвращает описания полей которые возвращает метод /Emitent/ScoringExt
    api_response = api_instance.v2_scoring_ext_fields_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoringApi->v2_scoring_ext_fields_get: %s\n" % e)
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

# **v2_scoring_ext_history_post**
> list[EfirDataHubModelsModelsEmitentScoringExtHistoryFields] v2_scoring_ext_history_post(body=body)

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
api_instance = swagger_client.ScoringApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScoringExtHistoryBody() # ScoringExtHistoryBody |  (optional)

try:
    # Возвращает историю расширенных скорингов для списка компаний
    api_response = api_instance.v2_scoring_ext_history_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoringApi->v2_scoring_ext_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScoringExtHistoryBody**](ScoringExtHistoryBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentScoringExtHistoryFields]**](EfirDataHubModelsModelsEmitentScoringExtHistoryFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_scoring_ext_stats_post**
> list[EfirDataHubModelsModelsEmitentScoringExtStatsFields] v2_scoring_ext_stats_post(body=body)

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
api_instance = swagger_client.ScoringApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScoringExtStatsBody() # ScoringExtStatsBody |  (optional)

try:
    # Возвращает статистики по расширенным скорингам
    api_response = api_instance.v2_scoring_ext_stats_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoringApi->v2_scoring_ext_stats_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScoringExtStatsBody**](ScoringExtStatsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentScoringExtStatsFields]**](EfirDataHubModelsModelsEmitentScoringExtStatsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_scoring_history_post**
> list[EfirDataHubModelsModelsEmitentScoringHistoryFields] v2_scoring_history_post(body=body)

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
api_instance = swagger_client.ScoringApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScoringHistoryBody() # ScoringHistoryBody |  (optional)

try:
    # Возвращает историю скорингов для списка компаний
    api_response = api_instance.v2_scoring_history_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoringApi->v2_scoring_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScoringHistoryBody**](ScoringHistoryBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentScoringHistoryFields]**](EfirDataHubModelsModelsEmitentScoringHistoryFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_scoring_rating_contribution_post**
> list[EfirDataHubModelsModelsScoringRatingContribution] v2_scoring_rating_contribution_post(body=body)

Возвращает распределение долей владения по значениям рейтинга родительских компаний

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
api_instance = swagger_client.ScoringApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScoringRatingcontributionBody() # ScoringRatingcontributionBody |  (optional)

try:
    # Возвращает распределение долей владения по значениям рейтинга родительских компаний
    api_response = api_instance.v2_scoring_rating_contribution_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoringApi->v2_scoring_rating_contribution_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScoringRatingcontributionBody**](ScoringRatingcontributionBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsScoringRatingContribution]**](EfirDataHubModelsModelsScoringRatingContribution.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_scoring_scale_post**
> list[EfirDataHubModelsModelsEmitentScoringScaleFields] v2_scoring_scale_post(body=body)

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
api_instance = swagger_client.ScoringApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScoringScaleBody() # ScoringScaleBody |  (optional)

try:
    # Возвращает описание рейтинговой шкалы - глобальной или национальной
    api_response = api_instance.v2_scoring_scale_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoringApi->v2_scoring_scale_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScoringScaleBody**](ScoringScaleBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentScoringScaleFields]**](EfirDataHubModelsModelsEmitentScoringScaleFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_scoring_scoring_ext_post**
> list[EfirDataHubModelsModelsEmitentScoringExtFields] v2_scoring_scoring_ext_post(body=body)

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
api_instance = swagger_client.ScoringApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScoringScoringExtBody() # ScoringScoringExtBody |  (optional)

try:
    # Возвращает расширенные скоринговые значения по компании за период отчетности
    api_response = api_instance.v2_scoring_scoring_ext_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoringApi->v2_scoring_scoring_ext_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScoringScoringExtBody**](ScoringScoringExtBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentScoringExtFields]**](EfirDataHubModelsModelsEmitentScoringExtFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_scoring_scoring_post**
> list[EfirDataHubModelsModelsEmitentScoringFields] v2_scoring_scoring_post(body=body)

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
api_instance = swagger_client.ScoringApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScoringScoringBody() # ScoringScoringBody |  (optional)

try:
    # Скоринг компаний
    api_response = api_instance.v2_scoring_scoring_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoringApi->v2_scoring_scoring_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScoringScoringBody**](ScoringScoringBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentScoringFields]**](EfirDataHubModelsModelsEmitentScoringFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_scoring_sector_weights_post**
> list[EfirDataHubModelsModelsEmitentScoringSectorWeightsFields] v2_scoring_sector_weights_post(body=body)

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
api_instance = swagger_client.ScoringApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScoringSectorWeightsBody() # ScoringSectorWeightsBody |  (optional)

try:
    # Возвращает веса скоринговой модели для для групп секторов экономики
    api_response = api_instance.v2_scoring_sector_weights_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoringApi->v2_scoring_sector_weights_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScoringSectorWeightsBody**](ScoringSectorWeightsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentScoringSectorWeightsFields]**](EfirDataHubModelsModelsEmitentScoringSectorWeightsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_scoring_slopes_post**
> EfirDataHubModelsModelsEmitentScoringSlopesResponse v2_scoring_slopes_post(body=body)

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
api_instance = swagger_client.ScoringApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScoringSlopesBody() # ScoringSlopesBody |  (optional)

try:
    # Возвращает значение свободного члена регрессии для скоринговой модели по типу отчетности
    api_response = api_instance.v2_scoring_slopes_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoringApi->v2_scoring_slopes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScoringSlopesBody**](ScoringSlopesBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsEmitentScoringSlopesResponse**](EfirDataHubModelsModelsEmitentScoringSlopesResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_scoring_stats_post**
> list[EfirDataHubModelsModelsEmitentScoringStatsFields] v2_scoring_stats_post(body=body)

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
api_instance = swagger_client.ScoringApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScoringStatsBody() # ScoringStatsBody |  (optional)

try:
    # Возвращает статистики по скорингам
    api_response = api_instance.v2_scoring_stats_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoringApi->v2_scoring_stats_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScoringStatsBody**](ScoringStatsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentScoringStatsFields]**](EfirDataHubModelsModelsEmitentScoringStatsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_scoring_transformants_post**
> EfirDataHubModelsModelsEmitentScoringTransformantsResponse v2_scoring_transformants_post(body=body)

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
api_instance = swagger_client.ScoringApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScoringTransformantsBody() # ScoringTransformantsBody |  (optional)

try:
    # Возвращает трансформанты для коэффициента скоринговой модели на дату
    api_response = api_instance.v2_scoring_transformants_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoringApi->v2_scoring_transformants_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScoringTransformantsBody**](ScoringTransformantsBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsEmitentScoringTransformantsResponse**](EfirDataHubModelsModelsEmitentScoringTransformantsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

