# swagger_client.SolvencyApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_solvency_classification_codes_post**](SolvencyApi.md#v2_solvency_classification_codes_post) | **POST** /v2/Solvency/ClassificationCodes | Получить значения справочника свойств контрагентов
[**v2_solvency_counterparty_classification_post**](SolvencyApi.md#v2_solvency_counterparty_classification_post) | **POST** /v2/Solvency/CounterpartyClassification | Возвращает значения классификаторов контрагентов
[**v2_solvency_counterparty_id_post**](SolvencyApi.md#v2_solvency_counterparty_id_post) | **POST** /v2/Solvency/CounterpartyId | Формирует идентификатор контрагента
[**v2_solvency_counterparty_post**](SolvencyApi.md#v2_solvency_counterparty_post) | **POST** /v2/Solvency/Counterparty | Возвращает описание контрагентов
[**v2_solvency_licenses_post**](SolvencyApi.md#v2_solvency_licenses_post) | **POST** /v2/Solvency/Licenses | Возвращает описания лицензий контрагентов
[**v2_solvency_rating_agg_company_post**](SolvencyApi.md#v2_solvency_rating_agg_company_post) | **POST** /v2/Solvency/RatingAggCompany | Агрегированные рейтинги компаний
[**v2_solvency_rating_agg_security_by_issuer_post**](SolvencyApi.md#v2_solvency_rating_agg_security_by_issuer_post) | **POST** /v2/Solvency/RatingAggSecurityByIssuer | Агрегированные рейтинги инструментов по эмитентам выпуска
[**v2_solvency_rating_agg_security_by_role_post**](SolvencyApi.md#v2_solvency_rating_agg_security_by_role_post) | **POST** /v2/Solvency/RatingAggSecurityByRole | Агрегированные рейтинги инструментов по ролям организаторов выпуска
[**v2_solvency_rating_agg_security_post**](SolvencyApi.md#v2_solvency_rating_agg_security_post) | **POST** /v2/Solvency/RatingAggSecurity | Агрегированные рейтинги инструментов
[**v2_solvency_rating_list_post**](SolvencyApi.md#v2_solvency_rating_list_post) | **POST** /v2/Solvency/RatingList | Список кодов рейтингов на дату

# **v2_solvency_classification_codes_post**
> EfirDataHubModelsModelsSolvencyClassificationCodesResponse v2_solvency_classification_codes_post()

Получить значения справочника свойств контрагентов

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
api_instance = swagger_client.SolvencyApi(swagger_client.ApiClient(configuration))

try:
    # Получить значения справочника свойств контрагентов
    api_response = api_instance.v2_solvency_classification_codes_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SolvencyApi->v2_solvency_classification_codes_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EfirDataHubModelsModelsSolvencyClassificationCodesResponse**](EfirDataHubModelsModelsSolvencyClassificationCodesResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_solvency_counterparty_classification_post**
> list[EfirDataHubModelsModelsSolvencyCounterpartyClassificationFields] v2_solvency_counterparty_classification_post(body=body)

Возвращает значения классификаторов контрагентов

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
api_instance = swagger_client.SolvencyApi(swagger_client.ApiClient(configuration))
body = swagger_client.SolvencyCounterpartyClassificationBody() # SolvencyCounterpartyClassificationBody |  (optional)

try:
    # Возвращает значения классификаторов контрагентов
    api_response = api_instance.v2_solvency_counterparty_classification_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SolvencyApi->v2_solvency_counterparty_classification_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SolvencyCounterpartyClassificationBody**](SolvencyCounterpartyClassificationBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsSolvencyCounterpartyClassificationFields]**](EfirDataHubModelsModelsSolvencyCounterpartyClassificationFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_solvency_counterparty_id_post**
> list[EfirDataHubModelsModelsSolvencyCounterpartyIdFields] v2_solvency_counterparty_id_post(body=body)

Формирует идентификатор контрагента

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
api_instance = swagger_client.SolvencyApi(swagger_client.ApiClient(configuration))
body = swagger_client.SolvencyCounterpartyIdBody() # SolvencyCounterpartyIdBody |  (optional)

try:
    # Формирует идентификатор контрагента
    api_response = api_instance.v2_solvency_counterparty_id_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SolvencyApi->v2_solvency_counterparty_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SolvencyCounterpartyIdBody**](SolvencyCounterpartyIdBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsSolvencyCounterpartyIdFields]**](EfirDataHubModelsModelsSolvencyCounterpartyIdFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_solvency_counterparty_post**
> list[EfirDataHubModelsModelsSolvencyCounterpartyFields] v2_solvency_counterparty_post(body=body)

Возвращает описание контрагентов

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
api_instance = swagger_client.SolvencyApi(swagger_client.ApiClient(configuration))
body = swagger_client.SolvencyCounterpartyBody() # SolvencyCounterpartyBody |  (optional)

try:
    # Возвращает описание контрагентов
    api_response = api_instance.v2_solvency_counterparty_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SolvencyApi->v2_solvency_counterparty_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SolvencyCounterpartyBody**](SolvencyCounterpartyBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsSolvencyCounterpartyFields]**](EfirDataHubModelsModelsSolvencyCounterpartyFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_solvency_licenses_post**
> list[EfirDataHubModelsModelsSolvencyLicenseFields] v2_solvency_licenses_post(body=body)

Возвращает описания лицензий контрагентов

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
api_instance = swagger_client.SolvencyApi(swagger_client.ApiClient(configuration))
body = swagger_client.SolvencyLicensesBody() # SolvencyLicensesBody |  (optional)

try:
    # Возвращает описания лицензий контрагентов
    api_response = api_instance.v2_solvency_licenses_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SolvencyApi->v2_solvency_licenses_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SolvencyLicensesBody**](SolvencyLicensesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsSolvencyLicenseFields]**](EfirDataHubModelsModelsSolvencyLicenseFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_solvency_rating_agg_company_post**
> list[EfirDataHubModelsModelsSolvencyRatingAggCompanyFields] v2_solvency_rating_agg_company_post(body=body)

Агрегированные рейтинги компаний

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
api_instance = swagger_client.SolvencyApi(swagger_client.ApiClient(configuration))
body = swagger_client.SolvencyRatingAggCompanyBody() # SolvencyRatingAggCompanyBody |  (optional)

try:
    # Агрегированные рейтинги компаний
    api_response = api_instance.v2_solvency_rating_agg_company_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SolvencyApi->v2_solvency_rating_agg_company_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SolvencyRatingAggCompanyBody**](SolvencyRatingAggCompanyBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsSolvencyRatingAggCompanyFields]**](EfirDataHubModelsModelsSolvencyRatingAggCompanyFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_solvency_rating_agg_security_by_issuer_post**
> list[EfirDataHubModelsModelsSolvencyRatingAggSecurityByIssuerFields] v2_solvency_rating_agg_security_by_issuer_post(body=body)

Агрегированные рейтинги инструментов по эмитентам выпуска

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
api_instance = swagger_client.SolvencyApi(swagger_client.ApiClient(configuration))
body = swagger_client.SolvencyRatingAggSecurityByIssuerBody() # SolvencyRatingAggSecurityByIssuerBody |  (optional)

try:
    # Агрегированные рейтинги инструментов по эмитентам выпуска
    api_response = api_instance.v2_solvency_rating_agg_security_by_issuer_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SolvencyApi->v2_solvency_rating_agg_security_by_issuer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SolvencyRatingAggSecurityByIssuerBody**](SolvencyRatingAggSecurityByIssuerBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsSolvencyRatingAggSecurityByIssuerFields]**](EfirDataHubModelsModelsSolvencyRatingAggSecurityByIssuerFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_solvency_rating_agg_security_by_role_post**
> list[EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields] v2_solvency_rating_agg_security_by_role_post(body=body)

Агрегированные рейтинги инструментов по ролям организаторов выпуска

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
api_instance = swagger_client.SolvencyApi(swagger_client.ApiClient(configuration))
body = swagger_client.SolvencyRatingAggSecurityByRoleBody() # SolvencyRatingAggSecurityByRoleBody |  (optional)

try:
    # Агрегированные рейтинги инструментов по ролям организаторов выпуска
    api_response = api_instance.v2_solvency_rating_agg_security_by_role_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SolvencyApi->v2_solvency_rating_agg_security_by_role_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SolvencyRatingAggSecurityByRoleBody**](SolvencyRatingAggSecurityByRoleBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields]**](EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_solvency_rating_agg_security_post**
> list[EfirDataHubModelsModelsSolvencyRatingAggSecurityFields] v2_solvency_rating_agg_security_post(body=body)

Агрегированные рейтинги инструментов

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
api_instance = swagger_client.SolvencyApi(swagger_client.ApiClient(configuration))
body = swagger_client.SolvencyRatingAggSecurityBody() # SolvencyRatingAggSecurityBody |  (optional)

try:
    # Агрегированные рейтинги инструментов
    api_response = api_instance.v2_solvency_rating_agg_security_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SolvencyApi->v2_solvency_rating_agg_security_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SolvencyRatingAggSecurityBody**](SolvencyRatingAggSecurityBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsSolvencyRatingAggSecurityFields]**](EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_solvency_rating_list_post**
> list[str] v2_solvency_rating_list_post(body=body)

Список кодов рейтингов на дату

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
api_instance = swagger_client.SolvencyApi(swagger_client.ApiClient(configuration))
body = swagger_client.SolvencyRatingListBody() # SolvencyRatingListBody |  (optional)

try:
    # Список кодов рейтингов на дату
    api_response = api_instance.v2_solvency_rating_list_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SolvencyApi->v2_solvency_rating_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SolvencyRatingListBody**](SolvencyRatingListBody.md)|  | [optional] 

### Return type

**list[str]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

