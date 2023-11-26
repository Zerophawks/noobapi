# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Campaign(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, campaign_name: str=None, description: str=None, dungeon_master: str=None, players: List[str]=None, start_date: date=None, end_date: date=None, world: str=None, main_story: str=None, side_quests: List[str]=None, major_events: List[str]=None, notes: str=None):  # noqa: E501
        """Campaign - a model defined in Swagger

        :param campaign_name: The campaign_name of this Campaign.  # noqa: E501
        :type campaign_name: str
        :param description: The description of this Campaign.  # noqa: E501
        :type description: str
        :param dungeon_master: The dungeon_master of this Campaign.  # noqa: E501
        :type dungeon_master: str
        :param players: The players of this Campaign.  # noqa: E501
        :type players: List[str]
        :param start_date: The start_date of this Campaign.  # noqa: E501
        :type start_date: date
        :param end_date: The end_date of this Campaign.  # noqa: E501
        :type end_date: date
        :param world: The world of this Campaign.  # noqa: E501
        :type world: str
        :param main_story: The main_story of this Campaign.  # noqa: E501
        :type main_story: str
        :param side_quests: The side_quests of this Campaign.  # noqa: E501
        :type side_quests: List[str]
        :param major_events: The major_events of this Campaign.  # noqa: E501
        :type major_events: List[str]
        :param notes: The notes of this Campaign.  # noqa: E501
        :type notes: str
        """
        self.swagger_types = {
            'campaign_name': str,
            'description': str,
            'dungeon_master': str,
            'players': List[str],
            'start_date': date,
            'end_date': date,
            'world': str,
            'main_story': str,
            'side_quests': List[str],
            'major_events': List[str],
            'notes': str
        }

        self.attribute_map = {
            'campaign_name': 'campaignName',
            'description': 'description',
            'dungeon_master': 'dungeonMaster',
            'players': 'players',
            'start_date': 'startDate',
            'end_date': 'endDate',
            'world': 'world',
            'main_story': 'mainStory',
            'side_quests': 'sideQuests',
            'major_events': 'majorEvents',
            'notes': 'notes'
        }
        self._campaign_name = campaign_name
        self._description = description
        self._dungeon_master = dungeon_master
        self._players = players
        self._start_date = start_date
        self._end_date = end_date
        self._world = world
        self._main_story = main_story
        self._side_quests = side_quests
        self._major_events = major_events
        self._notes = notes

    @classmethod
    def from_dict(cls, dikt) -> 'Campaign':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Campaign of this Campaign.  # noqa: E501
        :rtype: Campaign
        """
        return util.deserialize_model(dikt, cls)

    @property
    def campaign_name(self) -> str:
        """Gets the campaign_name of this Campaign.


        :return: The campaign_name of this Campaign.
        :rtype: str
        """
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, campaign_name: str):
        """Sets the campaign_name of this Campaign.


        :param campaign_name: The campaign_name of this Campaign.
        :type campaign_name: str
        """
        if campaign_name is None:
            raise ValueError("Invalid value for `campaign_name`, must not be `None`")  # noqa: E501

        self._campaign_name = campaign_name

    @property
    def description(self) -> str:
        """Gets the description of this Campaign.


        :return: The description of this Campaign.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Campaign.


        :param description: The description of this Campaign.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def dungeon_master(self) -> str:
        """Gets the dungeon_master of this Campaign.


        :return: The dungeon_master of this Campaign.
        :rtype: str
        """
        return self._dungeon_master

    @dungeon_master.setter
    def dungeon_master(self, dungeon_master: str):
        """Sets the dungeon_master of this Campaign.


        :param dungeon_master: The dungeon_master of this Campaign.
        :type dungeon_master: str
        """
        if dungeon_master is None:
            raise ValueError("Invalid value for `dungeon_master`, must not be `None`")  # noqa: E501

        self._dungeon_master = dungeon_master

    @property
    def players(self) -> List[str]:
        """Gets the players of this Campaign.


        :return: The players of this Campaign.
        :rtype: List[str]
        """
        return self._players

    @players.setter
    def players(self, players: List[str]):
        """Sets the players of this Campaign.


        :param players: The players of this Campaign.
        :type players: List[str]
        """
        if players is None:
            raise ValueError("Invalid value for `players`, must not be `None`")  # noqa: E501

        self._players = players

    @property
    def start_date(self) -> date:
        """Gets the start_date of this Campaign.


        :return: The start_date of this Campaign.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: date):
        """Sets the start_date of this Campaign.


        :param start_date: The start_date of this Campaign.
        :type start_date: date
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self) -> date:
        """Gets the end_date of this Campaign.


        :return: The end_date of this Campaign.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: date):
        """Sets the end_date of this Campaign.


        :param end_date: The end_date of this Campaign.
        :type end_date: date
        """

        self._end_date = end_date

    @property
    def world(self) -> str:
        """Gets the world of this Campaign.


        :return: The world of this Campaign.
        :rtype: str
        """
        return self._world

    @world.setter
    def world(self, world: str):
        """Sets the world of this Campaign.


        :param world: The world of this Campaign.
        :type world: str
        """
        if world is None:
            raise ValueError("Invalid value for `world`, must not be `None`")  # noqa: E501

        self._world = world

    @property
    def main_story(self) -> str:
        """Gets the main_story of this Campaign.


        :return: The main_story of this Campaign.
        :rtype: str
        """
        return self._main_story

    @main_story.setter
    def main_story(self, main_story: str):
        """Sets the main_story of this Campaign.


        :param main_story: The main_story of this Campaign.
        :type main_story: str
        """
        if main_story is None:
            raise ValueError("Invalid value for `main_story`, must not be `None`")  # noqa: E501

        self._main_story = main_story

    @property
    def side_quests(self) -> List[str]:
        """Gets the side_quests of this Campaign.


        :return: The side_quests of this Campaign.
        :rtype: List[str]
        """
        return self._side_quests

    @side_quests.setter
    def side_quests(self, side_quests: List[str]):
        """Sets the side_quests of this Campaign.


        :param side_quests: The side_quests of this Campaign.
        :type side_quests: List[str]
        """

        self._side_quests = side_quests

    @property
    def major_events(self) -> List[str]:
        """Gets the major_events of this Campaign.


        :return: The major_events of this Campaign.
        :rtype: List[str]
        """
        return self._major_events

    @major_events.setter
    def major_events(self, major_events: List[str]):
        """Sets the major_events of this Campaign.


        :param major_events: The major_events of this Campaign.
        :type major_events: List[str]
        """

        self._major_events = major_events

    @property
    def notes(self) -> str:
        """Gets the notes of this Campaign.


        :return: The notes of this Campaign.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes: str):
        """Sets the notes of this Campaign.


        :param notes: The notes of this Campaign.
        :type notes: str
        """

        self._notes = notes