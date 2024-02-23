import random
import json

from loguru import logger
from API.api_message import at_user
from API.api_iirose import APIIirose  # 大部分接口都在这里
from globals.globals import GlobalVal  # 一些全局变量 now_room_id 是机器人当前所在的房间标识，websocket是ws链接，请勿更改其他参数防止出bug，也不要去监听ws，websockets库只允许一个接收流
from API.api_get_config import get_master_id  # 用于获取配置文件中主人的唯一标识
from API.decorator.command import on_command, MessageType  # 注册指令装饰器和消息类型Enmu

API = APIIirose()
with open('./plugins/iirose_what2eat/eating.json', 'r') as f:
    eating = json.load(f)
with open('./plugins/iirose_what2eat/drinks.json', 'r') as f:
    drinking = json.load(f)

@on_command('>今天吃什么', False, command_type=[MessageType.room_chat, MessageType.private_chat])
async def what2eat(Message):
    await API.send_msg(Message, f'建议吃{random.choice(eating.get("basic_food"))}')

@on_command('>今天喝什么', False, command_type=[MessageType.room_chat, MessageType.private_chat])
async def  what2drink(Message):
    shop = random.choice(list(drinking.keys()))
    await API.send_msg(Message, f'建议喝{shop}的{random.choice(drinking.get(shop))}')
