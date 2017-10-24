
import pytest
import bot
import os
import telegram
import json

b = telegram.Bot(str(os.environ["TGKEY"]))
u = telegram.Update(1243)

def test_test():  # tests tests
    assert(2+2 == 4)  # hmm

def test_chatinfo():
    jsonparsed = json.loads("{'group_chat_created': False,
    'caption_entities': [], 'photo': [], 'new_chat_members': [],
    'chat': {'type': 'private', 'id': 83218061, 'username': 'TesterUser', 'first_name': 'Tester'},
    'date': 1508876530, 'text': 'Pong', 'channel_chat_created': False,
    'message_id': 20, 'new_chat_photo': [], 'new_chat_member': None,
    'entities': [], 'from': {'is_bot': True, 'id': 431157060, 'username':
    'RealmDbot', 'first_name': 'RealmD'}, 'supergroup_chat_created': False,
    'delete_chat_photo': False}");

    u = Update.de_json(jsonparsed , b)

    bot.chatinfo(b, u)

def test_ping():
    jsonparsed = json.loads("{'group_chat_created': False,
    'caption_entities': [], 'photo': [], 'new_chat_members': [],
    'chat': {'type': 'private', 'id': 83218061, 'username': 'Epowerj', 'TesterUser': 'Tester'},
    'date': 1508876530, 'text': 'Pong', 'channel_chat_created': False,
    'message_id': 20, 'new_chat_photo': [], 'new_chat_member': None,
    'entities': [], 'from': {'is_bot': True, 'id': 431157060, 'username':
    'RealmDbot', 'first_name': 'RealmD'}, 'supergroup_chat_created': False,
    'delete_chat_photo': False}");

    u = Update.de_json(jsonparsed , b)

    bot.ping(b, u)
