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


class GrpcTimeSeriesRequest(object):
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
        'step': 'str',
        'filters': 'list[GrpcFilter]',
        'source_filters': 'list[GrpcFilter]',
        'destination_filters': 'list[GrpcFilter]',
        'metric': 'str',
        'focus_zoom': 'str',
        'peer_zoom': 'str',
        'source_grouping': 'list[str]',
        'destination_grouping': 'list[str]',
        'edge_grouping': 'list[str]',
        'anonymize': 'bool',
        'directionality': 'GrpcDirectionality',
        'locality': 'GrpcLocality',
        'top_k': 'int',
        'min_total_values_threshold': 'float',
        'no_rollups': 'bool',
        'label_equality': 'list[GrpcLabelEqualityPair]',
        'aggregation': 'GrpcAggregationMethod'
    }

    attribute_map = {
        'start': 'start',
        'end': 'end',
        'step': 'step',
        'filters': 'filters',
        'source_filters': 'sourceFilters',
        'destination_filters': 'destinationFilters',
        'metric': 'metric',
        'focus_zoom': 'focusZoom',
        'peer_zoom': 'peerZoom',
        'source_grouping': 'sourceGrouping',
        'destination_grouping': 'destinationGrouping',
        'edge_grouping': 'edgeGrouping',
        'anonymize': 'anonymize',
        'directionality': 'directionality',
        'locality': 'locality',
        'top_k': 'topK',
        'min_total_values_threshold': 'minTotalValuesThreshold',
        'no_rollups': 'noRollups',
        'label_equality': 'labelEquality',
        'aggregation': 'aggregation'
    }

    def __init__(self, start=None, end=None, step=None, filters=None, source_filters=None, destination_filters=None, metric=None, focus_zoom=None, peer_zoom=None, source_grouping=None, destination_grouping=None, edge_grouping=None, anonymize=None, directionality=None, locality=None, top_k=None, min_total_values_threshold=None, no_rollups=None, label_equality=None, aggregation=None):  # noqa: E501
        """GrpcTimeSeriesRequest - a model defined in Swagger"""  # noqa: E501

        self._start = None
        self._end = None
        self._step = None
        self._filters = None
        self._source_filters = None
        self._destination_filters = None
        self._metric = None
        self._focus_zoom = None
        self._peer_zoom = None
        self._source_grouping = None
        self._destination_grouping = None
        self._edge_grouping = None
        self._anonymize = None
        self._directionality = None
        self._locality = None
        self._top_k = None
        self._min_total_values_threshold = None
        self._no_rollups = None
        self._label_equality = None
        self._aggregation = None
        self.discriminator = None

        if start is not None:
            self.start = start
        if end is not None:
            self.end = end
        if step is not None:
            self.step = step
        if filters is not None:
            self.filters = filters
        if source_filters is not None:
            self.source_filters = source_filters
        if destination_filters is not None:
            self.destination_filters = destination_filters
        if metric is not None:
            self.metric = metric
        if focus_zoom is not None:
            self.focus_zoom = focus_zoom
        if peer_zoom is not None:
            self.peer_zoom = peer_zoom
        if source_grouping is not None:
            self.source_grouping = source_grouping
        if destination_grouping is not None:
            self.destination_grouping = destination_grouping
        if edge_grouping is not None:
            self.edge_grouping = edge_grouping
        if anonymize is not None:
            self.anonymize = anonymize
        if directionality is not None:
            self.directionality = directionality
        if locality is not None:
            self.locality = locality
        if top_k is not None:
            self.top_k = top_k
        if min_total_values_threshold is not None:
            self.min_total_values_threshold = min_total_values_threshold
        if no_rollups is not None:
            self.no_rollups = no_rollups
        if label_equality is not None:
            self.label_equality = label_equality
        if aggregation is not None:
            self.aggregation = aggregation

    @property
    def start(self):
        """Gets the start of this GrpcTimeSeriesRequest.  # noqa: E501


        :return: The start of this GrpcTimeSeriesRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this GrpcTimeSeriesRequest.


        :param start: The start of this GrpcTimeSeriesRequest.  # noqa: E501
        :type: datetime
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this GrpcTimeSeriesRequest.  # noqa: E501


        :return: The end of this GrpcTimeSeriesRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this GrpcTimeSeriesRequest.


        :param end: The end of this GrpcTimeSeriesRequest.  # noqa: E501
        :type: datetime
        """

        self._end = end

    @property
    def step(self):
        """Gets the step of this GrpcTimeSeriesRequest.  # noqa: E501

        Note: if using grpc-gateway, protobuf.Duration should be received as nanoseconds. The number of points returned is capped at a maximum, currently MaxPointsPerTimeseries = 10000. The returned result's step might be adjusted.  # noqa: E501

        :return: The step of this GrpcTimeSeriesRequest.  # noqa: E501
        :rtype: str
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this GrpcTimeSeriesRequest.

        Note: if using grpc-gateway, protobuf.Duration should be received as nanoseconds. The number of points returned is capped at a maximum, currently MaxPointsPerTimeseries = 10000. The returned result's step might be adjusted.  # noqa: E501

        :param step: The step of this GrpcTimeSeriesRequest.  # noqa: E501
        :type: str
        """

        self._step = step

    @property
    def filters(self):
        """Gets the filters of this GrpcTimeSeriesRequest.  # noqa: E501


        :return: The filters of this GrpcTimeSeriesRequest.  # noqa: E501
        :rtype: list[GrpcFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this GrpcTimeSeriesRequest.


        :param filters: The filters of this GrpcTimeSeriesRequest.  # noqa: E501
        :type: list[GrpcFilter]
        """

        self._filters = filters

    @property
    def source_filters(self):
        """Gets the source_filters of this GrpcTimeSeriesRequest.  # noqa: E501

        Lists of filters for the source and destinations. The `directionality` field determines how these labels get converted to labels queried against the backing TSDB.  For instance, lets say I do a query with `role=\"my-role\"` in `source_filters` and `az=\"my-az\"` in `destination_filters`. If `directionality` is ...   - ...FORWARD, then these become `{saz=\"my-az\", drole=\"my-role\"}`   - ...BACKWARD, then these become `{srole=\"my-role\", daz=\"my-az\"}`   - ...BOTH, then both of the above queries are done and the results are        merged together.  # noqa: E501

        :return: The source_filters of this GrpcTimeSeriesRequest.  # noqa: E501
        :rtype: list[GrpcFilter]
        """
        return self._source_filters

    @source_filters.setter
    def source_filters(self, source_filters):
        """Sets the source_filters of this GrpcTimeSeriesRequest.

        Lists of filters for the source and destinations. The `directionality` field determines how these labels get converted to labels queried against the backing TSDB.  For instance, lets say I do a query with `role=\"my-role\"` in `source_filters` and `az=\"my-az\"` in `destination_filters`. If `directionality` is ...   - ...FORWARD, then these become `{saz=\"my-az\", drole=\"my-role\"}`   - ...BACKWARD, then these become `{srole=\"my-role\", daz=\"my-az\"}`   - ...BOTH, then both of the above queries are done and the results are        merged together.  # noqa: E501

        :param source_filters: The source_filters of this GrpcTimeSeriesRequest.  # noqa: E501
        :type: list[GrpcFilter]
        """

        self._source_filters = source_filters

    @property
    def destination_filters(self):
        """Gets the destination_filters of this GrpcTimeSeriesRequest.  # noqa: E501


        :return: The destination_filters of this GrpcTimeSeriesRequest.  # noqa: E501
        :rtype: list[GrpcFilter]
        """
        return self._destination_filters

    @destination_filters.setter
    def destination_filters(self, destination_filters):
        """Sets the destination_filters of this GrpcTimeSeriesRequest.


        :param destination_filters: The destination_filters of this GrpcTimeSeriesRequest.  # noqa: E501
        :type: list[GrpcFilter]
        """

        self._destination_filters = destination_filters

    @property
    def metric(self):
        """Gets the metric of this GrpcTimeSeriesRequest.  # noqa: E501


        :return: The metric of this GrpcTimeSeriesRequest.  # noqa: E501
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this GrpcTimeSeriesRequest.


        :param metric: The metric of this GrpcTimeSeriesRequest.  # noqa: E501
        :type: str
        """

        self._metric = metric

    @property
    def focus_zoom(self):
        """Gets the focus_zoom of this GrpcTimeSeriesRequest.  # noqa: E501


        :return: The focus_zoom of this GrpcTimeSeriesRequest.  # noqa: E501
        :rtype: str
        """
        return self._focus_zoom

    @focus_zoom.setter
    def focus_zoom(self, focus_zoom):
        """Sets the focus_zoom of this GrpcTimeSeriesRequest.


        :param focus_zoom: The focus_zoom of this GrpcTimeSeriesRequest.  # noqa: E501
        :type: str
        """

        self._focus_zoom = focus_zoom

    @property
    def peer_zoom(self):
        """Gets the peer_zoom of this GrpcTimeSeriesRequest.  # noqa: E501


        :return: The peer_zoom of this GrpcTimeSeriesRequest.  # noqa: E501
        :rtype: str
        """
        return self._peer_zoom

    @peer_zoom.setter
    def peer_zoom(self, peer_zoom):
        """Sets the peer_zoom of this GrpcTimeSeriesRequest.


        :param peer_zoom: The peer_zoom of this GrpcTimeSeriesRequest.  # noqa: E501
        :type: str
        """

        self._peer_zoom = peer_zoom

    @property
    def source_grouping(self):
        """Gets the source_grouping of this GrpcTimeSeriesRequest.  # noqa: E501

        A list of labels that the returned timeseries will include.  If only one side of the groupings are specified, then the returned timeseries will be aggregated for that one side. E.g., if we specify a query for source_grouping = ['address'], then the returned timeseries will be the sum of the specified metric aggregated by source address. If no grouping is specified, no cross-timeseries aggregation is performed.  Note: The response's `series.source_labels` and `series.destination_labels` will contain `source_grouping` and `destination_grouping`, for both FORWARD and REVERSED responses, i.e., reversed timeseries don't reverse the source and destination grouping labels.  # noqa: E501

        :return: The source_grouping of this GrpcTimeSeriesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._source_grouping

    @source_grouping.setter
    def source_grouping(self, source_grouping):
        """Sets the source_grouping of this GrpcTimeSeriesRequest.

        A list of labels that the returned timeseries will include.  If only one side of the groupings are specified, then the returned timeseries will be aggregated for that one side. E.g., if we specify a query for source_grouping = ['address'], then the returned timeseries will be the sum of the specified metric aggregated by source address. If no grouping is specified, no cross-timeseries aggregation is performed.  Note: The response's `series.source_labels` and `series.destination_labels` will contain `source_grouping` and `destination_grouping`, for both FORWARD and REVERSED responses, i.e., reversed timeseries don't reverse the source and destination grouping labels.  # noqa: E501

        :param source_grouping: The source_grouping of this GrpcTimeSeriesRequest.  # noqa: E501
        :type: list[str]
        """

        self._source_grouping = source_grouping

    @property
    def destination_grouping(self):
        """Gets the destination_grouping of this GrpcTimeSeriesRequest.  # noqa: E501


        :return: The destination_grouping of this GrpcTimeSeriesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._destination_grouping

    @destination_grouping.setter
    def destination_grouping(self, destination_grouping):
        """Sets the destination_grouping of this GrpcTimeSeriesRequest.


        :param destination_grouping: The destination_grouping of this GrpcTimeSeriesRequest.  # noqa: E501
        :type: list[str]
        """

        self._destination_grouping = destination_grouping

    @property
    def edge_grouping(self):
        """Gets the edge_grouping of this GrpcTimeSeriesRequest.  # noqa: E501

        No longer supported. Returns an unimplemented error if defined.  # noqa: E501

        :return: The edge_grouping of this GrpcTimeSeriesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._edge_grouping

    @edge_grouping.setter
    def edge_grouping(self, edge_grouping):
        """Sets the edge_grouping of this GrpcTimeSeriesRequest.

        No longer supported. Returns an unimplemented error if defined.  # noqa: E501

        :param edge_grouping: The edge_grouping of this GrpcTimeSeriesRequest.  # noqa: E501
        :type: list[str]
        """

        self._edge_grouping = edge_grouping

    @property
    def anonymize(self):
        """Gets the anonymize of this GrpcTimeSeriesRequest.  # noqa: E501

        No longer supported. Returns an unimplemented error if defined.  # noqa: E501

        :return: The anonymize of this GrpcTimeSeriesRequest.  # noqa: E501
        :rtype: bool
        """
        return self._anonymize

    @anonymize.setter
    def anonymize(self, anonymize):
        """Sets the anonymize of this GrpcTimeSeriesRequest.

        No longer supported. Returns an unimplemented error if defined.  # noqa: E501

        :param anonymize: The anonymize of this GrpcTimeSeriesRequest.  # noqa: E501
        :type: bool
        """

        self._anonymize = anonymize

    @property
    def directionality(self):
        """Gets the directionality of this GrpcTimeSeriesRequest.  # noqa: E501

        Used to conditionally reverse the specified filters.  For example, if we query for flows with srole=(a), then we would get these results for different directionality values:  - FORWARD - all flows with srole=(a),  - REVERSE - all flows with drole=(a), and  - BOTH - the union of forward and reverse.  # noqa: E501

        :return: The directionality of this GrpcTimeSeriesRequest.  # noqa: E501
        :rtype: GrpcDirectionality
        """
        return self._directionality

    @directionality.setter
    def directionality(self, directionality):
        """Sets the directionality of this GrpcTimeSeriesRequest.

        Used to conditionally reverse the specified filters.  For example, if we query for flows with srole=(a), then we would get these results for different directionality values:  - FORWARD - all flows with srole=(a),  - REVERSE - all flows with drole=(a), and  - BOTH - the union of forward and reverse.  # noqa: E501

        :param directionality: The directionality of this GrpcTimeSeriesRequest.  # noqa: E501
        :type: GrpcDirectionality
        """

        self._directionality = directionality

    @property
    def locality(self):
        """Gets the locality of this GrpcTimeSeriesRequest.  # noqa: E501

        No longer supported. Returns an unimplemented error if defined.  # noqa: E501

        :return: The locality of this GrpcTimeSeriesRequest.  # noqa: E501
        :rtype: GrpcLocality
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """Sets the locality of this GrpcTimeSeriesRequest.

        No longer supported. Returns an unimplemented error if defined.  # noqa: E501

        :param locality: The locality of this GrpcTimeSeriesRequest.  # noqa: E501
        :type: GrpcLocality
        """

        self._locality = locality

    @property
    def top_k(self):
        """Gets the top_k of this GrpcTimeSeriesRequest.  # noqa: E501

        Maximum number of time series to return. The default value is 30. Uses the default value if not set. The hit_limit field in the response is set to true if some time series have been omitted. Returns all time series if set to -1.  # noqa: E501

        :return: The top_k of this GrpcTimeSeriesRequest.  # noqa: E501
        :rtype: int
        """
        return self._top_k

    @top_k.setter
    def top_k(self, top_k):
        """Sets the top_k of this GrpcTimeSeriesRequest.

        Maximum number of time series to return. The default value is 30. Uses the default value if not set. The hit_limit field in the response is set to true if some time series have been omitted. Returns all time series if set to -1.  # noqa: E501

        :param top_k: The top_k of this GrpcTimeSeriesRequest.  # noqa: E501
        :type: int
        """

        self._top_k = top_k

    @property
    def min_total_values_threshold(self):
        """Gets the min_total_values_threshold of this GrpcTimeSeriesRequest.  # noqa: E501

        No longer supported. Returns an unimplemented error if defined.  # noqa: E501

        :return: The min_total_values_threshold of this GrpcTimeSeriesRequest.  # noqa: E501
        :rtype: float
        """
        return self._min_total_values_threshold

    @min_total_values_threshold.setter
    def min_total_values_threshold(self, min_total_values_threshold):
        """Sets the min_total_values_threshold of this GrpcTimeSeriesRequest.

        No longer supported. Returns an unimplemented error if defined.  # noqa: E501

        :param min_total_values_threshold: The min_total_values_threshold of this GrpcTimeSeriesRequest.  # noqa: E501
        :type: float
        """

        self._min_total_values_threshold = min_total_values_threshold

    @property
    def no_rollups(self):
        """Gets the no_rollups of this GrpcTimeSeriesRequest.  # noqa: E501

        If true, the service will disable use of rolled-up timeseries in the request. The rollups are currently 30 seconds. I.e., each timeseries is stored as a 30 second aggregate in the timeseries database. Rollups can significantly speed up large queries due to less points needed to cover the interval.  # noqa: E501

        :return: The no_rollups of this GrpcTimeSeriesRequest.  # noqa: E501
        :rtype: bool
        """
        return self._no_rollups

    @no_rollups.setter
    def no_rollups(self, no_rollups):
        """Sets the no_rollups of this GrpcTimeSeriesRequest.

        If true, the service will disable use of rolled-up timeseries in the request. The rollups are currently 30 seconds. I.e., each timeseries is stored as a 30 second aggregate in the timeseries database. Rollups can significantly speed up large queries due to less points needed to cover the interval.  # noqa: E501

        :param no_rollups: The no_rollups of this GrpcTimeSeriesRequest.  # noqa: E501
        :type: bool
        """

        self._no_rollups = no_rollups

    @property
    def label_equality(self):
        """Gets the label_equality of this GrpcTimeSeriesRequest.  # noqa: E501


        :return: The label_equality of this GrpcTimeSeriesRequest.  # noqa: E501
        :rtype: list[GrpcLabelEqualityPair]
        """
        return self._label_equality

    @label_equality.setter
    def label_equality(self, label_equality):
        """Sets the label_equality of this GrpcTimeSeriesRequest.


        :param label_equality: The label_equality of this GrpcTimeSeriesRequest.  # noqa: E501
        :type: list[GrpcLabelEqualityPair]
        """

        self._label_equality = label_equality

    @property
    def aggregation(self):
        """Gets the aggregation of this GrpcTimeSeriesRequest.  # noqa: E501

        What type of aggregation to perform. See comment in GetTimeSeriesRequestV2 for more details.  # noqa: E501

        :return: The aggregation of this GrpcTimeSeriesRequest.  # noqa: E501
        :rtype: GrpcAggregationMethod
        """
        return self._aggregation

    @aggregation.setter
    def aggregation(self, aggregation):
        """Sets the aggregation of this GrpcTimeSeriesRequest.

        What type of aggregation to perform. See comment in GetTimeSeriesRequestV2 for more details.  # noqa: E501

        :param aggregation: The aggregation of this GrpcTimeSeriesRequest.  # noqa: E501
        :type: GrpcAggregationMethod
        """

        self._aggregation = aggregation

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
        if issubclass(GrpcTimeSeriesRequest, dict):
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
        if not isinstance(other, GrpcTimeSeriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
