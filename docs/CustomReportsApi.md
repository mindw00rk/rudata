# swagger_client.CustomReportsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_custom_reports_calculation_status_post**](CustomReportsApi.md#v2_custom_reports_calculation_status_post) | **POST** /v2/custom-reports/calculation-status | Возвращает статус расчета скоринга
[**v2_custom_reports_msfo_guid_delete**](CustomReportsApi.md#v2_custom_reports_msfo_guid_delete) | **DELETE** /v2/custom-reports/msfo/{guid} | Метод для удаления пользовательской МСФО отчётности
[**v2_custom_reports_msfo_put**](CustomReportsApi.md#v2_custom_reports_msfo_put) | **PUT** /v2/custom-reports/msfo | Метод для загрузки пользовательской отчётности формата МСФО
[**v2_custom_reports_msfo_report_list_post**](CustomReportsApi.md#v2_custom_reports_msfo_report_list_post) | **POST** /v2/custom-reports/msfo-report-list | Метод для выгрузки пользовательских списков доступных отчетов по МСФО
[**v2_custom_reports_msfo_report_post**](CustomReportsApi.md#v2_custom_reports_msfo_report_post) | **POST** /v2/custom-reports/msfo-report | Метод для выгрузки пользовательской отчётности формата МСФО
[**v2_custom_reports_rsbu_guid_delete**](CustomReportsApi.md#v2_custom_reports_rsbu_guid_delete) | **DELETE** /v2/custom-reports/rsbu/{guid} | Метод для удаления пользовательской РСБУ отчётности
[**v2_custom_reports_rsbu_put**](CustomReportsApi.md#v2_custom_reports_rsbu_put) | **PUT** /v2/custom-reports/rsbu | Метод для загрузки пользовательской отчётности формата РСБУ
[**v2_custom_reports_rsbu_report_list_post**](CustomReportsApi.md#v2_custom_reports_rsbu_report_list_post) | **POST** /v2/custom-reports/rsbu-report-list | Метод для выгрузки пользовательских списков доступных отчетов по РСБУ
[**v2_custom_reports_rsbu_report_post**](CustomReportsApi.md#v2_custom_reports_rsbu_report_post) | **POST** /v2/custom-reports/rsbu-report | Метод для выгрузки пользовательской отчётности формата РСБУ
[**v2_custom_reports_scoring_calculate_put**](CustomReportsApi.md#v2_custom_reports_scoring_calculate_put) | **PUT** /v2/custom-reports/scoring-calculate | Добавляет запрос на расчет скоринга в очередь
[**v2_custom_reports_scoring_ext_post**](CustomReportsApi.md#v2_custom_reports_scoring_ext_post) | **POST** /v2/custom-reports/scoring-ext | Метод для запроса расширенного скоринга по пользовательской отчётности.
[**v2_custom_reports_scoring_post**](CustomReportsApi.md#v2_custom_reports_scoring_post) | **POST** /v2/custom-reports/scoring | Метод для запроса скоринга по пользовательской отчётности.

# **v2_custom_reports_calculation_status_post**
> list[EfirDataHubModelsModelsReportCustomReportStatusFields] v2_custom_reports_calculation_status_post(body=body)

Возвращает статус расчета скоринга

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
api_instance = swagger_client.CustomReportsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomreportsCalculationstatusBody() # CustomreportsCalculationstatusBody |  (optional)

try:
    # Возвращает статус расчета скоринга
    api_response = api_instance.v2_custom_reports_calculation_status_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomReportsApi->v2_custom_reports_calculation_status_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomreportsCalculationstatusBody**](CustomreportsCalculationstatusBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsReportCustomReportStatusFields]**](EfirDataHubModelsModelsReportCustomReportStatusFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_custom_reports_msfo_guid_delete**
> EfirDataHubModelsModelsReportCustomReportDeleteResponse v2_custom_reports_msfo_guid_delete(guid)

Метод для удаления пользовательской МСФО отчётности

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
api_instance = swagger_client.CustomReportsApi(swagger_client.ApiClient(configuration))
guid = 'guid_example' # str | guid отчета

try:
    # Метод для удаления пользовательской МСФО отчётности
    api_response = api_instance.v2_custom_reports_msfo_guid_delete(guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomReportsApi->v2_custom_reports_msfo_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| guid отчета | 

### Return type

[**EfirDataHubModelsModelsReportCustomReportDeleteResponse**](EfirDataHubModelsModelsReportCustomReportDeleteResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_custom_reports_msfo_put**
> EfirDataHubModelsModelsReportCustomReportUploadResponse v2_custom_reports_msfo_put(body=body)

Метод для загрузки пользовательской отчётности формата МСФО

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
api_instance = swagger_client.CustomReportsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomreportsMsfoBody() # CustomreportsMsfoBody |  (optional)

try:
    # Метод для загрузки пользовательской отчётности формата МСФО
    api_response = api_instance.v2_custom_reports_msfo_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomReportsApi->v2_custom_reports_msfo_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomreportsMsfoBody**](CustomreportsMsfoBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsReportCustomReportUploadResponse**](EfirDataHubModelsModelsReportCustomReportUploadResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_custom_reports_msfo_report_list_post**
> list[EfirDataHubModelsModelsReportCustomReportListFields] v2_custom_reports_msfo_report_list_post(body=body)

Метод для выгрузки пользовательских списков доступных отчетов по МСФО

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
api_instance = swagger_client.CustomReportsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomreportsMsforeportlistBody() # CustomreportsMsforeportlistBody |  (optional)

try:
    # Метод для выгрузки пользовательских списков доступных отчетов по МСФО
    api_response = api_instance.v2_custom_reports_msfo_report_list_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomReportsApi->v2_custom_reports_msfo_report_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomreportsMsforeportlistBody**](CustomreportsMsforeportlistBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsReportCustomReportListFields]**](EfirDataHubModelsModelsReportCustomReportListFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_custom_reports_msfo_report_post**
> EfirDataHubModelsModelsReportCustomMsfoReportFields v2_custom_reports_msfo_report_post(body=body)

Метод для выгрузки пользовательской отчётности формата МСФО

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
api_instance = swagger_client.CustomReportsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomreportsMsforeportBody() # CustomreportsMsforeportBody |  (optional)

try:
    # Метод для выгрузки пользовательской отчётности формата МСФО
    api_response = api_instance.v2_custom_reports_msfo_report_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomReportsApi->v2_custom_reports_msfo_report_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomreportsMsforeportBody**](CustomreportsMsforeportBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsReportCustomMsfoReportFields**](EfirDataHubModelsModelsReportCustomMsfoReportFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_custom_reports_rsbu_guid_delete**
> EfirDataHubModelsModelsReportCustomReportDeleteResponse v2_custom_reports_rsbu_guid_delete(guid)

Метод для удаления пользовательской РСБУ отчётности

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
api_instance = swagger_client.CustomReportsApi(swagger_client.ApiClient(configuration))
guid = 'guid_example' # str | guid отчета

try:
    # Метод для удаления пользовательской РСБУ отчётности
    api_response = api_instance.v2_custom_reports_rsbu_guid_delete(guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomReportsApi->v2_custom_reports_rsbu_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| guid отчета | 

### Return type

[**EfirDataHubModelsModelsReportCustomReportDeleteResponse**](EfirDataHubModelsModelsReportCustomReportDeleteResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_custom_reports_rsbu_put**
> EfirDataHubModelsModelsReportCustomReportUploadResponse v2_custom_reports_rsbu_put(body=body)

Метод для загрузки пользовательской отчётности формата РСБУ

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
api_instance = swagger_client.CustomReportsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomreportsRsbuBody() # CustomreportsRsbuBody |  (optional)

try:
    # Метод для загрузки пользовательской отчётности формата РСБУ
    api_response = api_instance.v2_custom_reports_rsbu_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomReportsApi->v2_custom_reports_rsbu_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomreportsRsbuBody**](CustomreportsRsbuBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsReportCustomReportUploadResponse**](EfirDataHubModelsModelsReportCustomReportUploadResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_custom_reports_rsbu_report_list_post**
> list[EfirDataHubModelsModelsReportCustomReportListFields] v2_custom_reports_rsbu_report_list_post(body=body)

Метод для выгрузки пользовательских списков доступных отчетов по РСБУ

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
api_instance = swagger_client.CustomReportsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomreportsRsbureportlistBody() # CustomreportsRsbureportlistBody |  (optional)

try:
    # Метод для выгрузки пользовательских списков доступных отчетов по РСБУ
    api_response = api_instance.v2_custom_reports_rsbu_report_list_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomReportsApi->v2_custom_reports_rsbu_report_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomreportsRsbureportlistBody**](CustomreportsRsbureportlistBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsReportCustomReportListFields]**](EfirDataHubModelsModelsReportCustomReportListFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_custom_reports_rsbu_report_post**
> EfirDataHubModelsModelsReportCustomRsbuReportFields v2_custom_reports_rsbu_report_post(body=body)

Метод для выгрузки пользовательской отчётности формата РСБУ

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
api_instance = swagger_client.CustomReportsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomreportsRsbureportBody() # CustomreportsRsbureportBody |  (optional)

try:
    # Метод для выгрузки пользовательской отчётности формата РСБУ
    api_response = api_instance.v2_custom_reports_rsbu_report_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomReportsApi->v2_custom_reports_rsbu_report_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomreportsRsbureportBody**](CustomreportsRsbureportBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsReportCustomRsbuReportFields**](EfirDataHubModelsModelsReportCustomRsbuReportFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_custom_reports_scoring_calculate_put**
> EfirDataHubModelsModelsReportCustomScoringCalculateResponse v2_custom_reports_scoring_calculate_put(body=body)

Добавляет запрос на расчет скоринга в очередь

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
api_instance = swagger_client.CustomReportsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomreportsScoringcalculateBody() # CustomreportsScoringcalculateBody |  (optional)

try:
    # Добавляет запрос на расчет скоринга в очередь
    api_response = api_instance.v2_custom_reports_scoring_calculate_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomReportsApi->v2_custom_reports_scoring_calculate_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomreportsScoringcalculateBody**](CustomreportsScoringcalculateBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsReportCustomScoringCalculateResponse**](EfirDataHubModelsModelsReportCustomScoringCalculateResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_custom_reports_scoring_ext_post**
> list[EfirDataHubModelsModelsCustomScoringCustomScoringExtFields] v2_custom_reports_scoring_ext_post(body=body)

Метод для запроса расширенного скоринга по пользовательской отчётности.

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
api_instance = swagger_client.CustomReportsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomreportsScoringextBody() # CustomreportsScoringextBody |  (optional)

try:
    # Метод для запроса расширенного скоринга по пользовательской отчётности.
    api_response = api_instance.v2_custom_reports_scoring_ext_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomReportsApi->v2_custom_reports_scoring_ext_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomreportsScoringextBody**](CustomreportsScoringextBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsCustomScoringCustomScoringExtFields]**](EfirDataHubModelsModelsCustomScoringCustomScoringExtFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_custom_reports_scoring_post**
> list[EfirDataHubModelsModelsCustomScoringCustomScoringFields] v2_custom_reports_scoring_post(body=body)

Метод для запроса скоринга по пользовательской отчётности.

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
api_instance = swagger_client.CustomReportsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomreportsScoringBody() # CustomreportsScoringBody |  (optional)

try:
    # Метод для запроса скоринга по пользовательской отчётности.
    api_response = api_instance.v2_custom_reports_scoring_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomReportsApi->v2_custom_reports_scoring_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomreportsScoringBody**](CustomreportsScoringBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsCustomScoringCustomScoringFields]**](EfirDataHubModelsModelsCustomScoringCustomScoringFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

