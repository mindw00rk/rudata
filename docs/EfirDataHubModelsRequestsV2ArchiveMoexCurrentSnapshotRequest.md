# EfirDataHubModelsRequestsV2ArchiveMoexCurrentSnapshotRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engine** | **str** | Краткое наименование торговой системы Мосбиржи (англ.).  Подсистема MOEX.  Допустимые значения см. в поле name массива engines ответа метода &#x27;/v2/Moex/Boards&#x27;  Обязательный параметр. | 
**market** | **str** | Краткое наименование рынка Мосбиржи (англ.).  Обязательный параметр.  Допустимые значения см. в поле name массива markets ответа метода &#x27;/v2/Moex/Boards&#x27; | 
**board_ids** | **list[str]** | Идентификатор режима торгов. Короткое имя режима торгов или группы режимов.  Допустимые значения см. в поле boardId массива boards ответа метода &#x27;/v2/Moex/Boards&#x27; | [optional] 
**fintool_ids** | **list[int]** | Идентификаторы финансового инструмента в БД Интерфакс  Не более 100. | [optional] 
**instruments** | **list[str]** | Массив идентификаторов торгуемых инструментов.  Не более 100.  Не используется, если задан Efir.DataHub.Models.Requests.V2.Archive.MoexCurrentSnapshotRequest.FintoolIds  Короткие биржевые коды, которые можно получить в сервисе Securities (поле SECID).  Например, SBER. | [optional] 
**fields** | **list[str]** | Список интересующих полей.  Обязательный параметр. | 
**page_num** | **int** | Номер страницы для выборки | [optional] [default to 1]
**page_size** | **int** | Размер страницы выборки. Максимум - 100 | [optional] [default to 100]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

