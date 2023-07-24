# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import circuitid_python
from circuitid_python.paths.virtualextensions_id import get  # noqa: E501
from circuitid_python import configuration, schemas, api_client

from .. import ApiTestMixin


class TestVirtualextensionsId(ApiTestMixin, unittest.TestCase):
    """
    VirtualextensionsId unit test stubs
        Get object by id  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
