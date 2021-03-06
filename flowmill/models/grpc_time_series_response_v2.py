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


class GrpcTimeSeriesResponseV2(object):
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
        'series': 'list[GrpcTimeSeriesV2]',
        'total_count': 'int'
    }

    attribute_map = {
        'series': 'series',
        'total_count': 'totalCount'
    }

    def __init__(self, series=None, total_count=None):  # noqa: E501
        """GrpcTimeSeriesResponseV2 - a model defined in Swagger"""  # noqa: E501

        self._series = None
        self._total_count = None
        self.discriminator = None

        if series is not None:
            self.series = series
        if total_count is not None:
            self.total_count = total_count

    @property
    def series(self):
        """Gets the series of this GrpcTimeSeriesResponseV2.  # noqa: E501

        List of timeseries that match the specified query.  # noqa: E501

        :return: The series of this GrpcTimeSeriesResponseV2.  # noqa: E501
        :rtype: list[GrpcTimeSeriesV2]
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this GrpcTimeSeriesResponseV2.

        List of timeseries that match the specified query.  # noqa: E501

        :param series: The series of this GrpcTimeSeriesResponseV2.  # noqa: E501
        :type: list[GrpcTimeSeriesV2]
        """

        self._series = series

    @property
    def total_count(self):
        """Gets the total_count of this GrpcTimeSeriesResponseV2.  # noqa: E501

        Total number of timeseries matching the specified query. If this is greater than len(series), then we filtered the results by top_k.  # noqa: E501

        :return: The total_count of this GrpcTimeSeriesResponseV2.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this GrpcTimeSeriesResponseV2.

        Total number of timeseries matching the specified query. If this is greater than len(series), then we filtered the results by top_k.  # noqa: E501

        :param total_count: The total_count of this GrpcTimeSeriesResponseV2.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

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
        if issubclass(GrpcTimeSeriesResponseV2, dict):
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
        if not isinstance(other, GrpcTimeSeriesResponseV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
