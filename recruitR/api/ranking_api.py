# coding: utf-8

"""
    Recruit Database

    Groups of services that manage the data for the 247Sports recruiting database.<br>                                         Documentation for this silo can be found here:                                         <a target=\"_blank\" href=\"https://atlassian.cbsi.com/confluence/display/TWOSPORTS/RDB+Information\">                                         Recruit Database Documentation</a>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from recruitR.api_client import ApiClient


class RankingApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def tfs_rankings(self, **kwargs):  # noqa: E501
        """Gets a ranking given a set of criteria  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tfs_rankings(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: the year associated with the ranking
        :param int sport_key: the sportKey associated with the ranking
        :param Types ranking_type: the rankingType associated with the ranking
        :param float ranking_version: the rankingVersion associated with the ranking
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.tfs_rankings_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.tfs_rankings_with_http_info(**kwargs)  # noqa: E501
            return data

    def tfs_rankings_with_http_info(self, **kwargs):  # noqa: E501
        """Gets a ranking given a set of criteria  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tfs_rankings_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: the year associated with the ranking
        :param int sport_key: the sportKey associated with the ranking
        :param Types ranking_type: the rankingType associated with the ranking
        :param float ranking_version: the rankingVersion associated with the ranking
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'sport_key', 'ranking_type', 'ranking_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tfs_rankings" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'sport_key' in params:
            query_params.append(('sportKey', params['sport_key']))  # noqa: E501
        if 'ranking_type' in params:
            query_params.append(('rankingType', params['ranking_type']))  # noqa: E501
        if 'ranking_version' in params:
            query_params.append(('rankingVersion', params['ranking_version']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/rdb/v1/rankings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    # def tfs_rankingspublish(self, **kwargs):  # noqa: E501
    #     """tfs_rankingspublish  # noqa: E501

    #     This method makes a synchronous HTTP request by default. To make an
    #     asynchronous HTTP request, please pass async_req=True
    #     >>> thread = api.tfs_rankingspublish(async_req=True)
    #     >>> result = thread.get()

    #     :param async_req bool
    #     :return: SuccessDto
    #              If the method is called asynchronously,
    #              returns the request thread.
    #     """
    #     kwargs['_return_http_data_only'] = True
    #     if kwargs.get('async_req'):
    #         return self.tfs_rankingspublish_with_http_info(**kwargs)  # noqa: E501
    #     else:
    #         (data) = self.tfs_rankingspublish_with_http_info(**kwargs)  # noqa: E501
    #         return data

    # def tfs_rankingspublish_with_http_info(self, **kwargs):  # noqa: E501
    #     """tfs_rankingspublish  # noqa: E501

    #     This method makes a synchronous HTTP request by default. To make an
    #     asynchronous HTTP request, please pass async_req=True
    #     >>> thread = api.tfs_rankingspublish_with_http_info(async_req=True)
    #     >>> result = thread.get()

    #     :param async_req bool
    #     :return: SuccessDto
    #              If the method is called asynchronously,
    #              returns the request thread.
    #     """

    #     all_params = []  # noqa: E501
    #     all_params.append('async_req')
    #     all_params.append('_return_http_data_only')
    #     all_params.append('_preload_content')
    #     all_params.append('_request_timeout')

    #     params = locals()
    #     for key, val in six.iteritems(params['kwargs']):
    #         if key not in all_params:
    #             raise TypeError(
    #                 "Got an unexpected keyword argument '%s'"
    #                 " to method tfs_rankingspublish" % key
    #             )
    #         params[key] = val
    #     del params['kwargs']

    #     collection_formats = {}

    #     path_params = {}

    #     query_params = []

    #     header_params = {}

    #     form_params = []
    #     local_var_files = {}

    #     body_params = None
    #     # HTTP header `Accept`
    #     header_params['Accept'] = self.api_client.select_header_accept(
    #         ['application/json'])  # noqa: E501

    #     # Authentication setting
    #     auth_settings = ['bearer']  # noqa: E501

    #     return self.api_client.call_api(
    #         '/rdb/v1/rankings/publish', 'POST',
    #         path_params,
    #         query_params,
    #         header_params,
    #         body=body_params,
    #         post_params=form_params,
    #         files=local_var_files,
    #         response_type='SuccessDto',  # noqa: E501
    #         auth_settings=auth_settings,
    #         async_req=params.get('async_req'),
    #         _return_http_data_only=params.get('_return_http_data_only'),
    #         _preload_content=params.get('_preload_content', True),
    #         _request_timeout=params.get('_request_timeout'),
    #         collection_formats=collection_formats)

    # def tfs_rankingsranking_key(self, ranking_key, **kwargs):  # noqa: E501
    #     """Updates a ranking  # noqa: E501

    #     This method makes a synchronous HTTP request by default. To make an
    #     asynchronous HTTP request, please pass async_req=True
    #     >>> thread = api.tfs_rankingsranking_key(ranking_key, async_req=True)
    #     >>> result = thread.get()

    #     :param async_req bool
    #     :param int ranking_key: The Key of the Ipa.DataAccess.MySql.Objects.Rdb.Ranking to lookup (required)
    #     :param RankingDto body: SkyNet.Api.Rdb.DTOs.RankingDto
    #     :return: None
    #              If the method is called asynchronously,
    #              returns the request thread.
    #     """
    #     kwargs['_return_http_data_only'] = True
    #     if kwargs.get('async_req'):
    #         return self.tfs_rankingsranking_key_with_http_info(ranking_key, **kwargs)  # noqa: E501
    #     else:
    #         (data) = self.tfs_rankingsranking_key_with_http_info(ranking_key, **kwargs)  # noqa: E501
    #         return data

    # def tfs_rankingsranking_key_with_http_info(self, ranking_key, **kwargs):  # noqa: E501
    #     """Updates a ranking  # noqa: E501

    #     This method makes a synchronous HTTP request by default. To make an
    #     asynchronous HTTP request, please pass async_req=True
    #     >>> thread = api.tfs_rankingsranking_key_with_http_info(ranking_key, async_req=True)
    #     >>> result = thread.get()

    #     :param async_req bool
    #     :param int ranking_key: The Key of the Ipa.DataAccess.MySql.Objects.Rdb.Ranking to lookup (required)
    #     :param RankingDto body: SkyNet.Api.Rdb.DTOs.RankingDto
    #     :return: None
    #              If the method is called asynchronously,
    #              returns the request thread.
    #     """

    #     all_params = ['ranking_key', 'body']  # noqa: E501
    #     all_params.append('async_req')
    #     all_params.append('_return_http_data_only')
    #     all_params.append('_preload_content')
    #     all_params.append('_request_timeout')

    #     params = locals()
    #     for key, val in six.iteritems(params['kwargs']):
    #         if key not in all_params:
    #             raise TypeError(
    #                 "Got an unexpected keyword argument '%s'"
    #                 " to method tfs_rankingsranking_key" % key
    #             )
    #         params[key] = val
    #     del params['kwargs']
    #     # verify the required parameter 'ranking_key' is set
    #     if ('ranking_key' not in params or
    #             params['ranking_key'] is None):
    #         raise ValueError("Missing the required parameter `ranking_key` when calling `tfs_rankingsranking_key`")  # noqa: E501

    #     collection_formats = {}

    #     path_params = {}
    #     if 'ranking_key' in params:
    #         path_params['rankingKey'] = params['ranking_key']  # noqa: E501

    #     query_params = []

    #     header_params = {}

    #     form_params = []
    #     local_var_files = {}

    #     body_params = None
    #     if 'body' in params:
    #         body_params = params['body']
    #     # HTTP header `Content-Type`
    #     header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
    #         ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

    #     # Authentication setting
    #     auth_settings = ['bearer']  # noqa: E501

    #     return self.api_client.call_api(
    #         '/rdb/v1/rankings/{rankingKey}', 'PATCH',
    #         path_params,
    #         query_params,
    #         header_params,
    #         body=body_params,
    #         post_params=form_params,
    #         files=local_var_files,
    #         response_type=None,  # noqa: E501
    #         auth_settings=auth_settings,
    #         async_req=params.get('async_req'),
    #         _return_http_data_only=params.get('_return_http_data_only'),
    #         _preload_content=params.get('_preload_content', True),
    #         _request_timeout=params.get('_request_timeout'),
    #         collection_formats=collection_formats)

    def tfs_rankingsranking_keyarchived_player_rankings(self, ranking_key, **kwargs):  # noqa: E501
        """Gets the archived recruit rankings by type  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tfs_rankingsranking_keyarchived_player_rankings(ranking_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int ranking_key: The Key of the Ipa.DataAccess.MySql.Objects.Rdb.Ranking to lookup (required)
        :param int pagesize:
        :param int page:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.tfs_rankingsranking_keyarchived_player_rankings_with_http_info(ranking_key, **kwargs)  # noqa: E501
        else:
            (data) = self.tfs_rankingsranking_keyarchived_player_rankings_with_http_info(ranking_key, **kwargs)  # noqa: E501
            return data

    def tfs_rankingsranking_keyarchived_player_rankings_with_http_info(self, ranking_key, **kwargs):  # noqa: E501
        """Gets the archived recruit rankings by type  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tfs_rankingsranking_keyarchived_player_rankings_with_http_info(ranking_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int ranking_key: The Key of the Ipa.DataAccess.MySql.Objects.Rdb.Ranking to lookup (required)
        :param int pagesize:
        :param int page:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ranking_key', 'pagesize', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tfs_rankingsranking_keyarchived_player_rankings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ranking_key' is set
        if ('ranking_key' not in params or
                params['ranking_key'] is None):
            raise ValueError("Missing the required parameter `ranking_key` when calling `tfs_rankingsranking_keyarchived_player_rankings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ranking_key' in params:
            path_params['rankingKey'] = params['ranking_key']  # noqa: E501

        query_params = []
        if 'pagesize' in params:
            query_params.append(('pagesize', params['pagesize']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/rdb/v1/rankings/{rankingKey}/archivedPlayerRankings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def tfs_year(self, **kwargs):  # noqa: E501
        """Returns either all years from 1999 to 5 years in the future, or a base ranking key if a rankingKey is passed in  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tfs_year(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int ranking_key:
        :return: list[YearBaseRankingDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.tfs_year_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.tfs_year_with_http_info(**kwargs)  # noqa: E501
            return data

    def tfs_year_with_http_info(self, **kwargs):  # noqa: E501
        """Returns either all years from 1999 to 5 years in the future, or a base ranking key if a rankingKey is passed in  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tfs_year_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int ranking_key:
        :return: list[YearBaseRankingDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ranking_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tfs_year" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ranking_key' in params:
            query_params.append(('rankingKey', params['ranking_key']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/rdb/v1/year', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[YearBaseRankingDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)