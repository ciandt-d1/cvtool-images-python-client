# coding: utf-8

"""
    Kingpick Image API

    Image  services.

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ImageApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def add(self, tenant_id, project_id, image_request, **kwargs):
        """
        Adds an image signature to the database.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add(tenant_id, project_id, image_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: tenant id (required)
        :param str project_id: project id (required)
        :param ImageRequest image_request: Image to create (required)
        :return: ImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_with_http_info(tenant_id, project_id, image_request, **kwargs)
        else:
            (data) = self.add_with_http_info(tenant_id, project_id, image_request, **kwargs)
            return data

    def add_with_http_info(self, tenant_id, project_id, image_request, **kwargs):
        """
        Adds an image signature to the database.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_with_http_info(tenant_id, project_id, image_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: tenant id (required)
        :param str project_id: project id (required)
        :param ImageRequest image_request: Image to create (required)
        :return: ImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id', 'project_id', 'image_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params) or (params['tenant_id'] is None):
            raise ValueError("Missing the required parameter `tenant_id` when calling `add`")
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params) or (params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `add`")
        # verify the required parameter 'image_request' is set
        if ('image_request' not in params) or (params['image_request'] is None):
            raise ValueError("Missing the required parameter `image_request` when calling `add`")


        collection_formats = {}

        path_params = {}

        query_params = {}
        if 'tenant_id' in params:
            query_params['tenant_id'] = params['tenant_id']
        if 'project_id' in params:
            query_params['project_id'] = params['project_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'image_request' in params:
            body_params = params['image_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/images', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ImageResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
