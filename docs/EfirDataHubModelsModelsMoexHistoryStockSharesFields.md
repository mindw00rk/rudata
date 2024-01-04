# EfirDataHubModelsModelsMoexHistoryStockSharesFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boardname** | **str** | Режим торгов | [optional] 
**regnumber** | **str** | Код гос. регистрации | [optional] 
**isin** | **str** | Код ISIN | [optional] 
**listname** | **str** | Уровень листинга | [optional] 
**facevalue** | **float** | Номинальная стоимость | [optional] 
**currencyid** | **str** | Валюта, в которой ведутся торги | [optional] 
**prevlegalcloseprice** | **float** | Цена закрытия предыдущего торгового дня рублей | [optional] 
**prev** | **float** | Цена последней сделки предыдущего торгового дня, рублей | [optional] 
**legalopenprice** | **float** | Цена открытия | [optional] 
**openperiod** | **float** | Цена предторгового периода | [optional] 
**closeperiod** | **float** | Цена послеторгового периода | [optional] 
**openval** | **float** | Объем первой сделки | [optional] 
**closeval** | **float** | Объем последней сделки | [optional] 
**legalcloseprice** | **float** | Цена закрытия | [optional] 
**trendclose** | **float** | Изменение цены последней сделки к цене последней сделки предыдущего торгового дня, пунктов | [optional] 
**trendclspr** | **float** | Изменение цены последней сделки к цене последней сделки предыдущего торгового дня, процентов | [optional] 
**highbid** | **float** | Наибольшая цена спроса (максимальная котировка на покупку), рублей | [optional] 
**bid** | **float** | Цена спроса (котировка на покупку) на момент окончания торговой сессии, рублей | [optional] 
**offer** | **float** | Цена предложения (котировка на продажу) на момент окончания торговой сессии, рублей | [optional] 
**lowoffer** | **float** | Наименьшая цена предложения (минимальная котировка на продажу), рублей | [optional] 
**waprice** | **float** | Средневзвешенная цена | [optional] 
**trendwap** | **float** | Изменение средневзвешенной цены к средневзвешенной цене предыдущего торгового дня, пунктов | [optional] 
**trendwappr** | **float** | Изменение средневзвешенной цены к средневзвешенной цене предыдущего торгового дня, процентов | [optional] 
**volume** | **int** | Объем сделок за день, штук ценных бумаг | [optional] 
**marketprice** | **float** | Рыночная цена (1), рублей | [optional] 
**marketprice2** | **float** | Рыночная цена (2), рублей | [optional] 
**mp2valtrd** | **float** | Объем сделок для расчета рыночной цены (2), рублей | [optional] 
**mpvaltrd** | **float** | Объем сделок для расчета рыночной цены (1), рублей | [optional] 
**value** | **float** | Объем сделок за день | [optional] 
**numtrades** | **int** | Количество сделок за день, штук | [optional] 
**issuesize** | **int** | Объем выпуска, штук ценных бумаг | [optional] 
**admittedquote** | **float** | Признаваемая котировка, рублей | [optional] 
**admittedvalue** | **float** | Объем сделок для расчета признаваемой котировки, рублей | [optional] 
**monthlycapitalization** | **float** | Ежемесячная рыночная капитализация, руб | [optional] 
**dailycapitalization** | **float** | Ежедневная капитализация, руб | [optional] 
**marketprice3** | **float** | Рыночная цена (3), рублей | [optional] 
**marketprice3tradesvalue** | **float** | Объем сделок(в рублях), по которым была рассчитана рыночная цена 3 | [optional] 
**type** | **str** | Тип бумаги | [optional] 
**closeauctionprice** | **float** | Цена послеторгового аукциона, рублей | [optional] 
**waval** | **float** | 3-х месячный среднедневной оборот по сделкам с паями | [optional] 
**lastprice** | **float** | Цена последней сделки(без учета послеторгового периода или аукциона закрытия), рублей | [optional] 
**engine** | **str** |  | [optional] 
**market** | **str** |  | [optional] 
**boardid** | **str** |  | [optional] 
**decimals** | **int** | Точность, знаков после запятой | [optional] 
**high** | **float** | Цена сделки максимальная | [optional] 
**low** | **float** | Цена сделки минимальная | [optional] 
**open** | **float** | Цена предторгового периода/Цена аукциона открытия | [optional] 
**close** | **float** | Цена последней сделки | [optional] 
**secid** | **str** | Идентификатор финансового инструмента | [optional] 
**shortname** | **str** | Краткое наименование | [optional] 
**tradedate** | **datetime** | Дата торгов | [optional] 
**tradingsession** | **int** | Номер сессии (1 - основная, 2 - вечерняя, 3 - общие итоги) | [optional] 
**counter** | **int** | Общее количество записей в выборке, если указан pageNum &#x3D; 1. Иначе &#x3D; null | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
