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


class GrpcEntityTimeseriesList(object):
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
        'metric': 'str',
        'series': 'list[GrpcEntityTimeseries]',
        'total_count': 'int'
    }

    attribute_map = {
        'metric': 'metric',
        'series': 'series',
        'total_count': 'totalCount'
    }

    def __init__(self, metric=None, series=None, total_count=None):  # noqa: E501
        """GrpcEntityTimeseriesList - a model defined in Swagger"""  # noqa: E501

        self._metric = None
        self._series = None
        self._total_count = None
        self.discriminator = None

        if metric is not None:
            self.metric = metric
        if series is not None:
            self.series = series
        if total_count is not None:
            self.total_count = total_count

    @property
    def metric(self):
        """Gets the metric of this GrpcEntityTimeseriesList.  # noqa: E501

        Metric for the timeseries included in this struct.  # noqa: E501

        :return: The metric of this GrpcEntityTimeseriesList.  # noqa: E501
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this GrpcEntityTimeseriesList.

        Metric for the timeseries included in this struct.  # noqa: E501

        :param metric: The metric of this GrpcEntityTimeseriesList.  # noqa: E501
        :type: str
        """

        self._metric = metric

    @property
    def series(self):
        """Gets the series of this GrpcEntityTimeseriesList.  # noqa: E501

        Timeseries for the corresponding metric sorted by ________.  Note: we should define a meaningful sort order for these timeseries. Some possibilities are the max value or labels.  # noqa: E501

        :return: The series of this GrpcEntityTimeseriesList.  # noqa: E501
        :rtype: list[GrpcEntityTimeseries]
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this GrpcEntityTimeseriesList.

        Timeseries for the corresponding metric sorted by ________.  Note: we should define a meaningful sort order for these timeseries. Some possibilities are the max value or labels.  # noqa: E501

        :param series: The series of this GrpcEntityTimeseriesList.  # noqa: E501
        :type: list[GrpcEntityTimeseries]
        """

        self._series = series

    @property
    def total_count(self):
        """Gets the total_count of this GrpcEntityTimeseriesList.  # noqa: E501

        Total number of timeseries matching the specified query for this metric.  If this is greater than len(series), then we know that timeseries have been filtered from the response.  # noqa: E501

        :return: The total_count of this GrpcEntityTimeseriesList.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this GrpcEntityTimeseriesList.

        Total number of timeseries matching the specified query for this metric.  If this is greater than len(series), then we know that timeseries have been filtered from the response.  # noqa: E501

        :param total_count: The total_count of this GrpcEntityTimeseriesList.  # noqa: E501
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
        if issubclass(GrpcEntityTimeseriesList, dict):
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
        if not isinstance(other, GrpcEntityTimeseriesList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
