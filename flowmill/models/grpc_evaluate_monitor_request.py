# coding: utf-8

"""
    Flowmill API Specification

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GrpcEvaluateMonitorRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'tenant': 'str',
        'monitor': 'GrpcMonitor',
        'over_window': 'EvaluateMonitorRequestWindowParams',
        'once': 'EvaluateMonitorRequestOnceParams'
    }

    attribute_map = {
        'tenant': 'tenant',
        'monitor': 'monitor',
        'over_window': 'overWindow',
        'once': 'once'
    }

    def __init__(self, tenant=None, monitor=None, over_window=None, once=None):  # noqa: E501
        """GrpcEvaluateMonitorRequest - a model defined in Swagger"""  # noqa: E501

        self._tenant = None
        self._monitor = None
        self._over_window = None
        self._once = None
        self.discriminator = None

        if tenant is not None:
            self.tenant = tenant
        if monitor is not None:
            self.monitor = monitor
        if over_window is not None:
            self.over_window = over_window
        if once is not None:
            self.once = once

    @property
    def tenant(self):
        """Gets the tenant of this GrpcEvaluateMonitorRequest.  # noqa: E501


        :return: The tenant of this GrpcEvaluateMonitorRequest.  # noqa: E501
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this GrpcEvaluateMonitorRequest.


        :param tenant: The tenant of this GrpcEvaluateMonitorRequest.  # noqa: E501
        :type: str
        """

        self._tenant = tenant

    @property
    def monitor(self):
        """Gets the monitor of this GrpcEvaluateMonitorRequest.  # noqa: E501

        The monitor to be evaluated.  # noqa: E501

        :return: The monitor of this GrpcEvaluateMonitorRequest.  # noqa: E501
        :rtype: GrpcMonitor
        """
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        """Sets the monitor of this GrpcEvaluateMonitorRequest.

        The monitor to be evaluated.  # noqa: E501

        :param monitor: The monitor of this GrpcEvaluateMonitorRequest.  # noqa: E501
        :type: GrpcMonitor
        """

        self._monitor = monitor

    @property
    def over_window(self):
        """Gets the over_window of this GrpcEvaluateMonitorRequest.  # noqa: E501

        Run the monitor for every step along the window. All fields (i.e. start, stop, step) must be present.  # noqa: E501

        :return: The over_window of this GrpcEvaluateMonitorRequest.  # noqa: E501
        :rtype: EvaluateMonitorRequestWindowParams
        """
        return self._over_window

    @over_window.setter
    def over_window(self, over_window):
        """Sets the over_window of this GrpcEvaluateMonitorRequest.

        Run the monitor for every step along the window. All fields (i.e. start, stop, step) must be present.  # noqa: E501

        :param over_window: The over_window of this GrpcEvaluateMonitorRequest.  # noqa: E501
        :type: EvaluateMonitorRequestWindowParams
        """

        self._over_window = over_window

    @property
    def once(self):
        """Gets the once of this GrpcEvaluateMonitorRequest.  # noqa: E501

        Execute the monitor once at the given time. Each MonitorEvaluationResult instance in the response will have a single point.  # noqa: E501

        :return: The once of this GrpcEvaluateMonitorRequest.  # noqa: E501
        :rtype: EvaluateMonitorRequestOnceParams
        """
        return self._once

    @once.setter
    def once(self, once):
        """Sets the once of this GrpcEvaluateMonitorRequest.

        Execute the monitor once at the given time. Each MonitorEvaluationResult instance in the response will have a single point.  # noqa: E501

        :param once: The once of this GrpcEvaluateMonitorRequest.  # noqa: E501
        :type: EvaluateMonitorRequestOnceParams
        """

        self._once = once

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GrpcEvaluateMonitorRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GrpcEvaluateMonitorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
