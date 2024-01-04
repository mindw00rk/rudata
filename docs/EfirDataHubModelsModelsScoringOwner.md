# EfirDataHubModelsModelsScoringOwner

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shortname** | **str** | Краткое наименование | [optional] 
**sparkid** | **int** | Идентификатор СПАРК родительской компании | [optional] 
**inn** | **str** | ИНН | [optional] 
**ogrn** | **str** | ОГРН | [optional] 
**sharepart_total** | **float** | Полная доля владения в компании c учетом перекрестного владения и промежуточных акционеров (может быть больше 1 при суммировании значений у разных акционеров). | [optional] 
**pd** | **float** | Вероятность дефолта, % | [optional] 
**scoring_rating** | **str** | Рейтинг (по скоринговой оценке Интерфакс) | [optional] 
**compaggv2_rating** | **str** | Рейтинг | [optional] 
**has_ifrs** | **bool** | Флаг наличия отчетности МСФО | [optional] 
**revenue** | **float** | Величина выручки по отчетности, руб. | [optional] 
**guar_size** | **float** | Величина гарантий по обязательствам, руб. | [optional] 
**liab_coverage** | **float** | Доля обязательств, покрытых гарантиями | [optional] 
**support_prob** | **float** | Вероятность поддержки со стороны владельцев, % | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

