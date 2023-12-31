# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CharacterHitPoints(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, maximum: int=None, current: int=None, temporary: int=None):  # noqa: E501
        """CharacterHitPoints - a model defined in Swagger

        :param maximum: The maximum of this CharacterHitPoints.  # noqa: E501
        :type maximum: int
        :param current: The current of this CharacterHitPoints.  # noqa: E501
        :type current: int
        :param temporary: The temporary of this CharacterHitPoints.  # noqa: E501
        :type temporary: int
        """
        self.swagger_types = {
            'maximum': int,
            'current': int,
            'temporary': int
        }

        self.attribute_map = {
            'maximum': 'maximum',
            'current': 'current',
            'temporary': 'temporary'
        }
        self._maximum = maximum
        self._current = current
        self._temporary = temporary

    @classmethod
    def from_dict(cls, dikt) -> 'CharacterHitPoints':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Character_hitPoints of this CharacterHitPoints.  # noqa: E501
        :rtype: CharacterHitPoints
        """
        return util.deserialize_model(dikt, cls)

    @property
    def maximum(self) -> int:
        """Gets the maximum of this CharacterHitPoints.


        :return: The maximum of this CharacterHitPoints.
        :rtype: int
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum: int):
        """Sets the maximum of this CharacterHitPoints.


        :param maximum: The maximum of this CharacterHitPoints.
        :type maximum: int
        """

        self._maximum = maximum

    @property
    def current(self) -> int:
        """Gets the current of this CharacterHitPoints.


        :return: The current of this CharacterHitPoints.
        :rtype: int
        """
        return self._current

    @current.setter
    def current(self, current: int):
        """Sets the current of this CharacterHitPoints.


        :param current: The current of this CharacterHitPoints.
        :type current: int
        """

        self._current = current

    @property
    def temporary(self) -> int:
        """Gets the temporary of this CharacterHitPoints.


        :return: The temporary of this CharacterHitPoints.
        :rtype: int
        """
        return self._temporary

    @temporary.setter
    def temporary(self, temporary: int):
        """Sets the temporary of this CharacterHitPoints.


        :param temporary: The temporary of this CharacterHitPoints.
        :type temporary: int
        """

        self._temporary = temporary
