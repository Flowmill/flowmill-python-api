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

    def test_system_overview_service_get_agent_info(self):
        """Test case for system_overview_service_get_agent_info

        Request info about connected agents  # noqa: E501
        """
        pass

    def test_system_overview_service_get_connection_summary(self):
        """Test case for system_overview_service_get_connection_summary

        Example request: curl -H \"$TOKEN\" \"http://127.0.0.1:8080/api/v1/system_overview/connection_summary?end=2019-08-04T10:47:59.182Z&summaryType=0\"  # noqa: E501
        """
        pass

    def test_system_overview_service_get_connection_summary_v2(self):
        """Test case for system_overview_service_get_connection_summary_v2

        """
        pass

    def test_system_overview_service_get_latency_summary(self):
        """Test case for system_overview_service_get_latency_summary

        Example request: curl -H \"$TOKEN\" \"http://127.0.0.1:8080/api/v1/system_overview/latency_summary?min_mrtt=20&latency_class=2\"  # noqa: E501
        """
        pass

    def test_system_overview_service_get_latency_summary_v2(self):
        """Test case for system_overview_service_get_latency_summary_v2

        """
        pass

    def test_system_overview_service_get_traffic_stats(self):
        """Test case for system_overview_service_get_traffic_stats

        Example request: curl -H \"$TOKEN\" \"http://127.0.0.1:8080/api/v1/system_overview/traffic_stats?end=2019-07-10T10:47:59.182Z\"  # noqa: E501
        """
        pass

    def test_system_overview_service_get_traffic_stats_v2(self):
        """Test case for system_overview_service_get_traffic_stats_v2

        """
        pass


if __name__ == '__main__':
    unittest.main()
