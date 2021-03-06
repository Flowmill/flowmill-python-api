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


class GrpcGetTrafficStatsRequest(object):
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
        'start': 'datetime',
        'end': 'datetime',
        'grouping': 'GrpcGrouping',
        'min_average_bytes_per_second': 'float',
        'min_absolute_percent_change': 'float',
        'source_filters': 'list[GrpcFilter]',
        'destination_filters': 'list[GrpcFilter]',
        'no_rollups': 'bool'
    }

    attribute_map = {
        'start': 'start',
        'end': 'end',
        'grouping': 'grouping',
        'min_average_bytes_per_second': 'minAverageBytesPerSecond',
        'min_absolute_percent_change': 'minAbsolutePercentChange',
        'source_filters': 'sourceFilters',
        'destination_filters': 'destinationFilters',
        'no_rollups': 'noRollups'
    }

    def __init__(self, start=None, end=None, grouping=None, min_average_bytes_per_second=None, min_absolute_percent_change=None, source_filters=None, destination_filters=None, no_rollups=None):  # noqa: E501
        """GrpcGetTrafficStatsRequest - a model defined in Swagger"""  # noqa: E501

        self._start = None
        self._end = None
        self._grouping = None
        self._min_average_bytes_per_second = None
        self._min_absolute_percent_change = None
        self._source_filters = None
        self._destination_filters = None
        self._no_rollups = None
        self.discriminator = None

        if start is not None:
            self.start = start
        if end is not None:
            self.end = end
        if grouping is not None:
            self.grouping = grouping
        if min_average_bytes_per_second is not None:
            self.min_average_bytes_per_second = min_average_bytes_per_second
        if min_absolute_percent_change is not None:
            self.min_absolute_percent_change = min_absolute_percent_change
        if source_filters is not None:
            self.source_filters = source_filters
        if destination_filters is not None:
            self.destination_filters = destination_filters
        if no_rollups is not None:
            self.no_rollups = no_rollups

    @property
    def start(self):
        """Gets the start of this GrpcGetTrafficStatsRequest.  # noqa: E501


        :return: The start of this GrpcGetTrafficStatsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this GrpcGetTrafficStatsRequest.


        :param start: The start of this GrpcGetTrafficStatsRequest.  # noqa: E501
        :type: datetime
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this GrpcGetTrafficStatsRequest.  # noqa: E501


        :return: The end of this GrpcGetTrafficStatsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this GrpcGetTrafficStatsRequest.


        :param end: The end of this GrpcGetTrafficStatsRequest.  # noqa: E501
        :type: datetime
        """

        self._end = end

    @property
    def grouping(self):
        """Gets the grouping of this GrpcGetTrafficStatsRequest.  # noqa: E501


        :return: The grouping of this GrpcGetTrafficStatsRequest.  # noqa: E501
        :rtype: GrpcGrouping
        """
        return self._grouping

    @grouping.setter
    def grouping(self, grouping):
        """Sets the grouping of this GrpcGetTrafficStatsRequest.


        :param grouping: The grouping of this GrpcGetTrafficStatsRequest.  # noqa: E501
        :type: GrpcGrouping
        """

        self._grouping = grouping

    @property
    def min_average_bytes_per_second(self):
        """Gets the min_average_bytes_per_second of this GrpcGetTrafficStatsRequest.  # noqa: E501

        only return connections that have entire_window_average_bytes_per_second greater than this value. default 0 (no filtering).  # noqa: E501

        :return: The min_average_bytes_per_second of this GrpcGetTrafficStatsRequest.  # noqa: E501
        :rtype: float
        """
        return self._min_average_bytes_per_second

    @min_average_bytes_per_second.setter
    def min_average_bytes_per_second(self, min_average_bytes_per_second):
        """Sets the min_average_bytes_per_second of this GrpcGetTrafficStatsRequest.

        only return connections that have entire_window_average_bytes_per_second greater than this value. default 0 (no filtering).  # noqa: E501

        :param min_average_bytes_per_second: The min_average_bytes_per_second of this GrpcGetTrafficStatsRequest.  # noqa: E501
        :type: float
        """

        self._min_average_bytes_per_second = min_average_bytes_per_second

    @property
    def min_absolute_percent_change(self):
        """Gets the min_absolute_percent_change of this GrpcGetTrafficStatsRequest.  # noqa: E501

        only return connections that have percent_change_in_traffic greater than this value. default 0 (no filtering).  # noqa: E501

        :return: The min_absolute_percent_change of this GrpcGetTrafficStatsRequest.  # noqa: E501
        :rtype: float
        """
        return self._min_absolute_percent_change

    @min_absolute_percent_change.setter
    def min_absolute_percent_change(self, min_absolute_percent_change):
        """Sets the min_absolute_percent_change of this GrpcGetTrafficStatsRequest.

        only return connections that have percent_change_in_traffic greater than this value. default 0 (no filtering).  # noqa: E501

        :param min_absolute_percent_change: The min_absolute_percent_change of this GrpcGetTrafficStatsRequest.  # noqa: E501
        :type: float
        """

        self._min_absolute_percent_change = min_absolute_percent_change

    @property
    def source_filters(self):
        """Gets the source_filters of this GrpcGetTrafficStatsRequest.  # noqa: E501


        :return: The source_filters of this GrpcGetTrafficStatsRequest.  # noqa: E501
        :rtype: list[GrpcFilter]
        """
        return self._source_filters

    @source_filters.setter
    def source_filters(self, source_filters):
        """Sets the source_filters of this GrpcGetTrafficStatsRequest.


        :param source_filters: The source_filters of this GrpcGetTrafficStatsRequest.  # noqa: E501
        :type: list[GrpcFilter]
        """

        self._source_filters = source_filters

    @property
    def destination_filters(self):
        """Gets the destination_filters of this GrpcGetTrafficStatsRequest.  # noqa: E501


        :return: The destination_filters of this GrpcGetTrafficStatsRequest.  # noqa: E501
        :rtype: list[GrpcFilter]
        """
        return self._destination_filters

    @destination_filters.setter
    def destination_filters(self, destination_filters):
        """Sets the destination_filters of this GrpcGetTrafficStatsRequest.


        :param destination_filters: The destination_filters of this GrpcGetTrafficStatsRequest.  # noqa: E501
        :type: list[GrpcFilter]
        """

        self._destination_filters = destination_filters

    @property
    def no_rollups(self):
        """Gets the no_rollups of this GrpcGetTrafficStatsRequest.  # noqa: E501


        :return: The no_rollups of this GrpcGetTrafficStatsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._no_rollups

    @no_rollups.setter
    def no_rollups(self, no_rollups):
        """Sets the no_rollups of this GrpcGetTrafficStatsRequest.


        :param no_rollups: The no_rollups of this GrpcGetTrafficStatsRequest.  # noqa: E501
        :type: bool
        """

        self._no_rollups = no_rollups

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
        if issubclass(GrpcGetTrafficStatsRequest, dict):
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
        if not isinstance(other, GrpcGetTrafficStatsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
