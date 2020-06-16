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


class GetAgentInfoResponseAgentInstance(object):
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
        'instance_ip': 'str',
        'version': 'str',
        'type': 'str'
    }

    attribute_map = {
        'instance_ip': 'instanceIp',
        'version': 'version',
        'type': 'type'
    }

    def __init__(self, instance_ip=None, version=None, type=None):  # noqa: E501
        """GetAgentInfoResponseAgentInstance - a model defined in Swagger"""  # noqa: E501

        self._instance_ip = None
        self._version = None
        self._type = None
        self.discriminator = None

        if instance_ip is not None:
            self.instance_ip = instance_ip
        if version is not None:
            self.version = version
        if type is not None:
            self.type = type

    @property
    def instance_ip(self):
        """Gets the instance_ip of this GetAgentInfoResponseAgentInstance.  # noqa: E501


        :return: The instance_ip of this GetAgentInfoResponseAgentInstance.  # noqa: E501
        :rtype: str
        """
        return self._instance_ip

    @instance_ip.setter
    def instance_ip(self, instance_ip):
        """Sets the instance_ip of this GetAgentInfoResponseAgentInstance.


        :param instance_ip: The instance_ip of this GetAgentInfoResponseAgentInstance.  # noqa: E501
        :type: str
        """

        self._instance_ip = instance_ip

    @property
    def version(self):
        """Gets the version of this GetAgentInfoResponseAgentInstance.  # noqa: E501


        :return: The version of this GetAgentInfoResponseAgentInstance.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this GetAgentInfoResponseAgentInstance.


        :param version: The version of this GetAgentInfoResponseAgentInstance.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def type(self):
        """Gets the type of this GetAgentInfoResponseAgentInstance.  # noqa: E501

        type of agent. Possible values include kernel, k8s, or aws.  # noqa: E501

        :return: The type of this GetAgentInfoResponseAgentInstance.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetAgentInfoResponseAgentInstance.

        type of agent. Possible values include kernel, k8s, or aws.  # noqa: E501

        :param type: The type of this GetAgentInfoResponseAgentInstance.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(GetAgentInfoResponseAgentInstance, dict):
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
        if not isinstance(other, GetAgentInfoResponseAgentInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
