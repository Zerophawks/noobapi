# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class WorldPoliticsKingdoms(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, ruler: str=None, capital: str=None, alliances: List[str]=None):  # noqa: E501
        """WorldPoliticsKingdoms - a model defined in Swagger

        :param name: The name of this WorldPoliticsKingdoms.  # noqa: E501
        :type name: str
        :param ruler: The ruler of this WorldPoliticsKingdoms.  # noqa: E501
        :type ruler: str
        :param capital: The capital of this WorldPoliticsKingdoms.  # noqa: E501
        :type capital: str
        :param alliances: The alliances of this WorldPoliticsKingdoms.  # noqa: E501
        :type alliances: List[str]
        """
        self.swagger_types = {
            'name': str,
            'ruler': str,
            'capital': str,
            'alliances': List[str]
        }

        self.attribute_map = {
            'name': 'name',
            'ruler': 'ruler',
            'capital': 'capital',
            'alliances': 'alliances'
        }
        self._name = name
        self._ruler = ruler
        self._capital = capital
        self._alliances = alliances

    @classmethod
    def from_dict(cls, dikt) -> 'WorldPoliticsKingdoms':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The World_politics_kingdoms of this WorldPoliticsKingdoms.  # noqa: E501
        :rtype: WorldPoliticsKingdoms
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this WorldPoliticsKingdoms.


        :return: The name of this WorldPoliticsKingdoms.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this WorldPoliticsKingdoms.


        :param name: The name of this WorldPoliticsKingdoms.
        :type name: str
        """

        self._name = name

    @property
    def ruler(self) -> str:
        """Gets the ruler of this WorldPoliticsKingdoms.


        :return: The ruler of this WorldPoliticsKingdoms.
        :rtype: str
        """
        return self._ruler

    @ruler.setter
    def ruler(self, ruler: str):
        """Sets the ruler of this WorldPoliticsKingdoms.


        :param ruler: The ruler of this WorldPoliticsKingdoms.
        :type ruler: str
        """

        self._ruler = ruler

    @property
    def capital(self) -> str:
        """Gets the capital of this WorldPoliticsKingdoms.


        :return: The capital of this WorldPoliticsKingdoms.
        :rtype: str
        """
        return self._capital

    @capital.setter
    def capital(self, capital: str):
        """Sets the capital of this WorldPoliticsKingdoms.


        :param capital: The capital of this WorldPoliticsKingdoms.
        :type capital: str
        """

        self._capital = capital

    @property
    def alliances(self) -> List[str]:
        """Gets the alliances of this WorldPoliticsKingdoms.


        :return: The alliances of this WorldPoliticsKingdoms.
        :rtype: List[str]
        """
        return self._alliances

    @alliances.setter
    def alliances(self, alliances: List[str]):
        """Sets the alliances of this WorldPoliticsKingdoms.


        :param alliances: The alliances of this WorldPoliticsKingdoms.
        :type alliances: List[str]
        """

        self._alliances = alliances
