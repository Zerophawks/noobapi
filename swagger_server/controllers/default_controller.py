import connexion
import six

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
from swagger_server import util


def campaigns_get():  # noqa: E501
    """Get a list of campaigns

     # noqa: E501


    :rtype: List[Campaign]
    """
    return 'do some magic!'


def campaigns_post(body):  # noqa: E501
    """Create a new campaign

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Campaign.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def characters_get():  # noqa: E501
    """Get a list of characters

     # noqa: E501


    :rtype: List[Character]
    """
    return 'do some magic!'


def characters_post(body):  # noqa: E501
    """Create a new character

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Character.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def dungeons_dungeon_id_delete(dungeon_id):  # noqa: E501
    """Delete a dungeon by ID

     # noqa: E501

    :param dungeon_id: 
    :type dungeon_id: str

    :rtype: None
    """
    return 'do some magic!'


def dungeons_dungeon_id_get(dungeon_id):  # noqa: E501
    """Get a dungeon by ID

     # noqa: E501

    :param dungeon_id: 
    :type dungeon_id: str

    :rtype: Dungeon
    """
    return 'do some magic!'


def dungeons_dungeon_id_put(body, dungeon_id):  # noqa: E501
    """Update a dungeon by ID

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param dungeon_id: 
    :type dungeon_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Dungeon.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def dungeons_get():  # noqa: E501
    """List all dungeons

     # noqa: E501


    :rtype: List[Dungeon]
    """
    return 'do some magic!'


def dungeons_post(body):  # noqa: E501
    """Create a new dungeon

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Dungeon.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def encounters_encounter_id_delete(encounter_id):  # noqa: E501
    """Delete an encounter by ID

     # noqa: E501

    :param encounter_id: 
    :type encounter_id: str

    :rtype: None
    """
    return 'do some magic!'


def encounters_encounter_id_get(encounter_id):  # noqa: E501
    """Get an encounter by ID

     # noqa: E501

    :param encounter_id: 
    :type encounter_id: str

    :rtype: Encounter
    """
    return 'do some magic!'


def encounters_encounter_id_put(body, encounter_id):  # noqa: E501
    """Update an encounter by ID

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param encounter_id: 
    :type encounter_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Encounter.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def encounters_get():  # noqa: E501
    """Get a list of encounters

     # noqa: E501


    :rtype: List[Encounter]
    """
    return 'do some magic!'


def encounters_post(body):  # noqa: E501
    """Create a new encounter

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Encounter.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def items_get():  # noqa: E501
    """Get a list of items

     # noqa: E501


    :rtype: List[Item]
    """
    return 'do some magic!'


def items_item_id_delete(item_id):  # noqa: E501
    """Delete an item by ID

     # noqa: E501

    :param item_id: 
    :type item_id: str

    :rtype: None
    """
    return 'do some magic!'


def items_item_id_get(item_id):  # noqa: E501
    """Get an item by ID

     # noqa: E501

    :param item_id: 
    :type item_id: str

    :rtype: Item
    """
    return 'do some magic!'


def items_item_id_put(body, item_id):  # noqa: E501
    """Update an item by ID

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param item_id: 
    :type item_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Item.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def items_post(body):  # noqa: E501
    """Create a new item

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Item.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def monsters_get():  # noqa: E501
    """Get a list of monsters

     # noqa: E501


    :rtype: List[Monster]
    """
    return 'do some magic!'


def monsters_monster_id_delete(monster_id):  # noqa: E501
    """Delete a monster by ID

     # noqa: E501

    :param monster_id: 
    :type monster_id: str

    :rtype: None
    """
    return 'do some magic!'


def monsters_monster_id_get(monster_id):  # noqa: E501
    """Get a monster by ID

     # noqa: E501

    :param monster_id: 
    :type monster_id: str

    :rtype: Monster
    """
    return 'do some magic!'


def monsters_monster_id_put(body, monster_id):  # noqa: E501
    """Update a monster by ID

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param monster_id: 
    :type monster_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Monster.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def monsters_post(body):  # noqa: E501
    """Create a new monster

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Monster.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def npcs_get():  # noqa: E501
    """Get a list of NPCs

     # noqa: E501


    :rtype: List[NPC]
    """
    return 'do some magic!'


def npcs_npc_id_delete(npc_id):  # noqa: E501
    """Delete an NPC by ID

     # noqa: E501

    :param npc_id: 
    :type npc_id: str

    :rtype: None
    """
    return 'do some magic!'


