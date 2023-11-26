# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ItemEffects(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, effect_name: str=None, effect_description: str=None):  # noqa: E501
        """ItemEffects - a model defined in Swagger

        :param effect_name: The effect_name of this ItemEffects.  # noqa: E501
        :type effect_name: str
        :param effect_description: The effect_description of this ItemEffects.  # noqa: E501
        :type effect_description: str
        """
        self.swagger_types = {
            'effect_name': str,
            'effect_description': str
        }

        self.attribute_map = {
            'effect_name': 'effectName',
            'effect_description': 'effectDescription'
        }
        self._effect_name = effect_name
        self._effect_description = effect_description

    @classmethod
    def from_dict(cls, dikt) -> 'ItemEffects':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Item_effects of this ItemEffects.  # noqa: E501
        :rtype: ItemEffects
        """
        return util.deserialize_model(dikt, cls)

    @property
    def effect_name(self) -> str:
        """Gets the effect_name of this ItemEffects.


        :return: The effect_name of this ItemEffects.
        :rtype: str
        """
        return self._effect_name

    @effect_name.setter
    def effect_name(self, effect_name: str):
        """Sets the effect_name of this ItemEffects.


        :param effect_name: The effect_name of this ItemEffects.
        :type effect_name: str
        """

        self._effect_name = effect_name

    @property
    def effect_description(self) -> str:
        """Gets the effect_description of this ItemEffects.


        :return: The effect_description of this ItemEffects.
        :rtype: str
        """
        return self._effect_description

    @effect_description.setter
    def effect_description(self, effect_description: str):
        """Sets the effect_description of this ItemEffects.


        :param effect_description: The effect_description of this ItemEffects.
        :type effect_description: str
        """

        self._effect_description = effect_description