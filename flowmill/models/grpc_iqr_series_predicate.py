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


class GrpcIqrSeriesPredicate(object):
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
        'median_interval': 'str',
        'iqr_interval': 'str',
        'thresholds': 'list[GrpcIqrSeriesPredicateThreshold]'
    }

    attribute_map = {
        'metric': 'metric',
        'window': 'window',
        'label_equality_pairs': 'labelEqualityPairs',
        'median_interval': 'medianInterval',
        'iqr_interval': 'iqrInterval',
        'thresholds': 'thresholds'
    }

    def __init__(self, metric=None, window=None, label_equality_pairs=None, median_interval=None, iqr_interval=None, thresholds=None):  # noqa: E501
        """GrpcIqrSeriesPredicate - a model defined in Swagger"""  # noqa: E501

        self._metric = None
        self._window = None
        self._label_equality_pairs = None
        self._median_interval = None
        self._iqr_interval = None
        self._thresholds = None
        self.discriminator = None

        if metric is not None:
            self.metric = metric
        if window is not None:
            self.window = window
        if label_equality_pairs is not None:
            self.label_equality_pairs = label_equality_pairs
        if median_interval is not None:
            self.median_interval = median_interval
        if iqr_interval is not None:
            self.iqr_interval = iqr_interval
        if thresholds is not None:
            self.thresholds = thresholds

    @property
    def metric(self):
        """Gets the metric of this GrpcIqrSeriesPredicate.  # noqa: E501


        :return: The metric of this GrpcIqrSeriesPredicate.  # noqa: E501
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this GrpcIqrSeriesPredicate.


        :param metric: The metric of this GrpcIqrSeriesPredicate.  # noqa: E501
        :type: str
        """

        self._metric = metric

    @property
    def window(self):
        """Gets the window of this GrpcIqrSeriesPredicate.  # noqa: E501

        The window against which this predicate will be evaluated.  # noqa: E501

        :return: The window of this GrpcIqrSeriesPredicate.  # noqa: E501
        :rtype: GrpcDataWindow
        """
        return self._window

    @window.setter
    def window(self, window):
        """Sets the window of this GrpcIqrSeriesPredicate.

        The window against which this predicate will be evaluated.  # noqa: E501

        :param window: The window of this GrpcIqrSeriesPredicate.  # noqa: E501
        :type: GrpcDataWindow
        """

        self._window = window

    @property
    def label_equality_pairs(self):
        """Gets the label_equality_pairs of this GrpcIqrSeriesPredicate.  # noqa: E501


        :return: The label_equality_pairs of this GrpcIqrSeriesPredicate.  # noqa: E501
        :rtype: list[GrpcLabelEqualityPair]
        """
        return self._label_equality_pairs

    @label_equality_pairs.setter
    def label_equality_pairs(self, label_equality_pairs):
        """Sets the label_equality_pairs of this GrpcIqrSeriesPredicate.


        :param label_equality_pairs: The label_equality_pairs of this GrpcIqrSeriesPredicate.  # noqa: E501
        :type: list[GrpcLabelEqualityPair]
        """

        self._label_equality_pairs = label_equality_pairs

    @property
    def median_interval(self):
        """Gets the median_interval of this GrpcIqrSeriesPredicate.  # noqa: E501

        The length of the moving window for the median.  # noqa: E501

        :return: The median_interval of this GrpcIqrSeriesPredicate.  # noqa: E501
        :rtype: str
        """
        return self._median_interval

    @median_interval.setter
    def median_interval(self, median_interval):
        """Sets the median_interval of this GrpcIqrSeriesPredicate.

        The length of the moving window for the median.  # noqa: E501

        :param median_interval: The median_interval of this GrpcIqrSeriesPredicate.  # noqa: E501
        :type: str
        """

        self._median_interval = median_interval

    @property
    def iqr_interval(self):
        """Gets the iqr_interval of this GrpcIqrSeriesPredicate.  # noqa: E501

        The length of the moving window for the IQR bounds.  # noqa: E501

        :return: The iqr_interval of this GrpcIqrSeriesPredicate.  # noqa: E501
        :rtype: str
        """
        return self._iqr_interval

    @iqr_interval.setter
    def iqr_interval(self, iqr_interval):
        """Sets the iqr_interval of this GrpcIqrSeriesPredicate.

        The length of the moving window for the IQR bounds.  # noqa: E501

        :param iqr_interval: The iqr_interval of this GrpcIqrSeriesPredicate.  # noqa: E501
        :type: str
        """

        self._iqr_interval = iqr_interval

    @property
    def thresholds(self):
        """Gets the thresholds of this GrpcIqrSeriesPredicate.  # noqa: E501


        :return: The thresholds of this GrpcIqrSeriesPredicate.  # noqa: E501
        :rtype: list[GrpcIqrSeriesPredicateThreshold]
        """
        return self._thresholds

    @thresholds.setter
    def thresholds(self, thresholds):
        """Sets the thresholds of this GrpcIqrSeriesPredicate.


        :param thresholds: The thresholds of this GrpcIqrSeriesPredicate.  # noqa: E501
        :type: list[GrpcIqrSeriesPredicateThreshold]
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
        if issubclass(GrpcIqrSeriesPredicate, dict):
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
        if not isinstance(other, GrpcIqrSeriesPredicate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
