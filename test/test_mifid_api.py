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
from swagger_client.rudata.api.mifid_api import MifidApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMifidApi(unittest.TestCase):
    """MifidApi unit test stubs"""

    def setUp(self):
        self.api = MifidApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v2_mifid_trade_filters_post(self):
        """Test case for v2_mifid_trade_filters_post

        Возвращает характеристики фильтров  # noqa: E501
        """
        pass

    def test_v2_mifid_trade_stat_start_dates_post(self):
        """Test case for v2_mifid_trade_stat_start_dates_post

        Получить перечень бумаг с указанием самых ранних торговых дней, по которым есть статистика.  Также указаны минимальные даты формирования статистики.  # noqa: E501
        """
        pass

    def test_v2_mifid_trade_stats_aggregated_post(self):
        """Test case for v2_mifid_trade_stats_aggregated_post

        Статистика по сделкам - агрегированная за период  # noqa: E501
        """
        pass

    def test_v2_mifid_trade_stats_by_days_post(self):
        """Test case for v2_mifid_trade_stats_by_days_post

        Статистика по сделкам - агрегированная по дням за период  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
