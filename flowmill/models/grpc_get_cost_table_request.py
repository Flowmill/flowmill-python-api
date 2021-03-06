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


class GrpcGetCostTableRequest(object):
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
        'source_filters': 'list[GrpcFilter]',
        'destination_filters': 'list[GrpcFilter]',
        'source_grouping': 'list[str]',
        'destination_grouping': 'list[str]',
        'cross_az_dollars_per_gb': 'float',
        'egress_dollars_per_gb': 'float',
        'minimum_cost_percent': 'float',
        'no_rollups': 'bool'
    }

    attribute_map = {
        'end': 'end',
        'duration': 'duration',
        'source_filters': 'sourceFilters',
        'destination_filters': 'destinationFilters',
        'source_grouping': 'sourceGrouping',
        'destination_grouping': 'destinationGrouping',
        'cross_az_dollars_per_gb': 'crossAzDollarsPerGb',
        'egress_dollars_per_gb': 'egressDollarsPerGb',
        'minimum_cost_percent': 'minimumCostPercent',
        'no_rollups': 'noRollups'
    }

    def __init__(self, end=None, duration=None, source_filters=None, destination_filters=None, source_grouping=None, destination_grouping=None, cross_az_dollars_per_gb=None, egress_dollars_per_gb=None, minimum_cost_percent=None, no_rollups=None):  # noqa: E501
        """GrpcGetCostTableRequest - a model defined in Swagger"""  # noqa: E501

        self._end = None
        self._duration = None
        self._source_filters = None
        self._destination_filters = None
        self._source_grouping = None
        self._destination_grouping = None
        self._cross_az_dollars_per_gb = None
        self._egress_dollars_per_gb = None
        self._minimum_cost_percent = None
        self._no_rollups = None
        self.discriminator = None

        if end is not None:
            self.end = end
        if duration is not None:
            self.duration = duration
        if source_filters is not None:
            self.source_filters = source_filters
        if destination_filters is not None:
            self.destination_filters = destination_filters
        if source_grouping is not None:
            self.source_grouping = source_grouping
        if destination_grouping is not None:
            self.destination_grouping = destination_grouping
        if cross_az_dollars_per_gb is not None:
            self.cross_az_dollars_per_gb = cross_az_dollars_per_gb
        if egress_dollars_per_gb is not None:
            self.egress_dollars_per_gb = egress_dollars_per_gb
        if minimum_cost_percent is not None:
            self.minimum_cost_percent = minimum_cost_percent
        if no_rollups is not None:
            self.no_rollups = no_rollups

    @property
    def end(self):
        """Gets the end of this GrpcGetCostTableRequest.  # noqa: E501


        :return: The end of this GrpcGetCostTableRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this GrpcGetCostTableRequest.


        :param end: The end of this GrpcGetCostTableRequest.  # noqa: E501
        :type: datetime
        """

        self._end = end

    @property
    def duration(self):
        """Gets the duration of this GrpcGetCostTableRequest.  # noqa: E501


        :return: The duration of this GrpcGetCostTableRequest.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this GrpcGetCostTableRequest.


        :param duration: The duration of this GrpcGetCostTableRequest.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def source_filters(self):
        """Gets the source_filters of this GrpcGetCostTableRequest.  # noqa: E501


        :return: The source_filters of this GrpcGetCostTableRequest.  # noqa: E501
        :rtype: list[GrpcFilter]
        """
        return self._source_filters

    @source_filters.setter
    def source_filters(self, source_filters):
        """Sets the source_filters of this GrpcGetCostTableRequest.


        :param source_filters: The source_filters of this GrpcGetCostTableRequest.  # noqa: E501
        :type: list[GrpcFilter]
        """

        self._source_filters = source_filters

    @property
    def destination_filters(self):
        """Gets the destination_filters of this GrpcGetCostTableRequest.  # noqa: E501


        :return: The destination_filters of this GrpcGetCostTableRequest.  # noqa: E501
        :rtype: list[GrpcFilter]
        """
        return self._destination_filters

    @destination_filters.setter
    def destination_filters(self, destination_filters):
        """Sets the destination_filters of this GrpcGetCostTableRequest.


        :param destination_filters: The destination_filters of this GrpcGetCostTableRequest.  # noqa: E501
        :type: list[GrpcFilter]
        """

        self._destination_filters = destination_filters

    @property
    def source_grouping(self):
        """Gets the source_grouping of this GrpcGetCostTableRequest.  # noqa: E501


        :return: The source_grouping of this GrpcGetCostTableRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._source_grouping

    @source_grouping.setter
    def source_grouping(self, source_grouping):
        """Sets the source_grouping of this GrpcGetCostTableRequest.


        :param source_grouping: The source_grouping of this GrpcGetCostTableRequest.  # noqa: E501
        :type: list[str]
        """

        self._source_grouping = source_grouping

    @property
    def destination_grouping(self):
        """Gets the destination_grouping of this GrpcGetCostTableRequest.  # noqa: E501


        :return: The destination_grouping of this GrpcGetCostTableRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._destination_grouping

    @destination_grouping.setter
    def destination_grouping(self, destination_grouping):
        """Sets the destination_grouping of this GrpcGetCostTableRequest.


        :param destination_grouping: The destination_grouping of this GrpcGetCostTableRequest.  # noqa: E501
        :type: list[str]
        """

        self._destination_grouping = destination_grouping

    @property
    def cross_az_dollars_per_gb(self):
        """Gets the cross_az_dollars_per_gb of this GrpcGetCostTableRequest.  # noqa: E501

        Value used to estimate the cost of cross-zone traffic. Default is 0.  Queries that fail to specify either this or egress_dollars_per_gb will return an INVALID_ARGUMENT error as at least one cost must be > 0.  # noqa: E501

        :return: The cross_az_dollars_per_gb of this GrpcGetCostTableRequest.  # noqa: E501
        :rtype: float
        """
        return self._cross_az_dollars_per_gb

    @cross_az_dollars_per_gb.setter
    def cross_az_dollars_per_gb(self, cross_az_dollars_per_gb):
        """Sets the cross_az_dollars_per_gb of this GrpcGetCostTableRequest.

        Value used to estimate the cost of cross-zone traffic. Default is 0.  Queries that fail to specify either this or egress_dollars_per_gb will return an INVALID_ARGUMENT error as at least one cost must be > 0.  # noqa: E501

        :param cross_az_dollars_per_gb: The cross_az_dollars_per_gb of this GrpcGetCostTableRequest.  # noqa: E501
        :type: float
        """

        self._cross_az_dollars_per_gb = cross_az_dollars_per_gb

    @property
    def egress_dollars_per_gb(self):
        """Gets the egress_dollars_per_gb of this GrpcGetCostTableRequest.  # noqa: E501

        Value used to estimate the cost of egress traffic. Default is 0.  Queries that fail to specify either this or cross_az_dollars_per_gb will return an INVALID_ARGUMENT error as at least one cost must be > 0.  # noqa: E501

        :return: The egress_dollars_per_gb of this GrpcGetCostTableRequest.  # noqa: E501
        :rtype: float
        """
        return self._egress_dollars_per_gb

    @egress_dollars_per_gb.setter
    def egress_dollars_per_gb(self, egress_dollars_per_gb):
        """Sets the egress_dollars_per_gb of this GrpcGetCostTableRequest.

        Value used to estimate the cost of egress traffic. Default is 0.  Queries that fail to specify either this or cross_az_dollars_per_gb will return an INVALID_ARGUMENT error as at least one cost must be > 0.  # noqa: E501

        :param egress_dollars_per_gb: The egress_dollars_per_gb of this GrpcGetCostTableRequest.  # noqa: E501
        :type: float
        """

        self._egress_dollars_per_gb = egress_dollars_per_gb

    @property
    def minimum_cost_percent(self):
        """Gets the minimum_cost_percent of this GrpcGetCostTableRequest.  # noqa: E501

        Return rows representing services that contribute > minimum_cost_percent of total estimated costs.  Example: use 0.01 for all connections contributing to > 1% of costs.  If unspecified, this will default to 0 (no filtering).  # noqa: E501

        :return: The minimum_cost_percent of this GrpcGetCostTableRequest.  # noqa: E501
        :rtype: float
        """
        return self._minimum_cost_percent

    @minimum_cost_percent.setter
    def minimum_cost_percent(self, minimum_cost_percent):
        """Sets the minimum_cost_percent of this GrpcGetCostTableRequest.

        Return rows representing services that contribute > minimum_cost_percent of total estimated costs.  Example: use 0.01 for all connections contributing to > 1% of costs.  If unspecified, this will default to 0 (no filtering).  # noqa: E501

        :param minimum_cost_percent: The minimum_cost_percent of this GrpcGetCostTableRequest.  # noqa: E501
        :type: float
        """

        self._minimum_cost_percent = minimum_cost_percent

    @property
    def no_rollups(self):
        """Gets the no_rollups of this GrpcGetCostTableRequest.  # noqa: E501


        :return: The no_rollups of this GrpcGetCostTableRequest.  # noqa: E501
        :rtype: bool
        """
        return self._no_rollups

    @no_rollups.setter
    def no_rollups(self, no_rollups):
        """Sets the no_rollups of this GrpcGetCostTableRequest.


        :param no_rollups: The no_rollups of this GrpcGetCostTableRequest.  # noqa: E501
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
        if issubclass(GrpcGetCostTableRequest, dict):
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
        if not isinstance(other, GrpcGetCostTableRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
