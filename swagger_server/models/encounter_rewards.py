# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class EncounterRewards(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, experience_points: int=None, items: List[str]=None):  # noqa: E501
        """EncounterRewards - a model defined in Swagger

        :param experience_points: The experience_points of this EncounterRewards.  # noqa: E501
        :type experience_points: int
        :param items: The items of this EncounterRewards.  # noqa: E501
        :type items: List[str]
        """
        self.swagger_types = {
            'experience_points': int,
            'items': List[str]
        }

        self.attribute_map = {
            'experience_points': 'experiencePoints',
            'items': 'items'
        }
        self._experience_points = experience_points
        self._items = items

    @classmethod
    def from_dict(cls, dikt) -> 'EncounterRewards':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Encounter_rewards of this EncounterRewards.  # noqa: E501
        :rtype: EncounterRewards
        """
        return util.deserialize_model(dikt, cls)

    @property
    def experience_points(self) -> int:
        """Gets the experience_points of this EncounterRewards.


        :return: The experience_points of this EncounterRewards.
        :rtype: int
        """
        return self._experience_points

    @experience_points.setter
    def experience_points(self, experience_points: int):
        """Sets the experience_points of this EncounterRewards.


        :param experience_points: The experience_points of this EncounterRewards.
        :type experience_points: int
        """

        self._experience_points = experience_points

    @property
    def items(self) -> List[str]:
        """Gets the items of this EncounterRewards.


        :return: The items of this EncounterRewards.
        :rtype: List[str]
        """
        return self._items

    @items.setter
    def items(self, items: List[str]):
        """Sets the items of this EncounterRewards.


        :param items: The items of this EncounterRewards.
        :type items: List[str]
        """

        self._items = items
