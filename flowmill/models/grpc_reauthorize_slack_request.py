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


class GrpcReauthorizeSlackRequest(object):
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
        'id': 'int',
        'code': 'str',
        'redirect_uri': 'str'
    }

    attribute_map = {
        'id': 'id',
        'code': 'code',
        'redirect_uri': 'redirectUri'
    }

    def __init__(self, id=None, code=None, redirect_uri=None):  # noqa: E501
        """GrpcReauthorizeSlackRequest - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._code = None
        self._redirect_uri = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if code is not None:
            self.code = code
        if redirect_uri is not None:
            self.redirect_uri = redirect_uri

    @property
    def id(self):
        """Gets the id of this GrpcReauthorizeSlackRequest.  # noqa: E501


        :return: The id of this GrpcReauthorizeSlackRequest.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GrpcReauthorizeSlackRequest.


        :param id: The id of this GrpcReauthorizeSlackRequest.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def code(self):
        """Gets the code of this GrpcReauthorizeSlackRequest.  # noqa: E501


        :return: The code of this GrpcReauthorizeSlackRequest.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this GrpcReauthorizeSlackRequest.


        :param code: The code of this GrpcReauthorizeSlackRequest.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def redirect_uri(self):
        """Gets the redirect_uri of this GrpcReauthorizeSlackRequest.  # noqa: E501


        :return: The redirect_uri of this GrpcReauthorizeSlackRequest.  # noqa: E501
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        """Sets the redirect_uri of this GrpcReauthorizeSlackRequest.


        :param redirect_uri: The redirect_uri of this GrpcReauthorizeSlackRequest.  # noqa: E501
        :type: str
        """

        self._redirect_uri = redirect_uri

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
        if issubclass(GrpcReauthorizeSlackRequest, dict):
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
        if not isinstance(other, GrpcReauthorizeSlackRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
