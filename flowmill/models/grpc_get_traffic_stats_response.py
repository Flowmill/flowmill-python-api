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


class GrpcGetTrafficStatsResponse(object):
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
        'increasing': 'list[GrpcTrafficStats]',
        'decreasing': 'list[GrpcTrafficStats]'
    }

    attribute_map = {
        'increasing': 'increasing',
        'decreasing': 'decreasing'
    }

    def __init__(self, increasing=None, decreasing=None):  # noqa: E501
        """GrpcGetTrafficStatsResponse - a model defined in Swagger"""  # noqa: E501

        self._increasing = None
        self._decreasing = None
        self.discriminator = None

        if increasing is not None:
            self.increasing = increasing
        if decreasing is not None:
            self.decreasing = decreasing

    @property
    def increasing(self):
        """Gets the increasing of this GrpcGetTrafficStatsResponse.  # noqa: E501

        Connections that match the specified criteria that have percent change in trafic > 0. Sorted by percent change in descending order.  # noqa: E501

        :return: The increasing of this GrpcGetTrafficStatsResponse.  # noqa: E501
        :rtype: list[GrpcTrafficStats]
        """
        return self._increasing

    @increasing.setter
    def increasing(self, increasing):
        """Sets the increasing of this GrpcGetTrafficStatsResponse.

        Connections that match the specified criteria that have percent change in trafic > 0. Sorted by percent change in descending order.  # noqa: E501

        :param increasing: The increasing of this GrpcGetTrafficStatsResponse.  # noqa: E501
        :type: list[GrpcTrafficStats]
        """

        self._increasing = increasing

    @property
    def decreasing(self):
        """Gets the decreasing of this GrpcGetTrafficStatsResponse.  # noqa: E501

        Connections that match the specified criteria that have percent change in traffic < 0. Sorted by percent change in ascending order.  # noqa: E501

        :return: The decreasing of this GrpcGetTrafficStatsResponse.  # noqa: E501
        :rtype: list[GrpcTrafficStats]
        """
        return self._decreasing

    @decreasing.setter
    def decreasing(self, decreasing):
        """Sets the decreasing of this GrpcGetTrafficStatsResponse.

        Connections that match the specified criteria that have percent change in traffic < 0. Sorted by percent change in ascending order.  # noqa: E501

        :param decreasing: The decreasing of this GrpcGetTrafficStatsResponse.  # noqa: E501
        :type: list[GrpcTrafficStats]
        """

        self._decreasing = decreasing

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
        if issubclass(GrpcGetTrafficStatsResponse, dict):
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
        if not isinstance(other, GrpcGetTrafficStatsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other