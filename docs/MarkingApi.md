# swagger_client.MarkingApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_marking_codes_post**](MarkingApi.md#v2_marking_codes_post) | **POST** /v2/Marking/Codes | Cправочник кодов, используемых для значений маркировки
[**v2_marking_rules_post**](MarkingApi.md#v2_marking_rules_post) | **POST** /v2/Marking/Rules | Справочник правил выполнения маркировки
[**v2_marking_values_post**](MarkingApi.md#v2_marking_values_post) | **POST** /v2/Marking/Values | Информация о маркировках инструментов, отрезки действия которых пересекаются с заданным

# **v2_marking_codes_post**
> list[EfirDataHubModelsModelsMarkingCodesFields] v2_marking_codes_post(body=body)

Cправочник кодов, используемых для значений маркировки

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
api_instance = swagger_client.MarkingApi(swagger_client.ApiClient(configuration))
body = swagger_client.MarkingCodesBody() # MarkingCodesBody |  (optional)

try:
    # Cправочник кодов, используемых для значений маркировки
    api_response = api_instance.v2_marking_codes_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarkingApi->v2_marking_codes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MarkingCodesBody**](MarkingCodesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsMarkingCodesFields]**](EfirDataHubModelsModelsMarkingCodesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_marking_rules_post**
> list[EfirDataHubModelsModelsMarkingRulesFields] v2_marking_rules_post(body=body)

Справочник правил выполнения маркировки

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
api_instance = swagger_client.MarkingApi(swagger_client.ApiClient(configuration))
body = swagger_client.MarkingRulesBody() # MarkingRulesBody |  (optional)

try:
    # Справочник правил выполнения маркировки
    api_response = api_instance.v2_marking_rules_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarkingApi->v2_marking_rules_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MarkingRulesBody**](MarkingRulesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsMarkingRulesFields]**](EfirDataHubModelsModelsMarkingRulesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_marking_values_post**
> list[EfirDataHubModelsModelsMarkingValuesFields] v2_marking_values_post(body=body)

Информация о маркировках инструментов, отрезки действия которых пересекаются с заданным

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
api_instance = swagger_client.MarkingApi(swagger_client.ApiClient(configuration))
body = swagger_client.MarkingValuesBody() # MarkingValuesBody |  (optional)

try:
    # Информация о маркировках инструментов, отрезки действия которых пересекаются с заданным
    api_response = api_instance.v2_marking_values_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarkingApi->v2_marking_values_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MarkingValuesBody**](MarkingValuesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsMarkingValuesFields]**](EfirDataHubModelsModelsMarkingValuesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