def npcs_npc_id_get(npc_id):  # noqa: E501
    """Get an NPC by ID

     # noqa: E501

    :param npc_id: 
    :type npc_id: str

    :rtype: NPC
    """
    return 'do some magic!'


def npcs_npc_id_put(body, npc_id):  # noqa: E501
    """Update an NPC by ID

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param npc_id: 
    :type npc_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = NPC.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def npcs_post(body):  # noqa: E501
    """Create a new NPC

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = NPC.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def quests_get():  # noqa: E501
    """Get a list of quests

     # noqa: E501


    :rtype: List[Quest]
    """
    return 'do some magic!'


def quests_post(body):  # noqa: E501
    """Create a new quest

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Quest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def quests_quest_id_delete(quest_id):  # noqa: E501
    """Delete a quest by ID

     # noqa: E501

    :param quest_id: 
    :type quest_id: str

    :rtype: None
    """
    return 'do some magic!'


def quests_quest_id_get(quest_id):  # noqa: E501
    """Get a quest by ID

     # noqa: E501

    :param quest_id: 
    :type quest_id: str

    :rtype: Quest
    """
    return 'do some magic!'


def quests_quest_id_put(body, quest_id):  # noqa: E501
    """Update a quest by ID

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param quest_id: 
    :type quest_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Quest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def sessions_get():  # noqa: E501
    """Get a list of sessions

     # noqa: E501


    :rtype: List[Session]
    """
    return 'do some magic!'


def sessions_post(body):  # noqa: E501
    """Create a new session

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Session.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def sessions_session_id_delete(session_id):  # noqa: E501
    """Delete a session by ID

     # noqa: E501

    :param session_id: 
    :type session_id: str

    :rtype: None
    """
    return 'do some magic!'


def sessions_session_id_get(session_id):  # noqa: E501
    """Get a session by ID

     # noqa: E501

    :param session_id: 
    :type session_id: str

    :rtype: Session
    """
    return 'do some magic!'


def sessions_session_id_put(body, session_id):  # noqa: E501
    """Update a session by ID

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param session_id: 
    :type session_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Session.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def spells_get():  # noqa: E501
    """Get a list of spells

     # noqa: E501


    :rtype: List[Spell]
    """
    return 'do some magic!'


def spells_post(body):  # noqa: E501
    """Create a new spell

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Spell.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def spells_spell_id_delete(spell_id):  # noqa: E501
    """Delete a spell by ID

     # noqa: E501

    :param spell_id: 
    :type spell_id: str

    :rtype: None
    """
    return 'do some magic!'


def spells_spell_id_get(spell_id):  # noqa: E501
    """Get a spell by ID

     # noqa: E501

    :param spell_id: 
    :type spell_id: str

    :rtype: Spell
    """
    return 'do some magic!'


def spells_spell_id_put(body, spell_id):  # noqa: E501
    """Update a spell by ID

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param spell_id: 
    :type spell_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Spell.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def users_get():  # noqa: E501
    """Get a list of users

     # noqa: E501


    :rtype: List[User]
    """
    return 'do some magic!'


def users_post(body):  # noqa: E501
    """Create a new user

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def users_user_id_delete(user_id):  # noqa: E501
    """Delete a user by ID

     # noqa: E501

    :param user_id: 
    :type user_id: str

    :rtype: None
    """
    return 'do some magic!'


def users_user_id_get(user_id):  # noqa: E501
    """Get a user by ID

     # noqa: E501

    :param user_id: 
    :type user_id: str

    :rtype: User
    """
    return 'do some magic!'


def users_user_id_put(body, user_id):  # noqa: E501
    """Update a user by ID

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param user_id: 
    :type user_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def worlds_get():  # noqa: E501
    """Get a list of worlds

     # noqa: E501


    :rtype: List[World]
    """
    return 'do some magic!'


def worlds_post(body):  # noqa: E501
    """Create a new world

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = World.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def worlds_world_id_delete(world_id):  # noqa: E501
    """Delete a world by ID

     # noqa: E501

    :param world_id: 
    :type world_id: str

    :rtype: None
    """
    return 'do some magic!'


def worlds_world_id_get(world_id):  # noqa: E501
    """Get a world by ID

     # noqa: E501

    :param world_id: 
    :type world_id: str

    :rtype: World
    """
    return 'do some magic!'


def worlds_world_id_put(body, world_id):  # noqa: E501
    """Update a world by ID

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param world_id: 
    :type world_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = World.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
