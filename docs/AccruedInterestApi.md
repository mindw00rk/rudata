# swagger_client.AccruedInterestApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_accrued_interest_accrued_interest_on_date_post**](AccruedInterestApi.md#v2_accrued_interest_accrued_interest_on_date_post) | **POST** /v2/AccruedInterest/AccruedInterestOnDate | Расчет НКД на дату
[**v2_accrued_interest_accrued_interest_on_period_post**](AccruedInterestApi.md#v2_accrued_interest_accrued_interest_on_period_post) | **POST** /v2/AccruedInterest/AccruedInterestOnPeriod | Расчет НКД за период

# **v2_accrued_interest_accrued_interest_on_date_post**
> list[BondCalculatorAccruedInterestModelsAccruedInterestRecord] v2_accrued_interest_accrued_interest_on_date_post(body=body)

Расчет НКД на дату

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
api_instance = swagger_client.AccruedInterestApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccruedInterestAccruedInterestOnDateBody() # AccruedInterestAccruedInterestOnDateBody |  (optional)

try:
    # Расчет НКД на дату
    api_response = api_instance.v2_accrued_interest_accrued_interest_on_date_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccruedInterestApi->v2_accrued_interest_accrued_interest_on_date_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccruedInterestAccruedInterestOnDateBody**](AccruedInterestAccruedInterestOnDateBody.md)|  | [optional] 

### Return type

[**list[BondCalculatorAccruedInterestModelsAccruedInterestRecord]**](BondCalculatorAccruedInterestModelsAccruedInterestRecord.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_accrued_interest_accrued_interest_on_period_post**
> list[BondCalculatorAccruedInterestModelsAccruedInterestRecord] v2_accrued_interest_accrued_interest_on_period_post(body=body)

Расчет НКД за период

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
api_instance = swagger_client.AccruedInterestApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccruedInterestAccruedInterestOnPeriodBody() # AccruedInterestAccruedInterestOnPeriodBody |  (optional)

try:
    # Расчет НКД за период
    api_response = api_instance.v2_accrued_interest_accrued_interest_on_period_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccruedInterestApi->v2_accrued_interest_accrued_interest_on_period_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccruedInterestAccruedInterestOnPeriodBody**](AccruedInterestAccruedInterestOnPeriodBody.md)|  | [optional] 

### Return type

[**list[BondCalculatorAccruedInterestModelsAccruedInterestRecord]**](BondCalculatorAccruedInterestModelsAccruedInterestRecord.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

