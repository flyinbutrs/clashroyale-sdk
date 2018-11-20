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


class ClansApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_clan(self, clan_tag, **kwargs):  # noqa: E501
        """Get clan information  # noqa: E501

        Get information about a single clan by clan tag. Clan tags can be found using clan search operation.  Note that clan tags start with hash character '#' and that needs to be URL-encoded properly to work in URL, so for example clan tag '#2ABC' would become '%232ABC' in the URL.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_clan(clan_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param str clan_tag: Tag of the clan to retrieve.  (required)
        :return: Clan
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_clan_with_http_info(clan_tag, **kwargs)  # noqa: E501
        else:
            (data) = self.get_clan_with_http_info(clan_tag, **kwargs)  # noqa: E501
            return data

    def get_clan_with_http_info(self, clan_tag, **kwargs):  # noqa: E501
        """Get clan information  # noqa: E501

        Get information about a single clan by clan tag. Clan tags can be found using clan search operation.  Note that clan tags start with hash character '#' and that needs to be URL-encoded properly to work in URL, so for example clan tag '#2ABC' would become '%232ABC' in the URL.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_clan_with_http_info(clan_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param str clan_tag: Tag of the clan to retrieve.  (required)
        :return: Clan
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['clan_tag']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_clan" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'clan_tag' is set
        if ('clan_tag' not in params or
                params['clan_tag'] is None):
            raise ValueError("Missing the required parameter `clan_tag` when calling `get_clan`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'clan_tag' in params:
            path_params['clanTag'] = params['clan_tag']  # noqa: E501

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
            '/clans/{clanTag}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Clan',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_clan_members(self, clan_tag, **kwargs):  # noqa: E501
        """List clan members  # noqa: E501

        List clan members  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_clan_members(clan_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param str clan_tag: Tag of the clan whose members to retrieve. (required)
        :param int limit: Limit the number of items returned in the response. 
        :param int after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param int before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :return: ClanMemberList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_clan_members_with_http_info(clan_tag, **kwargs)  # noqa: E501
        else:
            (data) = self.get_clan_members_with_http_info(clan_tag, **kwargs)  # noqa: E501
            return data

    def get_clan_members_with_http_info(self, clan_tag, **kwargs):  # noqa: E501
        """List clan members  # noqa: E501

        List clan members  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_clan_members_with_http_info(clan_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param str clan_tag: Tag of the clan whose members to retrieve. (required)
        :param int limit: Limit the number of items returned in the response. 
        :param int after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param int before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :return: ClanMemberList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['clan_tag', 'limit', 'after', 'before']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_clan_members" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'clan_tag' is set
        if ('clan_tag' not in params or
                params['clan_tag'] is None):
            raise ValueError("Missing the required parameter `clan_tag` when calling `get_clan_members`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'clan_tag' in params:
            path_params['clanTag'] = params['clan_tag']  # noqa: E501

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
            '/clans/{clanTag}/members', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClanMemberList',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_clan_war_log(self, clan_tag, **kwargs):  # noqa: E501
        """Retrieve clan&#39;s clan war log  # noqa: E501

        Retrieve clan's clan war log  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_clan_war_log(clan_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param str clan_tag: Tag of the clan whose war log to retrieve. (required)
        :param int limit: Limit the number of items returned in the response. 
        :param int after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param int before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :return: WarLog
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_clan_war_log_with_http_info(clan_tag, **kwargs)  # noqa: E501
        else:
            (data) = self.get_clan_war_log_with_http_info(clan_tag, **kwargs)  # noqa: E501
            return data

    def get_clan_war_log_with_http_info(self, clan_tag, **kwargs):  # noqa: E501
        """Retrieve clan&#39;s clan war log  # noqa: E501

        Retrieve clan's clan war log  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_clan_war_log_with_http_info(clan_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param str clan_tag: Tag of the clan whose war log to retrieve. (required)
        :param int limit: Limit the number of items returned in the response. 
        :param int after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param int before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :return: WarLog
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['clan_tag', 'limit', 'after', 'before']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_clan_war_log" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'clan_tag' is set
        if ('clan_tag' not in params or
                params['clan_tag'] is None):
            raise ValueError("Missing the required parameter `clan_tag` when calling `get_clan_war_log`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'clan_tag' in params:
            path_params['clanTag'] = params['clan_tag']  # noqa: E501

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
            '/clans/{clanTag}/warlog', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WarLog',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_current_war(self, clan_tag, **kwargs):  # noqa: E501
        """Retrieve information about clan&#39;s current clan war  # noqa: E501

        Retrieve information about clan's current clan war  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_current_war(clan_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param str clan_tag: Tag of the clan whose war log to retrieve. (required)
        :return: CurrentWar
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_current_war_with_http_info(clan_tag, **kwargs)  # noqa: E501
        else:
            (data) = self.get_current_war_with_http_info(clan_tag, **kwargs)  # noqa: E501
            return data

    def get_current_war_with_http_info(self, clan_tag, **kwargs):  # noqa: E501
        """Retrieve information about clan&#39;s current clan war  # noqa: E501

        Retrieve information about clan's current clan war  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_current_war_with_http_info(clan_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param str clan_tag: Tag of the clan whose war log to retrieve. (required)
        :return: CurrentWar
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['clan_tag']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_current_war" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'clan_tag' is set
        if ('clan_tag' not in params or
                params['clan_tag'] is None):
            raise ValueError("Missing the required parameter `clan_tag` when calling `get_current_war`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'clan_tag' in params:
            path_params['clanTag'] = params['clan_tag']  # noqa: E501

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
            '/clans/{clanTag}/currentwar', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CurrentWar',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_clans(self, **kwargs):  # noqa: E501
        """Search clans  # noqa: E501

        Search all clans by name and/or filtering the results using various criteria. At least one filtering criteria must be defined and if name is used as part of search, it is required to be at least three characters long.  It is not possible to specify ordering for results so clients should not rely on any specific ordering as that may change in the future releases of the API.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_clans(async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: Search clans by name. If name is used as part of search query, it needs to be at least three characters long. Name search parameter is interpreted as wild card search, so it may appear anywhere in the clan name. 
        :param int location_id: Filter by clan location identifier. For list of available locations, refer to getLocations operation. 
        :param int min_members: Filter by minimum amount of clan members. 
        :param int max_members: Filter by maximum amount of clan members. 
        :param int min_score: Filter by minimum amount of clan score. 
        :param int limit: Limit the number of items returned in the response. 
        :param int after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param int before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :return: ClanSearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.search_clans_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_clans_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_clans_with_http_info(self, **kwargs):  # noqa: E501
        """Search clans  # noqa: E501

        Search all clans by name and/or filtering the results using various criteria. At least one filtering criteria must be defined and if name is used as part of search, it is required to be at least three characters long.  It is not possible to specify ordering for results so clients should not rely on any specific ordering as that may change in the future releases of the API.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_clans_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: Search clans by name. If name is used as part of search query, it needs to be at least three characters long. Name search parameter is interpreted as wild card search, so it may appear anywhere in the clan name. 
        :param int location_id: Filter by clan location identifier. For list of available locations, refer to getLocations operation. 
        :param int min_members: Filter by minimum amount of clan members. 
        :param int max_members: Filter by maximum amount of clan members. 
        :param int min_score: Filter by minimum amount of clan score. 
        :param int limit: Limit the number of items returned in the response. 
        :param int after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param int before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :return: ClanSearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'location_id', 'min_members', 'max_members', 'min_score', 'limit', 'after', 'before']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_clans" % key
                )
            params[key] = val
        del params['kwargs']

        if ('name' in params and
                len(params['name']) < 3):
            raise ValueError("Invalid value for parameter `name` when calling `search_clans`, length must be greater than or equal to `3`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'location_id' in params:
            query_params.append(('locationId', params['location_id']))  # noqa: E501
        if 'min_members' in params:
            query_params.append(('minMembers', params['min_members']))  # noqa: E501
        if 'max_members' in params:
            query_params.append(('maxMembers', params['max_members']))  # noqa: E501
        if 'min_score' in params:
            query_params.append(('minScore', params['min_score']))  # noqa: E501
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
            '/clans', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClanSearchResult',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
