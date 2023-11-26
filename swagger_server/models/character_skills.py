# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CharacterSkills(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, acrobatics: int=None, animal_handling: int=None, arcana: int=None, athletics: int=None, deception: int=None, history: int=None, insight: int=None, intimidation: int=None, investigation: int=None, medicine: int=None, nature: int=None, perception: int=None, performance: int=None, persuasion: int=None, religion: int=None, sleight_of_hand: int=None, stealth: int=None, survival: int=None):  # noqa: E501
        """CharacterSkills - a model defined in Swagger

        :param acrobatics: The acrobatics of this CharacterSkills.  # noqa: E501
        :type acrobatics: int
        :param animal_handling: The animal_handling of this CharacterSkills.  # noqa: E501
        :type animal_handling: int
        :param arcana: The arcana of this CharacterSkills.  # noqa: E501
        :type arcana: int
        :param athletics: The athletics of this CharacterSkills.  # noqa: E501
        :type athletics: int
        :param deception: The deception of this CharacterSkills.  # noqa: E501
        :type deception: int
        :param history: The history of this CharacterSkills.  # noqa: E501
        :type history: int
        :param insight: The insight of this CharacterSkills.  # noqa: E501
        :type insight: int
        :param intimidation: The intimidation of this CharacterSkills.  # noqa: E501
        :type intimidation: int
        :param investigation: The investigation of this CharacterSkills.  # noqa: E501
        :type investigation: int
        :param medicine: The medicine of this CharacterSkills.  # noqa: E501
        :type medicine: int
        :param nature: The nature of this CharacterSkills.  # noqa: E501
        :type nature: int
        :param perception: The perception of this CharacterSkills.  # noqa: E501
        :type perception: int
        :param performance: The performance of this CharacterSkills.  # noqa: E501
        :type performance: int
        :param persuasion: The persuasion of this CharacterSkills.  # noqa: E501
        :type persuasion: int
        :param religion: The religion of this CharacterSkills.  # noqa: E501
        :type religion: int
        :param sleight_of_hand: The sleight_of_hand of this CharacterSkills.  # noqa: E501
        :type sleight_of_hand: int
        :param stealth: The stealth of this CharacterSkills.  # noqa: E501
        :type stealth: int
        :param survival: The survival of this CharacterSkills.  # noqa: E501
        :type survival: int
        """
        self.swagger_types = {
            'acrobatics': int,
            'animal_handling': int,
            'arcana': int,
            'athletics': int,
            'deception': int,
            'history': int,
            'insight': int,
            'intimidation': int,
            'investigation': int,
            'medicine': int,
            'nature': int,
            'perception': int,
            'performance': int,
            'persuasion': int,
            'religion': int,
            'sleight_of_hand': int,
            'stealth': int,
            'survival': int
        }

        self.attribute_map = {
            'acrobatics': 'acrobatics',
            'animal_handling': 'animalHandling',
            'arcana': 'arcana',
            'athletics': 'athletics',
            'deception': 'deception',
            'history': 'history',
            'insight': 'insight',
            'intimidation': 'intimidation',
            'investigation': 'investigation',
            'medicine': 'medicine',
            'nature': 'nature',
            'perception': 'perception',
            'performance': 'performance',
            'persuasion': 'persuasion',
            'religion': 'religion',
            'sleight_of_hand': 'sleightOfHand',
            'stealth': 'stealth',
            'survival': 'survival'
        }
        self._acrobatics = acrobatics
        self._animal_handling = animal_handling
        self._arcana = arcana
        self._athletics = athletics
        self._deception = deception
        self._history = history
        self._insight = insight
        self._intimidation = intimidation
        self._investigation = investigation
        self._medicine = medicine
        self._nature = nature
        self._perception = perception
        self._performance = performance
        self._persuasion = persuasion
        self._religion = religion
        self._sleight_of_hand = sleight_of_hand
        self._stealth = stealth
        self._survival = survival

    @classmethod
    def from_dict(cls, dikt) -> 'CharacterSkills':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Character_skills of this CharacterSkills.  # noqa: E501
        :rtype: CharacterSkills
        """
        return util.deserialize_model(dikt, cls)

    @property
    def acrobatics(self) -> int:
        """Gets the acrobatics of this CharacterSkills.


        :return: The acrobatics of this CharacterSkills.
        :rtype: int
        """
        return self._acrobatics

    @acrobatics.setter
    def acrobatics(self, acrobatics: int):
        """Sets the acrobatics of this CharacterSkills.


        :param acrobatics: The acrobatics of this CharacterSkills.
        :type acrobatics: int
        """

        self._acrobatics = acrobatics

    @property
    def animal_handling(self) -> int:
        """Gets the animal_handling of this CharacterSkills.


        :return: The animal_handling of this CharacterSkills.
        :rtype: int
        """
        return self._animal_handling

    @animal_handling.setter
    def animal_handling(self, animal_handling: int):
        """Sets the animal_handling of this CharacterSkills.


        :param animal_handling: The animal_handling of this CharacterSkills.
        :type animal_handling: int
        """

        self._animal_handling = animal_handling

    @property
    def arcana(self) -> int:
        """Gets the arcana of this CharacterSkills.


        :return: The arcana of this CharacterSkills.
        :rtype: int
        """
        return self._arcana

    @arcana.setter
    def arcana(self, arcana: int):
        """Sets the arcana of this CharacterSkills.


        :param arcana: The arcana of this CharacterSkills.
        :type arcana: int
        """

        self._arcana = arcana

    @property
    def athletics(self) -> int:
        """Gets the athletics of this CharacterSkills.


        :return: The athletics of this CharacterSkills.
        :rtype: int
        """
        return self._athletics

    @athletics.setter
    def athletics(self, athletics: int):
        """Sets the athletics of this CharacterSkills.


        :param athletics: The athletics of this CharacterSkills.
        :type athletics: int
        """

        self._athletics = athletics

    @property
    def deception(self) -> int:
        """Gets the deception of this CharacterSkills.


        :return: The deception of this CharacterSkills.
        :rtype: int
        """
        return self._deception

    @deception.setter
    def deception(self, deception: int):
        """Sets the deception of this CharacterSkills.


        :param deception: The deception of this CharacterSkills.
        :type deception: int
        """

        self._deception = deception

    @property
    def history(self) -> int:
        """Gets the history of this CharacterSkills.


        :return: The history of this CharacterSkills.
        :rtype: int
        """
        return self._history

    @history.setter
    def history(self, history: int):
        """Sets the history of this CharacterSkills.


        :param history: The history of this CharacterSkills.
        :type history: int
        """

        self._history = history

    @property
    def insight(self) -> int:
        """Gets the insight of this CharacterSkills.


        :return: The insight of this CharacterSkills.
        :rtype: int
        """
        return self._insight

    @insight.setter
    def insight(self, insight: int):
        """Sets the insight of this CharacterSkills.


        :param insight: The insight of this CharacterSkills.
        :type insight: int
        """

        self._insight = insight

    @property
    def intimidation(self) -> int:
        """Gets the intimidation of this CharacterSkills.


        :return: The intimidation of this CharacterSkills.
        :rtype: int
        """
        return self._intimidation

    @intimidation.setter
    def intimidation(self, intimidation: int):
        """Sets the intimidation of this CharacterSkills.


        :param intimidation: The intimidation of this CharacterSkills.
        :type intimidation: int
        """

        self._intimidation = intimidation

    @property
    def investigation(self) -> int:
        """Gets the investigation of this CharacterSkills.


        :return: The investigation of this CharacterSkills.
        :rtype: int
        """
        return self._investigation

    @investigation.setter
    def investigation(self, investigation: int):
        """Sets the investigation of this CharacterSkills.


        :param investigation: The investigation of this CharacterSkills.
        :type investigation: int
        """

        self._investigation = investigation

    @property
    def medicine(self) -> int:
        """Gets the medicine of this CharacterSkills.


        :return: The medicine of this CharacterSkills.
        :rtype: int
        """
        return self._medicine

    @medicine.setter
    def medicine(self, medicine: int):
        """Sets the medicine of this CharacterSkills.


        :param medicine: The medicine of this CharacterSkills.
        :type medicine: int
        """

        self._medicine = medicine

    @property
    def nature(self) -> int:
        """Gets the nature of this CharacterSkills.


        :return: The nature of this CharacterSkills.
        :rtype: int
        """
        return self._nature

    @nature.setter
    def nature(self, nature: int):
        """Sets the nature of this CharacterSkills.


        :param nature: The nature of this CharacterSkills.
        :type nature: int
        """

        self._nature = nature

    @property
    def perception(self) -> int:
        """Gets the perception of this CharacterSkills.


        :return: The perception of this CharacterSkills.
        :rtype: int
        """
        return self._perception

    @perception.setter
    def perception(self, perception: int):
        """Sets the perception of this CharacterSkills.


        :param perception: The perception of this CharacterSkills.
        :type perception: int
        """

        self._perception = perception

    @property
    def performance(self) -> int:
        """Gets the performance of this CharacterSkills.


        :return: The performance of this CharacterSkills.
        :rtype: int
        """
        return self._performance

    @performance.setter
    def performance(self, performance: int):
        """Sets the performance of this CharacterSkills.


        :param performance: The performance of this CharacterSkills.
        :type performance: int
        """

        self._performance = performance

    @property
    def persuasion(self) -> int:
        """Gets the persuasion of this CharacterSkills.


        :return: The persuasion of this CharacterSkills.
        :rtype: int
        """
        return self._persuasion

    @persuasion.setter
    def persuasion(self, persuasion: int):
        """Sets the persuasion of this CharacterSkills.


        :param persuasion: The persuasion of this CharacterSkills.
        :type persuasion: int
        """

        self._persuasion = persuasion

    @property
    def religion(self) -> int:
        """Gets the religion of this CharacterSkills.


        :return: The religion of this CharacterSkills.
        :rtype: int
        """
        return self._religion

    @religion.setter
    def religion(self, religion: int):
        """Sets the religion of this CharacterSkills.


        :param religion: The religion of this CharacterSkills.
        :type religion: int
        """

        self._religion = religion

    @property
    def sleight_of_hand(self) -> int:
        """Gets the sleight_of_hand of this CharacterSkills.


        :return: The sleight_of_hand of this CharacterSkills.
        :rtype: int
        """
        return self._sleight_of_hand

    @sleight_of_hand.setter
    def sleight_of_hand(self, sleight_of_hand: int):
        """Sets the sleight_of_hand of this CharacterSkills.


        :param sleight_of_hand: The sleight_of_hand of this CharacterSkills.
        :type sleight_of_hand: int
        """

        self._sleight_of_hand = sleight_of_hand

    @property
    def stealth(self) -> int:
        """Gets the stealth of this CharacterSkills.


        :return: The stealth of this CharacterSkills.
        :rtype: int
        """
        return self._stealth

    @stealth.setter
    def stealth(self, stealth: int):
        """Sets the stealth of this CharacterSkills.


        :param stealth: The stealth of this CharacterSkills.
        :type stealth: int
        """

        self._stealth = stealth

    @property
    def survival(self) -> int:
        """Gets the survival of this CharacterSkills.


        :return: The survival of this CharacterSkills.
        :rtype: int
        """
        return self._survival

    @survival.setter
    def survival(self, survival: int):
        """Sets the survival of this CharacterSkills.


        :param survival: The survival of this CharacterSkills.
        :type survival: int
        """

        self._survival = survival
