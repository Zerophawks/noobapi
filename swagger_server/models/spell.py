# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.spell_components import SpellComponents  # noqa: F401,E501
from swagger_server import util


class Spell(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, spell_name: str=None, level: int=None, school: str=None, casting_time: str=None, range: str=None, components: SpellComponents=None, duration: str=None, description: str=None, higher_level: str=None, ritual: bool=None, concentration: bool=None, classes: List[str]=None):  # noqa: E501
        """Spell - a model defined in Swagger

        :param spell_name: The spell_name of this Spell.  # noqa: E501
        :type spell_name: str
        :param level: The level of this Spell.  # noqa: E501
        :type level: int
        :param school: The school of this Spell.  # noqa: E501
        :type school: str
        :param casting_time: The casting_time of this Spell.  # noqa: E501
        :type casting_time: str
        :param range: The range of this Spell.  # noqa: E501
        :type range: str
        :param components: The components of this Spell.  # noqa: E501
        :type components: SpellComponents
        :param duration: The duration of this Spell.  # noqa: E501
        :type duration: str
        :param description: The description of this Spell.  # noqa: E501
        :type description: str
        :param higher_level: The higher_level of this Spell.  # noqa: E501
        :type higher_level: str
        :param ritual: The ritual of this Spell.  # noqa: E501
        :type ritual: bool
        :param concentration: The concentration of this Spell.  # noqa: E501
        :type concentration: bool
        :param classes: The classes of this Spell.  # noqa: E501
        :type classes: List[str]
        """
        self.swagger_types = {
            'spell_name': str,
            'level': int,
            'school': str,
            'casting_time': str,
            'range': str,
            'components': SpellComponents,
            'duration': str,
            'description': str,
            'higher_level': str,
            'ritual': bool,
            'concentration': bool,
            'classes': List[str]
        }

        self.attribute_map = {
            'spell_name': 'spellName',
            'level': 'level',
            'school': 'school',
            'casting_time': 'castingTime',
            'range': 'range',
            'components': 'components',
            'duration': 'duration',
            'description': 'description',
            'higher_level': 'higherLevel',
            'ritual': 'ritual',
            'concentration': 'concentration',
            'classes': 'classes'
        }
        self._spell_name = spell_name
        self._level = level
        self._school = school
        self._casting_time = casting_time
        self._range = range
        self._components = components
        self._duration = duration
        self._description = description
        self._higher_level = higher_level
        self._ritual = ritual
        self._concentration = concentration
        self._classes = classes

    @classmethod
    def from_dict(cls, dikt) -> 'Spell':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Spell of this Spell.  # noqa: E501
        :rtype: Spell
        """
        return util.deserialize_model(dikt, cls)

    @property
    def spell_name(self) -> str:
        """Gets the spell_name of this Spell.


        :return: The spell_name of this Spell.
        :rtype: str
        """
        return self._spell_name

    @spell_name.setter
    def spell_name(self, spell_name: str):
        """Sets the spell_name of this Spell.


        :param spell_name: The spell_name of this Spell.
        :type spell_name: str
        """
        if spell_name is None:
            raise ValueError("Invalid value for `spell_name`, must not be `None`")  # noqa: E501

        self._spell_name = spell_name

    @property
    def level(self) -> int:
        """Gets the level of this Spell.


        :return: The level of this Spell.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level: int):
        """Sets the level of this Spell.


        :param level: The level of this Spell.
        :type level: int
        """
        if level is None:
            raise ValueError("Invalid value for `level`, must not be `None`")  # noqa: E501

        self._level = level

    @property
    def school(self) -> str:
        """Gets the school of this Spell.


        :return: The school of this Spell.
        :rtype: str
        """
        return self._school

    @school.setter
    def school(self, school: str):
        """Sets the school of this Spell.


        :param school: The school of this Spell.
        :type school: str
        """
        if school is None:
            raise ValueError("Invalid value for `school`, must not be `None`")  # noqa: E501

        self._school = school

    @property
    def casting_time(self) -> str:
        """Gets the casting_time of this Spell.


        :return: The casting_time of this Spell.
        :rtype: str
        """
        return self._casting_time

    @casting_time.setter
    def casting_time(self, casting_time: str):
        """Sets the casting_time of this Spell.


        :param casting_time: The casting_time of this Spell.
        :type casting_time: str
        """
        if casting_time is None:
            raise ValueError("Invalid value for `casting_time`, must not be `None`")  # noqa: E501

        self._casting_time = casting_time

    @property
    def range(self) -> str:
        """Gets the range of this Spell.


        :return: The range of this Spell.
        :rtype: str
        """
        return self._range

    @range.setter
    def range(self, range: str):
        """Sets the range of this Spell.


        :param range: The range of this Spell.
        :type range: str
        """
        if range is None:
            raise ValueError("Invalid value for `range`, must not be `None`")  # noqa: E501

        self._range = range

    @property
    def components(self) -> SpellComponents:
        """Gets the components of this Spell.


        :return: The components of this Spell.
        :rtype: SpellComponents
        """
        return self._components

    @components.setter
    def components(self, components: SpellComponents):
        """Sets the components of this Spell.


        :param components: The components of this Spell.
        :type components: SpellComponents
        """
        if components is None:
            raise ValueError("Invalid value for `components`, must not be `None`")  # noqa: E501

        self._components = components

    @property
    def duration(self) -> str:
        """Gets the duration of this Spell.


        :return: The duration of this Spell.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration: str):
        """Sets the duration of this Spell.


        :param duration: The duration of this Spell.
        :type duration: str
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def description(self) -> str:
        """Gets the description of this Spell.


        :return: The description of this Spell.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Spell.


        :param description: The description of this Spell.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def higher_level(self) -> str:
        """Gets the higher_level of this Spell.


        :return: The higher_level of this Spell.
        :rtype: str
        """
        return self._higher_level

    @higher_level.setter
    def higher_level(self, higher_level: str):
        """Sets the higher_level of this Spell.


        :param higher_level: The higher_level of this Spell.
        :type higher_level: str
        """

        self._higher_level = higher_level

    @property
    def ritual(self) -> bool:
        """Gets the ritual of this Spell.


        :return: The ritual of this Spell.
        :rtype: bool
        """
        return self._ritual

    @ritual.setter
    def ritual(self, ritual: bool):
        """Sets the ritual of this Spell.


        :param ritual: The ritual of this Spell.
        :type ritual: bool
        """

        self._ritual = ritual

    @property
    def concentration(self) -> bool:
        """Gets the concentration of this Spell.


        :return: The concentration of this Spell.
        :rtype: bool
        """
        return self._concentration

    @concentration.setter
    def concentration(self, concentration: bool):
        """Sets the concentration of this Spell.


        :param concentration: The concentration of this Spell.
        :type concentration: bool
        """

        self._concentration = concentration

    @property
    def classes(self) -> List[str]:
        """Gets the classes of this Spell.


        :return: The classes of this Spell.
        :rtype: List[str]
        """
        return self._classes

    @classes.setter
    def classes(self, classes: List[str]):
        """Sets the classes of this Spell.


        :param classes: The classes of this Spell.
        :type classes: List[str]
        """

        self._classes = classes