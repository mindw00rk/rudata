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

class EfirDataHubModelsRequestsV2InfoMoneyFlowRequestForecast(object):
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
        'coupon_forecast': 'float',
        'coupon_id': 'int',
        'coupon_date': 'datetime'
    }

    attribute_map = {
        'coupon_forecast': 'couponForecast',
        'coupon_id': 'couponId',
        'coupon_date': 'couponDate'
    }

    def __init__(self, coupon_forecast=None, coupon_id=None, coupon_date=None):  # noqa: E501
        """EfirDataHubModelsRequestsV2InfoMoneyFlowRequestForecast - a model defined in Swagger"""  # noqa: E501
        self._coupon_forecast = None
        self._coupon_id = None
        self._coupon_date = None
        self.discriminator = None
        if coupon_forecast is not None:
            self.coupon_forecast = coupon_forecast
        if coupon_id is not None:
            self.coupon_id = coupon_id
        if coupon_date is not None:
            self.coupon_date = coupon_date

    @property
    def coupon_forecast(self):
        """Gets the coupon_forecast of this EfirDataHubModelsRequestsV2InfoMoneyFlowRequestForecast.  # noqa: E501

        Значение доходности для купона  # noqa: E501

        :return: The coupon_forecast of this EfirDataHubModelsRequestsV2InfoMoneyFlowRequestForecast.  # noqa: E501
        :rtype: float
        """
        return self._coupon_forecast

    @coupon_forecast.setter
    def coupon_forecast(self, coupon_forecast):
        """Sets the coupon_forecast of this EfirDataHubModelsRequestsV2InfoMoneyFlowRequestForecast.

        Значение доходности для купона  # noqa: E501

        :param coupon_forecast: The coupon_forecast of this EfirDataHubModelsRequestsV2InfoMoneyFlowRequestForecast.  # noqa: E501
        :type: float
        """

        self._coupon_forecast = coupon_forecast

    @property
    def coupon_id(self):
        """Gets the coupon_id of this EfirDataHubModelsRequestsV2InfoMoneyFlowRequestForecast.  # noqa: E501

        Порядкоовый номер купона, если не задается поле CouponDate  # noqa: E501

        :return: The coupon_id of this EfirDataHubModelsRequestsV2InfoMoneyFlowRequestForecast.  # noqa: E501
        :rtype: int
        """
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, coupon_id):
        """Sets the coupon_id of this EfirDataHubModelsRequestsV2InfoMoneyFlowRequestForecast.

        Порядкоовый номер купона, если не задается поле CouponDate  # noqa: E501

        :param coupon_id: The coupon_id of this EfirDataHubModelsRequestsV2InfoMoneyFlowRequestForecast.  # noqa: E501
        :type: int
        """

        self._coupon_id = coupon_id

    @property
    def coupon_date(self):
        """Gets the coupon_date of this EfirDataHubModelsRequestsV2InfoMoneyFlowRequestForecast.  # noqa: E501

        Даты купона  # noqa: E501

        :return: The coupon_date of this EfirDataHubModelsRequestsV2InfoMoneyFlowRequestForecast.  # noqa: E501
        :rtype: datetime
        """
        return self._coupon_date

    @coupon_date.setter
    def coupon_date(self, coupon_date):
        """Sets the coupon_date of this EfirDataHubModelsRequestsV2InfoMoneyFlowRequestForecast.

        Даты купона  # noqa: E501

        :param coupon_date: The coupon_date of this EfirDataHubModelsRequestsV2InfoMoneyFlowRequestForecast.  # noqa: E501
        :type: datetime
        """

        self._coupon_date = coupon_date

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
        if issubclass(EfirDataHubModelsRequestsV2InfoMoneyFlowRequestForecast, dict):
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
        if not isinstance(other, EfirDataHubModelsRequestsV2InfoMoneyFlowRequestForecast):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other