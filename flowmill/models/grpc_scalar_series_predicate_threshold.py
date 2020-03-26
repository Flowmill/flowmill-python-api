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


class GrpcScalarSeriesPredicateThreshold(object):
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
        'value': 'float',
        'severity': 'MonitorSeverity'
    }

    attribute_map = {
        'value': 'value',
        'severity': 'severity'
    }

    def __init__(self, value=None, severity=None):  # noqa: E501
        """GrpcScalarSeriesPredicateThreshold - a model defined in Swagger"""  # noqa: E501

        self._value = None
        self._severity = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if severity is not None:
            self.severity = severity

    @property
    def value(self):
        """Gets the value of this GrpcScalarSeriesPredicateThreshold.  # noqa: E501


        :return: The value of this GrpcScalarSeriesPredicateThreshold.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GrpcScalarSeriesPredicateThreshold.


        :param value: The value of this GrpcScalarSeriesPredicateThreshold.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def severity(self):
        """Gets the severity of this GrpcScalarSeriesPredicateThreshold.  # noqa: E501


        :return: The severity of this GrpcScalarSeriesPredicateThreshold.  # noqa: E501
        :rtype: MonitorSeverity
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this GrpcScalarSeriesPredicateThreshold.


        :param severity: The severity of this GrpcScalarSeriesPredicateThreshold.  # noqa: E501
        :type: MonitorSeverity
        """

        self._severity = severity

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
        if issubclass(GrpcScalarSeriesPredicateThreshold, dict):
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
        if not isinstance(other, GrpcScalarSeriesPredicateThreshold):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other