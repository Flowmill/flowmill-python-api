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
from flowmill.api.integrations_service_api import IntegrationsServiceApi  # noqa: E501
from flowmill.rest import ApiException


class TestIntegrationsServiceApi(unittest.TestCase):
    """IntegrationsServiceApi unit test stubs"""

    def setUp(self):
        self.api = flowmill.api.integrations_service_api.IntegrationsServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_authorize_pagerduty(self):
        """Test case for authorize_pagerduty

        authorize new PagerDuty client and obtain an internal access token  # noqa: E501
        """
        pass

    def test_authorize_slack(self):
        """Test case for authorize_slack

        authorize new slack team and obtain an internal access token  # noqa: E501
        """
        pass

    def test_delete_pagerduty_authorized(self):
        """Test case for delete_pagerduty_authorized

        delete token with specified id  # noqa: E501
        """
        pass

    def test_delete_slack_authorized(self):
        """Test case for delete_slack_authorized

        delete token with specified id  # noqa: E501
        """
        pass

    def test_list_pagerduty_authorized(self):
        """Test case for list_pagerduty_authorized

        list all clients authorized for this tenant  # noqa: E501
        """
        pass

    def test_list_slack_authorized(self):
        """Test case for list_slack_authorized

        list all teams authorized for this tenant  # noqa: E501
        """
        pass

    def test_reauthorize_slack(self):
        """Test case for reauthorize_slack

        reauthorize slack team with the specified id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()