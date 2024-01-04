# swagger_client.CorporateActionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_corporate_action_actions_post**](CorporateActionApi.md#v2_corporate_action_actions_post) | **POST** /v2/CorporateAction/Actions | Получить корпоративные действия.
[**v2_corporate_action_fields_post**](CorporateActionApi.md#v2_corporate_action_fields_post) | **POST** /v2/CorporateAction/Fields | Получить справочник полей по корпоративным действиям.
[**v2_corporate_action_kind_groups_post**](CorporateActionApi.md#v2_corporate_action_kind_groups_post) | **POST** /v2/CorporateAction/KindGroups | Получить список групп видов корпоративных действий.
[**v2_corporate_action_kinds_post**](CorporateActionApi.md#v2_corporate_action_kinds_post) | **POST** /v2/CorporateAction/Kinds | Получить список видов корпоративных действий.
[**v2_corporate_action_sources_post**](CorporateActionApi.md#v2_corporate_action_sources_post) | **POST** /v2/CorporateAction/Sources | Получить список источников информации.

# **v2_corporate_action_actions_post**
> list[EfirDataHubModelsModelsCorporateActionActionsFields] v2_corporate_action_actions_post(body=body)

Получить корпоративные действия.

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
api_instance = swagger_client.CorporateActionApi(swagger_client.ApiClient(configuration))
body = swagger_client.CorporateActionActionsBody() # CorporateActionActionsBody |  (optional)

try:
    # Получить корпоративные действия.
    api_response = api_instance.v2_corporate_action_actions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporateActionApi->v2_corporate_action_actions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CorporateActionActionsBody**](CorporateActionActionsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsCorporateActionActionsFields]**](EfirDataHubModelsModelsCorporateActionActionsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_corporate_action_fields_post**
> v2_corporate_action_fields_post(body=body)

Получить справочник полей по корпоративным действиям.

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
api_instance = swagger_client.CorporateActionApi(swagger_client.ApiClient(configuration))
body = swagger_client.CorporateActionFieldsBody() # CorporateActionFieldsBody |  (optional)

try:
    # Получить справочник полей по корпоративным действиям.
    api_instance.v2_corporate_action_fields_post(body=body)
except ApiException as e:
    print("Exception when calling CorporateActionApi->v2_corporate_action_fields_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CorporateActionFieldsBody**](CorporateActionFieldsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_corporate_action_kind_groups_post**
> list[EfirDataHubModelsModelsCorporateActionKindGroupsFields] v2_corporate_action_kind_groups_post()

Получить список групп видов корпоративных действий.

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
api_instance = swagger_client.CorporateActionApi(swagger_client.ApiClient(configuration))

try:
    # Получить список групп видов корпоративных действий.
    api_response = api_instance.v2_corporate_action_kind_groups_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporateActionApi->v2_corporate_action_kind_groups_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EfirDataHubModelsModelsCorporateActionKindGroupsFields]**](EfirDataHubModelsModelsCorporateActionKindGroupsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_corporate_action_kinds_post**
> list[EfirDataHubModelsModelsCorporateActionKindsFields] v2_corporate_action_kinds_post(body=body)

Получить список видов корпоративных действий.

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
api_instance = swagger_client.CorporateActionApi(swagger_client.ApiClient(configuration))
body = swagger_client.CorporateActionKindsBody() # CorporateActionKindsBody |  (optional)

try:
    # Получить список видов корпоративных действий.
    api_response = api_instance.v2_corporate_action_kinds_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporateActionApi->v2_corporate_action_kinds_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CorporateActionKindsBody**](CorporateActionKindsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsCorporateActionKindsFields]**](EfirDataHubModelsModelsCorporateActionKindsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_corporate_action_sources_post**
> list[EfirDataHubModelsModelsCorporateActionSourcesFields] v2_corporate_action_sources_post()

Получить список источников информации.

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
api_instance = swagger_client.CorporateActionApi(swagger_client.ApiClient(configuration))

try:
    # Получить список источников информации.
    api_response = api_instance.v2_corporate_action_sources_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporateActionApi->v2_corporate_action_sources_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EfirDataHubModelsModelsCorporateActionSourcesFields]**](EfirDataHubModelsModelsCorporateActionSourcesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

