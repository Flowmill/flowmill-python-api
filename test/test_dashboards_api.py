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
from flowmill.api.dashboards_api import DashboardsApi  # noqa: E501
from flowmill.rest import ApiException


class TestDashboardsApi(unittest.TestCase):
    """DashboardsApi unit test stubs"""

    def setUp(self):
        self.api = flowmill.api.dashboards_api.DashboardsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_dashboard(self):
        """Test case for delete_dashboard

        """
        pass

    def test_delete_favorite(self):
        """Test case for delete_favorite

        """
        pass

    def test_get_dashboard(self):
        """Test case for get_dashboard

        """
        pass

    def test_get_dashboard2(self):
        """Test case for get_dashboard2

        """
        pass

    def test_post_dashboard(self):
        """Test case for post_dashboard

        """
        pass

    def test_post_favorite(self):
        """Test case for post_favorite

        """
        pass

    def test_put_dashboard(self):
        """Test case for put_dashboard

        """
        pass


if __name__ == '__main__':
    unittest.main()