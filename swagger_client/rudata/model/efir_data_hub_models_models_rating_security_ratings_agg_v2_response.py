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

class EfirDataHubModelsModelsRatingSecurityRatingsAggV2Response(object):
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
        'agg_type': 'str',
        'dt': 'datetime',
        'instruments': 'list[EfirDataHubModelsModelsRatingAggInstrument]'
    }

    attribute_map = {
        'agg_type': 'agg_type',
        'dt': 'dt',
        'instruments': 'instruments'
    }

    def __init__(self, agg_type=None, dt=None, instruments=None):  # noqa: E501
        """EfirDataHubModelsModelsRatingSecurityRatingsAggV2Response - a model defined in Swagger"""  # noqa: E501
        self._agg_type = None
        self._dt = None
        self._instruments = None
        self.discriminator = None
        if agg_type is not None:
            self.agg_type = agg_type
        if dt is not None:
            self.dt = dt
        if instruments is not None:
            self.instruments = instruments

    @property
    def agg_type(self):
        """Gets the agg_type of this EfirDataHubModelsModelsRatingSecurityRatingsAggV2Response.  # noqa: E501


        :return: The agg_type of this EfirDataHubModelsModelsRatingSecurityRatingsAggV2Response.  # noqa: E501
        :rtype: str
        """
        return self._agg_type

    @agg_type.setter
    def agg_type(self, agg_type):
        """Sets the agg_type of this EfirDataHubModelsModelsRatingSecurityRatingsAggV2Response.


        :param agg_type: The agg_type of this EfirDataHubModelsModelsRatingSecurityRatingsAggV2Response.  # noqa: E501
        :type: str
        """

        self._agg_type = agg_type

    @property
    def dt(self):
        """Gets the dt of this EfirDataHubModelsModelsRatingSecurityRatingsAggV2Response.  # noqa: E501


        :return: The dt of this EfirDataHubModelsModelsRatingSecurityRatingsAggV2Response.  # noqa: E501
        :rtype: datetime
        """
        return self._dt

    @dt.setter
    def dt(self, dt):
        """Sets the dt of this EfirDataHubModelsModelsRatingSecurityRatingsAggV2Response.


        :param dt: The dt of this EfirDataHubModelsModelsRatingSecurityRatingsAggV2Response.  # noqa: E501
        :type: datetime
        """

        self._dt = dt

    @property
    def instruments(self):
        """Gets the instruments of this EfirDataHubModelsModelsRatingSecurityRatingsAggV2Response.  # noqa: E501


        :return: The instruments of this EfirDataHubModelsModelsRatingSecurityRatingsAggV2Response.  # noqa: E501
        :rtype: list[EfirDataHubModelsModelsRatingAggInstrument]
        """
        return self._instruments

    @instruments.setter
    def instruments(self, instruments):
        """Sets the instruments of this EfirDataHubModelsModelsRatingSecurityRatingsAggV2Response.


        :param instruments: The instruments of this EfirDataHubModelsModelsRatingSecurityRatingsAggV2Response.  # noqa: E501
        :type: list[EfirDataHubModelsModelsRatingAggInstrument]
        """

        self._instruments = instruments

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
        if issubclass(EfirDataHubModelsModelsRatingSecurityRatingsAggV2Response, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsRatingSecurityRatingsAggV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
