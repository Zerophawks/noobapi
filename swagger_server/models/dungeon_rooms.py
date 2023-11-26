# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DungeonRooms(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, room_name: str=None, description: str=None, monsters: List[str]=None, items: List[str]=None, traps: str=None, treasure: str=None):  # noqa: E501
        """DungeonRooms - a model defined in Swagger

        :param room_name: The room_name of this DungeonRooms.  # noqa: E501
        :type room_name: str
        :param description: The description of this DungeonRooms.  # noqa: E501
        :type description: str
        :param monsters: The monsters of this DungeonRooms.  # noqa: E501
        :type monsters: List[str]
        :param items: The items of this DungeonRooms.  # noqa: E501
        :type items: List[str]
        :param traps: The traps of this DungeonRooms.  # noqa: E501
        :type traps: str
        :param treasure: The treasure of this DungeonRooms.  # noqa: E501
        :type treasure: str
        """
        self.swagger_types = {
            'room_name': str,
            'description': str,
            'monsters': List[str],
            'items': List[str],
            'traps': str,
            'treasure': str
        }

        self.attribute_map = {
            'room_name': 'roomName',
            'description': 'description',
            'monsters': 'monsters',
            'items': 'items',
            'traps': 'traps',
            'treasure': 'treasure'
        }
        self._room_name = room_name
        self._description = description
        self._monsters = monsters
        self._items = items
        self._traps = traps
        self._treasure = treasure

    @classmethod
    def from_dict(cls, dikt) -> 'DungeonRooms':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Dungeon_rooms of this DungeonRooms.  # noqa: E501
        :rtype: DungeonRooms
        """
        return util.deserialize_model(dikt, cls)

    @property
    def room_name(self) -> str:
        """Gets the room_name of this DungeonRooms.


        :return: The room_name of this DungeonRooms.
        :rtype: str
        """
        return self._room_name

    @room_name.setter
    def room_name(self, room_name: str):
        """Sets the room_name of this DungeonRooms.


        :param room_name: The room_name of this DungeonRooms.
        :type room_name: str
        """

        self._room_name = room_name

    @property
    def description(self) -> str:
        """Gets the description of this DungeonRooms.


        :return: The description of this DungeonRooms.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this DungeonRooms.


        :param description: The description of this DungeonRooms.
        :type description: str
        """

        self._description = description

    @property
    def monsters(self) -> List[str]:
        """Gets the monsters of this DungeonRooms.


        :return: The monsters of this DungeonRooms.
        :rtype: List[str]
        """
        return self._monsters

    @monsters.setter
    def monsters(self, monsters: List[str]):
        """Sets the monsters of this DungeonRooms.


        :param monsters: The monsters of this DungeonRooms.
        :type monsters: List[str]
        """

        self._monsters = monsters

    @property
    def items(self) -> List[str]:
        """Gets the items of this DungeonRooms.


        :return: The items of this DungeonRooms.
        :rtype: List[str]
        """
        return self._items

    @items.setter
    def items(self, items: List[str]):
        """Sets the items of this DungeonRooms.


        :param items: The items of this DungeonRooms.
        :type items: List[str]
        """

        self._items = items

    @property
    def traps(self) -> str:
        """Gets the traps of this DungeonRooms.


        :return: The traps of this DungeonRooms.
        :rtype: str
        """
        return self._traps

    @traps.setter
    def traps(self, traps: str):
        """Sets the traps of this DungeonRooms.


        :param traps: The traps of this DungeonRooms.
        :type traps: str
        """

        self._traps = traps

    @property
    def treasure(self) -> str:
        """Gets the treasure of this DungeonRooms.


        :return: The treasure of this DungeonRooms.
        :rtype: str
        """
        return self._treasure

    @treasure.setter
    def treasure(self, treasure: str):
        """Sets the treasure of this DungeonRooms.


        :param treasure: The treasure of this DungeonRooms.
        :type treasure: str
        """

        self._treasure = treasure
