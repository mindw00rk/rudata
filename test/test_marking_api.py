# coding: utf-8

"""
    API Reference United Data (RU DATA) v2.0

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: DataHub: v2, Models: 1.23.21.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.rudata.api.marking_api import MarkingApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMarkingApi(unittest.TestCase):
    """MarkingApi unit test stubs"""

    def setUp(self):
        self.api = MarkingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v2_marking_codes_post(self):
        """Test case for v2_marking_codes_post

        Cправочник кодов, используемых для значений маркировки  # noqa: E501
        """
        pass

    def test_v2_marking_rules_post(self):
        """Test case for v2_marking_rules_post

        Справочник правил выполнения маркировки  # noqa: E501
        """
        pass

    def test_v2_marking_values_post(self):
        """Test case for v2_marking_values_post

        Информация о маркировках инструментов, отрезки действия которых пересекаются с заданным  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()