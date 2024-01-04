# swagger_client.AccountApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_account_login_post**](AccountApi.md#v2_account_login_post) | **POST** /v2/Account/Login | Авторизация пользователя. Получить авторизационный токен.
[**v2_account_logoff_post**](AccountApi.md#v2_account_logoff_post) | **POST** /v2/Account/Logoff | Завершение сессии пользователя.
[**v2_account_subscription_post**](AccountApi.md#v2_account_subscription_post) | **POST** /v2/Account/Subscription | Подписка пользователя
[**v2_account_validate_post**](AccountApi.md#v2_account_validate_post) | **POST** /v2/Account/Validate | Валидация текущего сеанса

# **v2_account_login_post**
> EfirDataHubModelsModelsAccountLoginResponse v2_account_login_post(body=body)

Авторизация пользователя. Получить авторизационный токен.

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccountLoginBody() # AccountLoginBody | Задает имя пользователя и пароль. (optional)

try:
    # Авторизация пользователя. Получить авторизационный токен.
    api_response = api_instance.v2_account_login_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->v2_account_login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountLoginBody**](AccountLoginBody.md)| Задает имя пользователя и пароль. | [optional] 

### Return type

[**EfirDataHubModelsModelsAccountLoginResponse**](EfirDataHubModelsModelsAccountLoginResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_account_logoff_post**
> EfirDataHubModelsModelsAccountLogoffResponse v2_account_logoff_post()

Завершение сессии пользователя.

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))

try:
    # Завершение сессии пользователя.
    api_response = api_instance.v2_account_logoff_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->v2_account_logoff_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EfirDataHubModelsModelsAccountLogoffResponse**](EfirDataHubModelsModelsAccountLogoffResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_account_subscription_post**
> EfirDataHubModelsModelsAccountSubscriptionResponse v2_account_subscription_post()

Подписка пользователя

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))

try:
    # Подписка пользователя
    api_response = api_instance.v2_account_subscription_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->v2_account_subscription_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EfirDataHubModelsModelsAccountSubscriptionResponse**](EfirDataHubModelsModelsAccountSubscriptionResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_account_validate_post**
> EfirDataHubModelsModelsAccountValidateResponse v2_account_validate_post()

Валидация текущего сеанса

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))

try:
    # Валидация текущего сеанса
    api_response = api_instance.v2_account_validate_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->v2_account_validate_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EfirDataHubModelsModelsAccountValidateResponse**](EfirDataHubModelsModelsAccountValidateResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

