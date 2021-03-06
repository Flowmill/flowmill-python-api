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


class GrpcConnectionSummary(object):
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
        'source_labels': 'list[GrpcLabel]',
        'destination_labels': 'list[GrpcLabel]',
        'num_ok': 'float',
        'num_bad': 'float',
        'percent_bad': 'float',
        'points_ok': 'GrpcPoint',
        'points_bad': 'GrpcPoint'
    }

    attribute_map = {
        'source_labels': 'sourceLabels',
        'destination_labels': 'destinationLabels',
        'num_ok': 'numOk',
        'num_bad': 'numBad',
        'percent_bad': 'percentBad',
        'points_ok': 'pointsOk',
        'points_bad': 'pointsBad'
    }

    def __init__(self, source_labels=None, destination_labels=None, num_ok=None, num_bad=None, percent_bad=None, points_ok=None, points_bad=None):  # noqa: E501
        """GrpcConnectionSummary - a model defined in Swagger"""  # noqa: E501

        self._source_labels = None
        self._destination_labels = None
        self._num_ok = None
        self._num_bad = None
        self._percent_bad = None
        self._points_ok = None
        self._points_bad = None
        self.discriminator = None

        if source_labels is not None:
            self.source_labels = source_labels
        if destination_labels is not None:
            self.destination_labels = destination_labels
        if num_ok is not None:
            self.num_ok = num_ok
        if num_bad is not None:
            self.num_bad = num_bad
        if percent_bad is not None:
            self.percent_bad = percent_bad
        if points_ok is not None:
            self.points_ok = points_ok
        if points_bad is not None:
            self.points_bad = points_bad

    @property
    def source_labels(self):
        """Gets the source_labels of this GrpcConnectionSummary.  # noqa: E501


        :return: The source_labels of this GrpcConnectionSummary.  # noqa: E501
        :rtype: list[GrpcLabel]
        """
        return self._source_labels

    @source_labels.setter
    def source_labels(self, source_labels):
        """Sets the source_labels of this GrpcConnectionSummary.


        :param source_labels: The source_labels of this GrpcConnectionSummary.  # noqa: E501
        :type: list[GrpcLabel]
        """

        self._source_labels = source_labels

    @property
    def destination_labels(self):
        """Gets the destination_labels of this GrpcConnectionSummary.  # noqa: E501


        :return: The destination_labels of this GrpcConnectionSummary.  # noqa: E501
        :rtype: list[GrpcLabel]
        """
        return self._destination_labels

    @destination_labels.setter
    def destination_labels(self, destination_labels):
        """Sets the destination_labels of this GrpcConnectionSummary.


        :param destination_labels: The destination_labels of this GrpcConnectionSummary.  # noqa: E501
        :type: list[GrpcLabel]
        """

        self._destination_labels = destination_labels

    @property
    def num_ok(self):
        """Gets the num_ok of this GrpcConnectionSummary.  # noqa: E501


        :return: The num_ok of this GrpcConnectionSummary.  # noqa: E501
        :rtype: float
        """
        return self._num_ok

    @num_ok.setter
    def num_ok(self, num_ok):
        """Sets the num_ok of this GrpcConnectionSummary.


        :param num_ok: The num_ok of this GrpcConnectionSummary.  # noqa: E501
        :type: float
        """

        self._num_ok = num_ok

    @property
    def num_bad(self):
        """Gets the num_bad of this GrpcConnectionSummary.  # noqa: E501


        :return: The num_bad of this GrpcConnectionSummary.  # noqa: E501
        :rtype: float
        """
        return self._num_bad

    @num_bad.setter
    def num_bad(self, num_bad):
        """Sets the num_bad of this GrpcConnectionSummary.


        :param num_bad: The num_bad of this GrpcConnectionSummary.  # noqa: E501
        :type: float
        """

        self._num_bad = num_bad

    @property
    def percent_bad(self):
        """Gets the percent_bad of this GrpcConnectionSummary.  # noqa: E501


        :return: The percent_bad of this GrpcConnectionSummary.  # noqa: E501
        :rtype: float
        """
        return self._percent_bad

    @percent_bad.setter
    def percent_bad(self, percent_bad):
        """Sets the percent_bad of this GrpcConnectionSummary.


        :param percent_bad: The percent_bad of this GrpcConnectionSummary.  # noqa: E501
        :type: float
        """

        self._percent_bad = percent_bad

    @property
    def points_ok(self):
        """Gets the points_ok of this GrpcConnectionSummary.  # noqa: E501


        :return: The points_ok of this GrpcConnectionSummary.  # noqa: E501
        :rtype: GrpcPoint
        """
        return self._points_ok

    @points_ok.setter
    def points_ok(self, points_ok):
        """Sets the points_ok of this GrpcConnectionSummary.


        :param points_ok: The points_ok of this GrpcConnectionSummary.  # noqa: E501
        :type: GrpcPoint
        """

        self._points_ok = points_ok

    @property
    def points_bad(self):
        """Gets the points_bad of this GrpcConnectionSummary.  # noqa: E501


        :return: The points_bad of this GrpcConnectionSummary.  # noqa: E501
        :rtype: GrpcPoint
        """
        return self._points_bad

    @points_bad.setter
    def points_bad(self, points_bad):
        """Sets the points_bad of this GrpcConnectionSummary.


        :param points_bad: The points_bad of this GrpcConnectionSummary.  # noqa: E501
        :type: GrpcPoint
        """

        self._points_bad = points_bad

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
        if issubclass(GrpcConnectionSummary, dict):
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
        if not isinstance(other, GrpcConnectionSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
