# coding: utf-8

"""
    Clash Royale API

    null  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from clashroyale_sdk.api_client import ApiClient


class TournamentsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_tournament(self, tournament_tag, **kwargs):  # noqa: E501
        """Get tournament information  # noqa: E501

        Get information about a single tournament by a tournament tag.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass send_async=True
        >>> thread = api.get_tournament(tournament_tag, send_async=True)
        >>> result = thread.get()

        :param send_async bool
        :param str tournament_tag: Tag of the tournament to retrieve.  (required)
        :return: Tournament
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('send_async'):
            return self.get_tournament_with_http_info(tournament_tag, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tournament_with_http_info(tournament_tag, **kwargs)  # noqa: E501
            return data

    def get_tournament_with_http_info(self, tournament_tag, **kwargs):  # noqa: E501
        """Get tournament information  # noqa: E501

        Get information about a single tournament by a tournament tag.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass send_async=True
        >>> thread = api.get_tournament_with_http_info(tournament_tag, send_async=True)
        >>> result = thread.get()

        :param send_async bool
        :param str tournament_tag: Tag of the tournament to retrieve.  (required)
        :return: Tournament
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tournament_tag']  # noqa: E501
        all_params.append('send_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tournament" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tournament_tag' is set
        if ('tournament_tag' not in params or
                params['tournament_tag'] is None):
            raise ValueError("Missing the required parameter `tournament_tag` when calling `get_tournament`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tournament_tag' in params:
            path_params['tournamentTag'] = params['tournament_tag']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/tournaments/{tournamentTag}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Tournament',  # noqa: E501
            auth_settings=auth_settings,
            send_async=params.get('send_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_tournaments(self, **kwargs):  # noqa: E501
        """Search tournaments  # noqa: E501

        Search all tournaments by name.  It is not possible to specify ordering for results so clients should not rely on any specific ordering as that may change in the future releases of the API.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass send_async=True
        >>> thread = api.search_tournaments(send_async=True)
        >>> result = thread.get()

        :param send_async bool
        :param str name: Search tournaments by name. 
        :param int limit: Limit the number of items returned in the response. 
        :param int after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param int before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :return: TournamentSearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('send_async'):
            return self.search_tournaments_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_tournaments_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_tournaments_with_http_info(self, **kwargs):  # noqa: E501
        """Search tournaments  # noqa: E501

        Search all tournaments by name.  It is not possible to specify ordering for results so clients should not rely on any specific ordering as that may change in the future releases of the API.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass send_async=True
        >>> thread = api.search_tournaments_with_http_info(send_async=True)
        >>> result = thread.get()

        :param send_async bool
        :param str name: Search tournaments by name. 
        :param int limit: Limit the number of items returned in the response. 
        :param int after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param int before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :return: TournamentSearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'limit', 'after', 'before']  # noqa: E501
        all_params.append('send_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_tournaments" % key
                )
            params[key] = val
        del params['kwargs']

        if ('name' in params and
                len(params['name']) < 1):
            raise ValueError("Invalid value for parameter `name` when calling `search_tournaments`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'before' in params:
            query_params.append(('before', params['before']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/tournaments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TournamentSearchResult',  # noqa: E501
            auth_settings=auth_settings,
            send_async=params.get('send_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
