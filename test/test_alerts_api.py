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
from flowmill.api.alerts_api import AlertsApi  # noqa: E501
from flowmill.rest import ApiException


class TestAlertsApi(unittest.TestCase):
    """AlertsApi unit test stubs"""

    def setUp(self):
        self.api = flowmill.api.alerts_api.AlertsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_alert(self):
        """Test case for get_alert

        """
        pass

    def test_post_alerts(self):
        """Test case for post_alerts

        """
        pass

    def test_read_alerts(self):
        """Test case for read_alerts

        """
        pass

    def test_update_alert_status(self):
        """Test case for update_alert_status

        """
        pass


if __name__ == '__main__':
    unittest.main()