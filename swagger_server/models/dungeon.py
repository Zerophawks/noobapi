# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.dungeon_rooms import DungeonRooms  # noqa: F401,E501
from swagger_server import util


class Dungeon(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, dungeon_name: str=None, description: str=None, location: str=None, maps: List[str]=None, rooms: List[DungeonRooms]=None, history: str=None, challenges: List[str]=None, notes: str=None):  # noqa: E501
        """Dungeon - a model defined in Swagger

        :param dungeon_name: The dungeon_name of this Dungeon.  # noqa: E501
        :type dungeon_name: str
        :param description: The description of this Dungeon.  # noqa: E501
        :type description: str
        :param location: The location of this Dungeon.  # noqa: E501
        :type location: str
        :param maps: The maps of this Dungeon.  # noqa: E501
        :type maps: List[str]
        :param rooms: The rooms of this Dungeon.  # noqa: E501
        :type rooms: List[DungeonRooms]
        :param history: The history of this Dungeon.  # noqa: E501
        :type history: str
        :param challenges: The challenges of this Dungeon.  # noqa: E501
        :type challenges: List[str]
        :param notes: The notes of this Dungeon.  # noqa: E501
        :type notes: str
        """
        self.swagger_types = {
            'dungeon_name': str,
            'description': str,
            'location': str,
            'maps': List[str],
            'rooms': List[DungeonRooms],
            'history': str,
            'challenges': List[str],
            'notes': str
        }

        self.attribute_map = {
            'dungeon_name': 'dungeonName',
            'description': 'description',
            'location': 'location',
            'maps': 'maps',
            'rooms': 'rooms',
            'history': 'history',
            'challenges': 'challenges',
            'notes': 'notes'
        }
        self._dungeon_name = dungeon_name
        self._description = description
        self._location = location
        self._maps = maps
        self._rooms = rooms
        self._history = history
        self._challenges = challenges
        self._notes = notes

    @classmethod
    def from_dict(cls, dikt) -> 'Dungeon':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Dungeon of this Dungeon.  # noqa: E501
        :rtype: Dungeon
        """
        return util.deserialize_model(dikt, cls)

    @property
    def dungeon_name(self) -> str:
        """Gets the dungeon_name of this Dungeon.


        :return: The dungeon_name of this Dungeon.
        :rtype: str
        """
        return self._dungeon_name

    @dungeon_name.setter
    def dungeon_name(self, dungeon_name: str):
        """Sets the dungeon_name of this Dungeon.


        :param dungeon_name: The dungeon_name of this Dungeon.
        :type dungeon_name: str
        """
        if dungeon_name is None:
            raise ValueError("Invalid value for `dungeon_name`, must not be `None`")  # noqa: E501

        self._dungeon_name = dungeon_name

    @property
    def description(self) -> str:
        """Gets the description of this Dungeon.


        :return: The description of this Dungeon.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Dungeon.


        :param description: The description of this Dungeon.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def location(self) -> str:
        """Gets the location of this Dungeon.


        :return: The location of this Dungeon.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location: str):
        """Sets the location of this Dungeon.


        :param location: The location of this Dungeon.
        :type location: str
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def maps(self) -> List[str]:
        """Gets the maps of this Dungeon.


        :return: The maps of this Dungeon.
        :rtype: List[str]
        """
        return self._maps

    @maps.setter
    def maps(self, maps: List[str]):
        """Sets the maps of this Dungeon.


        :param maps: The maps of this Dungeon.
        :type maps: List[str]
        """

        self._maps = maps

    @property
    def rooms(self) -> List[DungeonRooms]:
        """Gets the rooms of this Dungeon.


        :return: The rooms of this Dungeon.
        :rtype: List[DungeonRooms]
        """
        return self._rooms

    @rooms.setter
    def rooms(self, rooms: List[DungeonRooms]):
        """Sets the rooms of this Dungeon.


        :param rooms: The rooms of this Dungeon.
        :type rooms: List[DungeonRooms]
        """
        if rooms is None:
            raise ValueError("Invalid value for `rooms`, must not be `None`")  # noqa: E501

        self._rooms = rooms

    @property
    def history(self) -> str:
        """Gets the history of this Dungeon.


        :return: The history of this Dungeon.
        :rtype: str
        """
        return self._history

    @history.setter
    def history(self, history: str):
        """Sets the history of this Dungeon.


        :param history: The history of this Dungeon.
        :type history: str
        """

        self._history = history

    @property
    def challenges(self) -> List[str]:
        """Gets the challenges of this Dungeon.


        :return: The challenges of this Dungeon.
        :rtype: List[str]
        """
        return self._challenges

    @challenges.setter
    def challenges(self, challenges: List[str]):
        """Sets the challenges of this Dungeon.


        :param challenges: The challenges of this Dungeon.
        :type challenges: List[str]
        """

        self._challenges = challenges

    @property
    def notes(self) -> str:
        """Gets the notes of this Dungeon.


        :return: The notes of this Dungeon.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes: str):
        """Sets the notes of this Dungeon.


        :param notes: The notes of this Dungeon.
        :type notes: str
        """

        self._notes = notes