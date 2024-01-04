# swagger_client.AffiliateApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_affiliate_company_group_chains_post**](AffiliateApi.md#v2_affiliate_company_group_chains_post) | **POST** /v2/Affiliate/CompanyGroupChains | Получить информацию о цепочке связей компании
[**v2_affiliate_company_group_members_post**](AffiliateApi.md#v2_affiliate_company_group_members_post) | **POST** /v2/Affiliate/CompanyGroupMembers | Получить информацию о принадлежности компаний к группам компаний
[**v2_affiliate_company_group_relations_post**](AffiliateApi.md#v2_affiliate_company_group_relations_post) | **POST** /v2/Affiliate/CompanyGroupRelations | Возвращает описание отношений в группах компаний
[**v2_affiliate_company_groups_post**](AffiliateApi.md#v2_affiliate_company_groups_post) | **POST** /v2/Affiliate/CompanyGroups | Получить состав групп по идентификаторам групп
[**v2_affiliate_fininst_id_list_post**](AffiliateApi.md#v2_affiliate_fininst_id_list_post) | **POST** /v2/Affiliate/{fininstId}/list | Возвращает список аффилированных лиц и организаций для указанной компании на заданную дату
[**v2_affiliate_fininst_id_reports_post**](AffiliateApi.md#v2_affiliate_fininst_id_reports_post) | **POST** /v2/Affiliate/{fininstId}/reports | Возвращает список ссылок на исходные отчеты по аффилированным лицам
[**v2_affiliate_types_post**](AffiliateApi.md#v2_affiliate_types_post) | **POST** /v2/Affiliate/types | Возвращает справочник типов аффилированности

# **v2_affiliate_company_group_chains_post**
> list[EfirDataHubModelsModelsEmitentCompanyGroupsChainsFieldsBase] v2_affiliate_company_group_chains_post(body=body)

Получить информацию о цепочке связей компании

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
api_instance = swagger_client.AffiliateApi(swagger_client.ApiClient(configuration))
body = swagger_client.AffiliateCompanyGroupChainsBody() # AffiliateCompanyGroupChainsBody |  (optional)

try:
    # Получить информацию о цепочке связей компании
    api_response = api_instance.v2_affiliate_company_group_chains_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AffiliateApi->v2_affiliate_company_group_chains_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AffiliateCompanyGroupChainsBody**](AffiliateCompanyGroupChainsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentCompanyGroupsChainsFieldsBase]**](EfirDataHubModelsModelsEmitentCompanyGroupsChainsFieldsBase.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_affiliate_company_group_members_post**
> list[EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields] v2_affiliate_company_group_members_post(body=body)

Получить информацию о принадлежности компаний к группам компаний

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
api_instance = swagger_client.AffiliateApi(swagger_client.ApiClient(configuration))
body = swagger_client.AffiliateCompanyGroupMembersBody() # AffiliateCompanyGroupMembersBody |  (optional)

try:
    # Получить информацию о принадлежности компаний к группам компаний
    api_response = api_instance.v2_affiliate_company_group_members_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AffiliateApi->v2_affiliate_company_group_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AffiliateCompanyGroupMembersBody**](AffiliateCompanyGroupMembersBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields]**](EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_affiliate_company_group_relations_post**
> list[EfirDataHubModelsModelsAffiliatesCompanyGroupRelationsFields] v2_affiliate_company_group_relations_post(body=body)

Возвращает описание отношений в группах компаний

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
api_instance = swagger_client.AffiliateApi(swagger_client.ApiClient(configuration))
body = swagger_client.AffiliateCompanyGroupRelationsBody() # AffiliateCompanyGroupRelationsBody |  (optional)

try:
    # Возвращает описание отношений в группах компаний
    api_response = api_instance.v2_affiliate_company_group_relations_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AffiliateApi->v2_affiliate_company_group_relations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AffiliateCompanyGroupRelationsBody**](AffiliateCompanyGroupRelationsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsAffiliatesCompanyGroupRelationsFields]**](EfirDataHubModelsModelsAffiliatesCompanyGroupRelationsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_affiliate_company_groups_post**
> list[EfirDataHubModelsModelsEmitentCompanyGroupsMembersFields] v2_affiliate_company_groups_post(body=body)

Получить состав групп по идентификаторам групп

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
api_instance = swagger_client.AffiliateApi(swagger_client.ApiClient(configuration))
body = swagger_client.AffiliateCompanyGroupsBody() # AffiliateCompanyGroupsBody |  (optional)

try:
    # Получить состав групп по идентификаторам групп
    api_response = api_instance.v2_affiliate_company_groups_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AffiliateApi->v2_affiliate_company_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AffiliateCompanyGroupsBody**](AffiliateCompanyGroupsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsEmitentCompanyGroupsMembersFields]**](EfirDataHubModelsModelsEmitentCompanyGroupsMembersFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_affiliate_fininst_id_list_post**
> list[EfirDataHubModelsModelsAffiliatesListFields] v2_affiliate_fininst_id_list_post(fininst_id, body=body)

Возвращает список аффилированных лиц и организаций для указанной компании на заданную дату

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
api_instance = swagger_client.AffiliateApi(swagger_client.ApiClient(configuration))
fininst_id = 789 # int | Идентификатор компании в БД Интерфакс
body = swagger_client.FininstIdListBody() # FininstIdListBody |  (optional)

try:
    # Возвращает список аффилированных лиц и организаций для указанной компании на заданную дату
    api_response = api_instance.v2_affiliate_fininst_id_list_post(fininst_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AffiliateApi->v2_affiliate_fininst_id_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fininst_id** | **int**| Идентификатор компании в БД Интерфакс | 
 **body** | [**FininstIdListBody**](FininstIdListBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsAffiliatesListFields]**](EfirDataHubModelsModelsAffiliatesListFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_affiliate_fininst_id_reports_post**
> list[EfirDataHubModelsModelsAffiliatesReportsFields] v2_affiliate_fininst_id_reports_post(fininst_id, body=body)

Возвращает список ссылок на исходные отчеты по аффилированным лицам

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
api_instance = swagger_client.AffiliateApi(swagger_client.ApiClient(configuration))
fininst_id = 789 # int | Идентификатор компании в БД Интерфакс
body = swagger_client.FininstIdReportsBody() # FininstIdReportsBody |  (optional)

try:
    # Возвращает список ссылок на исходные отчеты по аффилированным лицам
    api_response = api_instance.v2_affiliate_fininst_id_reports_post(fininst_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AffiliateApi->v2_affiliate_fininst_id_reports_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fininst_id** | **int**| Идентификатор компании в БД Интерфакс | 
 **body** | [**FininstIdReportsBody**](FininstIdReportsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsAffiliatesReportsFields]**](EfirDataHubModelsModelsAffiliatesReportsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_affiliate_types_post**
> list[EfirDataHubModelsModelsAffiliatesTypesFields] v2_affiliate_types_post()

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
api_instance = swagger_client.AffiliateApi(swagger_client.ApiClient(configuration))

try:
    # Возвращает справочник типов аффилированности
    api_response = api_instance.v2_affiliate_types_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AffiliateApi->v2_affiliate_types_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EfirDataHubModelsModelsAffiliatesTypesFields]**](EfirDataHubModelsModelsAffiliatesTypesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

