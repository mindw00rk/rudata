# swagger_client.NsdApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_nsd_bond_coupons_post**](NsdApi.md#v2_nsd_bond_coupons_post) | **POST** /v2/Nsd/BondCoupons | Получить данные по купонам из базы НРД.
[**v2_nsd_bond_offers_post**](NsdApi.md#v2_nsd_bond_offers_post) | **POST** /v2/Nsd/BondOffers | Получить данные по погашениям из базы НРД.
[**v2_nsd_common_data_post**](NsdApi.md#v2_nsd_common_data_post) | **POST** /v2/Nsd/CommonData | Получить общие данные по бумаге из базы НРД.
[**v2_nsd_emitent_licenses_post**](NsdApi.md#v2_nsd_emitent_licenses_post) | **POST** /v2/Nsd/EmitentLicenses | Получить данные по лицензиям эмитентов из базы НРД.
[**v2_nsd_emitents_post**](NsdApi.md#v2_nsd_emitents_post) | **POST** /v2/Nsd/Emitents | Получить данные по эмитентам из базы НРД.
[**v2_nsd_fintool_codes_post**](NsdApi.md#v2_nsd_fintool_codes_post) | **POST** /v2/Nsd/FintoolCodes | Получить присвоенные инструментам коды из базы НРД (код инструмента на МБ, в НКЦ Фортс т.п.).
[**v2_nsd_sir_file_date_get**](NsdApi.md#v2_nsd_sir_file_date_get) | **GET** /v2/Nsd/SirFile/{date} | Получить SIR-файл (zip-архив) НРД за указанную дату.
[**v2_nsd_tax_info_post**](NsdApi.md#v2_nsd_tax_info_post) | **POST** /v2/Nsd/TaxInfo | Информация о налоговых ставках

# **v2_nsd_bond_coupons_post**
> list[EfirDataHubModelsModelsNsdNsdBondCouponsFields] v2_nsd_bond_coupons_post(body=body)

Получить данные по купонам из базы НРД.

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
api_instance = swagger_client.NsdApi(swagger_client.ApiClient(configuration))
body = swagger_client.NsdBondCouponsBody() # NsdBondCouponsBody |  (optional)

try:
    # Получить данные по купонам из базы НРД.
    api_response = api_instance.v2_nsd_bond_coupons_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NsdApi->v2_nsd_bond_coupons_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NsdBondCouponsBody**](NsdBondCouponsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsNsdNsdBondCouponsFields]**](EfirDataHubModelsModelsNsdNsdBondCouponsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_nsd_bond_offers_post**
> list[EfirDataHubModelsModelsNsdNsdBondOffersFields] v2_nsd_bond_offers_post(body=body)

Получить данные по погашениям из базы НРД.

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
api_instance = swagger_client.NsdApi(swagger_client.ApiClient(configuration))
body = swagger_client.NsdBondOffersBody() # NsdBondOffersBody |  (optional)

try:
    # Получить данные по погашениям из базы НРД.
    api_response = api_instance.v2_nsd_bond_offers_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NsdApi->v2_nsd_bond_offers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NsdBondOffersBody**](NsdBondOffersBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsNsdNsdBondOffersFields]**](EfirDataHubModelsModelsNsdNsdBondOffersFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_nsd_common_data_post**
> list[EfirDataHubModelsModelsNsdCommonDataFields] v2_nsd_common_data_post(body=body)

Получить общие данные по бумаге из базы НРД.

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
api_instance = swagger_client.NsdApi(swagger_client.ApiClient(configuration))
body = swagger_client.NsdCommonDataBody() # NsdCommonDataBody |  (optional)

try:
    # Получить общие данные по бумаге из базы НРД.
    api_response = api_instance.v2_nsd_common_data_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NsdApi->v2_nsd_common_data_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NsdCommonDataBody**](NsdCommonDataBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsNsdCommonDataFields]**](EfirDataHubModelsModelsNsdCommonDataFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_nsd_emitent_licenses_post**
> list[EfirDataHubModelsModelsNsdNsdEmitentLicensesFields] v2_nsd_emitent_licenses_post(body=body)

Получить данные по лицензиям эмитентов из базы НРД.

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
api_instance = swagger_client.NsdApi(swagger_client.ApiClient(configuration))
body = swagger_client.NsdEmitentLicensesBody() # NsdEmitentLicensesBody |  (optional)

try:
    # Получить данные по лицензиям эмитентов из базы НРД.
    api_response = api_instance.v2_nsd_emitent_licenses_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NsdApi->v2_nsd_emitent_licenses_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NsdEmitentLicensesBody**](NsdEmitentLicensesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsNsdNsdEmitentLicensesFields]**](EfirDataHubModelsModelsNsdNsdEmitentLicensesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_nsd_emitents_post**
> list[EfirDataHubModelsModelsNsdNsdEmitentsFields] v2_nsd_emitents_post(body=body)

Получить данные по эмитентам из базы НРД.

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
api_instance = swagger_client.NsdApi(swagger_client.ApiClient(configuration))
body = swagger_client.NsdEmitentsBody() # NsdEmitentsBody |  (optional)

try:
    # Получить данные по эмитентам из базы НРД.
    api_response = api_instance.v2_nsd_emitents_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NsdApi->v2_nsd_emitents_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NsdEmitentsBody**](NsdEmitentsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsNsdNsdEmitentsFields]**](EfirDataHubModelsModelsNsdNsdEmitentsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_nsd_fintool_codes_post**
> list[EfirDataHubModelsModelsNsdNsdFintoolCodesFields] v2_nsd_fintool_codes_post(body=body)

Получить присвоенные инструментам коды из базы НРД (код инструмента на МБ, в НКЦ Фортс т.п.).

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
api_instance = swagger_client.NsdApi(swagger_client.ApiClient(configuration))
body = swagger_client.NsdFintoolCodesBody() # NsdFintoolCodesBody |  (optional)

try:
    # Получить присвоенные инструментам коды из базы НРД (код инструмента на МБ, в НКЦ Фортс т.п.).
    api_response = api_instance.v2_nsd_fintool_codes_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NsdApi->v2_nsd_fintool_codes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NsdFintoolCodesBody**](NsdFintoolCodesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsNsdNsdFintoolCodesFields]**](EfirDataHubModelsModelsNsdNsdFintoolCodesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_nsd_sir_file_date_get**
> v2_nsd_sir_file_date_get(_date)

Получить SIR-файл (zip-архив) НРД за указанную дату.

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
api_instance = swagger_client.NsdApi(swagger_client.ApiClient(configuration))
_date = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    # Получить SIR-файл (zip-архив) НРД за указанную дату.
    api_instance.v2_nsd_sir_file_date_get(_date)
except ApiException as e:
    print("Exception when calling NsdApi->v2_nsd_sir_file_date_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **datetime**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_nsd_tax_info_post**
> list[EfirDataHubModelsModelsNsdTaxInfoFields] v2_nsd_tax_info_post(body=body)

Информация о налоговых ставках

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
api_instance = swagger_client.NsdApi(swagger_client.ApiClient(configuration))
body = swagger_client.NsdTaxInfoBody() # NsdTaxInfoBody |  (optional)

try:
    # Информация о налоговых ставках
    api_response = api_instance.v2_nsd_tax_info_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NsdApi->v2_nsd_tax_info_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NsdTaxInfoBody**](NsdTaxInfoBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsNsdTaxInfoFields]**](EfirDataHubModelsModelsNsdTaxInfoFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

