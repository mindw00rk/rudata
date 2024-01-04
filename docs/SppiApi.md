# swagger_client.SppiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_sppi_covenant_list_post**](SppiApi.md#v2_sppi_covenant_list_post) | **POST** /v2/SPPI/CovenantList | Возвращает список ковенантов с классификацией по умолчанию для SPPI-тестирования
[**v2_sppi_criteria_list_get**](SppiApi.md#v2_sppi_criteria_list_get) | **GET** /v2/SPPI/CriteriaList | Возвращает список доступных критериев SPPI-тестирования
[**v2_sppi_param_list_get**](SppiApi.md#v2_sppi_param_list_get) | **GET** /v2/SPPI/ParamList | Возвращает список параметров облигации для SPPI-тестирования
[**v2_sppi_testing_post**](SppiApi.md#v2_sppi_testing_post) | **POST** /v2/SPPI/Testing | Возвращает итоги SPPI-тестирования по бумаге

# **v2_sppi_covenant_list_post**
> list[EfirDataHubModelsModelsSppiCovenantFields] v2_sppi_covenant_list_post(body=body)

Возвращает список ковенантов с классификацией по умолчанию для SPPI-тестирования

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
api_instance = swagger_client.SppiApi(swagger_client.ApiClient(configuration))
body = swagger_client.SPPICovenantListBody() # SPPICovenantListBody |  (optional)

try:
    # Возвращает список ковенантов с классификацией по умолчанию для SPPI-тестирования
    api_response = api_instance.v2_sppi_covenant_list_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SppiApi->v2_sppi_covenant_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SPPICovenantListBody**](SPPICovenantListBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsSppiCovenantFields]**](EfirDataHubModelsModelsSppiCovenantFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_sppi_criteria_list_get**
> list[EfirDataHubModelsModelsSppiCriterionFields] v2_sppi_criteria_list_get()

Возвращает список доступных критериев SPPI-тестирования

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
api_instance = swagger_client.SppiApi(swagger_client.ApiClient(configuration))

try:
    # Возвращает список доступных критериев SPPI-тестирования
    api_response = api_instance.v2_sppi_criteria_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SppiApi->v2_sppi_criteria_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EfirDataHubModelsModelsSppiCriterionFields]**](EfirDataHubModelsModelsSppiCriterionFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_sppi_param_list_get**
> list[EfirDataHubModelsModelsSppiParamFields] v2_sppi_param_list_get()

Возвращает список параметров облигации для SPPI-тестирования

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
api_instance = swagger_client.SppiApi(swagger_client.ApiClient(configuration))

try:
    # Возвращает список параметров облигации для SPPI-тестирования
    api_response = api_instance.v2_sppi_param_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SppiApi->v2_sppi_param_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EfirDataHubModelsModelsSppiParamFields]**](EfirDataHubModelsModelsSppiParamFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_sppi_testing_post**
> list[EfirDataHubModelsModelsSppiTestingFields] v2_sppi_testing_post(body=body)

Возвращает итоги SPPI-тестирования по бумаге

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
api_instance = swagger_client.SppiApi(swagger_client.ApiClient(configuration))
body = swagger_client.SPPITestingBody() # SPPITestingBody |  (optional)

try:
    # Возвращает итоги SPPI-тестирования по бумаге
    api_response = api_instance.v2_sppi_testing_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SppiApi->v2_sppi_testing_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SPPITestingBody**](SPPITestingBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsSppiTestingFields]**](EfirDataHubModelsModelsSppiTestingFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

