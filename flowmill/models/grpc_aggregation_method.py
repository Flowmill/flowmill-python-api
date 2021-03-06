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


class GrpcAggregationMethod(object):
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
        'quantile': 'AggregationMethodQuantileParams',
        'sum': 'object',
        'mean': 'object'
    }

    attribute_map = {
        'quantile': 'quantile',
        'sum': 'sum',
        'mean': 'mean'
    }

    def __init__(self, quantile=None, sum=None, mean=None):  # noqa: E501
        """GrpcAggregationMethod - a model defined in Swagger"""  # noqa: E501

        self._quantile = None
        self._sum = None
        self._mean = None
        self.discriminator = None

        if quantile is not None:
            self.quantile = quantile
        if sum is not None:
            self.sum = sum
        if mean is not None:
            self.mean = mean

    @property
    def quantile(self):
        """Gets the quantile of this GrpcAggregationMethod.  # noqa: E501


        :return: The quantile of this GrpcAggregationMethod.  # noqa: E501
        :rtype: AggregationMethodQuantileParams
        """
        return self._quantile

    @quantile.setter
    def quantile(self, quantile):
        """Sets the quantile of this GrpcAggregationMethod.


        :param quantile: The quantile of this GrpcAggregationMethod.  # noqa: E501
        :type: AggregationMethodQuantileParams
        """

        self._quantile = quantile

    @property
    def sum(self):
        """Gets the sum of this GrpcAggregationMethod.  # noqa: E501


        :return: The sum of this GrpcAggregationMethod.  # noqa: E501
        :rtype: object
        """
        return self._sum

    @sum.setter
    def sum(self, sum):
        """Sets the sum of this GrpcAggregationMethod.


        :param sum: The sum of this GrpcAggregationMethod.  # noqa: E501
        :type: object
        """

        self._sum = sum

    @property
    def mean(self):
        """Gets the mean of this GrpcAggregationMethod.  # noqa: E501


        :return: The mean of this GrpcAggregationMethod.  # noqa: E501
        :rtype: object
        """
        return self._mean

    @mean.setter
    def mean(self, mean):
        """Sets the mean of this GrpcAggregationMethod.


        :param mean: The mean of this GrpcAggregationMethod.  # noqa: E501
        :type: object
        """

        self._mean = mean

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
        if issubclass(GrpcAggregationMethod, dict):
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
        if not isinstance(other, GrpcAggregationMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
