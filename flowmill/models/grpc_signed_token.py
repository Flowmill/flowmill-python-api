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


class GrpcSignedToken(object):
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
        'token': 'str',
        'issued_at_s': 'str',
        'expiration_s': 'str'
    }

    attribute_map = {
        'token': 'token',
        'issued_at_s': 'issuedAtS',
        'expiration_s': 'expirationS'
    }

    def __init__(self, token=None, issued_at_s=None, expiration_s=None):  # noqa: E501
        """GrpcSignedToken - a model defined in Swagger"""  # noqa: E501

        self._token = None
        self._issued_at_s = None
        self._expiration_s = None
        self.discriminator = None

        if token is not None:
            self.token = token
        if issued_at_s is not None:
            self.issued_at_s = issued_at_s
        if expiration_s is not None:
            self.expiration_s = expiration_s

    @property
    def token(self):
        """Gets the token of this GrpcSignedToken.  # noqa: E501


        :return: The token of this GrpcSignedToken.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GrpcSignedToken.


        :param token: The token of this GrpcSignedToken.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def issued_at_s(self):
        """Gets the issued_at_s of this GrpcSignedToken.  # noqa: E501


        :return: The issued_at_s of this GrpcSignedToken.  # noqa: E501
        :rtype: str
        """
        return self._issued_at_s

    @issued_at_s.setter
    def issued_at_s(self, issued_at_s):
        """Sets the issued_at_s of this GrpcSignedToken.


        :param issued_at_s: The issued_at_s of this GrpcSignedToken.  # noqa: E501
        :type: str
        """

        self._issued_at_s = issued_at_s

    @property
    def expiration_s(self):
        """Gets the expiration_s of this GrpcSignedToken.  # noqa: E501


        :return: The expiration_s of this GrpcSignedToken.  # noqa: E501
        :rtype: str
        """
        return self._expiration_s

    @expiration_s.setter
    def expiration_s(self, expiration_s):
        """Sets the expiration_s of this GrpcSignedToken.


        :param expiration_s: The expiration_s of this GrpcSignedToken.  # noqa: E501
        :type: str
        """

        self._expiration_s = expiration_s

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
        if issubclass(GrpcSignedToken, dict):
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
        if not isinstance(other, GrpcSignedToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
