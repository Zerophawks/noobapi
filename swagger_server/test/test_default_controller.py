# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.campaign import Campaign  # noqa: E501
from swagger_server.models.character import Character  # noqa: E501
from swagger_server.models.dungeon import Dungeon  # noqa: E501
from swagger_server.models.encounter import Encounter  # noqa: E501
from swagger_server.models.item import Item  # noqa: E501
from swagger_server.models.monster import Monster  # noqa: E501
from swagger_server.models.npc import NPC  # noqa: E501
from swagger_server.models.quest import Quest  # noqa: E501
from swagger_server.models.session import Session  # noqa: E501
from swagger_server.models.spell import Spell  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.world import World  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_campaigns_get(self):
        """Test case for campaigns_get

        Get a list of campaigns
        """
        response = self.client.open(
            '/campaigns',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_campaigns_post(self):
        """Test case for campaigns_post

        Create a new campaign
        """
        body = Campaign()
        response = self.client.open(
            '/campaigns',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_characters_get(self):
        """Test case for characters_get

        Get a list of characters
        """
        response = self.client.open(
            '/characters',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_characters_post(self):
        """Test case for characters_post

        Create a new character
        """
        body = Character()
        response = self.client.open(
            '/characters',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dungeons_dungeon_id_delete(self):
        """Test case for dungeons_dungeon_id_delete

        Delete a dungeon by ID
        """
        response = self.client.open(
            '/dungeons/{dungeonId}'.format(dungeon_id='dungeon_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dungeons_dungeon_id_get(self):
        """Test case for dungeons_dungeon_id_get

        Get a dungeon by ID
        """
        response = self.client.open(
            '/dungeons/{dungeonId}'.format(dungeon_id='dungeon_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dungeons_dungeon_id_put(self):
        """Test case for dungeons_dungeon_id_put

        Update a dungeon by ID
        """
        body = Dungeon()
        response = self.client.open(
            '/dungeons/{dungeonId}'.format(dungeon_id='dungeon_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dungeons_get(self):
        """Test case for dungeons_get

        List all dungeons
        """
        response = self.client.open(
            '/dungeons',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dungeons_post(self):
        """Test case for dungeons_post

        Create a new dungeon
        """
        body = Dungeon()
        response = self.client.open(
            '/dungeons',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_encounters_encounter_id_delete(self):
        """Test case for encounters_encounter_id_delete

        Delete an encounter by ID
        """
        response = self.client.open(
            '/encounters/{encounterId}'.format(encounter_id='encounter_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_encounters_encounter_id_get(self):
        """Test case for encounters_encounter_id_get

        Get an encounter by ID
        """
        response = self.client.open(
            '/encounters/{encounterId}'.format(encounter_id='encounter_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_encounters_encounter_id_put(self):
        """Test case for encounters_encounter_id_put

        Update an encounter by ID
        """
        body = Encounter()
        response = self.client.open(
            '/encounters/{encounterId}'.format(encounter_id='encounter_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_encounters_get(self):
        """Test case for encounters_get

        Get a list of encounters
        """
        response = self.client.open(
            '/encounters',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_encounters_post(self):
        """Test case for encounters_post

        Create a new encounter
        """
        body = Encounter()
        response = self.client.open(
            '/encounters',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_items_get(self):
        """Test case for items_get

        Get a list of items
        """
        response = self.client.open(
            '/items',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_items_item_id_delete(self):
        """Test case for items_item_id_delete

        Delete an item by ID
        """
        response = self.client.open(
            '/items/{itemId}'.format(item_id='item_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_items_item_id_get(self):
        """Test case for items_item_id_get

        Get an item by ID
        """
        response = self.client.open(
            '/items/{itemId}'.format(item_id='item_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_items_item_id_put(self):
        """Test case for items_item_id_put

        Update an item by ID
        """
        body = Item()
        response = self.client.open(
            '/items/{itemId}'.format(item_id='item_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_items_post(self):
        """Test case for items_post

        Create a new item
        """
        body = Item()
        response = self.client.open(
            '/items',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_monsters_get(self):
        """Test case for monsters_get

        Get a list of monsters
        """
        response = self.client.open(
            '/monsters',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_monsters_monster_id_delete(self):
        """Test case for monsters_monster_id_delete

        Delete a monster by ID
        """
        response = self.client.open(
            '/monsters/{monsterId}'.format(monster_id='monster_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_monsters_monster_id_get(self):
        """Test case for monsters_monster_id_get

        Get a monster by ID
        """
        response = self.client.open(
            '/monsters/{monsterId}'.format(monster_id='monster_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_monsters_monster_id_put(self):
        """Test case for monsters_monster_id_put

        Update a monster by ID
        """
        body = Monster()
        response = self.client.open(
            '/monsters/{monsterId}'.format(monster_id='monster_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_monsters_post(self):
        """Test case for monsters_post

        Create a new monster
        """
        body = Monster()
        response = self.client.open(
            '/monsters',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_npcs_get(self):
        """Test case for npcs_get

        Get a list of NPCs
        """
        response = self.client.open(
            '/npcs',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_npcs_npc_id_delete(self):
        """Test case for npcs_npc_id_delete

        Delete an NPC by ID
        """
        response = self.client.open(
            '/npcs/{npcId}'.format(npc_id='npc_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_npcs_npc_id_get(self):
        """Test case for npcs_npc_id_get

        Get an NPC by ID
        """
        response = self.client.open(
            '/npcs/{npcId}'.format(npc_id='npc_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_npcs_npc_id_put(self):
        """Test case for npcs_npc_id_put

        Update an NPC by ID
        """
        body = NPC()
        response = self.client.open(
            '/npcs/{npcId}'.format(npc_id='npc_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_npcs_post(self):
        """Test case for npcs_post

        Create a new NPC
        """
        body = NPC()
        response = self.client.open(
            '/npcs',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_quests_get(self):
        """Test case for quests_get

        Get a list of quests
        """
        response = self.client.open(
            '/quests',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_quests_post(self):
        """Test case for quests_post

        Create a new quest
        """
        body = Quest()
        response = self.client.open(
            '/quests',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_quests_quest_id_delete(self):
        """Test case for quests_quest_id_delete

        Delete a quest by ID
        """
        response = self.client.open(
            '/quests/{questId}'.format(quest_id='quest_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_quests_quest_id_get(self):
        """Test case for quests_quest_id_get

        Get a quest by ID
        """
        response = self.client.open(
            '/quests/{questId}'.format(quest_id='quest_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_quests_quest_id_put(self):
        """Test case for quests_quest_id_put

        Update a quest by ID
        """
        body = Quest()
        response = self.client.open(
            '/quests/{questId}'.format(quest_id='quest_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sessions_get(self):
        """Test case for sessions_get

        Get a list of sessions
        """
        response = self.client.open(
            '/sessions',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sessions_post(self):
        """Test case for sessions_post

        Create a new session
        """
        body = Session()
        response = self.client.open(
            '/sessions',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sessions_session_id_delete(self):
        """Test case for sessions_session_id_delete

        Delete a session by ID
        """
        response = self.client.open(
            '/sessions/{sessionId}'.format(session_id='session_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sessions_session_id_get(self):
        """Test case for sessions_session_id_get

        Get a session by ID
        """
        response = self.client.open(
            '/sessions/{sessionId}'.format(session_id='session_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sessions_session_id_put(self):
        """Test case for sessions_session_id_put

        Update a session by ID
        """
        body = Session()
        response = self.client.open(
            '/sessions/{sessionId}'.format(session_id='session_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_spells_get(self):
        """Test case for spells_get

        Get a list of spells
        """
        response = self.client.open(
            '/spells',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_spells_post(self):
        """Test case for spells_post

        Create a new spell
        """
        body = Spell()
        response = self.client.open(
            '/spells',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_spells_spell_id_delete(self):
        """Test case for spells_spell_id_delete

        Delete a spell by ID
        """
        response = self.client.open(
            '/spells/{spellId}'.format(spell_id='spell_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_spells_spell_id_get(self):
        """Test case for spells_spell_id_get

        Get a spell by ID
        """
        response = self.client.open(
            '/spells/{spellId}'.format(spell_id='spell_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_spells_spell_id_put(self):
        """Test case for spells_spell_id_put

        Update a spell by ID
        """
        body = Spell()
        response = self.client.open(
            '/spells/{spellId}'.format(spell_id='spell_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_get(self):
        """Test case for users_get

        Get a list of users
        """
        response = self.client.open(
            '/users',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_post(self):
        """Test case for users_post

        Create a new user
        """
        body = User()
        response = self.client.open(
            '/users',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_user_id_delete(self):
        """Test case for users_user_id_delete

        Delete a user by ID
        """
        response = self.client.open(
            '/users/{userId}'.format(user_id='user_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_user_id_get(self):
        """Test case for users_user_id_get

        Get a user by ID
        """
        response = self.client.open(
            '/users/{userId}'.format(user_id='user_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_user_id_put(self):
        """Test case for users_user_id_put

        Update a user by ID
        """
        body = User()
        response = self.client.open(
            '/users/{userId}'.format(user_id='user_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_worlds_get(self):
        """Test case for worlds_get

        Get a list of worlds
        """
        response = self.client.open(
            '/worlds',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_worlds_post(self):
        """Test case for worlds_post

        Create a new world
        """
        body = World()
        response = self.client.open(
            '/worlds',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_worlds_world_id_delete(self):
        """Test case for worlds_world_id_delete

        Delete a world by ID
        """
        response = self.client.open(
            '/worlds/{worldId}'.format(world_id='world_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_worlds_world_id_get(self):
        """Test case for worlds_world_id_get

        Get a world by ID
        """
        response = self.client.open(
            '/worlds/{worldId}'.format(world_id='world_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_worlds_world_id_put(self):
        """Test case for worlds_world_id_put

        Update a world by ID
        """
        body = World()
        response = self.client.open(
            '/worlds/{worldId}'.format(world_id='world_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
