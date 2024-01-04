# swagger_client.RiskApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_risk2_liquidity_adjustment_post**](RiskApi.md#v2_risk2_liquidity_adjustment_post) | **POST** /v2/Risk/2/LiquidityAdjustment | 
[**v2_risk_amortisations_by_id_post**](RiskApi.md#v2_risk_amortisations_by_id_post) | **POST** /v2/Risk/AmortisationsById | Получить график погашения по FintoolId.
[**v2_risk_amortisations_post**](RiskApi.md#v2_risk_amortisations_post) | **POST** /v2/Risk/Amortisations | Получить график погашения.
[**v2_risk_bank_basel_class_post**](RiskApi.md#v2_risk_bank_basel_class_post) | **POST** /v2/Risk/BankBaselClass | Возвращает классификацию банков по классам \&quot;Базель III\&quot;
[**v2_risk_bank_norm_rule_post**](RiskApi.md#v2_risk_bank_norm_rule_post) | **POST** /v2/Risk/BankNormRule | Возвращает правило определения группы актива согласно инструкциям ЦБ РФ об обязательных нормативах банков.
[**v2_risk_capital_adequacy_finalized_post**](RiskApi.md#v2_risk_capital_adequacy_finalized_post) | **POST** /v2/Risk/capital-adequacy-finalized | Возвращает классификатор финансового инструмента и коэффициент риска для взвешивания в капитале, их расшифровку:  обоснование (номер и абзац пункта из нормативного акта),  принадлежность к ПК (операции с повышенным коэффициентам риска),  агрегат RWA и код актива по финализированному подходу,  в соответствии с инструкцией Банка России (199-И).  Метод не распространяется на активы фондов, производные финансовые инструменты.
[**v2_risk_capital_adequacy_params_post**](RiskApi.md#v2_risk_capital_adequacy_params_post) | **POST** /v2/Risk/CapitalAdequacyParams | Получить классификатор инструмента и коэффициент кредитного риска, их расшифровку: обоснование (номер абзаца), группу риска и код, в соответствии с инструкцией, актуальной на дату расчета (ЦБ 180-И или 139-И).
[**v2_risk_corp_invest_class_post**](RiskApi.md#v2_risk_corp_invest_class_post) | **POST** /v2/Risk/CorpInvestClass | Возвращает информацию о принадлежности компании к инвестиционному классу в соответствии с рекомендациями \&quot;Базель III\&quot;
[**v2_risk_coupon_yield_post**](RiskApi.md#v2_risk_coupon_yield_post) | **POST** /v2/Risk/CouponYield | Получить доходность инструмента для расчета рисков. Актуально для облигаций и привилегированных акций.
[**v2_risk_equity_risk_rate_post**](RiskApi.md#v2_risk_equity_risk_rate_post) | **POST** /v2/Risk/EquityRiskRate | Получить коэффициент риска.
[**v2_risk_fair_value_post**](RiskApi.md#v2_risk_fair_value_post) | **POST** /v2/Risk/FairValue | Получить справедливую цену.
[**v2_risk_fintools_risk_group_params_post**](RiskApi.md#v2_risk_fintools_risk_group_params_post) | **POST** /v2/Risk/FintoolsRiskGroupParams | Получить все или фильтрованные значения параметров группы риска для списка инструментов
[**v2_risk_frozen_risk_group_params_post**](RiskApi.md#v2_risk_frozen_risk_group_params_post) | **POST** /v2/Risk/FrozenRiskGroupParams | 
[**v2_risk_info_shocks_post**](RiskApi.md#v2_risk_info_shocks_post) | **POST** /v2/Risk/InfoShocks | Возвращает правило определения группы актива согласно инструкциям ЦБ РФ об обязательных нормативах банков.
[**v2_risk_instrument_has_risk_post**](RiskApi.md#v2_risk_instrument_has_risk_post) | **POST** /v2/Risk/InstrumentHasRisk | Наличие процентного и фондового рисков.
[**v2_risk_liquidity_adjustment_post**](RiskApi.md#v2_risk_liquidity_adjustment_post) | **POST** /v2/Risk/LiquidityAdjustment | Получить таблицу с коэффициентами корректировки ликвидности на заданную дату по одной или нескольким облигациям.
[**v2_risk_liquidity_params_post**](RiskApi.md#v2_risk_liquidity_params_post) | **POST** /v2/Risk/LiquidityParams | Получить параметры ликвидности инструмента на заданную дату.
[**v2_risk_liquidity_rating_post**](RiskApi.md#v2_risk_liquidity_rating_post) | **POST** /v2/Risk/LiquidityRating | Получить таблицу с данными по рейтингу ликвидности и используемым для его вычисления параметрам на заданную дату по одной или нескольким облигациям.
[**v2_risk_market_risk_data_post**](RiskApi.md#v2_risk_market_risk_data_post) | **POST** /v2/Risk/MarketRiskData | Получить данные для расчета рыночного риска.
[**v2_risk_nominal_currency_post**](RiskApi.md#v2_risk_nominal_currency_post) | **POST** /v2/Risk/NominalCurrency | Валюта номинала.
[**v2_risk_option_params_post**](RiskApi.md#v2_risk_option_params_post) | **POST** /v2/Risk/OptionParams | Получить параметры опциона.
[**v2_risk_option_values_post**](RiskApi.md#v2_risk_option_values_post) | **POST** /v2/Risk/OptionValues | Получить расчетные параметры опциона на заданную дату.
[**v2_risk_pfi_params_post**](RiskApi.md#v2_risk_pfi_params_post) | **POST** /v2/Risk/PfiParams | Параметры производных финансовых инструментов.
[**v2_risk_repo_discount139_post**](RiskApi.md#v2_risk_repo_discount139_post) | **POST** /v2/Risk/RepoDiscount139 | Определение величины дисконта для расчета риска по операциям РЕПО в соответствии с инструкцией 139-И.
[**v2_risk_risk_date_post**](RiskApi.md#v2_risk_risk_date_post) | **POST** /v2/Risk/RiskDate | Получить дату, по которой вычисляется группа срочности.
[**v2_risk_risk_group_param_post**](RiskApi.md#v2_risk_risk_group_param_post) | **POST** /v2/Risk/RiskGroupParam | Получить значение параметра для определения группы риска.
[**v2_risk_risk_group_params_post**](RiskApi.md#v2_risk_risk_group_params_post) | **POST** /v2/Risk/RiskGroupParams | Получить все или фильтрованные значения параметров группы риска для инструмента
[**v2_risk_risk_group_post**](RiskApi.md#v2_risk_risk_group_post) | **POST** /v2/Risk/RiskGroup | Получить группу риска для инструмента
[**v2_risk_risk_group_rule_post**](RiskApi.md#v2_risk_risk_group_rule_post) | **POST** /v2/Risk/RiskGroupRule | Определить правило группы риска по положению 387-П.
[**v2_risk_rule139_post**](RiskApi.md#v2_risk_rule139_post) | **POST** /v2/Risk/Rule139 | Определить правило по инструкции 139-И.
[**v2_risk_rule421_post**](RiskApi.md#v2_risk_rule421_post) | **POST** /v2/Risk/Rule421 | Определить правило по положению 421-П.
[**v2_risk_rule_hla_post**](RiskApi.md#v2_risk_rule_hla_post) | **POST** /v2/Risk/RuleHLA | Возвращает значения обесценения на дату
[**v2_risk_var_data_post**](RiskApi.md#v2_risk_var_data_post) | **POST** /v2/Risk/VarData | Возвращает массив значений, необходимых для расчета показателей риска VaR (Value at Risk) или ES (Expected Shortfall) по одному инструменту.
[**v2_risk_var_matrix_post**](RiskApi.md#v2_risk_var_matrix_post) | **POST** /v2/Risk/VarMatrix | Получить VaR матрицу корреляции и ковариации на определенную дату

# **v2_risk2_liquidity_adjustment_post**
> EfirDataHubModelsModelsRiskLiquidityAdjustmentResponse v2_risk2_liquidity_adjustment_post(body=body)



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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.Model2LiquidityAdjustmentBody() # Model2LiquidityAdjustmentBody |  (optional)

try:
    api_response = api_instance.v2_risk2_liquidity_adjustment_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk2_liquidity_adjustment_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Model2LiquidityAdjustmentBody**](Model2LiquidityAdjustmentBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsRiskLiquidityAdjustmentResponse**](EfirDataHubModelsModelsRiskLiquidityAdjustmentResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_amortisations_by_id_post**
> EfirDataHubModelsModelsRiskAmortisationsResponse v2_risk_amortisations_by_id_post(body=body)

Получить график погашения по FintoolId.

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskAmortisationsByIdBody() # RiskAmortisationsByIdBody |  (optional)

try:
    # Получить график погашения по FintoolId.
    api_response = api_instance.v2_risk_amortisations_by_id_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_amortisations_by_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskAmortisationsByIdBody**](RiskAmortisationsByIdBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsRiskAmortisationsResponse**](EfirDataHubModelsModelsRiskAmortisationsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_amortisations_post**
> EfirDataHubModelsModelsRiskAmortisationsResponse v2_risk_amortisations_post(body=body)

Получить график погашения.

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskAmortisationsBody() # RiskAmortisationsBody |  (optional)

try:
    # Получить график погашения.
    api_response = api_instance.v2_risk_amortisations_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_amortisations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskAmortisationsBody**](RiskAmortisationsBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsRiskAmortisationsResponse**](EfirDataHubModelsModelsRiskAmortisationsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_bank_basel_class_post**
> list[EfirDataHubModelsModelsRiskBankBaselClassFields] v2_risk_bank_basel_class_post(body=body)

Возвращает классификацию банков по классам \"Базель III\"

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskBankBaselClassBody() # RiskBankBaselClassBody |  (optional)

try:
    # Возвращает классификацию банков по классам \"Базель III\"
    api_response = api_instance.v2_risk_bank_basel_class_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_bank_basel_class_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskBankBaselClassBody**](RiskBankBaselClassBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRiskBankBaselClassFields]**](EfirDataHubModelsModelsRiskBankBaselClassFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_bank_norm_rule_post**
> EfirDataHubModelsModelsRiskBankNormRuleResponse v2_risk_bank_norm_rule_post(body=body)

Возвращает правило определения группы актива согласно инструкциям ЦБ РФ об обязательных нормативах банков.

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskBankNormRuleBody() # RiskBankNormRuleBody |  (optional)

try:
    # Возвращает правило определения группы актива согласно инструкциям ЦБ РФ об обязательных нормативах банков.
    api_response = api_instance.v2_risk_bank_norm_rule_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_bank_norm_rule_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskBankNormRuleBody**](RiskBankNormRuleBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsRiskBankNormRuleResponse**](EfirDataHubModelsModelsRiskBankNormRuleResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_capital_adequacy_finalized_post**
> list[EfirDataHubModelsModelsRiskCapitalAdequacyFinalizedFields] v2_risk_capital_adequacy_finalized_post(body=body)

Возвращает классификатор финансового инструмента и коэффициент риска для взвешивания в капитале, их расшифровку:  обоснование (номер и абзац пункта из нормативного акта),  принадлежность к ПК (операции с повышенным коэффициентам риска),  агрегат RWA и код актива по финализированному подходу,  в соответствии с инструкцией Банка России (199-И).  Метод не распространяется на активы фондов, производные финансовые инструменты.

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskCapitaladequacyfinalizedBody() # RiskCapitaladequacyfinalizedBody |  (optional)

try:
    # Возвращает классификатор финансового инструмента и коэффициент риска для взвешивания в капитале, их расшифровку:  обоснование (номер и абзац пункта из нормативного акта),  принадлежность к ПК (операции с повышенным коэффициентам риска),  агрегат RWA и код актива по финализированному подходу,  в соответствии с инструкцией Банка России (199-И).  Метод не распространяется на активы фондов, производные финансовые инструменты.
    api_response = api_instance.v2_risk_capital_adequacy_finalized_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_capital_adequacy_finalized_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskCapitaladequacyfinalizedBody**](RiskCapitaladequacyfinalizedBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRiskCapitalAdequacyFinalizedFields]**](EfirDataHubModelsModelsRiskCapitalAdequacyFinalizedFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_capital_adequacy_params_post**
> EfirDataHubModelsModelsRiskCapitalAdequacyResponse v2_risk_capital_adequacy_params_post(body=body)

Получить классификатор инструмента и коэффициент кредитного риска, их расшифровку: обоснование (номер абзаца), группу риска и код, в соответствии с инструкцией, актуальной на дату расчета (ЦБ 180-И или 139-И).

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskCapitalAdequacyParamsBody() # RiskCapitalAdequacyParamsBody |  (optional)

try:
    # Получить классификатор инструмента и коэффициент кредитного риска, их расшифровку: обоснование (номер абзаца), группу риска и код, в соответствии с инструкцией, актуальной на дату расчета (ЦБ 180-И или 139-И).
    api_response = api_instance.v2_risk_capital_adequacy_params_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_capital_adequacy_params_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskCapitalAdequacyParamsBody**](RiskCapitalAdequacyParamsBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsRiskCapitalAdequacyResponse**](EfirDataHubModelsModelsRiskCapitalAdequacyResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_corp_invest_class_post**
> list[EfirDataHubModelsModelsRiskCorpInvestClassFields] v2_risk_corp_invest_class_post(body=body)

Возвращает информацию о принадлежности компании к инвестиционному классу в соответствии с рекомендациями \"Базель III\"

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskCorpInvestClassBody() # RiskCorpInvestClassBody |  (optional)

try:
    # Возвращает информацию о принадлежности компании к инвестиционному классу в соответствии с рекомендациями \"Базель III\"
    api_response = api_instance.v2_risk_corp_invest_class_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_corp_invest_class_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskCorpInvestClassBody**](RiskCorpInvestClassBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRiskCorpInvestClassFields]**](EfirDataHubModelsModelsRiskCorpInvestClassFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_coupon_yield_post**
> EfirDataHubModelsModelsRiskCouponYieldResponse v2_risk_coupon_yield_post(body=body)

Получить доходность инструмента для расчета рисков. Актуально для облигаций и привилегированных акций.

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskCouponYieldBody() # RiskCouponYieldBody |  (optional)

try:
    # Получить доходность инструмента для расчета рисков. Актуально для облигаций и привилегированных акций.
    api_response = api_instance.v2_risk_coupon_yield_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_coupon_yield_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskCouponYieldBody**](RiskCouponYieldBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsRiskCouponYieldResponse**](EfirDataHubModelsModelsRiskCouponYieldResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_equity_risk_rate_post**
> EfirDataHubModelsModelsRiskEquityRiskRateResponse v2_risk_equity_risk_rate_post(body=body)

Получить коэффициент риска.

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskEquityRiskRateBody() # RiskEquityRiskRateBody |  (optional)

try:
    # Получить коэффициент риска.
    api_response = api_instance.v2_risk_equity_risk_rate_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_equity_risk_rate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskEquityRiskRateBody**](RiskEquityRiskRateBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsRiskEquityRiskRateResponse**](EfirDataHubModelsModelsRiskEquityRiskRateResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_fair_value_post**
> EfirDataHubModelsModelsRiskFairValueResponse v2_risk_fair_value_post(body=body)

Получить справедливую цену.

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskFairValueBody() # RiskFairValueBody |  (optional)

try:
    # Получить справедливую цену.
    api_response = api_instance.v2_risk_fair_value_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_fair_value_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskFairValueBody**](RiskFairValueBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsRiskFairValueResponse**](EfirDataHubModelsModelsRiskFairValueResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_fintools_risk_group_params_post**
> list[EfirDataHubModelsModelsRiskFintoolsRiskGroupParams] v2_risk_fintools_risk_group_params_post(body=body)

Получить все или фильтрованные значения параметров группы риска для списка инструментов

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskFintoolsRiskGroupParamsBody() # RiskFintoolsRiskGroupParamsBody |  (optional)

try:
    # Получить все или фильтрованные значения параметров группы риска для списка инструментов
    api_response = api_instance.v2_risk_fintools_risk_group_params_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_fintools_risk_group_params_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskFintoolsRiskGroupParamsBody**](RiskFintoolsRiskGroupParamsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRiskFintoolsRiskGroupParams]**](EfirDataHubModelsModelsRiskFintoolsRiskGroupParams.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_frozen_risk_group_params_post**
> list[EfirDataHubModelsModelsRiskFrozenRiskParam] v2_risk_frozen_risk_group_params_post(body=body)



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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskFrozenRiskGroupParamsBody() # RiskFrozenRiskGroupParamsBody |  (optional)

try:
    api_response = api_instance.v2_risk_frozen_risk_group_params_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_frozen_risk_group_params_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskFrozenRiskGroupParamsBody**](RiskFrozenRiskGroupParamsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRiskFrozenRiskParam]**](EfirDataHubModelsModelsRiskFrozenRiskParam.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_info_shocks_post**
> list[EfirDataHubModelsModelsRiskInfoShocksFields] v2_risk_info_shocks_post(body=body)

Возвращает правило определения группы актива согласно инструкциям ЦБ РФ об обязательных нормативах банков.

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskInfoShocksBody() # RiskInfoShocksBody |  (optional)

try:
    # Возвращает правило определения группы актива согласно инструкциям ЦБ РФ об обязательных нормативах банков.
    api_response = api_instance.v2_risk_info_shocks_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_info_shocks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskInfoShocksBody**](RiskInfoShocksBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRiskInfoShocksFields]**](EfirDataHubModelsModelsRiskInfoShocksFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_instrument_has_risk_post**
> EfirDataHubModelsModelsRiskHasRiskResponse v2_risk_instrument_has_risk_post(body=body)

Наличие процентного и фондового рисков.

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskInstrumentHasRiskBody() # RiskInstrumentHasRiskBody |  (optional)

try:
    # Наличие процентного и фондового рисков.
    api_response = api_instance.v2_risk_instrument_has_risk_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_instrument_has_risk_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskInstrumentHasRiskBody**](RiskInstrumentHasRiskBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsRiskHasRiskResponse**](EfirDataHubModelsModelsRiskHasRiskResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_liquidity_adjustment_post**
> list[EfirDataHubModelsModelsRiskLiquidityAdjustmentFields] v2_risk_liquidity_adjustment_post(body=body)

Получить таблицу с коэффициентами корректировки ликвидности на заданную дату по одной или нескольким облигациям.

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskLiquidityAdjustmentBody() # RiskLiquidityAdjustmentBody |  (optional)

try:
    # Получить таблицу с коэффициентами корректировки ликвидности на заданную дату по одной или нескольким облигациям.
    api_response = api_instance.v2_risk_liquidity_adjustment_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_liquidity_adjustment_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskLiquidityAdjustmentBody**](RiskLiquidityAdjustmentBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRiskLiquidityAdjustmentFields]**](EfirDataHubModelsModelsRiskLiquidityAdjustmentFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_liquidity_params_post**
> list[EfirDataHubModelsModelsRiskLiquidityParamsFields] v2_risk_liquidity_params_post(body=body)

Получить параметры ликвидности инструмента на заданную дату.

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskLiquidityParamsBody() # RiskLiquidityParamsBody |  (optional)

try:
    # Получить параметры ликвидности инструмента на заданную дату.
    api_response = api_instance.v2_risk_liquidity_params_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_liquidity_params_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskLiquidityParamsBody**](RiskLiquidityParamsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRiskLiquidityParamsFields]**](EfirDataHubModelsModelsRiskLiquidityParamsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_liquidity_rating_post**
> list[EfirDataHubModelsModelsRiskLiquidityRatingFields] v2_risk_liquidity_rating_post(body=body)

Получить таблицу с данными по рейтингу ликвидности и используемым для его вычисления параметрам на заданную дату по одной или нескольким облигациям.

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskLiquidityRatingBody() # RiskLiquidityRatingBody |  (optional)

try:
    # Получить таблицу с данными по рейтингу ликвидности и используемым для его вычисления параметрам на заданную дату по одной или нескольким облигациям.
    api_response = api_instance.v2_risk_liquidity_rating_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_liquidity_rating_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskLiquidityRatingBody**](RiskLiquidityRatingBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRiskLiquidityRatingFields]**](EfirDataHubModelsModelsRiskLiquidityRatingFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_market_risk_data_post**
> list[EfirDataHubModelsModelsRiskMarketRiskDataFields] v2_risk_market_risk_data_post(body=body)

Получить данные для расчета рыночного риска.

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskMarketRiskDataBody() # RiskMarketRiskDataBody |  (optional)

try:
    # Получить данные для расчета рыночного риска.
    api_response = api_instance.v2_risk_market_risk_data_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_market_risk_data_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskMarketRiskDataBody**](RiskMarketRiskDataBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRiskMarketRiskDataFields]**](EfirDataHubModelsModelsRiskMarketRiskDataFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_nominal_currency_post**
> EfirDataHubModelsModelsRiskNominalCurrencyResponse v2_risk_nominal_currency_post(body=body)

Валюта номинала.

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskNominalCurrencyBody() # RiskNominalCurrencyBody |  (optional)

try:
    # Валюта номинала.
    api_response = api_instance.v2_risk_nominal_currency_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_nominal_currency_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskNominalCurrencyBody**](RiskNominalCurrencyBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsRiskNominalCurrencyResponse**](EfirDataHubModelsModelsRiskNominalCurrencyResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_option_params_post**
> EfirDataHubModelsModelsRiskOptionParamsResponse v2_risk_option_params_post(body=body)

Получить параметры опциона.

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskOptionParamsBody() # RiskOptionParamsBody |  (optional)

try:
    # Получить параметры опциона.
    api_response = api_instance.v2_risk_option_params_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_option_params_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskOptionParamsBody**](RiskOptionParamsBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsRiskOptionParamsResponse**](EfirDataHubModelsModelsRiskOptionParamsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_option_values_post**
> list[EfirDataHubModelsModelsRiskOptionValuesFields] v2_risk_option_values_post(body=body)

Получить расчетные параметры опциона на заданную дату.

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskOptionValuesBody() # RiskOptionValuesBody |  (optional)

try:
    # Получить расчетные параметры опциона на заданную дату.
    api_response = api_instance.v2_risk_option_values_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_option_values_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskOptionValuesBody**](RiskOptionValuesBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRiskOptionValuesFields]**](EfirDataHubModelsModelsRiskOptionValuesFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_pfi_params_post**
> EfirDataHubModelsModelsRiskPfiParamsResponse v2_risk_pfi_params_post(body=body)

Параметры производных финансовых инструментов.

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskPfiParamsBody() # RiskPfiParamsBody |  (optional)

try:
    # Параметры производных финансовых инструментов.
    api_response = api_instance.v2_risk_pfi_params_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_pfi_params_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskPfiParamsBody**](RiskPfiParamsBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsRiskPfiParamsResponse**](EfirDataHubModelsModelsRiskPfiParamsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_repo_discount139_post**
> EfirDataHubModelsModelsRiskRepoDiscount139Response v2_risk_repo_discount139_post(body=body)

Определение величины дисконта для расчета риска по операциям РЕПО в соответствии с инструкцией 139-И.

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskRepoDiscount139Body() # RiskRepoDiscount139Body |  (optional)

try:
    # Определение величины дисконта для расчета риска по операциям РЕПО в соответствии с инструкцией 139-И.
    api_response = api_instance.v2_risk_repo_discount139_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_repo_discount139_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskRepoDiscount139Body**](RiskRepoDiscount139Body.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsRiskRepoDiscount139Response**](EfirDataHubModelsModelsRiskRepoDiscount139Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_risk_date_post**
> EfirDataHubModelsModelsRiskRiskDateResponse v2_risk_risk_date_post(body=body)

Получить дату, по которой вычисляется группа срочности.

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskRiskDateBody() # RiskRiskDateBody |  (optional)

try:
    # Получить дату, по которой вычисляется группа срочности.
    api_response = api_instance.v2_risk_risk_date_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_risk_date_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskRiskDateBody**](RiskRiskDateBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsRiskRiskDateResponse**](EfirDataHubModelsModelsRiskRiskDateResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_risk_group_param_post**
> EfirDataHubModelsModelsRiskRiskGroupParamResponse v2_risk_risk_group_param_post(body=body)

Получить значение параметра для определения группы риска.

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskRiskGroupParamBody() # RiskRiskGroupParamBody |  (optional)

try:
    # Получить значение параметра для определения группы риска.
    api_response = api_instance.v2_risk_risk_group_param_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_risk_group_param_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskRiskGroupParamBody**](RiskRiskGroupParamBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsRiskRiskGroupParamResponse**](EfirDataHubModelsModelsRiskRiskGroupParamResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_risk_group_params_post**
> list[EfirDataHubModelsModelsRiskRiskGroupParamsFields] v2_risk_risk_group_params_post(body=body)

Получить все или фильтрованные значения параметров группы риска для инструмента

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskRiskGroupParamsBody() # RiskRiskGroupParamsBody |  (optional)

try:
    # Получить все или фильтрованные значения параметров группы риска для инструмента
    api_response = api_instance.v2_risk_risk_group_params_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_risk_group_params_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskRiskGroupParamsBody**](RiskRiskGroupParamsBody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRiskRiskGroupParamsFields]**](EfirDataHubModelsModelsRiskRiskGroupParamsFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_risk_group_post**
> EfirDataHubModelsModelsRiskRiskGroupResponse v2_risk_risk_group_post(body=body)

Получить группу риска для инструмента

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskRiskGroupBody() # RiskRiskGroupBody |  (optional)

try:
    # Получить группу риска для инструмента
    api_response = api_instance.v2_risk_risk_group_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_risk_group_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskRiskGroupBody**](RiskRiskGroupBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsRiskRiskGroupResponse**](EfirDataHubModelsModelsRiskRiskGroupResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_risk_group_rule_post**
> EfirDataHubModelsModelsRiskRiskGroupRuleResponse v2_risk_risk_group_rule_post(body=body)

Определить правило группы риска по положению 387-П.

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskRiskGroupRuleBody() # RiskRiskGroupRuleBody |  (optional)

try:
    # Определить правило группы риска по положению 387-П.
    api_response = api_instance.v2_risk_risk_group_rule_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_risk_group_rule_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskRiskGroupRuleBody**](RiskRiskGroupRuleBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsRiskRiskGroupRuleResponse**](EfirDataHubModelsModelsRiskRiskGroupRuleResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_rule139_post**
> EfirDataHubModelsModelsRiskRule139Response v2_risk_rule139_post(body=body)

Определить правило по инструкции 139-И.

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskRule139Body() # RiskRule139Body |  (optional)

try:
    # Определить правило по инструкции 139-И.
    api_response = api_instance.v2_risk_rule139_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_rule139_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskRule139Body**](RiskRule139Body.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsRiskRule139Response**](EfirDataHubModelsModelsRiskRule139Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_rule421_post**
> EfirDataHubModelsModelsRiskRule421Response v2_risk_rule421_post(body=body)

Определить правило по положению 421-П.

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskRule421Body() # RiskRule421Body |  (optional)

try:
    # Определить правило по положению 421-П.
    api_response = api_instance.v2_risk_rule421_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_rule421_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskRule421Body**](RiskRule421Body.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsRiskRule421Response**](EfirDataHubModelsModelsRiskRule421Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_rule_hla_post**
> list[EfirDataHubModelsModelsRiskRuleHlaFields] v2_risk_rule_hla_post(body=body)

Возвращает значения обесценения на дату

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskRuleHLABody() # RiskRuleHLABody |  (optional)

try:
    # Возвращает значения обесценения на дату
    api_response = api_instance.v2_risk_rule_hla_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_rule_hla_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskRuleHLABody**](RiskRuleHLABody.md)|  | [optional] 

### Return type

[**list[EfirDataHubModelsModelsRiskRuleHlaFields]**](EfirDataHubModelsModelsRiskRuleHlaFields.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_var_data_post**
> EfirDataHubModelsModelsRiskVarDataResponse v2_risk_var_data_post(body=body)

Возвращает массив значений, необходимых для расчета показателей риска VaR (Value at Risk) или ES (Expected Shortfall) по одному инструменту.

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskVarDataBody() # RiskVarDataBody |  (optional)

try:
    # Возвращает массив значений, необходимых для расчета показателей риска VaR (Value at Risk) или ES (Expected Shortfall) по одному инструменту.
    api_response = api_instance.v2_risk_var_data_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_var_data_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskVarDataBody**](RiskVarDataBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsRiskVarDataResponse**](EfirDataHubModelsModelsRiskVarDataResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_risk_var_matrix_post**
> EfirDataHubModelsModelsRiskVarMatrixResponse v2_risk_var_matrix_post(body=body)

Получить VaR матрицу корреляции и ковариации на определенную дату

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
api_instance = swagger_client.RiskApi(swagger_client.ApiClient(configuration))
body = swagger_client.RiskVarMatrixBody() # RiskVarMatrixBody |  (optional)

try:
    # Получить VaR матрицу корреляции и ковариации на определенную дату
    api_response = api_instance.v2_risk_var_matrix_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->v2_risk_var_matrix_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskVarMatrixBody**](RiskVarMatrixBody.md)|  | [optional] 

### Return type

[**EfirDataHubModelsModelsRiskVarMatrixResponse**](EfirDataHubModelsModelsRiskVarMatrixResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

