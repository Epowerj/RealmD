
import pytest
import bot
import os
import telegram

b = telegram.Bot(str(os.environ["TGKEY"]))
u = telegram.Update(1243)

def test_test():  # tests tests
    assert(2+2 == 4)  # hmm

def test_chatinfo():
    global b, u

    jsonparsed = eval("{'update_id': 389907451, 'message': {'group_chat_created': False, 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'chat': {'type': 'private', 'id': 83218061, 'username': 'Epowerj', 'first_name': 'EspookyJ'}, 'date': 1508876530, 'text': '/chatinfo', 'channel_chat_created': False, 'message_id': 19, 'new_chat_photo': [], 'new_chat_member': None, 'entities': [{'type': 'bot_command', 'length': 5, 'offset': 0}], 'from': {'is_bot': False, 'id': 83218061, 'first_name': 'Epowerj', 'username': 'Epowerj', 'language_code': 'en-US'}, 'supergroup_chat_created': False, 'delete_chat_photo': False}}");

    u = u.de_json(jsonparsed , b)

    bot.chatinfo(b, u)

def test_ping():
    global b, u

    jsonparsed = eval("{'update_id': 389907451, 'message': {'group_chat_created': False, 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'chat': {'type': 'private', 'id': 83218061, 'username': 'Epowerj', 'first_name': 'EspookyJ'}, 'date': 1508876530, 'text': '/chatinfo', 'channel_chat_created': False, 'message_id': 19, 'new_chat_photo': [], 'new_chat_member': None, 'entities': [{'type': 'bot_command', 'length': 5, 'offset': 0}], 'from': {'is_bot': False, 'id': 83218061, 'first_name': 'Epowerj', 'username': 'Epowerj', 'language_code': 'en-US'}, 'supergroup_chat_created': False, 'delete_chat_photo': False}}");

    u = u.de_json(jsonparsed , b)

    bot.ping(b, u)
