# swagger_client.ReportApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**report_cbrf_reports_file_post**](ReportApi.md#report_cbrf_reports_file_post) | **POST** /Report/cbrf-reports/file | Метод для выдачи ссылки на скачивание файла отчётности ЦБ РФ нового формата
[**report_cbrf_reports_list_get**](ReportApi.md#report_cbrf_reports_list_get) | **GET** /Report/cbrf-reports/list | Метод для выдачи списка доступных к скачиванию файлов отчётности ЦБ РФ нового формата
[**report_user_reports_file_post**](ReportApi.md#report_user_reports_file_post) | **POST** /Report/UserReports/File | Позволяет получить файл отчета по имени и типу
[**report_user_reports_list_post**](ReportApi.md#report_user_reports_list_post) | **POST** /Report/UserReports/List | Возвращает список файлов указанного типа отчетов. Напр.: EndOfDay

# **report_cbrf_reports_file_post**
> report_cbrf_reports_file_post(body=body)

Метод для выдачи ссылки на скачивание файла отчётности ЦБ РФ нового формата

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
api_instance = swagger_client.ReportApi(swagger_client.ApiClient(configuration))
body = swagger_client.CbrfreportsFileBody() # CbrfreportsFileBody |  (optional)

try:
    # Метод для выдачи ссылки на скачивание файла отчётности ЦБ РФ нового формата
    api_instance.report_cbrf_reports_file_post(body=body)
except ApiException as e:
    print("Exception when calling ReportApi->report_cbrf_reports_file_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CbrfreportsFileBody**](CbrfreportsFileBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_cbrf_reports_list_get**
> list[EfirDataHubModelsModelsReportListFields] report_cbrf_reports_list_get()

Метод для выдачи списка доступных к скачиванию файлов отчётности ЦБ РФ нового формата

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
api_instance = swagger_client.ReportApi(swagger_client.ApiClient(configuration))

try:
    # Метод для выдачи списка доступных к скачиванию файлов отчётности ЦБ РФ нового формата
    api_response = api_instance.report_cbrf_reports_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportApi->report_cbrf_reports_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EfirDataHubModelsModelsReportListFields]**](EfirDataHubModelsModelsReportListFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_user_reports_file_post**
> report_user_reports_file_post(body=body)

Позволяет получить файл отчета по имени и типу

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
api_instance = swagger_client.ReportApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserReportsFileBody() # UserReportsFileBody |  (optional)

try:
    # Позволяет получить файл отчета по имени и типу
    api_instance.report_user_reports_file_post(body=body)
except ApiException as e:
    print("Exception when calling ReportApi->report_user_reports_file_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserReportsFileBody**](UserReportsFileBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_user_reports_list_post**
> list[EfirDataHubModelsModelsReportListFields] report_user_reports_list_post(body=body)

Возвращает список файлов указанного типа отчетов. Напр.: EndOfDay

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
api_instance = swagger_client.ReportApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserReportsListBody() # UserReportsListBody |  (optional)

try:
    # Возвращает список файлов указанного типа отчетов. Напр.: EndOfDay
    api_response = api_instance.report_user_reports_list_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportApi->report_user_reports_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserReportsListBody**](UserReportsListBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsReportListFields]**](EfirDataHubModelsModelsReportListFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

