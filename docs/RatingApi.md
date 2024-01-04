# swagger_client.RatingApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_rating_aggregation_list_post**](RatingApi.md#v2_rating_aggregation_list_post) | **POST** /v2/Rating/AggregationList | Возвращает рейтинги, включенные в заданный список
[**v2_rating_aggregation_lists_post**](RatingApi.md#v2_rating_aggregation_lists_post) | **POST** /v2/Rating/AggregationLists | Возвращает списки рейтингов
[**v2_rating_aggregation_scale_ratio_post**](RatingApi.md#v2_rating_aggregation_scale_ratio_post) | **POST** /v2/Rating/AggregationScaleRatio | Возвращает соотношение рейтинговых шкал RU и BIG3
[**v2_rating_aggregation_scale_ratios_post**](RatingApi.md#v2_rating_aggregation_scale_ratios_post) | **POST** /v2/Rating/AggregationScaleRatios | Возвращает соотношения рейтинговых шкал RU и BIG3
[**v2_rating_company_ratings_agg_post**](RatingApi.md#v2_rating_company_ratings_agg_post) | **POST** /v2/Rating/CompanyRatingsAgg | Метод позволяет получить таблицу с данными по уровням рейтингов на заданную дату по одной или нескольким компаниям.
[**v2_rating_company_ratings_agg_v2_post**](RatingApi.md#v2_rating_company_ratings_agg_v2_post) | **POST** /v2/Rating/CompanyRatingsAgg_v2 | Метод позволяет получить структуру с данными по уровням рейтингов на заданную дату по одной или нескольким компаниям.
[**v2_rating_company_ratings_hist_id_post**](RatingApi.md#v2_rating_company_ratings_hist_id_post) | **POST** /v2/Rating/CompanyRatingsHist/{id} | Получить рейтинги компании за период.
[**v2_rating_company_ratings_hist_post**](RatingApi.md#v2_rating_company_ratings_hist_post) | **POST** /v2/Rating/CompanyRatingsHist | Получить все рейтинги компании за период, но не более чем за неделю (с dateTo-6 по dateTo)
[**v2_rating_company_ratings_id_post**](RatingApi.md#v2_rating_company_ratings_id_post) | **POST** /v2/Rating/CompanyRatings/{id} | Получить рейтинги компании на заданную дату.
[**v2_rating_company_ratings_table_post**](RatingApi.md#v2_rating_company_ratings_table_post) | **POST** /v2/Rating/CompanyRatingsTable | Получить рейтинги нескольких компаний на заданную дату.
[**v2_rating_custom_agg_company_by_agency_post**](RatingApi.md#v2_rating_custom_agg_company_by_agency_post) | **POST** /v2/Rating/CustomAggCompanyByAgency | Агрегированные рейтинги компаний по агентствам
[**v2_rating_custom_agg_company_post**](RatingApi.md#v2_rating_custom_agg_company_post) | **POST** /v2/Rating/CustomAggCompany | Агрегированные рейтинги компаний
[**v2_rating_custom_agg_security_by_agency_post**](RatingApi.md#v2_rating_custom_agg_security_by_agency_post) | **POST** /v2/Rating/CustomAggSecurityByAgency | Агрегированные рейтинги инструментов по агентствам
[**v2_rating_custom_agg_security_by_role_post**](RatingApi.md#v2_rating_custom_agg_security_by_role_post) | **POST** /v2/Rating/CustomAggSecurityByRole | Агрегированные по ролям организаторов выпуска рейтинги ценных бумаг
[**v2_rating_custom_agg_security_post**](RatingApi.md#v2_rating_custom_agg_security_post) | **POST** /v2/Rating/CustomAggSecurity | Агрегированные рейтинги инструментов
[**v2_rating_list_companies_post**](RatingApi.md#v2_rating_list_companies_post) | **POST** /v2/Rating/ListCompanies | Получить список компаний (не рекомендуется к использованию, надо использовать /Info/Emitents).
[**v2_rating_list_ratings_post**](RatingApi.md#v2_rating_list_ratings_post) | **POST** /v2/Rating/ListRatings | Получить список рейтингов.
[**v2_rating_list_scale_values_post**](RatingApi.md#v2_rating_list_scale_values_post) | **POST** /v2/Rating/ListScaleValues | Список шкал значений рейтингов
[**v2_rating_list_scales_post**](RatingApi.md#v2_rating_list_scales_post) | **POST** /v2/Rating/ListScales | Список рейтинговых шкал
[**v2_rating_list_securities_post**](RatingApi.md#v2_rating_list_securities_post) | **POST** /v2/Rating/ListSecurities | Получить список финансовых инструментов (не рекомендуется к использованию, надо использовать /Info/Securities; именно этот метод будет развиваться).
[**v2_rating_ratings_history_post**](RatingApi.md#v2_rating_ratings_history_post) | **POST** /v2/Rating/RatingsHistory | Получить рейтинговые события за период.
[**v2_rating_security_rating_table_post**](RatingApi.md#v2_rating_security_rating_table_post) | **POST** /v2/Rating/SecurityRatingTable | Получить рейтинги нескольких бумаг и связанных с ними компаний на заданную дату.
[**v2_rating_security_ratings_agg_post**](RatingApi.md#v2_rating_security_ratings_agg_post) | **POST** /v2/Rating/SecurityRatingsAgg | Метод позволяет получить таблицу с данными по уровням рейтингов на заданную дату по одному или нескольким инструментам
[**v2_rating_security_ratings_agg_v2_post**](RatingApi.md#v2_rating_security_ratings_agg_v2_post) | **POST** /v2/Rating/SecurityRatingsAgg_v2 | Метод позволяет получить структуру с данными по уровням рейтингов на заданную дату по одному или нескольким инструментам
[**v2_rating_security_ratings_fintool_id_post**](RatingApi.md#v2_rating_security_ratings_fintool_id_post) | **POST** /v2/Rating/SecurityRatings/{fintoolId} | Получить рейтинги инструмента, его эмитента и основных организаторов выпуска по FintoolId
[**v2_rating_security_ratings_hist_post**](RatingApi.md#v2_rating_security_ratings_hist_post) | **POST** /v2/Rating/SecurityRatingsHist | Получить рейтинги инструмента, его эмитента и основных организаторов выпуска.
[**v2_rating_security_ratings_post**](RatingApi.md#v2_rating_security_ratings_post) | **POST** /v2/Rating/SecurityRatings | Получить рейтинги инструмента, его эмитента и основных организаторов выпуска по ISIN
[**v2_rating_surety_ratings_agg_post**](RatingApi.md#v2_rating_surety_ratings_agg_post) | **POST** /v2/Rating/SuretyRatingsAgg | Позволяет получить таблицу с данными по уровням рейтингов на заданную дату для гарантов/поручителей одного или нескольких инструментов.
[**v2_rating_surety_ratings_agg_v2_post**](RatingApi.md#v2_rating_surety_ratings_agg_v2_post) | **POST** /v2/Rating/SuretyRatingsAgg_v2 | Позволяет получить структуру с данными по уровням рейтингов на заданную дату для гарантов/поручителей одного или нескольких инструментов.

# **v2_rating_aggregation_list_post**
> list[EfirDataHubModelsModelsRatingAggregationListFields] v2_rating_aggregation_list_post(body=body)

Возвращает рейтинги, включенные в заданный список

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.RatingAggregationListBody() # RatingAggregationListBody |  (optional)

try:
    # Возвращает рейтинги, включенные в заданный список
    api_response = api_instance.v2_rating_aggregation_list_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_aggregation_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingAggregationListBody**](RatingAggregationListBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingAggregationListFields]**](EfirDataHubModelsModelsRatingAggregationListFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_aggregation_lists_post**
> list[EfirDataHubModelsModelsRatingAggregationList] v2_rating_aggregation_lists_post()

Возвращает списки рейтингов

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))

try:
    # Возвращает списки рейтингов
    api_response = api_instance.v2_rating_aggregation_lists_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_aggregation_lists_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EfirDataHubModelsModelsRatingAggregationList]**](EfirDataHubModelsModelsRatingAggregationList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_aggregation_scale_ratio_post**
> list[EfirDataHubModelsModelsRatingAggregationScaleRatioFields] v2_rating_aggregation_scale_ratio_post(body=body)

Возвращает соотношение рейтинговых шкал RU и BIG3

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.RatingAggregationScaleRatioBody() # RatingAggregationScaleRatioBody |  (optional)

try:
    # Возвращает соотношение рейтинговых шкал RU и BIG3
    api_response = api_instance.v2_rating_aggregation_scale_ratio_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_aggregation_scale_ratio_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingAggregationScaleRatioBody**](RatingAggregationScaleRatioBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingAggregationScaleRatioFields]**](EfirDataHubModelsModelsRatingAggregationScaleRatioFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_aggregation_scale_ratios_post**
> list[EfirDataHubModelsModelsRatingAggregationScaleMappingFields] v2_rating_aggregation_scale_ratios_post()

Возвращает соотношения рейтинговых шкал RU и BIG3

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))

try:
    # Возвращает соотношения рейтинговых шкал RU и BIG3
    api_response = api_instance.v2_rating_aggregation_scale_ratios_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_aggregation_scale_ratios_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EfirDataHubModelsModelsRatingAggregationScaleMappingFields]**](EfirDataHubModelsModelsRatingAggregationScaleMappingFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_company_ratings_agg_post**
> list[EfirDataHubModelsModelsRatingCompanyRatingsAggFields] v2_rating_company_ratings_agg_post(body=body)

Метод позволяет получить таблицу с данными по уровням рейтингов на заданную дату по одной или нескольким компаниям.

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.RatingCompanyRatingsAggBody() # RatingCompanyRatingsAggBody |  (optional)

try:
    # Метод позволяет получить таблицу с данными по уровням рейтингов на заданную дату по одной или нескольким компаниям.
    api_response = api_instance.v2_rating_company_ratings_agg_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_company_ratings_agg_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingCompanyRatingsAggBody**](RatingCompanyRatingsAggBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingCompanyRatingsAggFields]**](EfirDataHubModelsModelsRatingCompanyRatingsAggFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_company_ratings_agg_v2_post**
> EfirDataHubModelsModelsRatingCompanyRatingsAggV2Response v2_rating_company_ratings_agg_v2_post(body=body)

Метод позволяет получить структуру с данными по уровням рейтингов на заданную дату по одной или нескольким компаниям.

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.RatingCompanyRatingsAggV2Body() # RatingCompanyRatingsAggV2Body |  (optional)

try:
    # Метод позволяет получить структуру с данными по уровням рейтингов на заданную дату по одной или нескольким компаниям.
    api_response = api_instance.v2_rating_company_ratings_agg_v2_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_company_ratings_agg_v2_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingCompanyRatingsAggV2Body**](RatingCompanyRatingsAggV2Body.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsRatingCompanyRatingsAggV2Response**](EfirDataHubModelsModelsRatingCompanyRatingsAggV2Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_company_ratings_hist_id_post**
> list[EfirDataHubModelsModelsRatingCompanyRatingsHistFields] v2_rating_company_ratings_hist_id_post(id, body=body)

Получить рейтинги компании за период.

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Идентификатор компании в базе Интерфакс FinInstID.
body = swagger_client.CompanyRatingsHistIdBody() # CompanyRatingsHistIdBody |  (optional)

try:
    # Получить рейтинги компании за период.
    api_response = api_instance.v2_rating_company_ratings_hist_id_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_company_ratings_hist_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Идентификатор компании в базе Интерфакс FinInstID. | 
 **body** | [**CompanyRatingsHistIdBody**](CompanyRatingsHistIdBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingCompanyRatingsHistFields]**](EfirDataHubModelsModelsRatingCompanyRatingsHistFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_company_ratings_hist_post**
> list[EfirDataHubModelsModelsRatingCompanyRatingsHistFields] v2_rating_company_ratings_hist_post(body=body)

Получить все рейтинги компании за период, но не более чем за неделю (с dateTo-6 по dateTo)

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.RatingCompanyRatingsHistBody() # RatingCompanyRatingsHistBody |  (optional)

try:
    # Получить все рейтинги компании за период, но не более чем за неделю (с dateTo-6 по dateTo)
    api_response = api_instance.v2_rating_company_ratings_hist_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_company_ratings_hist_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingCompanyRatingsHistBody**](RatingCompanyRatingsHistBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingCompanyRatingsHistFields]**](EfirDataHubModelsModelsRatingCompanyRatingsHistFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_company_ratings_id_post**
> list[EfirDataHubModelsModelsRatingCompanyRatingsFields] v2_rating_company_ratings_id_post(id, body=body)

Получить рейтинги компании на заданную дату.

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Код страны (обозначение по ISO 3166-1 Alpha-3 или ISO 3166-1 Alpha-2) или код организации по ОКПО/ОГРН, ИНН либо ID зарубежной организации (FinInstID).
body = swagger_client.CompanyRatingsIdBody() # CompanyRatingsIdBody |  (optional)

try:
    # Получить рейтинги компании на заданную дату.
    api_response = api_instance.v2_rating_company_ratings_id_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_company_ratings_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Код страны (обозначение по ISO 3166-1 Alpha-3 или ISO 3166-1 Alpha-2) или код организации по ОКПО/ОГРН, ИНН либо ID зарубежной организации (FinInstID). | 
 **body** | [**CompanyRatingsIdBody**](CompanyRatingsIdBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingCompanyRatingsFields]**](EfirDataHubModelsModelsRatingCompanyRatingsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_company_ratings_table_post**
> list[EfirDataHubModelsModelsRatingCompanyRatingsTableFields] v2_rating_company_ratings_table_post(body=body)

Получить рейтинги нескольких компаний на заданную дату.

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.RatingCompanyRatingsTableBody() # RatingCompanyRatingsTableBody |  (optional)

try:
    # Получить рейтинги нескольких компаний на заданную дату.
    api_response = api_instance.v2_rating_company_ratings_table_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_company_ratings_table_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingCompanyRatingsTableBody**](RatingCompanyRatingsTableBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingCompanyRatingsTableFields]**](EfirDataHubModelsModelsRatingCompanyRatingsTableFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_custom_agg_company_by_agency_post**
> list[EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields] v2_rating_custom_agg_company_by_agency_post(body=body)

Агрегированные рейтинги компаний по агентствам

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.RatingCustomAggCompanyByAgencyBody() # RatingCustomAggCompanyByAgencyBody |  (optional)

try:
    # Агрегированные рейтинги компаний по агентствам
    api_response = api_instance.v2_rating_custom_agg_company_by_agency_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_custom_agg_company_by_agency_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingCustomAggCompanyByAgencyBody**](RatingCustomAggCompanyByAgencyBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields]**](EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_custom_agg_company_post**
> list[EfirDataHubModelsModelsRatingRatingAggCompanyFields] v2_rating_custom_agg_company_post(body=body)

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.RatingCustomAggCompanyBody() # RatingCustomAggCompanyBody |  (optional)

try:
    # Агрегированные рейтинги компаний
    api_response = api_instance.v2_rating_custom_agg_company_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_custom_agg_company_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingCustomAggCompanyBody**](RatingCustomAggCompanyBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingRatingAggCompanyFields]**](EfirDataHubModelsModelsRatingRatingAggCompanyFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_custom_agg_security_by_agency_post**
> list[EfirDataHubModelsModelsRatingRatingSecurityByAgenciesFields] v2_rating_custom_agg_security_by_agency_post(body=body)

Агрегированные рейтинги инструментов по агентствам

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.RatingCustomAggSecurityByAgencyBody() # RatingCustomAggSecurityByAgencyBody |  (optional)

try:
    # Агрегированные рейтинги инструментов по агентствам
    api_response = api_instance.v2_rating_custom_agg_security_by_agency_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_custom_agg_security_by_agency_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingCustomAggSecurityByAgencyBody**](RatingCustomAggSecurityByAgencyBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingRatingSecurityByAgenciesFields]**](EfirDataHubModelsModelsRatingRatingSecurityByAgenciesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_custom_agg_security_by_role_post**
> list[EfirDataHubModelsModelsRatingRatingAggSecurityByRoleFields] v2_rating_custom_agg_security_by_role_post(body=body)

Агрегированные по ролям организаторов выпуска рейтинги ценных бумаг

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.RatingCustomAggSecurityByRoleBody() # RatingCustomAggSecurityByRoleBody |  (optional)

try:
    # Агрегированные по ролям организаторов выпуска рейтинги ценных бумаг
    api_response = api_instance.v2_rating_custom_agg_security_by_role_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_custom_agg_security_by_role_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingCustomAggSecurityByRoleBody**](RatingCustomAggSecurityByRoleBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingRatingAggSecurityByRoleFields]**](EfirDataHubModelsModelsRatingRatingAggSecurityByRoleFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_custom_agg_security_post**
> list[EfirDataHubModelsModelsRatingRatingAggSecurityFields] v2_rating_custom_agg_security_post(body=body)

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.RatingCustomAggSecurityBody() # RatingCustomAggSecurityBody |  (optional)

try:
    # Агрегированные рейтинги инструментов
    api_response = api_instance.v2_rating_custom_agg_security_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_custom_agg_security_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingCustomAggSecurityBody**](RatingCustomAggSecurityBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingRatingAggSecurityFields]**](EfirDataHubModelsModelsRatingRatingAggSecurityFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_list_companies_post**
> list[EfirDataHubModelsModelsRatingListCompaniesFields] v2_rating_list_companies_post(body=body)

Получить список компаний (не рекомендуется к использованию, надо использовать /Info/Emitents).

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.RatingListCompaniesBody() # RatingListCompaniesBody |  (optional)

try:
    # Получить список компаний (не рекомендуется к использованию, надо использовать /Info/Emitents).
    api_response = api_instance.v2_rating_list_companies_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_list_companies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingListCompaniesBody**](RatingListCompaniesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingListCompaniesFields]**](EfirDataHubModelsModelsRatingListCompaniesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_list_ratings_post**
> list[EfirDataHubModelsModelsRatingListRatingsFields] v2_rating_list_ratings_post(body=body)

Получить список рейтингов.

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.RatingListRatingsBody() # RatingListRatingsBody |  (optional)

try:
    # Получить список рейтингов.
    api_response = api_instance.v2_rating_list_ratings_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_list_ratings_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingListRatingsBody**](RatingListRatingsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingListRatingsFields]**](EfirDataHubModelsModelsRatingListRatingsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_list_scale_values_post**
> list[EfirDataHubModelsModelsRatingScaleValueFields] v2_rating_list_scale_values_post(body=body)

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.RatingListScaleValuesBody() # RatingListScaleValuesBody |  (optional)

try:
    # Список шкал значений рейтингов
    api_response = api_instance.v2_rating_list_scale_values_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_list_scale_values_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingListScaleValuesBody**](RatingListScaleValuesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingScaleValueFields]**](EfirDataHubModelsModelsRatingScaleValueFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_list_scales_post**
> list[EfirDataHubModelsModelsRatingScaleFields] v2_rating_list_scales_post(body=body)

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.RatingListScalesBody() # RatingListScalesBody |  (optional)

try:
    # Список рейтинговых шкал
    api_response = api_instance.v2_rating_list_scales_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_list_scales_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingListScalesBody**](RatingListScalesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingScaleFields]**](EfirDataHubModelsModelsRatingScaleFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_list_securities_post**
> list[EfirDataHubModelsModelsRatingListSecuritiesFields] v2_rating_list_securities_post(body=body)

Получить список финансовых инструментов (не рекомендуется к использованию, надо использовать /Info/Securities; именно этот метод будет развиваться).

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.RatingListSecuritiesBody() # RatingListSecuritiesBody |  (optional)

try:
    # Получить список финансовых инструментов (не рекомендуется к использованию, надо использовать /Info/Securities; именно этот метод будет развиваться).
    api_response = api_instance.v2_rating_list_securities_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_list_securities_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingListSecuritiesBody**](RatingListSecuritiesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingListSecuritiesFields]**](EfirDataHubModelsModelsRatingListSecuritiesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_ratings_history_post**
> list[EfirDataHubModelsModelsRatingRatingsHistoryFields] v2_rating_ratings_history_post(body=body)

Получить рейтинговые события за период.

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.RatingRatingsHistoryBody() # RatingRatingsHistoryBody |  (optional)

try:
    # Получить рейтинговые события за период.
    api_response = api_instance.v2_rating_ratings_history_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_ratings_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingRatingsHistoryBody**](RatingRatingsHistoryBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingRatingsHistoryFields]**](EfirDataHubModelsModelsRatingRatingsHistoryFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_security_rating_table_post**
> list[EfirDataHubModelsModelsRatingSecurityRatingTableFields] v2_rating_security_rating_table_post(body=body)

Получить рейтинги нескольких бумаг и связанных с ними компаний на заданную дату.

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.RatingSecurityRatingTableBody() # RatingSecurityRatingTableBody |  (optional)

try:
    # Получить рейтинги нескольких бумаг и связанных с ними компаний на заданную дату.
    api_response = api_instance.v2_rating_security_rating_table_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_security_rating_table_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingSecurityRatingTableBody**](RatingSecurityRatingTableBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingSecurityRatingTableFields]**](EfirDataHubModelsModelsRatingSecurityRatingTableFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_security_ratings_agg_post**
> list[EfirDataHubModelsModelsRatingSecurityRatingsAggFields] v2_rating_security_ratings_agg_post(body=body)

Метод позволяет получить таблицу с данными по уровням рейтингов на заданную дату по одному или нескольким инструментам

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.RatingSecurityRatingsAggBody() # RatingSecurityRatingsAggBody |  (optional)

try:
    # Метод позволяет получить таблицу с данными по уровням рейтингов на заданную дату по одному или нескольким инструментам
    api_response = api_instance.v2_rating_security_ratings_agg_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_security_ratings_agg_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingSecurityRatingsAggBody**](RatingSecurityRatingsAggBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingSecurityRatingsAggFields]**](EfirDataHubModelsModelsRatingSecurityRatingsAggFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_security_ratings_agg_v2_post**
> EfirDataHubModelsModelsRatingSecurityRatingsAggV2Response v2_rating_security_ratings_agg_v2_post(body=body)

Метод позволяет получить структуру с данными по уровням рейтингов на заданную дату по одному или нескольким инструментам

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.RatingSecurityRatingsAggV2Body() # RatingSecurityRatingsAggV2Body |  (optional)

try:
    # Метод позволяет получить структуру с данными по уровням рейтингов на заданную дату по одному или нескольким инструментам
    api_response = api_instance.v2_rating_security_ratings_agg_v2_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_security_ratings_agg_v2_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingSecurityRatingsAggV2Body**](RatingSecurityRatingsAggV2Body.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsRatingSecurityRatingsAggV2Response**](EfirDataHubModelsModelsRatingSecurityRatingsAggV2Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_security_ratings_fintool_id_post**
> list[EfirDataHubModelsModelsRatingSecurityRatingsFields] v2_rating_security_ratings_fintool_id_post(fintool_id, body=body)

Получить рейтинги инструмента, его эмитента и основных организаторов выпуска по FintoolId

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
fintool_id = 789 # int | 
body = swagger_client.SecurityRatingsFintoolIdBody() # SecurityRatingsFintoolIdBody |  (optional)

try:
    # Получить рейтинги инструмента, его эмитента и основных организаторов выпуска по FintoolId
    api_response = api_instance.v2_rating_security_ratings_fintool_id_post(fintool_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_security_ratings_fintool_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fintool_id** | **int**|  | 
 **body** | [**SecurityRatingsFintoolIdBody**](SecurityRatingsFintoolIdBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingSecurityRatingsFields]**](EfirDataHubModelsModelsRatingSecurityRatingsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_security_ratings_hist_post**
> list[EfirDataHubModelsModelsRatingSecurityRatingsHistFields] v2_rating_security_ratings_hist_post(body=body)

Получить рейтинги инструмента, его эмитента и основных организаторов выпуска.

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.RatingSecurityRatingsHistBody() # RatingSecurityRatingsHistBody |  (optional)

try:
    # Получить рейтинги инструмента, его эмитента и основных организаторов выпуска.
    api_response = api_instance.v2_rating_security_ratings_hist_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_security_ratings_hist_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingSecurityRatingsHistBody**](RatingSecurityRatingsHistBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingSecurityRatingsHistFields]**](EfirDataHubModelsModelsRatingSecurityRatingsHistFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_security_ratings_post**
> list[EfirDataHubModelsModelsRatingSecurityRatingsFields] v2_rating_security_ratings_post(body=body)

Получить рейтинги инструмента, его эмитента и основных организаторов выпуска по ISIN

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.RatingSecurityRatingsBody() # RatingSecurityRatingsBody |  (optional)

try:
    # Получить рейтинги инструмента, его эмитента и основных организаторов выпуска по ISIN
    api_response = api_instance.v2_rating_security_ratings_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_security_ratings_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingSecurityRatingsBody**](RatingSecurityRatingsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingSecurityRatingsFields]**](EfirDataHubModelsModelsRatingSecurityRatingsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_surety_ratings_agg_post**
> list[EfirDataHubModelsModelsRatingSuretyRatingsAggFields] v2_rating_surety_ratings_agg_post(body=body)

Позволяет получить таблицу с данными по уровням рейтингов на заданную дату для гарантов/поручителей одного или нескольких инструментов.

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.RatingSuretyRatingsAggBody() # RatingSuretyRatingsAggBody |  (optional)

try:
    # Позволяет получить таблицу с данными по уровням рейтингов на заданную дату для гарантов/поручителей одного или нескольких инструментов.
    api_response = api_instance.v2_rating_surety_ratings_agg_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_surety_ratings_agg_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingSuretyRatingsAggBody**](RatingSuretyRatingsAggBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRatingSuretyRatingsAggFields]**](EfirDataHubModelsModelsRatingSuretyRatingsAggFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_rating_surety_ratings_agg_v2_post**
> EfirDataHubModelsModelsRatingCompanyRatingsAggV2Response v2_rating_surety_ratings_agg_v2_post(body=body)

Позволяет получить структуру с данными по уровням рейтингов на заданную дату для гарантов/поручителей одного или нескольких инструментов.

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
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.RatingSuretyRatingsAggV2Body() # RatingSuretyRatingsAggV2Body |  (optional)

try:
    # Позволяет получить структуру с данными по уровням рейтингов на заданную дату для гарантов/поручителей одного или нескольких инструментов.
    api_response = api_instance.v2_rating_surety_ratings_agg_v2_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->v2_rating_surety_ratings_agg_v2_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingSuretyRatingsAggV2Body**](RatingSuretyRatingsAggV2Body.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsRatingCompanyRatingsAggV2Response**](EfirDataHubModelsModelsRatingCompanyRatingsAggV2Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

