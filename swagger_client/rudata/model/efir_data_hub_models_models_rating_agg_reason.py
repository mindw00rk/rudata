# coding: utf-8

"""
    API Reference United Data (RU DATA) v2.0

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: DataHub: v2, Models: 1.23.21.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EfirDataHubModelsModelsRatingAggReason(object):
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
        'id_rating': 'int',
        'last_dt': 'datetime',
        'last': 'str'
    }

    attribute_map = {
        'id_rating': 'id_rating',
        'last_dt': 'last_dt',
        'last': 'last'
    }

    def __init__(self, id_rating=None, last_dt=None, last=None):  # noqa: E501
        """EfirDataHubModelsModelsRatingAggReason - a model defined in Swagger"""  # noqa: E501
        self._id_rating = None
        self._last_dt = None
        self._last = None
        self.discriminator = None
        if id_rating is not None:
            self.id_rating = id_rating
        if last_dt is not None:
            self.last_dt = last_dt
        if last is not None:
            self.last = last

    @property
    def id_rating(self):
        """Gets the id_rating of this EfirDataHubModelsModelsRatingAggReason.  # noqa: E501


        :return: The id_rating of this EfirDataHubModelsModelsRatingAggReason.  # noqa: E501
        :rtype: int
        """
        return self._id_rating

    @id_rating.setter
    def id_rating(self, id_rating):
        """Sets the id_rating of this EfirDataHubModelsModelsRatingAggReason.


        :param id_rating: The id_rating of this EfirDataHubModelsModelsRatingAggReason.  # noqa: E501
        :type: int
        """

        self._id_rating = id_rating

    @property
    def last_dt(self):
        """Gets the last_dt of this EfirDataHubModelsModelsRatingAggReason.  # noqa: E501


        :return: The last_dt of this EfirDataHubModelsModelsRatingAggReason.  # noqa: E501
        :rtype: datetime
        """
        return self._last_dt

    @last_dt.setter
    def last_dt(self, last_dt):
        """Sets the last_dt of this EfirDataHubModelsModelsRatingAggReason.


        :param last_dt: The last_dt of this EfirDataHubModelsModelsRatingAggReason.  # noqa: E501
        :type: datetime
        """

        self._last_dt = last_dt

    @property
    def last(self):
        """Gets the last of this EfirDataHubModelsModelsRatingAggReason.  # noqa: E501


        :return: The last of this EfirDataHubModelsModelsRatingAggReason.  # noqa: E501
        :rtype: str
        """
        return self._last

    @last.setter
    def last(self, last):
        """Sets the last of this EfirDataHubModelsModelsRatingAggReason.


        :param last: The last of this EfirDataHubModelsModelsRatingAggReason.  # noqa: E501
        :type: str
        """

        self._last = last

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
        if issubclass(EfirDataHubModelsModelsRatingAggReason, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsRatingAggReason):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
