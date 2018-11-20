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


class LocationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_clan_ranking(self, location_id, **kwargs):  # noqa: E501
        """Get clan rankings for a specific location  # noqa: E501

        Get clan rankings for a specific location  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass send_async=True
        >>> thread = api.get_clan_ranking(location_id, send_async=True)
        >>> result = thread.get()

        :param send_async bool
        :param str location_id: Identifier of the location to retrieve. (required)
        :param int limit: Limit the number of items returned in the response. 
        :param int after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param int before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :return: ClanRankingList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('send_async'):
            return self.get_clan_ranking_with_http_info(location_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_clan_ranking_with_http_info(location_id, **kwargs)  # noqa: E501
            return data

    def get_clan_ranking_with_http_info(self, location_id, **kwargs):  # noqa: E501
        """Get clan rankings for a specific location  # noqa: E501

        Get clan rankings for a specific location  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass send_async=True
        >>> thread = api.get_clan_ranking_with_http_info(location_id, send_async=True)
        >>> result = thread.get()

        :param send_async bool
        :param str location_id: Identifier of the location to retrieve. (required)
        :param int limit: Limit the number of items returned in the response. 
        :param int after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param int before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :return: ClanRankingList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['location_id', 'limit', 'after', 'before']  # noqa: E501
        all_params.append('send_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_clan_ranking" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'location_id' is set
        if ('location_id' not in params or
                params['location_id'] is None):
            raise ValueError("Missing the required parameter `location_id` when calling `get_clan_ranking`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'location_id' in params:
            path_params['locationId'] = params['location_id']  # noqa: E501

        query_params = []
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
            '/locations/{locationId}/rankings/clans', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClanRankingList',  # noqa: E501
            auth_settings=auth_settings,
            send_async=params.get('send_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_clan_wars_ranking(self, location_id, **kwargs):  # noqa: E501
        """Get clan war rankings for a specific location  # noqa: E501

        Get clan war rankings for a specific location  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass send_async=True
        >>> thread = api.get_clan_wars_ranking(location_id, send_async=True)
        >>> result = thread.get()

        :param send_async bool
        :param str location_id: Identifier of the location to retrieve. (required)
        :param int limit: Limit the number of items returned in the response. 
        :param int after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param int before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :return: ClanWarsRankingList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('send_async'):
            return self.get_clan_wars_ranking_with_http_info(location_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_clan_wars_ranking_with_http_info(location_id, **kwargs)  # noqa: E501
            return data

    def get_clan_wars_ranking_with_http_info(self, location_id, **kwargs):  # noqa: E501
        """Get clan war rankings for a specific location  # noqa: E501

        Get clan war rankings for a specific location  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass send_async=True
        >>> thread = api.get_clan_wars_ranking_with_http_info(location_id, send_async=True)
        >>> result = thread.get()

        :param send_async bool
        :param str location_id: Identifier of the location to retrieve. (required)
        :param int limit: Limit the number of items returned in the response. 
        :param int after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param int before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :return: ClanWarsRankingList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['location_id', 'limit', 'after', 'before']  # noqa: E501
        all_params.append('send_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_clan_wars_ranking" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'location_id' is set
        if ('location_id' not in params or
                params['location_id'] is None):
            raise ValueError("Missing the required parameter `location_id` when calling `get_clan_wars_ranking`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'location_id' in params:
            path_params['locationId'] = params['location_id']  # noqa: E501

        query_params = []
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
            '/locations/{locationId}/rankings/clanwars', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClanWarsRankingList',  # noqa: E501
            auth_settings=auth_settings,
            send_async=params.get('send_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_location(self, location_id, **kwargs):  # noqa: E501
        """Get location information  # noqa: E501

        Get information about specific location  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass send_async=True
        >>> thread = api.get_location(location_id, send_async=True)
        >>> result = thread.get()

        :param send_async bool
        :param str location_id: Identifier of the location to retrieve. (required)
        :return: Location
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('send_async'):
            return self.get_location_with_http_info(location_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_location_with_http_info(location_id, **kwargs)  # noqa: E501
            return data

    def get_location_with_http_info(self, location_id, **kwargs):  # noqa: E501
        """Get location information  # noqa: E501

        Get information about specific location  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass send_async=True
        >>> thread = api.get_location_with_http_info(location_id, send_async=True)
        >>> result = thread.get()

        :param send_async bool
        :param str location_id: Identifier of the location to retrieve. (required)
        :return: Location
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['location_id']  # noqa: E501
        all_params.append('send_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_location" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'location_id' is set
        if ('location_id' not in params or
                params['location_id'] is None):
            raise ValueError("Missing the required parameter `location_id` when calling `get_location`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'location_id' in params:
            path_params['locationId'] = params['location_id']  # noqa: E501

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
            '/locations/{locationId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Location',  # noqa: E501
            auth_settings=auth_settings,
            send_async=params.get('send_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_locations(self, **kwargs):  # noqa: E501
        """List locations  # noqa: E501

        List all available locations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass send_async=True
        >>> thread = api.get_locations(send_async=True)
        >>> result = thread.get()

        :param send_async bool
        :param int limit: Limit the number of items returned in the response. 
        :param int after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param int before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :return: LocationList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('send_async'):
            return self.get_locations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_locations_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_locations_with_http_info(self, **kwargs):  # noqa: E501
        """List locations  # noqa: E501

        List all available locations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass send_async=True
        >>> thread = api.get_locations_with_http_info(send_async=True)
        >>> result = thread.get()

        :param send_async bool
        :param int limit: Limit the number of items returned in the response. 
        :param int after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param int before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :return: LocationList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'after', 'before']  # noqa: E501
        all_params.append('send_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_locations" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
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
            '/locations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LocationList',  # noqa: E501
            auth_settings=auth_settings,
            send_async=params.get('send_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_player_ranking(self, location_id, **kwargs):  # noqa: E501
        """Get player rankings for a specific location  # noqa: E501

        Get player rankings for a specific location  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass send_async=True
        >>> thread = api.get_player_ranking(location_id, send_async=True)
        >>> result = thread.get()

        :param send_async bool
        :param str location_id: Identifier of the location to retrieve. (required)
        :param int limit: Limit the number of items returned in the response. 
        :param int after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param int before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :return: PlayerRankingList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('send_async'):
            return self.get_player_ranking_with_http_info(location_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_player_ranking_with_http_info(location_id, **kwargs)  # noqa: E501
            return data

    def get_player_ranking_with_http_info(self, location_id, **kwargs):  # noqa: E501
        """Get player rankings for a specific location  # noqa: E501

        Get player rankings for a specific location  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass send_async=True
        >>> thread = api.get_player_ranking_with_http_info(location_id, send_async=True)
        >>> result = thread.get()

        :param send_async bool
        :param str location_id: Identifier of the location to retrieve. (required)
        :param int limit: Limit the number of items returned in the response. 
        :param int after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param int before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :return: PlayerRankingList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['location_id', 'limit', 'after', 'before']  # noqa: E501
        all_params.append('send_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_player_ranking" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'location_id' is set
        if ('location_id' not in params or
                params['location_id'] is None):
            raise ValueError("Missing the required parameter `location_id` when calling `get_player_ranking`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'location_id' in params:
            path_params['locationId'] = params['location_id']  # noqa: E501

        query_params = []
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
            '/locations/{locationId}/rankings/players', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PlayerRankingList',  # noqa: E501
            auth_settings=auth_settings,
            send_async=params.get('send_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
