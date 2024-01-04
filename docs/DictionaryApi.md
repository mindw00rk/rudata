# swagger_client.DictionaryApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_dictionary_affiliate_types_get**](DictionaryApi.md#v2_dictionary_affiliate_types_get) | **GET** /v2/Dictionary/AffiliateTypes | Возвращает справочник типов аффилированности
[**v2_dictionary_commodity_codes_get**](DictionaryApi.md#v2_dictionary_commodity_codes_get) | **GET** /v2/Dictionary/CommodityCodes | Коды товаров
[**v2_dictionary_countries_post**](DictionaryApi.md#v2_dictionary_countries_post) | **POST** /v2/Dictionary/Countries | Справочник стран
[**v2_dictionary_covenant_list_get**](DictionaryApi.md#v2_dictionary_covenant_list_get) | **GET** /v2/Dictionary/CovenantList | Метод для получения справочника ковенантов
[**v2_dictionary_covenant_types_get**](DictionaryApi.md#v2_dictionary_covenant_types_get) | **GET** /v2/Dictionary/CovenantTypes | Возвращает справочник типов ковенантов
[**v2_dictionary_currencies_post**](DictionaryApi.md#v2_dictionary_currencies_post) | **POST** /v2/Dictionary/Currencies | Получить справочник валют.
[**v2_dictionary_currency_codes_post**](DictionaryApi.md#v2_dictionary_currency_codes_post) | **POST** /v2/Dictionary/CurrencyCodes | Получить коды валют по различным классификаторам.
[**v2_dictionary_emitent_category_post**](DictionaryApi.md#v2_dictionary_emitent_category_post) | **POST** /v2/Dictionary/emitent-category | Метод для получения категорий компаний
[**v2_dictionary_emitent_type_category_post**](DictionaryApi.md#v2_dictionary_emitent_type_category_post) | **POST** /v2/Dictionary/emitent-type-category | Метод для получения типов категорий компаний
[**v2_dictionary_fintool_category_post**](DictionaryApi.md#v2_dictionary_fintool_category_post) | **POST** /v2/Dictionary/fintool-category | Метод для получения категорий инструментов
[**v2_dictionary_fintool_type_category_post**](DictionaryApi.md#v2_dictionary_fintool_type_category_post) | **POST** /v2/Dictionary/fintool-type-category | Метод для получения типов категорий инструментов
[**v2_dictionary_holiday_types_post**](DictionaryApi.md#v2_dictionary_holiday_types_post) | **POST** /v2/Dictionary/HolidayTypes | Справочник названий неторговых дней по странам
[**v2_dictionary_list_org_roles_post**](DictionaryApi.md#v2_dictionary_list_org_roles_post) | **POST** /v2/Dictionary/ListOrgRoles | Получить справочник ролей организаций
[**v2_dictionary_list_ratings_post**](DictionaryApi.md#v2_dictionary_list_ratings_post) | **POST** /v2/Dictionary/ListRatings | Список рейтингов
[**v2_dictionary_liter_list_post**](DictionaryApi.md#v2_dictionary_liter_list_post) | **POST** /v2/Dictionary/LiterList | Метод для получения справочника литеров
[**v2_dictionary_market_sectors_post**](DictionaryApi.md#v2_dictionary_market_sectors_post) | **POST** /v2/Dictionary/MarketSectors | Возвращает перечень секторов рынка по различным классификаторам
[**v2_dictionary_moex_boards_post**](DictionaryApi.md#v2_dictionary_moex_boards_post) | **POST** /v2/Dictionary/MoexBoards | Список торговых площадок Московской биржи
[**v2_dictionary_rating_scale_values_post**](DictionaryApi.md#v2_dictionary_rating_scale_values_post) | **POST** /v2/Dictionary/RatingScaleValues | Список шкал значений рейтингов
[**v2_dictionary_rating_scales_post**](DictionaryApi.md#v2_dictionary_rating_scales_post) | **POST** /v2/Dictionary/RatingScales | Список рейтинговых шкал
[**v2_dictionary_regions_post**](DictionaryApi.md#v2_dictionary_regions_post) | **POST** /v2/Dictionary/Regions | Возвращает справочник регионов

# **v2_dictionary_affiliate_types_get**
> list[EfirDataHubModelsModelsAffiliatesTypesFields] v2_dictionary_affiliate_types_get()

Возвращает справочник типов аффилированности

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
api_instance = swagger_client.DictionaryApi(swagger_client.ApiClient(configuration))

try:
    # Возвращает справочник типов аффилированности
    api_response = api_instance.v2_dictionary_affiliate_types_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryApi->v2_dictionary_affiliate_types_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EfirDataHubModelsModelsAffiliatesTypesFields]**](EfirDataHubModelsModelsAffiliatesTypesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_dictionary_commodity_codes_get**
> list[EfirDataHubModelsModelsDictionaryCommodityCodeFields] v2_dictionary_commodity_codes_get()

Коды товаров

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
api_instance = swagger_client.DictionaryApi(swagger_client.ApiClient(configuration))

try:
    # Коды товаров
    api_response = api_instance.v2_dictionary_commodity_codes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryApi->v2_dictionary_commodity_codes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EfirDataHubModelsModelsDictionaryCommodityCodeFields]**](EfirDataHubModelsModelsDictionaryCommodityCodeFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_dictionary_countries_post**
> list[EfirDataHubModelsModelsDictionaryCountriesFields] v2_dictionary_countries_post(body=body)

Справочник стран

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
api_instance = swagger_client.DictionaryApi(swagger_client.ApiClient(configuration))
body = swagger_client.DictionaryCountriesBody() # DictionaryCountriesBody |  (optional)

try:
    # Справочник стран
    api_response = api_instance.v2_dictionary_countries_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryApi->v2_dictionary_countries_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DictionaryCountriesBody**](DictionaryCountriesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsDictionaryCountriesFields]**](EfirDataHubModelsModelsDictionaryCountriesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_dictionary_covenant_list_get**
> list[EfirDataHubModelsModelsBondCovenant] v2_dictionary_covenant_list_get()

Метод для получения справочника ковенантов

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
api_instance = swagger_client.DictionaryApi(swagger_client.ApiClient(configuration))

try:
    # Метод для получения справочника ковенантов
    api_response = api_instance.v2_dictionary_covenant_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryApi->v2_dictionary_covenant_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EfirDataHubModelsModelsBondCovenant]**](EfirDataHubModelsModelsBondCovenant.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_dictionary_covenant_types_get**
> list[EfirDataHubModelsModelsDictionaryCovenantType] v2_dictionary_covenant_types_get()

Возвращает справочник типов ковенантов

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
api_instance = swagger_client.DictionaryApi(swagger_client.ApiClient(configuration))

try:
    # Возвращает справочник типов ковенантов
    api_response = api_instance.v2_dictionary_covenant_types_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryApi->v2_dictionary_covenant_types_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EfirDataHubModelsModelsDictionaryCovenantType]**](EfirDataHubModelsModelsDictionaryCovenantType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_dictionary_currencies_post**
> EfirDataHubModelsModelsInfoCurrenciesWithKkvFields v2_dictionary_currencies_post(body=body)

Получить справочник валют.

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
api_instance = swagger_client.DictionaryApi(swagger_client.ApiClient(configuration))
body = swagger_client.DictionaryCurrenciesBody() # DictionaryCurrenciesBody |  (optional)

try:
    # Получить справочник валют.
    api_response = api_instance.v2_dictionary_currencies_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryApi->v2_dictionary_currencies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DictionaryCurrenciesBody**](DictionaryCurrenciesBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsInfoCurrenciesWithKkvFields**](EfirDataHubModelsModelsInfoCurrenciesWithKkvFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_dictionary_currency_codes_post**
> list[EfirDataHubModelsModelsInfoCurrencyCodesFields] v2_dictionary_currency_codes_post(body=body)

Получить коды валют по различным классификаторам.

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
api_instance = swagger_client.DictionaryApi(swagger_client.ApiClient(configuration))
body = swagger_client.DictionaryCurrencyCodesBody() # DictionaryCurrencyCodesBody |  (optional)

try:
    # Получить коды валют по различным классификаторам.
    api_response = api_instance.v2_dictionary_currency_codes_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryApi->v2_dictionary_currency_codes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DictionaryCurrencyCodesBody**](DictionaryCurrencyCodesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoCurrencyCodesFields]**](EfirDataHubModelsModelsInfoCurrencyCodesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_dictionary_emitent_category_post**
> list[EfirDataHubModelsModelsDictionaryEmitentCategoryFields] v2_dictionary_emitent_category_post(body=body)

Метод для получения категорий компаний

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
api_instance = swagger_client.DictionaryApi(swagger_client.ApiClient(configuration))
body = swagger_client.DictionaryEmitentcategoryBody() # DictionaryEmitentcategoryBody |  (optional)

try:
    # Метод для получения категорий компаний
    api_response = api_instance.v2_dictionary_emitent_category_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryApi->v2_dictionary_emitent_category_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DictionaryEmitentcategoryBody**](DictionaryEmitentcategoryBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsDictionaryEmitentCategoryFields]**](EfirDataHubModelsModelsDictionaryEmitentCategoryFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_dictionary_emitent_type_category_post**
> list[EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields] v2_dictionary_emitent_type_category_post(body=body)

Метод для получения типов категорий компаний

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
api_instance = swagger_client.DictionaryApi(swagger_client.ApiClient(configuration))
body = swagger_client.DictionaryEmitenttypecategoryBody() # DictionaryEmitenttypecategoryBody |  (optional)

try:
    # Метод для получения типов категорий компаний
    api_response = api_instance.v2_dictionary_emitent_type_category_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryApi->v2_dictionary_emitent_type_category_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DictionaryEmitenttypecategoryBody**](DictionaryEmitenttypecategoryBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields]**](EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_dictionary_fintool_category_post**
> list[EfirDataHubModelsModelsDictionaryFintoolCategoryFields] v2_dictionary_fintool_category_post(body=body)

Метод для получения категорий инструментов

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
api_instance = swagger_client.DictionaryApi(swagger_client.ApiClient(configuration))
body = swagger_client.DictionaryFintoolcategoryBody() # DictionaryFintoolcategoryBody |  (optional)

try:
    # Метод для получения категорий инструментов
    api_response = api_instance.v2_dictionary_fintool_category_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryApi->v2_dictionary_fintool_category_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DictionaryFintoolcategoryBody**](DictionaryFintoolcategoryBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsDictionaryFintoolCategoryFields]**](EfirDataHubModelsModelsDictionaryFintoolCategoryFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_dictionary_fintool_type_category_post**
> list[EfirDataHubModelsModelsDictionaryFintoolTypeCategoryFields] v2_dictionary_fintool_type_category_post(body=body)

Метод для получения типов категорий инструментов

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
api_instance = swagger_client.DictionaryApi(swagger_client.ApiClient(configuration))
body = swagger_client.DictionaryFintooltypecategoryBody() # DictionaryFintooltypecategoryBody |  (optional)

try:
    # Метод для получения типов категорий инструментов
    api_response = api_instance.v2_dictionary_fintool_type_category_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryApi->v2_dictionary_fintool_type_category_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DictionaryFintooltypecategoryBody**](DictionaryFintooltypecategoryBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsDictionaryFintoolTypeCategoryFields]**](EfirDataHubModelsModelsDictionaryFintoolTypeCategoryFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_dictionary_holiday_types_post**
> list[EfirDataHubModelsModelsInfoHolidayTypesFields] v2_dictionary_holiday_types_post(body=body)

Справочник названий неторговых дней по странам

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
api_instance = swagger_client.DictionaryApi(swagger_client.ApiClient(configuration))
body = swagger_client.DictionaryHolidayTypesBody() # DictionaryHolidayTypesBody |  (optional)

try:
    # Справочник названий неторговых дней по странам
    api_response = api_instance.v2_dictionary_holiday_types_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryApi->v2_dictionary_holiday_types_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DictionaryHolidayTypesBody**](DictionaryHolidayTypesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoHolidayTypesFields]**](EfirDataHubModelsModelsInfoHolidayTypesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_dictionary_list_org_roles_post**
> list[EfirDataHubModelsModelsInfoListOrgRolesFields] v2_dictionary_list_org_roles_post(body=body)

Получить справочник ролей организаций

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
api_instance = swagger_client.DictionaryApi(swagger_client.ApiClient(configuration))
body = swagger_client.DictionaryListOrgRolesBody() # DictionaryListOrgRolesBody |  (optional)

try:
    # Получить справочник ролей организаций
    api_response = api_instance.v2_dictionary_list_org_roles_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryApi->v2_dictionary_list_org_roles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DictionaryListOrgRolesBody**](DictionaryListOrgRolesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoListOrgRolesFields]**](EfirDataHubModelsModelsInfoListOrgRolesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_dictionary_list_ratings_post**
> list[EfirDataHubModelsModelsRatingListRatingsFields] v2_dictionary_list_ratings_post(body=body)

Список рейтингов

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
api_instance = swagger_client.DictionaryApi(swagger_client.ApiClient(configuration))
body = swagger_client.DictionaryListRatingsBody() # DictionaryListRatingsBody |  (optional)

try:
    # Список рейтингов
    api_response = api_instance.v2_dictionary_list_ratings_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryApi->v2_dictionary_list_ratings_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DictionaryListRatingsBody**](DictionaryListRatingsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingListRatingsFields]**](EfirDataHubModelsModelsRatingListRatingsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_dictionary_liter_list_post**
> list[EfirDataHubModelsModelsInfoLiterListFields] v2_dictionary_liter_list_post(body=body)

Метод для получения справочника литеров

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
api_instance = swagger_client.DictionaryApi(swagger_client.ApiClient(configuration))
body = swagger_client.DictionaryLiterListBody() # DictionaryLiterListBody |  (optional)

try:
    # Метод для получения справочника литеров
    api_response = api_instance.v2_dictionary_liter_list_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryApi->v2_dictionary_liter_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DictionaryLiterListBody**](DictionaryLiterListBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsInfoLiterListFields]**](EfirDataHubModelsModelsInfoLiterListFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_dictionary_market_sectors_post**
> list[EfirDataHubModelsModelsDictionaryMarketSectorsFields] v2_dictionary_market_sectors_post(body=body)

Возвращает перечень секторов рынка по различным классификаторам

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
api_instance = swagger_client.DictionaryApi(swagger_client.ApiClient(configuration))
body = swagger_client.DictionaryMarketSectorsBody() # DictionaryMarketSectorsBody |  (optional)

try:
    # Возвращает перечень секторов рынка по различным классификаторам
    api_response = api_instance.v2_dictionary_market_sectors_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryApi->v2_dictionary_market_sectors_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DictionaryMarketSectorsBody**](DictionaryMarketSectorsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsDictionaryMarketSectorsFields]**](EfirDataHubModelsModelsDictionaryMarketSectorsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_dictionary_moex_boards_post**
> EfirDataHubModelsModelsMoexBoardsResponse v2_dictionary_moex_boards_post()

Список торговых площадок Московской биржи

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
api_instance = swagger_client.DictionaryApi(swagger_client.ApiClient(configuration))

try:
    # Список торговых площадок Московской биржи
    api_response = api_instance.v2_dictionary_moex_boards_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryApi->v2_dictionary_moex_boards_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EfirDataHubModelsModelsMoexBoardsResponse**](EfirDataHubModelsModelsMoexBoardsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_dictionary_rating_scale_values_post**
> list[EfirDataHubModelsModelsRatingScaleValueFields] v2_dictionary_rating_scale_values_post(body=body)

Список шкал значений рейтингов

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
api_instance = swagger_client.DictionaryApi(swagger_client.ApiClient(configuration))
body = swagger_client.DictionaryRatingScaleValuesBody() # DictionaryRatingScaleValuesBody |  (optional)

try:
    # Список шкал значений рейтингов
    api_response = api_instance.v2_dictionary_rating_scale_values_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryApi->v2_dictionary_rating_scale_values_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DictionaryRatingScaleValuesBody**](DictionaryRatingScaleValuesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingScaleValueFields]**](EfirDataHubModelsModelsRatingScaleValueFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_dictionary_rating_scales_post**
> list[EfirDataHubModelsModelsRatingScaleFields] v2_dictionary_rating_scales_post(body=body)

Список рейтинговых шкал

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
api_instance = swagger_client.DictionaryApi(swagger_client.ApiClient(configuration))
body = swagger_client.DictionaryRatingScalesBody() # DictionaryRatingScalesBody |  (optional)

try:
    # Список рейтинговых шкал
    api_response = api_instance.v2_dictionary_rating_scales_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryApi->v2_dictionary_rating_scales_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DictionaryRatingScalesBody**](DictionaryRatingScalesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingScaleFields]**](EfirDataHubModelsModelsRatingScaleFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_dictionary_regions_post**
> list[EfirDataHubModelsModelsDictionaryRegionsFields] v2_dictionary_regions_post(body=body)

Возвращает справочник регионов

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
api_instance = swagger_client.DictionaryApi(swagger_client.ApiClient(configuration))
body = swagger_client.DictionaryRegionsBody() # DictionaryRegionsBody |  (optional)

try:
    # Возвращает справочник регионов
    api_response = api_instance.v2_dictionary_regions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryApi->v2_dictionary_regions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DictionaryRegionsBody**](DictionaryRegionsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsDictionaryRegionsFields]**](EfirDataHubModelsModelsDictionaryRegionsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

