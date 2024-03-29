# EfirDataHubModelsModelsInfoEmitentsFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_emitent** | **int** | Идентификатор эмитента | [optional] 
**fininstid** | **int** | Идентификатор эмитента в базе Интерфакс | [optional] 
**shortname_rus** | **str** | Наименование эмитента (рус.) | [optional] 
**shortname_eng** | **str** | Наименование эмитента (англ.) | [optional] 
**inn** | **str** | ИНН для российских компаний, TIN/TAX для остальных | [optional] 
**okpo** | **str** | ОКПО | [optional] 
**ogrn** | **str** | ОГРН | [optional] 
**code** | **str** | Символьный идентификатор эмитента | [optional] 
**sector** | **str** | Отрасль (по основной деятельности) | [optional] 
**legal_address** | **str** | Юридический адрес | [optional] 
**phone** | **str** | Телефоны | [optional] 
**www** | **str** | Адрес веб-сайта | [optional] 
**update_date** | **datetime** | Дата последних изменений информации по эмитенту | [optional] 
**fullname_rus_nrd** | **str** | Полное наименование эмитента в базе НРД (рус) | [optional] 
**fullname_eng_nrd** | **str** | Полное наименование эмитента на ин. языке в базе НРД | [optional] 
**shortname_rus_nrd** | **str** | Краткое наименование эмитента в базе НРД (рус) | [optional] 
**shortname_eng_nrd** | **str** | Краткое наименование на ин. языке в базе НРД | [optional] 
**company_type_short_name** | **str** | Краткое наименование организационно-правовой формы (рус) | [optional] 
**state_reg_num** | **str** | Регистрационный номер | [optional] 
**state_reg_date** | **datetime** | Дата первичной регистрации | [optional] 
**state_reg_name** | **str** | Орган, зарегистрировавший юр.лицо | [optional] 
**egrul_date** | **datetime** | Дата государственной регистрации | [optional] 
**egrul_organ_name** | **str** | Орган, внесший запись в ЕГРЮЛ | [optional] 
**country** | **str** | Страна регистрации, 3-букв.код по ОКСМ | [optional] 
**lei_code** | **str** | LEI-код | [optional] 
**bik** | **str** | БИК | [optional] 
**fax** | **str** | Факс | [optional] 
**e_mail** | **str** | Электронная почта | [optional] 
**credit_cmp** | **str** | “Y” для кредитной организации | [optional] 
**is_bank_4_non_resident** | **str** | “Y” для иностранной кредитной организации | [optional] 
**swift** | **str** | Код SWIFT | [optional] 
**country_oksm** | **int** | Цифровой код страны по ОКСМ | [optional] 
**country_name_rus** | **str** | Наименование страны (рус) | [optional] 
**country_name_eng** | **str** | Наименование страны (анг) | [optional] 
**region_inn** | **str** | Код региона по ИНН | [optional] 
**region_soato** | **str** | Код региона по СОАТО | [optional] 
**region_name** | **str** | Наименование региона (для российских эмитентов) | [optional] 
**fullname_rus** | **str** | Полное наименование эмитента (рус) | [optional] 
**sparkid** | **int** | Идентификатор эмитента в базе СПАРК | [optional] 
**br_fcsm_reg_code** | **str** | Регистрационный номер ФСФР/ЦБ РФ | [optional] 
**capital** | **float** | Уставный капитал | [optional] 
**capital_unit** | **str** | Валюта уставного капитала | [optional] 
**okved** | **str** | Код основного ОКВЭД2 | [optional] 
**oecd_lvl** | **str** | Классификация страны ОЭСР | [optional] 
**oktmo** | **str** | Код общероссийского классификатора территорий муниципальных образований | [optional] 
**okato** | **str** | Код общероссийского классификатора объектов административно-территориального деления | [optional] 
**post_address** | **str** | Адрес почтовый | [optional] 
**okopf** | **str** | ОКОПФ | [optional] 
**okogu** | **str** | ОКОГУ | [optional] 
**have_rating** | **int** | &#x27;Y&#x27; если есть хоть один активный рейтинг | [optional] 
**have_risk** | **int** | &#x27;Y&#x27; если организация представлена в блоке по рискам | [optional] 
**is_finorg** | **int** | &#x27;Y&#x27; для финансовой организации | [optional] 
**is_control_by_finorg** | **int** | &#x27;Y&#x27; для компаний, контролируемых финансовыми организациями | [optional] 
**is_gov_or_cb** | **int** | Правительство или Центральный Банк | [optional] 
**on_behalf_of_state** | **int** | Имеет право заимствовать от лица государства, страны | [optional] 
**is_subjectrf** | **int** | Субъект РФ или муниципальное образование РФ | [optional] 
**is_cis_reg** | **int** | Признак регистрации на территории СНГ(кроме России) | [optional] 
**issuer_nrd** | **str** | Идентификатор эмитента в базе НРД | [optional] 
**tin** | **str** | TIN (США) | [optional] 
**kpp** | **str** | КПП | [optional] 
**state_reg_number** | **str** | Номер государственной регистрации при создании | [optional] 
**market_id_nrd** | **int** | Идентификатор сектора рынка НРД | [optional] 
**market_name_rus_nrd** | **str** | Наименование сектора рынка НРД (рус.) | [optional] 
**market_name_eng_nrd** | **str** | Наименование сектора рынка НРД (англ.) | [optional] 
**sp_rx_entity_id** | **str** | Standard&amp;Poor&#x27;s Rating Express Entity Identificator | [optional] 
**sp_shortname** | **str** | Standard &amp; Poor&#x27;s NickName | [optional] 
**mds_shortname** | **str** | Moody&#x27;s NickName | [optional] 
**mds_org_id** | **str** | Moody&#x27;s Organization Identificator | [optional] 
**fch_id** | **str** | Fitch Investors Identificator | [optional] 
**fch_shortname** | **str** | Fitch Investors NickName | [optional] 
**is_monopoly** | **int** | Реестр естественных монополий | [optional] 
**is_strategic** | **int** | Перечень стратегических предприятий | [optional] 
**ifo_list** | **str** | Вхождение эмитента в список МФО(&#x27;МФО1&#x27; или &#x27;МФО2&#x27;) | [optional] 
**isregion** | **int** | 1 – субъект РФ; 0 – муниципалитет РФ; пусто – иное. | [optional] 
**sic** | **str** | Классификация в соответствии с Standard Industrial Classification | [optional] 
**sector4212u** | **str** | Сектор в соответствии с указанием Банка России 4212-У | [optional] 
**sna2008** | **str** | Классификация в соответствии с System of National Accounts 2008 | [optional] 
**reg_code** | **str** | Государственный регистрационный номер | [optional] 
**reg_date** | **datetime** | Дата регистрации (данные Интерфакс) | [optional] 
**reg_org** | **str** | Регистрирующий орган (данные Интерфакс) | [optional] 
**note** | **str** | Примечание | [optional] 
**primary_reg_date** | **datetime** | Первичная дата регистрации (данные Интерфакс) | [optional] 
**inn_fle** | **str** | Индивидуальный номер налогоплательщика (ИНН) иностранного юридического лица в России | [optional] 
**other_tin** | **str** | Дополнительный налоговый (или иной) код для компаний за рубежом | [optional] 
**other_tin_name** | **str** | Наименование дополнительного кода для компаний за рубежом | [optional] 
**okfs_id** | **str** | Код по ОКФС | [optional] 
**okfs_name** | **str** | Наименование по ОКФС | [optional] 
**is_branch** | **bool** | Флаг филиала | [optional] 
**counter** | **int** | Общее количество записей в выборке | [optional] 
**rn** | **int** | Номер записи в выборке | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

