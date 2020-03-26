# coding: utf-8

"""
    Flowmill API Specification

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import flowmill
from flowmill.api.system_overview_service_api import SystemOverviewServiceApi  # noqa: E501
from flowmill.rest import ApiException


class TestSystemOverviewServiceApi(unittest.TestCase):
    """SystemOverviewServiceApi unit test stubs"""

    def setUp(self):
        self.api = flowmill.api.system_overview_service_api.SystemOverviewServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_agent_info(self):
        """Test case for get_agent_info

        """
        pass

    def test_get_connection_summary(self):
        """Test case for get_connection_summary

        """
        pass

    def test_get_connection_summary_v2(self):
        """Test case for get_connection_summary_v2

        """
        pass

    def test_get_latency_summary(self):
        """Test case for get_latency_summary

        """
        pass

    def test_get_latency_summary_v2(self):
        """Test case for get_latency_summary_v2

        """
        pass

    def test_get_traffic_stats(self):
        """Test case for get_traffic_stats

        """
        pass

    def test_get_traffic_stats_v2(self):
        """Test case for get_traffic_stats_v2

        """
        pass


if __name__ == '__main__':
    unittest.main()