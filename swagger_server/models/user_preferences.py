# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class UserPreferences(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, theme: str=None, notifications: bool=None):  # noqa: E501
        """UserPreferences - a model defined in Swagger

        :param theme: The theme of this UserPreferences.  # noqa: E501
        :type theme: str
        :param notifications: The notifications of this UserPreferences.  # noqa: E501
        :type notifications: bool
        """
        self.swagger_types = {
            'theme': str,
            'notifications': bool
        }

        self.attribute_map = {
            'theme': 'theme',
            'notifications': 'notifications'
        }
        self._theme = theme
        self._notifications = notifications

    @classmethod
    def from_dict(cls, dikt) -> 'UserPreferences':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User_preferences of this UserPreferences.  # noqa: E501
        :rtype: UserPreferences
        """
        return util.deserialize_model(dikt, cls)

    @property
    def theme(self) -> str:
        """Gets the theme of this UserPreferences.


        :return: The theme of this UserPreferences.
        :rtype: str
        """
        return self._theme

    @theme.setter
    def theme(self, theme: str):
        """Sets the theme of this UserPreferences.


        :param theme: The theme of this UserPreferences.
        :type theme: str
        """

        self._theme = theme

    @property
    def notifications(self) -> bool:
        """Gets the notifications of this UserPreferences.


        :return: The notifications of this UserPreferences.
        :rtype: bool
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications: bool):
        """Sets the notifications of this UserPreferences.


        :param notifications: The notifications of this UserPreferences.
        :type notifications: bool
        """

        self._notifications = notifications
