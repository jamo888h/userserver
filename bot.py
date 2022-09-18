from telethon.sync import TelegramClient
from telethon import *
import time
from telethon.tl.types import ReplyInlineMarkup
from telethon import events, Button
from telethon import functions, types, events, utils
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.errors import SessionPasswordNeededError
from telethon.tl.types import ReplyInlineMarkup
from telethon.tl.types import KeyboardButtonRow
from telethon.tl.types import KeyboardButtonUrl
import configparser
from telethon import TelegramClient, Button, events 
import json
import asyncio
from datetime import date, datetime
import re
from telethon import TelegramClient
from telethon.sync import TelegramClient
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
    PeerChannel
)
from sys import argv
import sys
import os
from telethon import TelegramClient
from pathlib import Path
import asyncio
from telethon import Button
import logging
import requests
import re
import telethon
from sys import argv
from prettytable import PrettyTable
api_id = 1234567890
api_hash = ''
username = 'r0ld3x'
    
def lista(dets):
    dets = str(dets)
    arrays = re.findall(r'[0-9]+', dets)
    return arrays
                


client = TelegramClient(username, api_id, api_hash)
client.start()

def RoldexVerseCcs(id):
    id = str(id)
    with open('RoldexVerseCcs.txt', 'w') as f:
        if f.write(id):
            return True
        else:
            return False


global str      

with client:
    print("started")
    while True:
        try:
            req = requests.Session()
            f = open('RoldexVerseCcs.txt', 'r')
            rd = int(f.read())
            message = client.iter_messages('https://t.me/RoldexVerseCcs',min_id=rd,wait_time=5)
            for message in message:
                msg = message.text
                if len(msg) == 0: raise Exception('empty data')
                else:
                    input = re.findall(r"[0-9]+", message.text)
                    try:
                        if len(input) == 0 or len(input) == 2: raise Exception("Invalid Data")
                        elif len(input) > 4 and len(input[1]) < 2:
                            cc = input[0]
                            mes = input[1]
                            ano = input[2]
                            cvv = input[3]
                        elif len(input[1]) == 3:
                            ano1 = input[2]
                            cc = input[0]
                            mes = input[2]
                            cvv = input[1]
                            ano = input[3]
                            if len(mes) > 3:
                                mes1 = mes
                                cc = cc
                                cvv = cvv
                                mes = mes[:2]
                                ano = mes1[2:]
                        elif len(input[1]) > 3:
                            ano1 = input[2]
                            cc = input[0]
                            cvv = input[2]
                            mes = input[1][:2]
                            ano = input[1][2:]
                        elif len(input[0]) < 15: raise Exception('Invalid data')
                        else:
                            cc = input[0]
                            mes = input[1]
                            ano = input[2]
                            cvv = input[3]
                    except Exception as e:
                        print(e)
                    else:                         
                        lista = cc + "|" + mes + "|" + ano + "|" + cvv
                        # req.get('https://<yourphpsitename>.herokuapp.com/?lista=' + lista)
                        respo = f"""
<b>〄 ROLDEXVERSE SCRAPPER</b>
<b>○ CARD</b>: <code>{lista}</code>
<b>○ CHANNEL</b>: @RoldexVerse || @RoldexVerseCcs
<b>○ RECHECK</b>: @RoldexVerseChats
<b>○ OWNER</b>: <code>r0ld3x</code>"""
                        client.send_message('channel you want to post', respo,parse_mode='html')
                wd = RoldexVerseCcs(message.id)
        except errors.FloodWaitError as e:
            print('Have to sleep', e.seconds, 'seconds')
            time.sleep(e.seconds)
        except Exception as e:
            print(e)
           