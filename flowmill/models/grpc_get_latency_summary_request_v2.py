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


class GrpcGetLatencySummaryRequestV2(object):
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
        'end': 'datetime',
        'duration': 'str',
        'num_steps': 'int',
        'latency_class': 'GrpcLatencyClass',
        'min_latency_sec': 'float',
        'latency_metric': 'GrpcLatencyMetric',
        'source_grouping': 'list[str]',
        'destination_grouping': 'list[str]',
        'source_filters': 'list[GrpcFilter]',
        'destination_filters': 'list[GrpcFilter]',
        'no_rollups': 'bool'
    }

    attribute_map = {
        'end': 'end',
        'duration': 'duration',
        'num_steps': 'numSteps',
        'latency_class': 'latencyClass',
        'min_latency_sec': 'minLatencySec',
        'latency_metric': 'latencyMetric',
        'source_grouping': 'sourceGrouping',
        'destination_grouping': 'destinationGrouping',
        'source_filters': 'sourceFilters',
        'destination_filters': 'destinationFilters',
        'no_rollups': 'noRollups'
    }

    def __init__(self, end=None, duration=None, num_steps=None, latency_class=None, min_latency_sec=None, latency_metric=None, source_grouping=None, destination_grouping=None, source_filters=None, destination_filters=None, no_rollups=None):  # noqa: E501
        """GrpcGetLatencySummaryRequestV2 - a model defined in Swagger"""  # noqa: E501

        self._end = None
        self._duration = None
        self._num_steps = None
        self._latency_class = None
        self._min_latency_sec = None
        self._latency_metric = None
        self._source_grouping = None
        self._destination_grouping = None
        self._source_filters = None
        self._destination_filters = None
        self._no_rollups = None
        self.discriminator = None

        if end is not None:
            self.end = end
        if duration is not None:
            self.duration = duration
        if num_steps is not None:
            self.num_steps = num_steps
        if latency_class is not None:
            self.latency_class = latency_class
        if min_latency_sec is not None:
            self.min_latency_sec = min_latency_sec
        if latency_metric is not None:
            self.latency_metric = latency_metric
        if source_grouping is not None:
            self.source_grouping = source_grouping
        if destination_grouping is not None:
            self.destination_grouping = destination_grouping
        if source_filters is not None:
            self.source_filters = source_filters
        if destination_filters is not None:
            self.destination_filters = destination_filters
        if no_rollups is not None:
            self.no_rollups = no_rollups

    @property
    def end(self):
        """Gets the end of this GrpcGetLatencySummaryRequestV2.  # noqa: E501

        See GetTimeSeriesRequestV2 for a description of constraints on time ranges.  # noqa: E501

        :return: The end of this GrpcGetLatencySummaryRequestV2.  # noqa: E501
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this GrpcGetLatencySummaryRequestV2.

        See GetTimeSeriesRequestV2 for a description of constraints on time ranges.  # noqa: E501

        :param end: The end of this GrpcGetLatencySummaryRequestV2.  # noqa: E501
        :type: datetime
        """

        self._end = end

    @property
    def duration(self):
        """Gets the duration of this GrpcGetLatencySummaryRequestV2.  # noqa: E501


        :return: The duration of this GrpcGetLatencySummaryRequestV2.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this GrpcGetLatencySummaryRequestV2.


        :param duration: The duration of this GrpcGetLatencySummaryRequestV2.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def num_steps(self):
        """Gets the num_steps of this GrpcGetLatencySummaryRequestV2.  # noqa: E501

        See GetTrafficStatsRequestV2 for a description of why num_steps is exposed in this context.  # noqa: E501

        :return: The num_steps of this GrpcGetLatencySummaryRequestV2.  # noqa: E501
        :rtype: int
        """
        return self._num_steps

    @num_steps.setter
    def num_steps(self, num_steps):
        """Sets the num_steps of this GrpcGetLatencySummaryRequestV2.

        See GetTrafficStatsRequestV2 for a description of why num_steps is exposed in this context.  # noqa: E501

        :param num_steps: The num_steps of this GrpcGetLatencySummaryRequestV2.  # noqa: E501
        :type: int
        """

        self._num_steps = num_steps

    @property
    def latency_class(self):
        """Gets the latency_class of this GrpcGetLatencySummaryRequestV2.  # noqa: E501

        Only return connections in this latency class.  # noqa: E501

        :return: The latency_class of this GrpcGetLatencySummaryRequestV2.  # noqa: E501
        :rtype: GrpcLatencyClass
        """
        return self._latency_class

    @latency_class.setter
    def latency_class(self, latency_class):
        """Sets the latency_class of this GrpcGetLatencySummaryRequestV2.

        Only return connections in this latency class.  # noqa: E501

        :param latency_class: The latency_class of this GrpcGetLatencySummaryRequestV2.  # noqa: E501
        :type: GrpcLatencyClass
        """

        self._latency_class = latency_class

    @property
    def min_latency_sec(self):
        """Gets the min_latency_sec of this GrpcGetLatencySummaryRequestV2.  # noqa: E501

        Only return connections with latency > min_latency_sec. Default = 0.  # noqa: E501

        :return: The min_latency_sec of this GrpcGetLatencySummaryRequestV2.  # noqa: E501
        :rtype: float
        """
        return self._min_latency_sec

    @min_latency_sec.setter
    def min_latency_sec(self, min_latency_sec):
        """Sets the min_latency_sec of this GrpcGetLatencySummaryRequestV2.

        Only return connections with latency > min_latency_sec. Default = 0.  # noqa: E501

        :param min_latency_sec: The min_latency_sec of this GrpcGetLatencySummaryRequestV2.  # noqa: E501
        :type: float
        """

        self._min_latency_sec = min_latency_sec

    @property
    def latency_metric(self):
        """Gets the latency_metric of this GrpcGetLatencySummaryRequestV2.  # noqa: E501

        Latency metric to use. Default is MRTT.  # noqa: E501

        :return: The latency_metric of this GrpcGetLatencySummaryRequestV2.  # noqa: E501
        :rtype: GrpcLatencyMetric
        """
        return self._latency_metric

    @latency_metric.setter
    def latency_metric(self, latency_metric):
        """Sets the latency_metric of this GrpcGetLatencySummaryRequestV2.

        Latency metric to use. Default is MRTT.  # noqa: E501

        :param latency_metric: The latency_metric of this GrpcGetLatencySummaryRequestV2.  # noqa: E501
        :type: GrpcLatencyMetric
        """

        self._latency_metric = latency_metric

    @property
    def source_grouping(self):
        """Gets the source_grouping of this GrpcGetLatencySummaryRequestV2.  # noqa: E501

        See GetTimeSeriesRequestV2 for a description of groupings and filters.  # noqa: E501

        :return: The source_grouping of this GrpcGetLatencySummaryRequestV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._source_grouping

    @source_grouping.setter
    def source_grouping(self, source_grouping):
        """Sets the source_grouping of this GrpcGetLatencySummaryRequestV2.

        See GetTimeSeriesRequestV2 for a description of groupings and filters.  # noqa: E501

        :param source_grouping: The source_grouping of this GrpcGetLatencySummaryRequestV2.  # noqa: E501
        :type: list[str]
        """

        self._source_grouping = source_grouping

    @property
    def destination_grouping(self):
        """Gets the destination_grouping of this GrpcGetLatencySummaryRequestV2.  # noqa: E501


        :return: The destination_grouping of this GrpcGetLatencySummaryRequestV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._destination_grouping

    @destination_grouping.setter
    def destination_grouping(self, destination_grouping):
        """Sets the destination_grouping of this GrpcGetLatencySummaryRequestV2.


        :param destination_grouping: The destination_grouping of this GrpcGetLatencySummaryRequestV2.  # noqa: E501
        :type: list[str]
        """

        self._destination_grouping = destination_grouping

    @property
    def source_filters(self):
        """Gets the source_filters of this GrpcGetLatencySummaryRequestV2.  # noqa: E501


        :return: The source_filters of this GrpcGetLatencySummaryRequestV2.  # noqa: E501
        :rtype: list[GrpcFilter]
        """
        return self._source_filters

    @source_filters.setter
    def source_filters(self, source_filters):
        """Sets the source_filters of this GrpcGetLatencySummaryRequestV2.


        :param source_filters: The source_filters of this GrpcGetLatencySummaryRequestV2.  # noqa: E501
        :type: list[GrpcFilter]
        """

        self._source_filters = source_filters

    @property
    def destination_filters(self):
        """Gets the destination_filters of this GrpcGetLatencySummaryRequestV2.  # noqa: E501


        :return: The destination_filters of this GrpcGetLatencySummaryRequestV2.  # noqa: E501
        :rtype: list[GrpcFilter]
        """
        return self._destination_filters

    @destination_filters.setter
    def destination_filters(self, destination_filters):
        """Sets the destination_filters of this GrpcGetLatencySummaryRequestV2.


        :param destination_filters: The destination_filters of this GrpcGetLatencySummaryRequestV2.  # noqa: E501
        :type: list[GrpcFilter]
        """

        self._destination_filters = destination_filters

    @property
    def no_rollups(self):
        """Gets the no_rollups of this GrpcGetLatencySummaryRequestV2.  # noqa: E501

        See GetTimeSeriesRequestV2 for a description of no_rollups.  # noqa: E501

        :return: The no_rollups of this GrpcGetLatencySummaryRequestV2.  # noqa: E501
        :rtype: bool
        """
        return self._no_rollups

    @no_rollups.setter
    def no_rollups(self, no_rollups):
        """Sets the no_rollups of this GrpcGetLatencySummaryRequestV2.

        See GetTimeSeriesRequestV2 for a description of no_rollups.  # noqa: E501

        :param no_rollups: The no_rollups of this GrpcGetLatencySummaryRequestV2.  # noqa: E501
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
        if issubclass(GrpcGetLatencySummaryRequestV2, dict):
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
        if not isinstance(other, GrpcGetLatencySummaryRequestV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
