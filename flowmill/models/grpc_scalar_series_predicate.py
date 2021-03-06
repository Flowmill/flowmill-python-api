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


class GrpcScalarSeriesPredicate(object):
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
        'window': 'GrpcDataWindow',
        'label_equality_pairs': 'list[GrpcLabelEqualityPair]',
        'comparator': 'GrpcComparatorType',
        'reducer': 'GrpcScalarReducerType',
        'thresholds': 'list[GrpcScalarSeriesPredicateThreshold]'
    }

    attribute_map = {
        'metric': 'metric',
        'window': 'window',
        'label_equality_pairs': 'labelEqualityPairs',
        'comparator': 'comparator',
        'reducer': 'reducer',
        'thresholds': 'thresholds'
    }

    def __init__(self, metric=None, window=None, label_equality_pairs=None, comparator=None, reducer=None, thresholds=None):  # noqa: E501
        """GrpcScalarSeriesPredicate - a model defined in Swagger"""  # noqa: E501

        self._metric = None
        self._window = None
        self._label_equality_pairs = None
        self._comparator = None
        self._reducer = None
        self._thresholds = None
        self.discriminator = None

        if metric is not None:
            self.metric = metric
        if window is not None:
            self.window = window
        if label_equality_pairs is not None:
            self.label_equality_pairs = label_equality_pairs
        if comparator is not None:
            self.comparator = comparator
        if reducer is not None:
            self.reducer = reducer
        if thresholds is not None:
            self.thresholds = thresholds

    @property
    def metric(self):
        """Gets the metric of this GrpcScalarSeriesPredicate.  # noqa: E501


        :return: The metric of this GrpcScalarSeriesPredicate.  # noqa: E501
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this GrpcScalarSeriesPredicate.


        :param metric: The metric of this GrpcScalarSeriesPredicate.  # noqa: E501
        :type: str
        """

        self._metric = metric

    @property
    def window(self):
        """Gets the window of this GrpcScalarSeriesPredicate.  # noqa: E501


        :return: The window of this GrpcScalarSeriesPredicate.  # noqa: E501
        :rtype: GrpcDataWindow
        """
        return self._window

    @window.setter
    def window(self, window):
        """Sets the window of this GrpcScalarSeriesPredicate.


        :param window: The window of this GrpcScalarSeriesPredicate.  # noqa: E501
        :type: GrpcDataWindow
        """

        self._window = window

    @property
    def label_equality_pairs(self):
        """Gets the label_equality_pairs of this GrpcScalarSeriesPredicate.  # noqa: E501


        :return: The label_equality_pairs of this GrpcScalarSeriesPredicate.  # noqa: E501
        :rtype: list[GrpcLabelEqualityPair]
        """
        return self._label_equality_pairs

    @label_equality_pairs.setter
    def label_equality_pairs(self, label_equality_pairs):
        """Sets the label_equality_pairs of this GrpcScalarSeriesPredicate.


        :param label_equality_pairs: The label_equality_pairs of this GrpcScalarSeriesPredicate.  # noqa: E501
        :type: list[GrpcLabelEqualityPair]
        """

        self._label_equality_pairs = label_equality_pairs

    @property
    def comparator(self):
        """Gets the comparator of this GrpcScalarSeriesPredicate.  # noqa: E501

        First operand is the reduced time series value, second is the threshold.  # noqa: E501

        :return: The comparator of this GrpcScalarSeriesPredicate.  # noqa: E501
        :rtype: GrpcComparatorType
        """
        return self._comparator

    @comparator.setter
    def comparator(self, comparator):
        """Sets the comparator of this GrpcScalarSeriesPredicate.

        First operand is the reduced time series value, second is the threshold.  # noqa: E501

        :param comparator: The comparator of this GrpcScalarSeriesPredicate.  # noqa: E501
        :type: GrpcComparatorType
        """

        self._comparator = comparator

    @property
    def reducer(self):
        """Gets the reducer of this GrpcScalarSeriesPredicate.  # noqa: E501

        Describes how to reduce the time series to a single value.  # noqa: E501

        :return: The reducer of this GrpcScalarSeriesPredicate.  # noqa: E501
        :rtype: GrpcScalarReducerType
        """
        return self._reducer

    @reducer.setter
    def reducer(self, reducer):
        """Sets the reducer of this GrpcScalarSeriesPredicate.

        Describes how to reduce the time series to a single value.  # noqa: E501

        :param reducer: The reducer of this GrpcScalarSeriesPredicate.  # noqa: E501
        :type: GrpcScalarReducerType
        """

        self._reducer = reducer

    @property
    def thresholds(self):
        """Gets the thresholds of this GrpcScalarSeriesPredicate.  # noqa: E501


        :return: The thresholds of this GrpcScalarSeriesPredicate.  # noqa: E501
        :rtype: list[GrpcScalarSeriesPredicateThreshold]
        """
        return self._thresholds

    @thresholds.setter
    def thresholds(self, thresholds):
        """Sets the thresholds of this GrpcScalarSeriesPredicate.


        :param thresholds: The thresholds of this GrpcScalarSeriesPredicate.  # noqa: E501
        :type: list[GrpcScalarSeriesPredicateThreshold]
        """

        self._thresholds = thresholds

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
        if issubclass(GrpcScalarSeriesPredicate, dict):
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
        if not isinstance(other, GrpcScalarSeriesPredicate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
