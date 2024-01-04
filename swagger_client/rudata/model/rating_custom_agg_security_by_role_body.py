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
from swagger_client.rudata.model.efir_data_hub_models_requests_v2_rating_rating_agg_security_by_role_request import EfirDataHubModelsRequestsV2RatingRatingAggSecurityByRoleRequest  # noqa: F401,E501

class RatingCustomAggSecurityByRoleBody(EfirDataHubModelsRequestsV2RatingRatingAggSecurityByRoleRequest):
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
    }
    if hasattr(EfirDataHubModelsRequestsV2RatingRatingAggSecurityByRoleRequest, "swagger_types"):
        swagger_types.update(EfirDataHubModelsRequestsV2RatingRatingAggSecurityByRoleRequest.swagger_types)

    attribute_map = {
    }
    if hasattr(EfirDataHubModelsRequestsV2RatingRatingAggSecurityByRoleRequest, "attribute_map"):
        attribute_map.update(EfirDataHubModelsRequestsV2RatingRatingAggSecurityByRoleRequest.attribute_map)

    def __init__(self, *args, **kwargs):  # noqa: E501
        """RatingCustomAggSecurityByRoleBody - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None
        EfirDataHubModelsRequestsV2RatingRatingAggSecurityByRoleRequest.__init__(self, *args, **kwargs)

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
        if issubclass(RatingCustomAggSecurityByRoleBody, dict):
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
        if not isinstance(other, RatingCustomAggSecurityByRoleBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
