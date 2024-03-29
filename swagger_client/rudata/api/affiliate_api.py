# coding: utf-8

"""
    API Reference United Data (RU DATA) v2.0

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: DataHub: v2, Models: 1.23.21.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AffiliateApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v2_affiliate_company_group_chains_post(self, **kwargs):  # noqa: E501
        """Получить информацию о цепочке связей компании  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_affiliate_company_group_chains_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AffiliateCompanyGroupChainsBody body:
        :return: list[EfirDataHubModelsModelsEmitentCompanyGroupsChainsFieldsBase]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_affiliate_company_group_chains_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v2_affiliate_company_group_chains_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def v2_affiliate_company_group_chains_post_with_http_info(self, **kwargs):  # noqa: E501
        """Получить информацию о цепочке связей компании  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_affiliate_company_group_chains_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AffiliateCompanyGroupChainsBody body:
        :return: list[EfirDataHubModelsModelsEmitentCompanyGroupsChainsFieldsBase]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_affiliate_company_group_chains_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v2/Affiliate/CompanyGroupChains', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[EfirDataHubModelsModelsEmitentCompanyGroupsChainsFieldsBase]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_affiliate_company_group_members_post(self, **kwargs):  # noqa: E501
        """Получить информацию о принадлежности компаний к группам компаний  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_affiliate_company_group_members_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AffiliateCompanyGroupMembersBody body:
        :return: list[EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_affiliate_company_group_members_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v2_affiliate_company_group_members_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def v2_affiliate_company_group_members_post_with_http_info(self, **kwargs):  # noqa: E501
        """Получить информацию о принадлежности компаний к группам компаний  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_affiliate_company_group_members_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AffiliateCompanyGroupMembersBody body:
        :return: list[EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_affiliate_company_group_members_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v2/Affiliate/CompanyGroupMembers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_affiliate_company_group_relations_post(self, **kwargs):  # noqa: E501
        """Возвращает описание отношений в группах компаний  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_affiliate_company_group_relations_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AffiliateCompanyGroupRelationsBody body:
        :return: list[EfirDataHubModelsModelsAffiliatesCompanyGroupRelationsFields]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_affiliate_company_group_relations_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v2_affiliate_company_group_relations_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def v2_affiliate_company_group_relations_post_with_http_info(self, **kwargs):  # noqa: E501
        """Возвращает описание отношений в группах компаний  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_affiliate_company_group_relations_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AffiliateCompanyGroupRelationsBody body:
        :return: list[EfirDataHubModelsModelsAffiliatesCompanyGroupRelationsFields]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_affiliate_company_group_relations_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v2/Affiliate/CompanyGroupRelations', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[EfirDataHubModelsModelsAffiliatesCompanyGroupRelationsFields]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_affiliate_company_groups_post(self, **kwargs):  # noqa: E501
        """Получить состав групп по идентификаторам групп  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_affiliate_company_groups_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AffiliateCompanyGroupsBody body:
        :return: list[EfirDataHubModelsModelsEmitentCompanyGroupsMembersFields]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_affiliate_company_groups_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v2_affiliate_company_groups_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def v2_affiliate_company_groups_post_with_http_info(self, **kwargs):  # noqa: E501
        """Получить состав групп по идентификаторам групп  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_affiliate_company_groups_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AffiliateCompanyGroupsBody body:
        :return: list[EfirDataHubModelsModelsEmitentCompanyGroupsMembersFields]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_affiliate_company_groups_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v2/Affiliate/CompanyGroups', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[EfirDataHubModelsModelsEmitentCompanyGroupsMembersFields]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_affiliate_fininst_id_list_post(self, fininst_id, **kwargs):  # noqa: E501
        """Возвращает список аффилированных лиц и организаций для указанной компании на заданную дату  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_affiliate_fininst_id_list_post(fininst_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int fininst_id: Идентификатор компании в БД Интерфакс (required)
        :param FininstIdListBody body:
        :return: list[EfirDataHubModelsModelsAffiliatesListFields]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_affiliate_fininst_id_list_post_with_http_info(fininst_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v2_affiliate_fininst_id_list_post_with_http_info(fininst_id, **kwargs)  # noqa: E501
            return data

    def v2_affiliate_fininst_id_list_post_with_http_info(self, fininst_id, **kwargs):  # noqa: E501
        """Возвращает список аффилированных лиц и организаций для указанной компании на заданную дату  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_affiliate_fininst_id_list_post_with_http_info(fininst_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int fininst_id: Идентификатор компании в БД Интерфакс (required)
        :param FininstIdListBody body:
        :return: list[EfirDataHubModelsModelsAffiliatesListFields]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fininst_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_affiliate_fininst_id_list_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fininst_id' is set
        if ('fininst_id' not in params or
                params['fininst_id'] is None):
            raise ValueError("Missing the required parameter `fininst_id` when calling `v2_affiliate_fininst_id_list_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fininst_id' in params:
            path_params['fininstId'] = params['fininst_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v2/Affiliate/{fininstId}/list', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[EfirDataHubModelsModelsAffiliatesListFields]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_affiliate_fininst_id_reports_post(self, fininst_id, **kwargs):  # noqa: E501
        """Возвращает список ссылок на исходные отчеты по аффилированным лицам  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_affiliate_fininst_id_reports_post(fininst_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int fininst_id: Идентификатор компании в БД Интерфакс (required)
        :param FininstIdReportsBody body:
        :return: list[EfirDataHubModelsModelsAffiliatesReportsFields]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_affiliate_fininst_id_reports_post_with_http_info(fininst_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v2_affiliate_fininst_id_reports_post_with_http_info(fininst_id, **kwargs)  # noqa: E501
            return data

    def v2_affiliate_fininst_id_reports_post_with_http_info(self, fininst_id, **kwargs):  # noqa: E501
        """Возвращает список ссылок на исходные отчеты по аффилированным лицам  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_affiliate_fininst_id_reports_post_with_http_info(fininst_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int fininst_id: Идентификатор компании в БД Интерфакс (required)
        :param FininstIdReportsBody body:
        :return: list[EfirDataHubModelsModelsAffiliatesReportsFields]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fininst_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_affiliate_fininst_id_reports_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fininst_id' is set
        if ('fininst_id' not in params or
                params['fininst_id'] is None):
            raise ValueError("Missing the required parameter `fininst_id` when calling `v2_affiliate_fininst_id_reports_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fininst_id' in params:
            path_params['fininstId'] = params['fininst_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v2/Affiliate/{fininstId}/reports', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[EfirDataHubModelsModelsAffiliatesReportsFields]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_affiliate_types_post(self, **kwargs):  # noqa: E501
        """Возвращает справочник типов аффилированности  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_affiliate_types_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[EfirDataHubModelsModelsAffiliatesTypesFields]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_affiliate_types_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v2_affiliate_types_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def v2_affiliate_types_post_with_http_info(self, **kwargs):  # noqa: E501
        """Возвращает справочник типов аффилированности  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_affiliate_types_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[EfirDataHubModelsModelsAffiliatesTypesFields]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_affiliate_types_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v2/Affiliate/types', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[EfirDataHubModelsModelsAffiliatesTypesFields]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
