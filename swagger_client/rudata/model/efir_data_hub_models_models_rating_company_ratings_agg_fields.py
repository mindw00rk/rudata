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

class EfirDataHubModelsModelsRatingCompanyRatingsAggFields(object):
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
        'agg_l5': 'str',
        'agg_n5': 'float',
        'agg_l12': 'str',
        'agg_n12': 'float',
        'agg_l26': 'str',
        'agg_n26': 'float',
        'id_rating': 'float',
        'last_dt': 'datetime',
        'last': 'str',
        'code': 'str',
        'code_type': 'str',
        'company_name': 'str',
        'agg_n10': 'float',
        'agg_l10': 'str'
    }

    attribute_map = {
        'agg_type': 'agg_type',
        'dt': 'dt',
        'agg_l5': 'agg_l5',
        'agg_n5': 'agg_n5',
        'agg_l12': 'agg_l12',
        'agg_n12': 'agg_n12',
        'agg_l26': 'agg_l26',
        'agg_n26': 'agg_n26',
        'id_rating': 'id_rating',
        'last_dt': 'last_dt',
        'last': 'last',
        'code': 'code',
        'code_type': 'code_type',
        'company_name': 'company_name',
        'agg_n10': 'agg_n10',
        'agg_l10': 'agg_l10'
    }

    def __init__(self, agg_type=None, dt=None, agg_l5=None, agg_n5=None, agg_l12=None, agg_n12=None, agg_l26=None, agg_n26=None, id_rating=None, last_dt=None, last=None, code=None, code_type=None, company_name=None, agg_n10=None, agg_l10=None):  # noqa: E501
        """EfirDataHubModelsModelsRatingCompanyRatingsAggFields - a model defined in Swagger"""  # noqa: E501
        self._agg_type = None
        self._dt = None
        self._agg_l5 = None
        self._agg_n5 = None
        self._agg_l12 = None
        self._agg_n12 = None
        self._agg_l26 = None
        self._agg_n26 = None
        self._id_rating = None
        self._last_dt = None
        self._last = None
        self._code = None
        self._code_type = None
        self._company_name = None
        self._agg_n10 = None
        self._agg_l10 = None
        self.discriminator = None
        if agg_type is not None:
            self.agg_type = agg_type
        if dt is not None:
            self.dt = dt
        if agg_l5 is not None:
            self.agg_l5 = agg_l5
        if agg_n5 is not None:
            self.agg_n5 = agg_n5
        if agg_l12 is not None:
            self.agg_l12 = agg_l12
        if agg_n12 is not None:
            self.agg_n12 = agg_n12
        if agg_l26 is not None:
            self.agg_l26 = agg_l26
        if agg_n26 is not None:
            self.agg_n26 = agg_n26
        if id_rating is not None:
            self.id_rating = id_rating
        if last_dt is not None:
            self.last_dt = last_dt
        if last is not None:
            self.last = last
        if code is not None:
            self.code = code
        if code_type is not None:
            self.code_type = code_type
        if company_name is not None:
            self.company_name = company_name
        if agg_n10 is not None:
            self.agg_n10 = agg_n10
        if agg_l10 is not None:
            self.agg_l10 = agg_l10

    @property
    def agg_type(self):
        """Gets the agg_type of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501


        :return: The agg_type of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :rtype: str
        """
        return self._agg_type

    @agg_type.setter
    def agg_type(self, agg_type):
        """Sets the agg_type of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.


        :param agg_type: The agg_type of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :type: str
        """

        self._agg_type = agg_type

    @property
    def dt(self):
        """Gets the dt of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501


        :return: The dt of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :rtype: datetime
        """
        return self._dt

    @dt.setter
    def dt(self, dt):
        """Sets the dt of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.


        :param dt: The dt of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :type: datetime
        """

        self._dt = dt

    @property
    def agg_l5(self):
        """Gets the agg_l5 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501


        :return: The agg_l5 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :rtype: str
        """
        return self._agg_l5

    @agg_l5.setter
    def agg_l5(self, agg_l5):
        """Sets the agg_l5 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.


        :param agg_l5: The agg_l5 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :type: str
        """

        self._agg_l5 = agg_l5

    @property
    def agg_n5(self):
        """Gets the agg_n5 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501


        :return: The agg_n5 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :rtype: float
        """
        return self._agg_n5

    @agg_n5.setter
    def agg_n5(self, agg_n5):
        """Sets the agg_n5 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.


        :param agg_n5: The agg_n5 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :type: float
        """

        self._agg_n5 = agg_n5

    @property
    def agg_l12(self):
        """Gets the agg_l12 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501


        :return: The agg_l12 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :rtype: str
        """
        return self._agg_l12

    @agg_l12.setter
    def agg_l12(self, agg_l12):
        """Sets the agg_l12 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.


        :param agg_l12: The agg_l12 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :type: str
        """

        self._agg_l12 = agg_l12

    @property
    def agg_n12(self):
        """Gets the agg_n12 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501


        :return: The agg_n12 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :rtype: float
        """
        return self._agg_n12

    @agg_n12.setter
    def agg_n12(self, agg_n12):
        """Sets the agg_n12 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.


        :param agg_n12: The agg_n12 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :type: float
        """

        self._agg_n12 = agg_n12

    @property
    def agg_l26(self):
        """Gets the agg_l26 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501


        :return: The agg_l26 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :rtype: str
        """
        return self._agg_l26

    @agg_l26.setter
    def agg_l26(self, agg_l26):
        """Sets the agg_l26 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.


        :param agg_l26: The agg_l26 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :type: str
        """

        self._agg_l26 = agg_l26

    @property
    def agg_n26(self):
        """Gets the agg_n26 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501


        :return: The agg_n26 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :rtype: float
        """
        return self._agg_n26

    @agg_n26.setter
    def agg_n26(self, agg_n26):
        """Sets the agg_n26 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.


        :param agg_n26: The agg_n26 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :type: float
        """

        self._agg_n26 = agg_n26

    @property
    def id_rating(self):
        """Gets the id_rating of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501


        :return: The id_rating of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :rtype: float
        """
        return self._id_rating

    @id_rating.setter
    def id_rating(self, id_rating):
        """Sets the id_rating of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.


        :param id_rating: The id_rating of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :type: float
        """

        self._id_rating = id_rating

    @property
    def last_dt(self):
        """Gets the last_dt of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501


        :return: The last_dt of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :rtype: datetime
        """
        return self._last_dt

    @last_dt.setter
    def last_dt(self, last_dt):
        """Sets the last_dt of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.


        :param last_dt: The last_dt of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :type: datetime
        """

        self._last_dt = last_dt

    @property
    def last(self):
        """Gets the last of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501


        :return: The last of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :rtype: str
        """
        return self._last

    @last.setter
    def last(self, last):
        """Sets the last of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.


        :param last: The last of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :type: str
        """

        self._last = last

    @property
    def code(self):
        """Gets the code of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501


        :return: The code of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.


        :param code: The code of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def code_type(self):
        """Gets the code_type of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501


        :return: The code_type of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :rtype: str
        """
        return self._code_type

    @code_type.setter
    def code_type(self, code_type):
        """Sets the code_type of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.


        :param code_type: The code_type of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :type: str
        """

        self._code_type = code_type

    @property
    def company_name(self):
        """Gets the company_name of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501


        :return: The company_name of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.


        :param company_name: The company_name of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def agg_n10(self):
        """Gets the agg_n10 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501


        :return: The agg_n10 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :rtype: float
        """
        return self._agg_n10

    @agg_n10.setter
    def agg_n10(self, agg_n10):
        """Sets the agg_n10 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.


        :param agg_n10: The agg_n10 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :type: float
        """

        self._agg_n10 = agg_n10

    @property
    def agg_l10(self):
        """Gets the agg_l10 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501


        :return: The agg_l10 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :rtype: str
        """
        return self._agg_l10

    @agg_l10.setter
    def agg_l10(self, agg_l10):
        """Sets the agg_l10 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.


        :param agg_l10: The agg_l10 of this EfirDataHubModelsModelsRatingCompanyRatingsAggFields.  # noqa: E501
        :type: str
        """

        self._agg_l10 = agg_l10

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
        if issubclass(EfirDataHubModelsModelsRatingCompanyRatingsAggFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsRatingCompanyRatingsAggFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
