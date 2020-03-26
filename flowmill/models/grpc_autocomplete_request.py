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


class GrpcAutocompleteRequest(object):
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
        'filters': 'list[GrpcFilter]',
        'label': 'str',
        'metric': 'str',
        'directionality': 'GrpcDirectionality'
    }

    attribute_map = {
        'start': 'start',
        'end': 'end',
        'filters': 'filters',
        'label': 'label',
        'metric': 'metric',
        'directionality': 'directionality'
    }

    def __init__(self, start=None, end=None, filters=None, label=None, metric=None, directionality=None):  # noqa: E501
        """GrpcAutocompleteRequest - a model defined in Swagger"""  # noqa: E501

        self._start = None
        self._end = None
        self._filters = None
        self._label = None
        self._metric = None
        self._directionality = None
        self.discriminator = None

        if start is not None:
            self.start = start
        if end is not None:
            self.end = end
        if filters is not None:
            self.filters = filters
        if label is not None:
            self.label = label
        if metric is not None:
            self.metric = metric
        if directionality is not None:
            self.directionality = directionality

    @property
    def start(self):
        """Gets the start of this GrpcAutocompleteRequest.  # noqa: E501

        start and end times that should be taken off the time control component.  # noqa: E501

        :return: The start of this GrpcAutocompleteRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this GrpcAutocompleteRequest.

        start and end times that should be taken off the time control component.  # noqa: E501

        :param start: The start of this GrpcAutocompleteRequest.  # noqa: E501
        :type: datetime
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this GrpcAutocompleteRequest.  # noqa: E501


        :return: The end of this GrpcAutocompleteRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this GrpcAutocompleteRequest.


        :param end: The end of this GrpcAutocompleteRequest.  # noqa: E501
        :type: datetime
        """

        self._end = end

    @property
    def filters(self):
        """Gets the filters of this GrpcAutocompleteRequest.  # noqa: E501


        :return: The filters of this GrpcAutocompleteRequest.  # noqa: E501
        :rtype: list[GrpcFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this GrpcAutocompleteRequest.


        :param filters: The filters of this GrpcAutocompleteRequest.  # noqa: E501
        :type: list[GrpcFilter]
        """

        self._filters = filters

    @property
    def label(self):
        """Gets the label of this GrpcAutocompleteRequest.  # noqa: E501


        :return: The label of this GrpcAutocompleteRequest.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this GrpcAutocompleteRequest.


        :param label: The label of this GrpcAutocompleteRequest.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def metric(self):
        """Gets the metric of this GrpcAutocompleteRequest.  # noqa: E501

        metric the autocomplete should work on.  # noqa: E501

        :return: The metric of this GrpcAutocompleteRequest.  # noqa: E501
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this GrpcAutocompleteRequest.

        metric the autocomplete should work on.  # noqa: E501

        :param metric: The metric of this GrpcAutocompleteRequest.  # noqa: E501
        :type: str
        """

        self._metric = metric

    @property
    def directionality(self):
        """Gets the directionality of this GrpcAutocompleteRequest.  # noqa: E501

        Which direction(s) to query. See TimeSeriesRequest.directionality comment for more context.  # noqa: E501

        :return: The directionality of this GrpcAutocompleteRequest.  # noqa: E501
        :rtype: GrpcDirectionality
        """
        return self._directionality

    @directionality.setter
    def directionality(self, directionality):
        """Sets the directionality of this GrpcAutocompleteRequest.

        Which direction(s) to query. See TimeSeriesRequest.directionality comment for more context.  # noqa: E501

        :param directionality: The directionality of this GrpcAutocompleteRequest.  # noqa: E501
        :type: GrpcDirectionality
        """

        self._directionality = directionality

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
        if issubclass(GrpcAutocompleteRequest, dict):
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
        if not isinstance(other, GrpcAutocompleteRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
