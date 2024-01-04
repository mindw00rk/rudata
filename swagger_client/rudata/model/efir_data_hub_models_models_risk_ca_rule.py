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

class EfirDataHubModelsModelsRiskCARule(object):
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
        'rule_type': 'int',
        'rule_type_name': 'str',
        'rule': 'str',
        'credit_risk_ratio': 'float',
        'risk_group': 'str',
        'reason': 'str',
        'code': 'str'
    }

    attribute_map = {
        'rule_type': 'ruleType',
        'rule_type_name': 'ruleTypeName',
        'rule': 'rule',
        'credit_risk_ratio': 'creditRiskRatio',
        'risk_group': 'riskGroup',
        'reason': 'reason',
        'code': 'code'
    }

    def __init__(self, rule_type=None, rule_type_name=None, rule=None, credit_risk_ratio=None, risk_group=None, reason=None, code=None):  # noqa: E501
        """EfirDataHubModelsModelsRiskCARule - a model defined in Swagger"""  # noqa: E501
        self._rule_type = None
        self._rule_type_name = None
        self._rule = None
        self._credit_risk_ratio = None
        self._risk_group = None
        self._reason = None
        self._code = None
        self.discriminator = None
        if rule_type is not None:
            self.rule_type = rule_type
        if rule_type_name is not None:
            self.rule_type_name = rule_type_name
        if rule is not None:
            self.rule = rule
        if credit_risk_ratio is not None:
            self.credit_risk_ratio = credit_risk_ratio
        if risk_group is not None:
            self.risk_group = risk_group
        if reason is not None:
            self.reason = reason
        if code is not None:
            self.code = code

    @property
    def rule_type(self):
        """Gets the rule_type of this EfirDataHubModelsModelsRiskCARule.  # noqa: E501

        Тип классификатора. Возможные значения:  0 – гарантированная часть выпуска при фондировании в рублях  1 – негарантированная часть выпуска при фондировании в рублях  2 – гарантированная часть выпуска при фондировании не в рублях  3 – негарантированная часть выпуска при фондировании не в рублях  # noqa: E501

        :return: The rule_type of this EfirDataHubModelsModelsRiskCARule.  # noqa: E501
        :rtype: int
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """Sets the rule_type of this EfirDataHubModelsModelsRiskCARule.

        Тип классификатора. Возможные значения:  0 – гарантированная часть выпуска при фондировании в рублях  1 – негарантированная часть выпуска при фондировании в рублях  2 – гарантированная часть выпуска при фондировании не в рублях  3 – негарантированная часть выпуска при фондировании не в рублях  # noqa: E501

        :param rule_type: The rule_type of this EfirDataHubModelsModelsRiskCARule.  # noqa: E501
        :type: int
        """

        self._rule_type = rule_type

    @property
    def rule_type_name(self):
        """Gets the rule_type_name of this EfirDataHubModelsModelsRiskCARule.  # noqa: E501

        “Расшифровка” значения RuleType в стороку:  0 – “GARANT_RUB”  1 – “NOGARANT_RUB”  2 – “GARANT_NOTRUB”  3 – “NOGARANT_NOTRUB  # noqa: E501

        :return: The rule_type_name of this EfirDataHubModelsModelsRiskCARule.  # noqa: E501
        :rtype: str
        """
        return self._rule_type_name

    @rule_type_name.setter
    def rule_type_name(self, rule_type_name):
        """Sets the rule_type_name of this EfirDataHubModelsModelsRiskCARule.

        “Расшифровка” значения RuleType в стороку:  0 – “GARANT_RUB”  1 – “NOGARANT_RUB”  2 – “GARANT_NOTRUB”  3 – “NOGARANT_NOTRUB  # noqa: E501

        :param rule_type_name: The rule_type_name of this EfirDataHubModelsModelsRiskCARule.  # noqa: E501
        :type: str
        """

        self._rule_type_name = rule_type_name

    @property
    def rule(self):
        """Gets the rule of this EfirDataHubModelsModelsRiskCARule.  # noqa: E501

        Значение классификатора  # noqa: E501

        :return: The rule of this EfirDataHubModelsModelsRiskCARule.  # noqa: E501
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this EfirDataHubModelsModelsRiskCARule.

        Значение классификатора  # noqa: E501

        :param rule: The rule of this EfirDataHubModelsModelsRiskCARule.  # noqa: E501
        :type: str
        """

        self._rule = rule

    @property
    def credit_risk_ratio(self):
        """Gets the credit_risk_ratio of this EfirDataHubModelsModelsRiskCARule.  # noqa: E501

        Коэффициент кредитного риска. Может быть NULL.  # noqa: E501

        :return: The credit_risk_ratio of this EfirDataHubModelsModelsRiskCARule.  # noqa: E501
        :rtype: float
        """
        return self._credit_risk_ratio

    @credit_risk_ratio.setter
    def credit_risk_ratio(self, credit_risk_ratio):
        """Sets the credit_risk_ratio of this EfirDataHubModelsModelsRiskCARule.

        Коэффициент кредитного риска. Может быть NULL.  # noqa: E501

        :param credit_risk_ratio: The credit_risk_ratio of this EfirDataHubModelsModelsRiskCARule.  # noqa: E501
        :type: float
        """

        self._credit_risk_ratio = credit_risk_ratio

    @property
    def risk_group(self):
        """Gets the risk_group of this EfirDataHubModelsModelsRiskCARule.  # noqa: E501

        Группа риска  # noqa: E501

        :return: The risk_group of this EfirDataHubModelsModelsRiskCARule.  # noqa: E501
        :rtype: str
        """
        return self._risk_group

    @risk_group.setter
    def risk_group(self, risk_group):
        """Sets the risk_group of this EfirDataHubModelsModelsRiskCARule.

        Группа риска  # noqa: E501

        :param risk_group: The risk_group of this EfirDataHubModelsModelsRiskCARule.  # noqa: E501
        :type: str
        """

        self._risk_group = risk_group

    @property
    def reason(self):
        """Gets the reason of this EfirDataHubModelsModelsRiskCARule.  # noqa: E501

        Обоснование (ссылка на абзац из инструкции)  # noqa: E501

        :return: The reason of this EfirDataHubModelsModelsRiskCARule.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this EfirDataHubModelsModelsRiskCARule.

        Обоснование (ссылка на абзац из инструкции)  # noqa: E501

        :param reason: The reason of this EfirDataHubModelsModelsRiskCARule.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def code(self):
        """Gets the code of this EfirDataHubModelsModelsRiskCARule.  # noqa: E501

        Код по инструкции  # noqa: E501

        :return: The code of this EfirDataHubModelsModelsRiskCARule.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this EfirDataHubModelsModelsRiskCARule.

        Код по инструкции  # noqa: E501

        :param code: The code of this EfirDataHubModelsModelsRiskCARule.  # noqa: E501
        :type: str
        """

        self._code = code

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
        if issubclass(EfirDataHubModelsModelsRiskCARule, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsRiskCARule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other