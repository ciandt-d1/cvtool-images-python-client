# coding: utf-8

"""
    Kingpick Image API

    Image  services.

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cvtool_images_client
from cvtool_images_client.rest import ApiException
from cvtool_images_client.models.annotation import Annotation


class TestAnnotation(unittest.TestCase):
    """ Annotation unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAnnotation(self):
        """
        Test Annotation
        """
        model = cvtool_images_client.models.annotation.Annotation()


if __name__ == '__main__':
    unittest.main()
