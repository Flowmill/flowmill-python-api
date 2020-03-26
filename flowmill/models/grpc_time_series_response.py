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


class GrpcTimeSeriesResponse(object):
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
        'series': 'list[TimeSeriesResponseTimeSeries]',
        'start': 'datetime',
        'end': 'datetime',
        'step': 'str',
        'hit_limit': 'bool',
        'total_count': 'int'
    }

    attribute_map = {
        'series': 'series',
        'start': 'start',
        'end': 'end',
        'step': 'step',
        'hit_limit': 'hitLimit',
        'total_count': 'totalCount'
    }

    def __init__(self, series=None, start=None, end=None, step=None, hit_limit=None, total_count=None):  # noqa: E501
        """GrpcTimeSeriesResponse - a model defined in Swagger"""  # noqa: E501

        self._series = None
        self._start = None
        self._end = None
        self._step = None
        self._hit_limit = None
        self._total_count = None
        self.discriminator = None

        if series is not None:
            self.series = series
        if start is not None:
            self.start = start
        if end is not None:
            self.end = end
        if step is not None:
            self.step = step
        if hit_limit is not None:
            self.hit_limit = hit_limit
        if total_count is not None:
            self.total_count = total_count

    @property
    def series(self):
        """Gets the series of this GrpcTimeSeriesResponse.  # noqa: E501


        :return: The series of this GrpcTimeSeriesResponse.  # noqa: E501
        :rtype: list[TimeSeriesResponseTimeSeries]
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this GrpcTimeSeriesResponse.


        :param series: The series of this GrpcTimeSeriesResponse.  # noqa: E501
        :type: list[TimeSeriesResponseTimeSeries]
        """

        self._series = series

    @property
    def start(self):
        """Gets the start of this GrpcTimeSeriesResponse.  # noqa: E501


        :return: The start of this GrpcTimeSeriesResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this GrpcTimeSeriesResponse.


        :param start: The start of this GrpcTimeSeriesResponse.  # noqa: E501
        :type: datetime
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this GrpcTimeSeriesResponse.  # noqa: E501


        :return: The end of this GrpcTimeSeriesResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this GrpcTimeSeriesResponse.


        :param end: The end of this GrpcTimeSeriesResponse.  # noqa: E501
        :type: datetime
        """

        self._end = end

    @property
    def step(self):
        """Gets the step of this GrpcTimeSeriesResponse.  # noqa: E501


        :return: The step of this GrpcTimeSeriesResponse.  # noqa: E501
        :rtype: str
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this GrpcTimeSeriesResponse.


        :param step: The step of this GrpcTimeSeriesResponse.  # noqa: E501
        :type: str
        """

        self._step = step

    @property
    def hit_limit(self):
        """Gets the hit_limit of this GrpcTimeSeriesResponse.  # noqa: E501


        :return: The hit_limit of this GrpcTimeSeriesResponse.  # noqa: E501
        :rtype: bool
        """
        return self._hit_limit

    @hit_limit.setter
    def hit_limit(self, hit_limit):
        """Sets the hit_limit of this GrpcTimeSeriesResponse.


        :param hit_limit: The hit_limit of this GrpcTimeSeriesResponse.  # noqa: E501
        :type: bool
        """

        self._hit_limit = hit_limit

    @property
    def total_count(self):
        """Gets the total_count of this GrpcTimeSeriesResponse.  # noqa: E501


        :return: The total_count of this GrpcTimeSeriesResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this GrpcTimeSeriesResponse.


        :param total_count: The total_count of this GrpcTimeSeriesResponse.  # noqa: E501
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
        if issubclass(GrpcTimeSeriesResponse, dict):
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
        if not isinstance(other, GrpcTimeSeriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
