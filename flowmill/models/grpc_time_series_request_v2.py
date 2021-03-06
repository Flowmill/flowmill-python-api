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


class GrpcTimeSeriesRequestV2(object):
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
        'source_filters': 'list[GrpcFilter]',
        'destination_filters': 'list[GrpcFilter]',
        'metric': 'str',
        'source_grouping': 'list[str]',
        'destination_grouping': 'list[str]',
        'directionality': 'GrpcDirectionality',
        'top_k': 'int',
        'no_rollups': 'bool',
        'label_equality': 'list[GrpcLabelEqualityPair]',
        'no_zero_padding': 'bool'
    }

    attribute_map = {
        'end': 'end',
        'duration': 'duration',
        'num_steps': 'numSteps',
        'source_filters': 'sourceFilters',
        'destination_filters': 'destinationFilters',
        'metric': 'metric',
        'source_grouping': 'sourceGrouping',
        'destination_grouping': 'destinationGrouping',
        'directionality': 'directionality',
        'top_k': 'topK',
        'no_rollups': 'noRollups',
        'label_equality': 'labelEquality',
        'no_zero_padding': 'noZeroPadding'
    }

    def __init__(self, end=None, duration=None, num_steps=None, source_filters=None, destination_filters=None, metric=None, source_grouping=None, destination_grouping=None, directionality=None, top_k=None, no_rollups=None, label_equality=None, no_zero_padding=None):  # noqa: E501
        """GrpcTimeSeriesRequestV2 - a model defined in Swagger"""  # noqa: E501

        self._end = None
        self._duration = None
        self._num_steps = None
        self._source_filters = None
        self._destination_filters = None
        self._metric = None
        self._source_grouping = None
        self._destination_grouping = None
        self._directionality = None
        self._top_k = None
        self._no_rollups = None
        self._label_equality = None
        self._no_zero_padding = None
        self.discriminator = None

        if end is not None:
            self.end = end
        if duration is not None:
            self.duration = duration
        if num_steps is not None:
            self.num_steps = num_steps
        if source_filters is not None:
            self.source_filters = source_filters
        if destination_filters is not None:
            self.destination_filters = destination_filters
        if metric is not None:
            self.metric = metric
        if source_grouping is not None:
            self.source_grouping = source_grouping
        if destination_grouping is not None:
            self.destination_grouping = destination_grouping
        if directionality is not None:
            self.directionality = directionality
        if top_k is not None:
            self.top_k = top_k
        if no_rollups is not None:
            self.no_rollups = no_rollups
        if label_equality is not None:
            self.label_equality = label_equality
        if no_zero_padding is not None:
            self.no_zero_padding = no_zero_padding

    @property
    def end(self):
        """Gets the end of this GrpcTimeSeriesRequestV2.  # noqa: E501

        We specify query time ranges with a tuple of (end, duration, num_steps).  From these values, we compute:    - step_sec = duration / num_steps    - start = end - (step_sec * num_steps)  The returned timeseries will contain points between start and end that are evenly spaced at step_sec. More precisely, points[i] will correspond to the range: ((start + (step_sec * i)), (start + step_sec * (i + 1)].  We enforce the following constraints on all queries:    - end is expected to be in the UTC timezone    - end must be at or before the current time    - duration must be less than some MAX_QUERY_DURATION, currently 2 days    - duration must be an integral number of seconds    - duration / num_steps must result in an integral number of samples    [1]    - duration / num_steps must be less than some MAX_NUM_SAMPLES    - num_steps must be less than MAX_NUM_POINTS (about 1000)  [1] We currently store data at 5sec, 30sec, and 600sec samples. So, when we derive step = duration / num_steps, we enfore that step is either:    - a multiple of 5s if < 30s as we read from the 5sec data, or    - a multiple of 30s if > 30s and < 600s as we read from the 30sec    data,    - a multiple of 600s if > 600s as we read from the 600sec data.  Queries that violate any of these constraints will result in an INVALID_ARGUMENT error.  # noqa: E501

        :return: The end of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this GrpcTimeSeriesRequestV2.

        We specify query time ranges with a tuple of (end, duration, num_steps).  From these values, we compute:    - step_sec = duration / num_steps    - start = end - (step_sec * num_steps)  The returned timeseries will contain points between start and end that are evenly spaced at step_sec. More precisely, points[i] will correspond to the range: ((start + (step_sec * i)), (start + step_sec * (i + 1)].  We enforce the following constraints on all queries:    - end is expected to be in the UTC timezone    - end must be at or before the current time    - duration must be less than some MAX_QUERY_DURATION, currently 2 days    - duration must be an integral number of seconds    - duration / num_steps must result in an integral number of samples    [1]    - duration / num_steps must be less than some MAX_NUM_SAMPLES    - num_steps must be less than MAX_NUM_POINTS (about 1000)  [1] We currently store data at 5sec, 30sec, and 600sec samples. So, when we derive step = duration / num_steps, we enfore that step is either:    - a multiple of 5s if < 30s as we read from the 5sec data, or    - a multiple of 30s if > 30s and < 600s as we read from the 30sec    data,    - a multiple of 600s if > 600s as we read from the 600sec data.  Queries that violate any of these constraints will result in an INVALID_ARGUMENT error.  # noqa: E501

        :param end: The end of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :type: datetime
        """

        self._end = end

    @property
    def duration(self):
        """Gets the duration of this GrpcTimeSeriesRequestV2.  # noqa: E501


        :return: The duration of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this GrpcTimeSeriesRequestV2.


        :param duration: The duration of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def num_steps(self):
        """Gets the num_steps of this GrpcTimeSeriesRequestV2.  # noqa: E501


        :return: The num_steps of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :rtype: int
        """
        return self._num_steps

    @num_steps.setter
    def num_steps(self, num_steps):
        """Sets the num_steps of this GrpcTimeSeriesRequestV2.


        :param num_steps: The num_steps of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :type: int
        """

        self._num_steps = num_steps

    @property
    def source_filters(self):
        """Gets the source_filters of this GrpcTimeSeriesRequestV2.  # noqa: E501

        Lists of filters for the source and destinations.  The `directionality`field determines how these labels get converted to labels queried against the backing TSDB.  For instance, if we query for    - source_filters = [{'role', IN ['my-role']} and    - destination_filters = [{'az', IN, ['my-az']}] Then they potentially get reversed with directionality:   - FORWARD, then these are executed as written.   - BACKWARD, then these become:       - source_filters = [{'az', IN, ['my-az']}]       - destination_filters = [{'role', IN ['my-role']}]   - BOTH, then both of the above queries are done and the results are        merged together.  # noqa: E501

        :return: The source_filters of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :rtype: list[GrpcFilter]
        """
        return self._source_filters

    @source_filters.setter
    def source_filters(self, source_filters):
        """Sets the source_filters of this GrpcTimeSeriesRequestV2.

        Lists of filters for the source and destinations.  The `directionality`field determines how these labels get converted to labels queried against the backing TSDB.  For instance, if we query for    - source_filters = [{'role', IN ['my-role']} and    - destination_filters = [{'az', IN, ['my-az']}] Then they potentially get reversed with directionality:   - FORWARD, then these are executed as written.   - BACKWARD, then these become:       - source_filters = [{'az', IN, ['my-az']}]       - destination_filters = [{'role', IN ['my-role']}]   - BOTH, then both of the above queries are done and the results are        merged together.  # noqa: E501

        :param source_filters: The source_filters of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :type: list[GrpcFilter]
        """

        self._source_filters = source_filters

    @property
    def destination_filters(self):
        """Gets the destination_filters of this GrpcTimeSeriesRequestV2.  # noqa: E501


        :return: The destination_filters of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :rtype: list[GrpcFilter]
        """
        return self._destination_filters

    @destination_filters.setter
    def destination_filters(self, destination_filters):
        """Sets the destination_filters of this GrpcTimeSeriesRequestV2.


        :param destination_filters: The destination_filters of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :type: list[GrpcFilter]
        """

        self._destination_filters = destination_filters

    @property
    def metric(self):
        """Gets the metric of this GrpcTimeSeriesRequestV2.  # noqa: E501

        Metric to return as timeseries.  We return metrics as durations, percents, or rates. A good rule of thumb for how to interpret metric values is: - metrics suffixed with _latency are in seconds, - metrics suffixed with _percent are percents of totals, and - all other metrics are rates, such as \"bytes per second\" or   \"udp_packets per second\" or \"http_code_200 per second.\"  # noqa: E501

        :return: The metric of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this GrpcTimeSeriesRequestV2.

        Metric to return as timeseries.  We return metrics as durations, percents, or rates. A good rule of thumb for how to interpret metric values is: - metrics suffixed with _latency are in seconds, - metrics suffixed with _percent are percents of totals, and - all other metrics are rates, such as \"bytes per second\" or   \"udp_packets per second\" or \"http_code_200 per second.\"  # noqa: E501

        :param metric: The metric of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :type: str
        """

        self._metric = metric

    @property
    def source_grouping(self):
        """Gets the source_grouping of this GrpcTimeSeriesRequestV2.  # noqa: E501

        A list of labels that the returned timeseries will include.  Queries must specify at least one grouping on either the source or destination side.  If only one side of the groupings are specified, then the returned timeseries will be aggregated for that one side, e.g., if we specify a query for source_grouping = ['id'], then the returned timeseries will be the sum of the specified metric aggregated by source address.  Note: The response's `series.source_labels` and `series.destination_labels` will contain `source_grouping` and `destination_grouping`, for both FORWARD and REVERSED responses, i.e., reversed timeseries don't reverse the source and destination grouping labels.  # noqa: E501

        :return: The source_grouping of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._source_grouping

    @source_grouping.setter
    def source_grouping(self, source_grouping):
        """Sets the source_grouping of this GrpcTimeSeriesRequestV2.

        A list of labels that the returned timeseries will include.  Queries must specify at least one grouping on either the source or destination side.  If only one side of the groupings are specified, then the returned timeseries will be aggregated for that one side, e.g., if we specify a query for source_grouping = ['id'], then the returned timeseries will be the sum of the specified metric aggregated by source address.  Note: The response's `series.source_labels` and `series.destination_labels` will contain `source_grouping` and `destination_grouping`, for both FORWARD and REVERSED responses, i.e., reversed timeseries don't reverse the source and destination grouping labels.  # noqa: E501

        :param source_grouping: The source_grouping of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :type: list[str]
        """

        self._source_grouping = source_grouping

    @property
    def destination_grouping(self):
        """Gets the destination_grouping of this GrpcTimeSeriesRequestV2.  # noqa: E501


        :return: The destination_grouping of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._destination_grouping

    @destination_grouping.setter
    def destination_grouping(self, destination_grouping):
        """Sets the destination_grouping of this GrpcTimeSeriesRequestV2.


        :param destination_grouping: The destination_grouping of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :type: list[str]
        """

        self._destination_grouping = destination_grouping

    @property
    def directionality(self):
        """Gets the directionality of this GrpcTimeSeriesRequestV2.  # noqa: E501

        Used to conditionally reverse the specified filters.  # noqa: E501

        :return: The directionality of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :rtype: GrpcDirectionality
        """
        return self._directionality

    @directionality.setter
    def directionality(self, directionality):
        """Sets the directionality of this GrpcTimeSeriesRequestV2.

        Used to conditionally reverse the specified filters.  # noqa: E501

        :param directionality: The directionality of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :type: GrpcDirectionality
        """

        self._directionality = directionality

    @property
    def top_k(self):
        """Gets the top_k of this GrpcTimeSeriesRequestV2.  # noqa: E501

        Maximum number of time series to return. Defaults to 30 if unspecified. If set to -1, then we'll return all timeseries.  When requesting directionality FORWARD or REVERSE, then we will return no more than k timeseries. If requesting directionality BOTH, then we'll return at most 2*k timeseries, which include the k FORWARD timeseries and their corresponding REVERSE timeseries.  # noqa: E501

        :return: The top_k of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :rtype: int
        """
        return self._top_k

    @top_k.setter
    def top_k(self, top_k):
        """Sets the top_k of this GrpcTimeSeriesRequestV2.

        Maximum number of time series to return. Defaults to 30 if unspecified. If set to -1, then we'll return all timeseries.  When requesting directionality FORWARD or REVERSE, then we will return no more than k timeseries. If requesting directionality BOTH, then we'll return at most 2*k timeseries, which include the k FORWARD timeseries and their corresponding REVERSE timeseries.  # noqa: E501

        :param top_k: The top_k of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :type: int
        """

        self._top_k = top_k

    @property
    def no_rollups(self):
        """Gets the no_rollups of this GrpcTimeSeriesRequestV2.  # noqa: E501

        Flag to manually disable the use of time-aggregated data.  Our default TSDB stores samples at 1sec resoltuion. Our \"rolled up\" TSDB stores data at 30s or 600s resolution.  # noqa: E501

        :return: The no_rollups of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :rtype: bool
        """
        return self._no_rollups

    @no_rollups.setter
    def no_rollups(self, no_rollups):
        """Sets the no_rollups of this GrpcTimeSeriesRequestV2.

        Flag to manually disable the use of time-aggregated data.  Our default TSDB stores samples at 1sec resoltuion. Our \"rolled up\" TSDB stores data at 30s or 600s resolution.  # noqa: E501

        :param no_rollups: The no_rollups of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :type: bool
        """

        self._no_rollups = no_rollups

    @property
    def label_equality(self):
        """Gets the label_equality of this GrpcTimeSeriesRequestV2.  # noqa: E501

        Query structure to perform '!=' or '==' operations on a subset of timeseries labels.  We commonly use these to query for cross-zone traffic, which looks like { \"label\": \"az\", \"equal\": false }.  # noqa: E501

        :return: The label_equality of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :rtype: list[GrpcLabelEqualityPair]
        """
        return self._label_equality

    @label_equality.setter
    def label_equality(self, label_equality):
        """Sets the label_equality of this GrpcTimeSeriesRequestV2.

        Query structure to perform '!=' or '==' operations on a subset of timeseries labels.  We commonly use these to query for cross-zone traffic, which looks like { \"label\": \"az\", \"equal\": false }.  # noqa: E501

        :param label_equality: The label_equality of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :type: list[GrpcLabelEqualityPair]
        """

        self._label_equality = label_equality

    @property
    def no_zero_padding(self):
        """Gets the no_zero_padding of this GrpcTimeSeriesRequestV2.  # noqa: E501

        Controls how we compute latency timeseries values when there are no samples in a given time range.  If true, then the value of latencies in time ranges with no samples will be marked with a -1.  Otherwise, latency timeseries will be filled with 0s when we have no samples. This is the default behavior to ensure backward compatability.  Beware: the default behavior makes it impossible to differentiate between \"0 measurements\" and \"measured 0.\"  This applies only to latency metrics because we use \"no samples\" to mean 0 for for all other metrics, such as rates and percents.  # noqa: E501

        :return: The no_zero_padding of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :rtype: bool
        """
        return self._no_zero_padding

    @no_zero_padding.setter
    def no_zero_padding(self, no_zero_padding):
        """Sets the no_zero_padding of this GrpcTimeSeriesRequestV2.

        Controls how we compute latency timeseries values when there are no samples in a given time range.  If true, then the value of latencies in time ranges with no samples will be marked with a -1.  Otherwise, latency timeseries will be filled with 0s when we have no samples. This is the default behavior to ensure backward compatability.  Beware: the default behavior makes it impossible to differentiate between \"0 measurements\" and \"measured 0.\"  This applies only to latency metrics because we use \"no samples\" to mean 0 for for all other metrics, such as rates and percents.  # noqa: E501

        :param no_zero_padding: The no_zero_padding of this GrpcTimeSeriesRequestV2.  # noqa: E501
        :type: bool
        """

        self._no_zero_padding = no_zero_padding

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
        if issubclass(GrpcTimeSeriesRequestV2, dict):
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
        if not isinstance(other, GrpcTimeSeriesRequestV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
