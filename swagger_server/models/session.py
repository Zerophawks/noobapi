# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Session(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, session_number: int=None, campaign_id: str=None, _date: datetime=None, duration: str=None, location: str=None, participants: List[str]=None, summary: str=None, key_events: List[str]=None, notes: str=None, next_session: datetime=None):  # noqa: E501
        """Session - a model defined in Swagger

        :param session_number: The session_number of this Session.  # noqa: E501
        :type session_number: int
        :param campaign_id: The campaign_id of this Session.  # noqa: E501
        :type campaign_id: str
        :param _date: The _date of this Session.  # noqa: E501
        :type _date: datetime
        :param duration: The duration of this Session.  # noqa: E501
        :type duration: str
        :param location: The location of this Session.  # noqa: E501
        :type location: str
        :param participants: The participants of this Session.  # noqa: E501
        :type participants: List[str]
        :param summary: The summary of this Session.  # noqa: E501
        :type summary: str
        :param key_events: The key_events of this Session.  # noqa: E501
        :type key_events: List[str]
        :param notes: The notes of this Session.  # noqa: E501
        :type notes: str
        :param next_session: The next_session of this Session.  # noqa: E501
        :type next_session: datetime
        """
        self.swagger_types = {
            'session_number': int,
            'campaign_id': str,
            '_date': datetime,
            'duration': str,
            'location': str,
            'participants': List[str],
            'summary': str,
            'key_events': List[str],
            'notes': str,
            'next_session': datetime
        }

        self.attribute_map = {
            'session_number': 'sessionNumber',
            'campaign_id': 'campaignID',
            '_date': 'date',
            'duration': 'duration',
            'location': 'location',
            'participants': 'participants',
            'summary': 'summary',
            'key_events': 'keyEvents',
            'notes': 'notes',
            'next_session': 'nextSession'
        }
        self._session_number = session_number
        self._campaign_id = campaign_id
        self.__date = _date
        self._duration = duration
        self._location = location
        self._participants = participants
        self._summary = summary
        self._key_events = key_events
        self._notes = notes
        self._next_session = next_session

    @classmethod
    def from_dict(cls, dikt) -> 'Session':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Session of this Session.  # noqa: E501
        :rtype: Session
        """
        return util.deserialize_model(dikt, cls)

    @property
    def session_number(self) -> int:
        """Gets the session_number of this Session.


        :return: The session_number of this Session.
        :rtype: int
        """
        return self._session_number

    @session_number.setter
    def session_number(self, session_number: int):
        """Sets the session_number of this Session.


        :param session_number: The session_number of this Session.
        :type session_number: int
        """
        if session_number is None:
            raise ValueError("Invalid value for `session_number`, must not be `None`")  # noqa: E501

        self._session_number = session_number

    @property
    def campaign_id(self) -> str:
        """Gets the campaign_id of this Session.


        :return: The campaign_id of this Session.
        :rtype: str
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id: str):
        """Sets the campaign_id of this Session.


        :param campaign_id: The campaign_id of this Session.
        :type campaign_id: str
        """
        if campaign_id is None:
            raise ValueError("Invalid value for `campaign_id`, must not be `None`")  # noqa: E501

        self._campaign_id = campaign_id

    @property
    def _date(self) -> datetime:
        """Gets the _date of this Session.


        :return: The _date of this Session.
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date: datetime):
        """Sets the _date of this Session.


        :param _date: The _date of this Session.
        :type _date: datetime
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def duration(self) -> str:
        """Gets the duration of this Session.


        :return: The duration of this Session.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration: str):
        """Sets the duration of this Session.


        :param duration: The duration of this Session.
        :type duration: str
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def location(self) -> str:
        """Gets the location of this Session.


        :return: The location of this Session.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location: str):
        """Sets the location of this Session.


        :param location: The location of this Session.
        :type location: str
        """

        self._location = location

    @property
    def participants(self) -> List[str]:
        """Gets the participants of this Session.


        :return: The participants of this Session.
        :rtype: List[str]
        """
        return self._participants

    @participants.setter
    def participants(self, participants: List[str]):
        """Sets the participants of this Session.


        :param participants: The participants of this Session.
        :type participants: List[str]
        """
        if participants is None:
            raise ValueError("Invalid value for `participants`, must not be `None`")  # noqa: E501

        self._participants = participants

    @property
    def summary(self) -> str:
        """Gets the summary of this Session.


        :return: The summary of this Session.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary: str):
        """Sets the summary of this Session.


        :param summary: The summary of this Session.
        :type summary: str
        """
        if summary is None:
            raise ValueError("Invalid value for `summary`, must not be `None`")  # noqa: E501

        self._summary = summary

    @property
    def key_events(self) -> List[str]:
        """Gets the key_events of this Session.


        :return: The key_events of this Session.
        :rtype: List[str]
        """
        return self._key_events

    @key_events.setter
    def key_events(self, key_events: List[str]):
        """Sets the key_events of this Session.


        :param key_events: The key_events of this Session.
        :type key_events: List[str]
        """

        self._key_events = key_events

    @property
    def notes(self) -> str:
        """Gets the notes of this Session.


        :return: The notes of this Session.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes: str):
        """Sets the notes of this Session.


        :param notes: The notes of this Session.
        :type notes: str
        """

        self._notes = notes

    @property
    def next_session(self) -> datetime:
        """Gets the next_session of this Session.


        :return: The next_session of this Session.
        :rtype: datetime
        """
        return self._next_session

    @next_session.setter
    def next_session(self, next_session: datetime):
        """Sets the next_session of this Session.


        :param next_session: The next_session of this Session.
        :type next_session: datetime
        """

        self._next_session = next_session