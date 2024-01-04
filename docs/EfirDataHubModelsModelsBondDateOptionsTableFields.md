# EfirDataHubModelsModelsBondDateOptionsTableFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_lombard** | **bool** | Признак включения в ломбардный список БР | [optional] 
**exch_main** | **str** | Название основной площадки, на которой торгуется бумага | [optional] 
**listing_level** | **int** | Уровень листинга Мосбиржи | [optional] 
**sum_mktval** | **float** | Объем в обращении в валюте номинала | [optional] 
**sum_mktvol** | **float** | Объем в обращении в штуках | [optional] 
**cpn_no** | **int** | Номер текущего купона | [optional] 
**cpn_begdate** | **datetime** | Дата начала текущего купона | [optional] 
**cpn_enddate** | **datetime** | Дата окончания текущего купона | [optional] 
**cpn_period** | **int** | Дней в текущем купонном периоде | [optional] 
**cpn_fixlist** | **datetime** | Дата фиксации списка на выплату купона | [optional] 
**cpn_rate** | **float** | Ставка текущего купона, % годовых | [optional] 
**cpn_value** | **float** | Выплата на облигацию в валюте номинала | [optional] 
**cpn_paydate** | **datetime** | Дата реальной выплаты купона | [optional] 
**cpn_knownno** | **int** | Номер последнего известного купона | [optional] 
**cpn_knowndate** | **datetime** | Дата окончания последнего известного купона | [optional] 
**newcpn_date** | **datetime** | Ближайшая дата определения неизвестных будущих купонов | [optional] 
**mty_date** | **datetime** | Ближайшая дата погашения части номинала | [optional] 
**mty_fixdate** | **datetime** | Дата фиксации списка на выплату погашения | [optional] 
**mty_part** | **float** | Погашаемый % от первоначального номинала | [optional] 
**mty_value** | **float** | Выплата на облигацию в валюте номинала | [optional] 
**mty_paydate** | **datetime** | Реальная дата погашения/выплаты | [optional] 
**call_date** | **datetime** | Дата досрочного погашения, опцион эмитента | [optional] 
**offer_date** | **datetime** | Расчетная дата(ближайшей) оферты | [optional] 
**offer_end** | **datetime** | Дата окончания периода предъявления к выкупу | [optional] 
**offer_price** | **float** | Цена выкупа, % от номинала, полная (с НКД) | [optional] 
**offer_paydate** | **datetime** | Дата реального выкупа | [optional] 
**conv_begdate** | **datetime** | Дата начала конвертации (ближайшей) | [optional] 
**conv_enddate** | **datetime** | Дата окончания конвертации (ближайшей) | [optional] 
**conv_coeff** | **float** | Коэффициент конвертации(ближайшей) | [optional] 
**conv_fintoolid** | **int** | ID ценной бумаги, в которую совершается конвертация | [optional] 
**default_date** | **datetime** | Дата дефолта | [optional] 
**default_type** | **str** | Тип дефолта, либо отсутствие на заданную дату | [optional] 
**event_type** | **str** | Тип события, на котором возник дефолт | [optional] 
**duty_paydate** | **datetime** | Дата реального исполнения обязательства | [optional] 
**auct_exch** | **str** | Название площадки, на кторой пройдет(до)размещение | [optional] 
**auct_begdate** | **datetime** | Дата начала(до)размещения (ближайшего) | [optional] 
**auct_askval** | **float** | Объем (до)размещаемых облигаций, в валюте номинала | [optional] 
**auct_askvol** | **float** | Количество (до)размещаемых облигаций, штук | [optional] 
**auct_enddate** | **datetime** | Дата окончания(до)размещения (ближайшего) | [optional] 
**accrued_int** | **float** | НКД в валюте номинала | [optional] 
**accrued_int_pct** | **float** | НКД в % от номинала | [optional] 
**current_fv** | **float** | Текущий номинал в валюте номинала | [optional] 
**current_fv_pct** | **float** | Текущий номинал в % от первоначального номинала | [optional] 
**fairvalue_avg** | **float** | ТСС в валюте номинала, средневзв.цена биржи | [optional] 
**fairvalue_nfa** | **float** | ТСС в валюте номинала, НРД | [optional] 
**mty_sumcpn** | **float** | Сумма купонов до погашения | [optional] 
**offer_sumcpn** | **float** | Сумма купонов до ближайшей оферты | [optional] 
**next_repayment_date** | **datetime** | Дата ближайшего возможного погашения | [optional] 
**fv_last_known_date** | **datetime** | Последняя известная дата номинала | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
