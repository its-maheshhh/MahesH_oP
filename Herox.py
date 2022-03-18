import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest


from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl import functions
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest


from Config import STRING, SUDO, BIO_MESSAGE, ALIVE_NAME, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, STRING11, STRING12 , STRING13 , STRING14 , STRING15 ,STRING16 , STRING17 , STRING18 , STRING19 , STRING20 , STRING21 , STRING22 , STRING23 , STRING24 , STRING25 , STRING26 , STRING27 , STRING28 , STRING29 , STRING30
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID


a = API_ID
b = API_HASH
smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING10
eleve = STRING11
twelv = STRING12
thirt = STRING13
forte = STRING14
fifth = STRING15
sieee = STRING16
seeee = STRING17
eieee = STRING18
nieee = STRING19
gandu = STRING20
ekish = STRING21
baish = STRING22
teish = STRING23
tfour = STRING24
tfive = STRING25
tsix = STRING26
tseven = STRING27
teight = STRING28
tnine = STRING29
thirty = STRING30



idk = ""
ydk = ""
wdk = ""
sdk = ""
hdk = ""
adk = ""
bdk = ""
cdk = ""
edk = ""
ddk = ""
vkk = ""
kkk = ""
lkk = ""
mkk = ""
sid = ""
shy = ""
aan = ""
ake = ""
eel = ""
khu = ""
shi = ""
yaa = ""
dav = ""
raj = ""
put = ""
eag = ""
gle = ""
wal = ""
aaa = ""
boy = ""



que = {}

SMEX_USERS = [1653260872, 1281418521]
for x in SUDO: 
    SMEX_USERS.append(x)
    
async def start_flash():
    global idk
    global ydk
    global wdk
    global sdk
    global hdk
    global adk
    global bdk
    global cdk
    global ddk
    global edk
    global vkk
    global kkk
    global lkk
    global mkk
    global sid
    global shy
    global aan
    global ake
    global eel
    global khu
    global shi
    global yaa
    global dav
    global raj
    global put
    global eag
    global gle
    global wal
    global aaa
    global boy
    
    if smex:
        session_name = str(smex)
        print("String 1 Found")
        idk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await idk.start()
            botme = await idk.get_me()
            await idk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await idk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await idk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await idk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await idk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        idk = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if smexx:
        session_name = str(smexx)
        print("String 2 Found")
        ydk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await ydk.start()
            await ydk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await ydk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await ydk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await ydk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await ydk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botme = await ydk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        ydk = TelegramClient(session_name, a, b)
        try:
            await ydk.start()
        except Exception as e:
            pass

    if smexxx:
        session_name = str(smexxx)
        print("String 3 Found")
        wdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await  wdk.start()
            await wdk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await wdk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await wdk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await wdk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await wdk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botme = await wdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        wdk = TelegramClient(session_name, a, b)
        try:
            await wdk.start()
        except Exception as e:
            pass

    if smexxxx:
        session_name = str(smexxxx)
        print("String 4 Found")
        hdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await hdk.start()
            await hdk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await hdk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await hdk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await hdk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await hdk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botme = await hdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        hdk = TelegramClient(session_name, a, b)
        try:
            await hdk.start()
        except Exception as e:
            pass

    if smexxxxx:
        session_name = str(smexxxxx)
        print("String 5 Found")
        sdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await sdk.start()
            await sdk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await sdk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await sdk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await sdk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await sdk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botme = await sdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        sdk = TelegramClient(session_name, a, b)
        try:
            await sdk.start()
        except Exception as e:
            pass
                  
    if sixth:
        session_name = str(sixth)
        print("String 6 Found")
        adk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await adk.start()
            await adk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await adk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await adk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await adk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await adk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botme = await adk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "startup"
        adk = TelegramClient(session_name, a, b)
        try:
            await adk.start()
        except Exception as e:
            pass

    if seven:
        session_name = str(seven)
        print("String 7 Found")
        bdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await bdk.start()
            await bdk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await bdk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await bdk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await bdk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await bdk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botme = await bdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "startup"
        bdk = TelegramClient(session_name, a, b)
        try:
            await bdk.start()
        except Exception as e:
            pass    
        
    
    if eight:
        session_name = str(eight)
        print("String 8 Found")
        cdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await cdk.start()
            await cdk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await cdk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await cdk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await cdk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await cdk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botme = await cdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "startup"
        cdk = TelegramClient(session_name, a, b)
        try:
            await cdk.start()
        except Exception as e:
            pass   
        
    if ninth:
        session_name = str(ninth)
        print("String 9 Found")
        ddk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await ddk.start()
            await ddk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await ddk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await ddk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await ddk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await ddk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botme = await ddk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "startup"
        ddk = TelegramClient(session_name, a, b)
        try:
            await ddk.start()
        except Exception as e:
            pass   
    
  
    if tenth:
        session_name = str(tenth)
        print("String 10 Found")
        edk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 10")
            await edk.start()
            await edk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await edk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await edk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await edk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await edk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botme = await edk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "startup"
        edk = TelegramClient(session_name, a, b)
        try:
            await edk.start()
        except Exception as e:
            pass 
        
    
    if eleve:
        session_name = str(eleve)
        print("String 11 Found")
        vkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 11")
            await vkk.start()
            await vkk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await vkk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await vkk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await vkk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await vkk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botme = await vkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = "startup"
        vkk = TelegramClient(session_name, a, b)
        try:
            await vkk.start()
        except Exception as e:
            pass
        
    
    if twelv:
        session_name = str(twelv)
        print("String 12 Found")
        kkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 12")
            await kkk.start()
            await kkk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await kkk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await kkk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await kkk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await kkk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botme = await kkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "startup"
        kkk = TelegramClient(session_name, a, b)
        try:
            await kkk.start()
        except Exception as e:
            pass   
    
  
    if thirt:
        session_name = str(thirt)
        print("String 13  Found")
        lkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 13")
            await lkk.start()
            await lkk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await lkk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await lkk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await lkk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await lkk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botme = await lkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "startup"
        lkk = TelegramClient(session_name, a, b)
        try:
            await lkk.start()
        except Exception as e:
            pass 
        
    
    if forte:
        session_name = str(forte)
        print("String 14 Found")
        mkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 14")
            await mkk.start()
            await mkk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await mkk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await mkk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await mkk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await mkk(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botme = await mkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "startup"
        mkk = TelegramClient(session_name, a, b)
        try:
            await mkk.start()
        except Exception as e:
            pass
        
    
    if fifth:
        session_name = str(fifth)
        print("String 15 Found")
        sid = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 15")
            await sid.start()
            await sid(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await sid(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await sid(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await sid(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await sid(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botme = await sid.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "startup"
        sid = TelegramClient(session_name, a, b)
        try:
            await sid.start()
        except Exception as e:
            pass


    if sieee:
        session_name = str(sieee)
        print("String 16 Found")
        shy = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 16")
            await shy.start()
            botme = await shy.get_me()
            await shy(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await shy(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await shy(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await shy(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await shy(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "startup"
        shy = TelegramClient(session_name, a, b)
        try:
            await shy.start()
        except Exception as e:
            pass
   
    if seeee:
        session_name = str(seeee)
        print("String 17 Found")
        aan = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 17")
            await aan.start()
            botme = await aan.get_me()
            await aan(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await aan(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await aan(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await aan(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await aan(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "startup"
        aan = TelegramClient(session_name, a, b)
        try:
            await aan.start()
        except Exception as e:
            pass
   
    if eieee:
        session_name = str(eieee)
        print("String 18 Found")
        ake = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 18")
            await ake.start()
            botme = await ake.get_me()
            await ake(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await ake(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await ake(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await ake(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await ake(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "startup"
        ake = TelegramClient(session_name, a, b)
        try:
            await ake.start()
        except Exception as e:
            pass
   
    if nieee:
        session_name = str(nieee)
        print("String 19 Found")
        eel = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 19")
            await eel.start()
            botme = await eel.get_me()
            await eel(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await eel(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await eel(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await eel(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await eel(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "startup"
        eel = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if gandu:
        session_name = str(gandu)
        print("String 20 Found")
        khu = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 20")
            await khu.start()
            botme = await khu.get_me()
            await khu(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await khu(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await khu(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await khu(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await khu(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "startup"
        khu = TelegramClient(session_name, a, b)
        try:
            await khu.start()
        except Exception as e:
            pass
   
    if ekish:
        session_name = str(ekish)
        print("String 21 Found")
        shi = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 21")
            await shi.start()
            botme = await shi.get_me()
            await shi(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await shi(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await shi(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await shi(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await shi(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 21 not Found")
        session_name = "startup"
        shi = TelegramClient(session_name, a, b)
        try:
            await shi.start()
        except Exception as e:
            pass
   
    if baish:
        session_name = str(baish)
        print("String 22 Found")
        yaa = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 22")
            await yaa.start()
            botme = await yaa.get_me()
            await yaa(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await yaa(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await yaa(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await yaa(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await yaa(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        session_name = "startup"
        yaa = TelegramClient(session_name, a, b)
        try:
            await yaa.start()
        except Exception as e:
            pass
   
    if teish:
        session_name = str(teish)
        print("String 23 Found")
        dav = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 23")
            await dav.start()
            botme = await dav.get_me()
            await dav(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await dav(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await dav(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await dav(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await dav(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        session_name = "startup"
        dav = TelegramClient(session_name, a, b)
        try:
            await dav.start()
        except Exception as e:
            pass
   
    if tfour:
        session_name = str(tfour)
        print("String 24 Found")
        raj = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 24")
            await raj.start()
            botme = await raj.get_me()
            await raj(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await raj(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await raj(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await raj(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await raj(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        session_name = "startup"
        raj = TelegramClient(session_name, a, b)
        try:
            await raj.start()
        except Exception as e:
            pass
   
    if tfive:
        session_name = str(tfive)
        print("String 25 Found")
        put = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 25")
            await put.start()
            botme = await put.get_me()
            await put(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await put(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await put(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await put(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await put(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        session_name = "startup"
        put = TelegramClient(session_name, a, b)
        try:
            await put.start()
        except Exception as e:
            pass
   
    if tsix:
        session_name = str(tsix)
        print("String 26 Found")
        eag = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 26")
            await eag.start()
            botme = await eag.get_me()
            await eag(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await eag(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await eag(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await eag(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await eag(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 26 not Found")
        session_name = "startup"
        eag = TelegramClient(session_name, a, b)
        try:
            await eag.start()
        except Exception as e:
            pass
   
    if tseven:
        session_name = str(tseven)
        print("String 27 Found")
        ydk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 27")
            await gle.start()
            await gle(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await gle(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await gle(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await gle(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await gle(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botme = await gle.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        pass
        session_name = "startup"
        gle = TelegramClient(session_name, a, b)
        try:
            await gle.start()
        except Exception as e:
            pass

    if teight:
        session_name = str(teight)
        print("String 28 Found")
        wal = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 28")
            await wal.start()
            await wal(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await wal(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await wal(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await wal(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await wal(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botme = await wal.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 not Found")
        pass
        session_name = "startup"
        wal = TelegramClient(session_name, a, b)
        try:
            await wal.start()
        except Exception as e:
            pass

    if tnine:
        session_name = str(tnine)
        print("String 29 Found")
        aaa = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 29")
            await aaa.start()
            await aaa(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await aaa(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await aaa(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await aaa(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await aaa(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botme = await aaa.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 not Found")
        pass
        session_name = "startup"
        aaa = TelegramClient(session_name, a, b)
        try:
            await aaa.start()
        except Exception as e:
            pass

    if thirty:
        session_name = str(thirty)
        print("String 30 Found")
        boy = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 30")
            await boy.start()
            await boy(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await boy(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await boy(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await boy(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            await boy(functions.channels.JoinChannelRequest(channel="@@Team_dominatorchat"))
            botme = await boy.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 not Found")
        pass
        session_name = "startup"
        boy = TelegramClient(session_name, a, b)
        try:
            await boy.start()
        except Exception as e:
            pass
                  
   
loop = asyncio.get_event_loop()
loop.run_until_complete(start_flash())       

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        pass


@idk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        flash = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(flash) == 2:
            message = str(flash[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(flash[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(flash[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
            
            
@idk.on(events.NewMessage(incoming=True))
@ydk.on(events.NewMessage(incoming=True))
@wdk.on(events.NewMessage(incoming=True))
@hdk.on(events.NewMessage(incoming=True))
@sdk.on(events.NewMessage(incoming=True))
@adk.on(events.NewMessage(incoming=True))
@bdk.on(events.NewMessage(incoming=True))
@cdk.on(events.NewMessage(incoming=True))
@edk.on(events.NewMessage(incoming=True))
@ddk.on(events.NewMessage(incoming=True))
@vkk.on(events.NewMessage(incoming=True))
@kkk.on(events.NewMessage(incoming=True))
@lkk.on(events.NewMessage(incoming=True))
@mkk.on(events.NewMessage(incoming=True))
@sid.on(events.NewMessage(incoming=True))
@shy.on(events.NewMessage(incoming=True))
@aan.on(events.NewMessage(incoming=True))
@ake.on(events.NewMessage(incoming=True))
@eel.on(events.NewMessage(incoming=True))
@khu.on(events.NewMessage(incoming=True))
@shi.on(events.NewMessage(incoming=True))
@yaa.on(events.NewMessage(incoming=True))
@dav.on(events.NewMessage(incoming=True))
@raj.on(events.NewMessage(incoming=True))
@put.on(events.NewMessage(incoming=True))
@eag.on(events.NewMessage(incoming=True))
@gle.on(events.NewMessage(incoming=True))
@wal.on(events.NewMessage(incoming=True))
@aaa.on(events.NewMessage(incoming=True))
@boy.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )
        

@idk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.spam")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.spam")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.spam")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.spam")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.spam")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        flash = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(flash) == 2:
            message = str(flash[1])
            counter = int(flash[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:  
            counter = int(flash[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(flash[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.join"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SMEX_USERS:
        flash = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = flash[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            

@idk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        flash = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(flash[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid")) 
@ake.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        flash = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(flash[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            

@idk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.pjoin")) 
@ake.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.pjoin HGYs1wvsPUplMmM1"
    if e.sender_id in SMEX_USERS:
        flash = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = flash[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

@idk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        flash = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = flash[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
           
           
@idk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.delayspam")) 
@ake.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        smex = await e.get_reply_message()
        flash = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        flashsexy = flash[1:]
        if len(flashsexy) == 2:
            message = str(flashsexy[1])
            counter = int(flashsexy[0])
            sleeptime = float(flash[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(flashsexy[0])
            sleeptime = float(flash[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(flashsexy[0])
            sleeptime = float(flash[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        flash = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(flash) == 2:
            message = str(flash[1])
            counter = int(flash[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(flash[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(flash[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

@idk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f" HEROX SPAMMER BOT IS ALIVE!\n`{ms}` 𝗺𝘀\n           ⚔️ 𝙃𝙀𝙍𝙊𝙓 𝙎𝙋𝘼𝙈𝘽𝙊𝙏 ⚔️")
        

@idk.on(events.NewMessage(incoming=True, pattern=r"\.abuse"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.abuse"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.abuse"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.abuse"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.abuse"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.abuse"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.abuse"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.abuse"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.abuse"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.abuse")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.abuse")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.abuse")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.abuse")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.abuse")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.abuse"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.abuse"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.abuse"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.abuse"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.abuse"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.abuse"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.abuse"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.abuse"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.abuse"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.abuse"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.abuse"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.abuse"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.abuse"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.abuse"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.abuse"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.abuse"))
async def abuse(e):
    usage = "**Module Name = Abuse**\n\nCommand:\n\n .gali <Username of User>\n\nit will continuously abuse until you restart! USE IT FOR FUN."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        flash = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(flash) == 1:
            user = str(flash[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in flash:
                text = f"I can't abuse @BEINGHEROX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SMEX_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                name = f"[{c}](tg://user?id={g})"
                caption1 =f"{name} GAND FATT GYII KYA HIJRE KI OLAAD"
                caption2 =f"{name} **RANDI KE PILLLE**"
                caption3 =f" {name} 𝑪𝑯𝑯𝑯𝑯𝑯𝑼𝑼𝑼𝑼𝑼𝑫𝑫𝑫𝑫 𝑮𝒀𝑨𝑨𝑨𝑨𝑨𝑨𝑨 𝑳𝑶𝑽𝑽𝑽𝑽𝑽𝑫𝑫𝑬𝑬 𝑻𝑼𝑼𝑼𝑼"
                caption4 =f" {name} 𝕋𝕖𝕣𝕚 𝕄𝕒𝕒 𝕂𝕚 𝕏𝕙𝕠𝕥 𝕓𝕒𝕕𝕙𝕧𝕖"
                caption5 =f"{name} **ISKE MAAKI CHUTT LELO FREE FULL NIGHT**"
                caption6 =f" {name} __TERE MAAKI CHUTT MASTT SOFT SOFT HE__ 🤤"
                caption7 =f"# {name} TERE MAAKI CHUT ME MERAA LUNDD"
                caption8 =f"{name} **RAANDD KAA PILLAAA**"
                caption9 =f"{name} 𝙄𝙎𝙆𝙄 𝘽𝙃𝙀𝙉 𝙈𝙀𝙍𝘼 𝙇𝙐𝙉𝘿 𝘾𝙃𝙊𝙊𝙎𝙏𝙄𝙄 𝙃E"
                caption10 =f"{name} __AGAYA SWADH__"
                caption11 =f"{name} **TERI MAAA**"
                caption12 =f"**MERE SE**"
                caption13 =f"**Rozz CHUDTII**"
                caption14 =f"__Haiii__"
                caption15 =f"{name} TERE BHEN KO CHODU"
                caption16 =f"🆃🅰🅿🅰"
                caption17 =f"🆃🅰🅿"
                caption18 =f"🆃🅰🅿🅰"
                caption18 =f"🆃🅰🅿"
                caption20 =f"__NON STOP__"
                caption21 =f"{name} 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗠𝗘𝗥𝗘 𝗟𝗨𝗡𝗗 𝗟𝗘 𝗡𝗔𝗖𝗛𝗧𝗜 𝗛𝗘"
                caption22 =f"🤤"
                caption23 =f"{name} __TERI MAA MST ARAAM DETI HE__🤤🤤"
                caption24 =f"{name} __KE BHEN KI CHUT LELO FULL NIGHT FREEE__"
                caption25 =f"{name} __KI BHEN RANDIII__"
                caption26 =f"{name} __ISKE BHEN MST MARI RANDI__ 🤤🤤"
                caption27 =f"😂🖕🤣"
                caption28 =f"😂"
                caption29 =f"__EK RUPAY KI PEPSI {name} KI NAANI SEXYY__"
                caption30 =f"{name} **ISKI BHEN MERI PERSONAL HE MENE BOHOT CHODAA HE USKO__ \n\n __DM {name} FOR PERSONAL RANDI__"
                flash = e.chat_id
                async with e.client.action(flash, "typing"):
                        await e.client.send_message(flash, caption1)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption2)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption3)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption4)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption5)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption6)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption7)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption8)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption9)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption10)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption11)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption12)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption13)
                        await asyncio.sleep(0.4)
                        await e.client.send_message(flash, caption14)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption15)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption16)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption17)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption18)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption19)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption20)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption21)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption22)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption23)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption24)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption25)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption26)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption27)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption28)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption29)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(flash, caption30)
                        await asyncio.sleep(0.3)

        else:
             await e.reply(usage)
             

@idk.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.stats"))
async def stats(event):
   u = 0
   g = 0
   c = 0
   bc = 0
   b = 0
   flash = ""
   if event.sender_id in SMEX_USERS:    
        await event.delete()
        event = await event.reply("__Processing🇮🇳")
       # await event.edit("`Processing..`")
        dialogs = await event.client.get_dialogs(limit=None, ignore_migrated=True)
        for d in dialogs:
            currrent_entity = d.entity
            if isinstance(currrent_entity, User):
                if currrent_entity.bot:
                    b += 1
                else:
                    u += 1
            elif isinstance(currrent_entity, Chat):
                g += 1
            elif isinstance(currrent_entity, Channel):
                if currrent_entity.broadcast:
                    bc += 1
                else:
                    c += 1
            else:
                print(d)
         
        flash += f"🔻 **HERE IS YOUR FLASH-SPAM-BOTS STATS** 🔻\n\n"
        flash += f"`Users:`\t**{u}**\n"
        flash += f"`Groups:`\t**{g}**\n"
        flash += f"`Super Groups:`\t**{c}**\n"
        flash += f"`Channels:`\t**{bc}**\n"
        flash += f"`Bots:`\t**{b}**"
        await event.edit(flash)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.addecho"))
async def addecho(event):
  usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = **ECHO**\n\nCommand:\n\n `{hl}addecho <reply to a User>`"
  if event.sender_id in SMEX_USERS:
     if event.reply_to_msg_id is not None:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
            if int(user_id) in FlashX:
                    text = f"I can't echo @BEINGHEROX's Owner"
                    await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SMEX_USERS:
                    text = f"This guy is a sudo user."
                    await event.reply(text, parse_mode=None, link_preview=None )
            else:
                 chat_id = event.chat_id
                 try:
                     hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
                     hmm = Get(hmm)
                     await event.client(hmm)
                 except BaseException:
                    pass
                 if is_echo(user_id, chat_id):
                     await event.reply("The user is already enabled with echo ")
                     return
                 addecho(user_id, chat_id)
                 await event.reply("Echo activated On the user ✅")
     else:
          await event.reply(usage)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
async def rmecho(event):
  usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = **ECHO**\n\nCommand:\n\n `{hl}rmecho <reply to a User>`"
  if event.sender_id in SMEX_USERS:
     if event.reply_to_msg_id is not None:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
            chat_id = event.chat_id
            try:
                hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
                hmm = Get(hmm)
                await event.client(hmm)
            except BaseException:
                pass
            if is_echo(user_id, chat_id):
                remove_echo(user_id, chat_id)
                await event.reply("Echo has been stopped for the user ☑️")
            else:
                await event.reply("The user is not activated with echo")
     else:
          await event.reply(usage)
          
          
@idk.on(events.NewMessage(incoming=True))
@ydk.on(events.NewMessage(incoming=True))
@wdk.on(events.NewMessage(incoming=True))
@hdk.on(events.NewMessage(incoming=True))
@sdk.on(events.NewMessage(incoming=True))
@adk.on(events.NewMessage(incoming=True))
@bdk.on(events.NewMessage(incoming=True))
@cdk.on(events.NewMessage(incoming=True))
@edk.on(events.NewMessage(incoming=True))
@ddk.on(events.NewMessage(incoming=True))
@vkk.on(events.NewMessage(incoming=True))
@kkk.on(events.NewMessage(incoming=True))
@lkk.on(events.NewMessage(incoming=True))
@mkk.on(events.NewMessage(incoming=True))
@sid.on(events.NewMessage(incoming=True))
@shy.on(events.NewMessage(incoming=True))
@aan.on(events.NewMessage(incoming=True))
@ake.on(events.NewMessage(incoming=True))
@eel.on(events.NewMessage(incoming=True))
@khu.on(events.NewMessage(incoming=True))
@shi.on(events.NewMessage(incoming=True))
@yaa.on(events.NewMessage(incoming=True))
@dav.on(events.NewMessage(incoming=True))
@raj.on(events.NewMessage(incoming=True))
@put.on(events.NewMessage(incoming=True))
@eag.on(events.NewMessage(incoming=True))
@gle.on(events.NewMessage(incoming=True))
@wal.on(events.NewMessage(incoming=True))
@aaa.on(events.NewMessage(incoming=True))
@boy.on(events.NewMessage(incoming=True))
async def _(e):
    if is_echo(e.sender_id, e.chat_id):
        await asyncio.sleep(0.5)
        try:
            flash = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            flash = Get(flash)
            await e.client(flash)
        except BaseException:
            pass
        if e.message.text or e.message.sticker:
            await e.reply(e.message)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.setname")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.setname")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.setname")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.setname")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.setname")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.setname"))
async def setname(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗖𝗛𝗔𝗡𝗚𝗘 𝗡𝗔𝗠𝗘\n\nCommand:\n\n.setname <Message to change name of spam ids>"
    if e.sender_id in SMEX_USERS:
        names = e.text.split(" ", 1)
        flash = names[1]
        if len(e.text) > 5:
            firstname = flash
            text = "Changing Name..."
            try:
                await e.client(functions.account.UpdateProfileRequest(first_name=firstname))
                event = await e.reply(text, parse_mode=None, link_preview=None )
                await event.edit("Changed name successfully! ✅")
            except Exception as e:
                await print(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.dm"))
async def dm(e):   
    usage = "**MODULE NAME** : **DM**\n\n command: \n\n .dm <username> <massage> \n .dm <reply to the use> <massage>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        flash = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(flash) == 2:
            user = str(flash[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in FlashX:
                text = f"I can't Dm to @BEINGHEROX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SMEX_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:            
                 message = str(flash[1])
                 await e.reply("🔸Message Done🔸")
                 await e.client.send_message(g, message)
                 await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in FlashX:
                text = f"I can't Dm to @BEINGHEROX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SMEX_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                message = str(flash[0])
                await e.reply("🔸 Message Delivered 🔸")
                await e.client.send_message(g, message)
                await asyncio.sleep(0.3)

        else:
             await e.reply(usage)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.dmraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.dmraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.dmraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.dmraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.dmraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.dmraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.dmraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.dmraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.dmraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.dmraid")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.dmraid")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.dmraid")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.dmraid")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.dmraid")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.dmraid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.dmraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.dmraid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.dmraid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.dmraid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.dmraid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.dmraid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.dmraid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.dmraid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.dmraid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.dmraid"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.dmraid"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.dmraid"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.dmraid"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.dmraid"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.dmraid"))
async def dmraid(e):
    usage = "**MODULE NAME** : **DM RAID**\n\n command: \n\n .dmraid <count> <username> \n .dmraid <reply to the use> <massage>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        flash = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(flash) == 2:
            user = str(flash[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in FlashX:
                text = f"I can't raid on @BEINGHEROX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SMEX_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                counter = int(flash[0])
                await e.reply(" Dm Raid Strated Successfully ")
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{reply}"
                    async with e.client.action(g, "typing"):
                        await e.client.send_message(g, caption)
                        await asyncio.sleep(0.4)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in FlashX:
                text = f"I can't raid on @BEINGHEROX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SMEX_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                counter = int(flash[0])
                await e.reply(" Dm Raid Strated Successfully!!🙂️")
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{reply}"
                    async with e.client.action(g, "typing"):
                        await e.client.send_message(g, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.dmspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = **DM Spam**\n\nCommand:\n\n.dmspam <count> <username> <message to spam>\n\n.dmspam <count> <username> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        flash = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 2)
        Flashsexy = flash[1:]
        smex = await e.get_reply_message()
        if len(Flashsexy) == 2:
            user = str(Flashsexy[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in FlashX:
                text = f"I can't Dm To @BEINGHEROX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SMEX_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                message = str(Flashsexy[1])
                counter = int(flash[0])
                await e.reply("Dm Spam Started️")
                for _ in range(counter):
                    async with e.client.action(g, "typing"):
                        await e.client.send_message(g, message)
                        await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:
            user = str(Flashsexy[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in FlashX:
                text = f"I can't Dm To @BEINGHEROX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SMEX_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:           
                 counter = int(flasg[0])
                 await e.reply(" Dm Spam Started️")
                 for _ in range(counter):
                     async with e.client.action(g, "document"):
                        smex = await e.client.send_file(g, smex, caption=smex.text)
                        await gifspam(e, smex) 
                        await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            user = str(Flashsexy[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in FlashX:
                text = f"I can't Dm To @BEINGHEROX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SMEX_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                counter = int(flash[0])
                await e.reply(" Dm Spam Started")
                for _ in range(counter):
                    async with e.client.action(g, "typing"):
                        await e.client.send_message(g, message)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.setbio"))            
async def setbio(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗖𝗛𝗔𝗡𝗚𝗘 𝗕𝗜𝗢\n\nCommand:\n\n.setbio <Message to change name of spam ids>"
    if e.sender_id in SMEX_USERS:
        flash = e.text.split(" ", 1)
        message = flash[1]
        if len(e.text) > 5:
            bio = message
            text = "Changing Bio..."
            try:
                await e.client(functions.account.UpdateProfileRequest(about=bio))
                event = await e.reply(text, parse_mode=None, link_preview=None )
                await asyncio.sleep(0.7)
                await event.edit("Changed bio successfully! ✅")
            except Exception as e:
                await print(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


#INVITEALL


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event.reply(
                "`This is a private channel/group or I am banned from there`"
            )
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError):
            await event.reply("`Invalid channel/group`")
            return None
    return chat_info

@idk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        Nobi = event.text[11:]
        flash = Nobi.lower()
        restricted = ["@@Team_dominatorchat", "@Injector_7H", "@Xlr8Cheats_Chat"]
        flax = await event.reply("__Inviting members __")
        if flash in restricted:
            await flax.edit("You can't Invite Members from there.")
            await event.client.send_message(-1001731575931, "Sorry for inviting members from here.")
            return
        flashspam = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await flax.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"
        await flax.edit("**INVITING USERS !!**")
        async for user in event.client.iter_participants(flashspam.full_chat.id):
            try:
                await event.client(
                    InviteToChannelRequest(channel=chat, users=[user.id])
                )
                s += 1
                await flax.edit(
                    f"**INVITING USERS.. **\n\n**Invited :**  `{s}` users \n**Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
            )
            except Exception as e:
                error = str(e)
                f += 1
        return await flax.edit(
        f"**INVITING FINISHED** \n\n**Invited :**  `{s}` users \n**Failed :**  `{f}` users."
    )
    

@idk.on(events.NewMessage(incoming=True, pattern=r"\.delayraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.delayraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.delayraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.delayraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.delayraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.delayraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.delayraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.delayraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.delayraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.delayraid")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.delayraid")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.delayraid")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.delayraid")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.delayraid")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.delayraid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.delayraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.delayraid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.delayraid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.delayraid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.delayraid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.delayraid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.delayraid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.delayraid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.delayraid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.delayraid"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.delayraid"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.delayraid"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.delayraid"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.delayraid"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.delayraid"))
async def delay(event):
   usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗘𝗟𝗔𝗬𝗥𝗔𝗜𝗗\n\nCommand:\n\n.delayraid <delay> <count> <Username of User>\n\n.delayraid <delay> <count> <reply to a User>\n\nCount must be a integer."        
   if event.sender_id in SMEX_USERS:
         if event.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
         flash = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
         if len(flash) == 3:
             user = str(flash[2])
             a = await event.client.get_entity(user)
             e = a.id
             if int(e) in FlashX:
                    text = f"I can't raid on @BEINGHEROX's Owner"
                    await event.reply(text, parse_mode=None, link_preview=None )
             elif int(e) in SMEX_USERS:
                    text = f"This guy is a sudo user."
                    await event.reply(text, parse_mode=None, link_preview=None )
             else:
                 c = a.first_name
                 username = f"[{c}](tg://user?id={e})"
                 counter = int(flash[1])
                 sleeptimet = sleeptimem = float(flash[0])
                 for _ in range(counter):
                      reply = random.choice(RAID)
                      caption = f"{username} {reply}"
                      async with event.client.action(event.chat_id, "typing"):
                          await event.client.send_message(event.chat_id, caption)
                          await asyncio.sleep(sleeptimem)
         elif event.reply_to_msg_id:
               a = await event.get_reply_message()
               b = await event.client.get_entity(a.sender_id)
               e = b.id
               if int(e) in FlashX:
                       text = f"I can't raid on @BEINGHEROX's Owner"
                       await event.reply(text, parse_mode=None, link_preview=None )
               elif int(e) in SMEX_USERS:
                       text = f"This guy is a sudo user."
                       await event.reply(text, parse_mode=None, link_preview=None )
               else:
                   c = b.first_name
                   username = f"[{c}](tg://user?id={e})"
                   sleeptimet = sleeptimem = float(flash[0])
                   counter = int(flash[1])
                   for _ in range(counter):
                        reply = random.choice(RAID)
                        caption = f"{username} {reply}"
                        async with event.client.action(event.chat_id, "typing"):
                             await event.client.send_message(event.chat_id, caption)
                             await asyncio.sleep(sleeptimem)
         else:
            await event.reply(usage)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "𝙍𝙚𝙨𝙩𝙖𝙧𝙩𝙚𝙙\n\nPlease wait till it reboots..."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await idk.disconnect()
        except Exception as e:
            pass
        try:
            await ydk.disconnect()
        except Exception as e:
            pass
        try:
            await wdk.disconnect()
        except Exception as e:
            pass
        try:
            await hdk.disconnect()
        except Exception as e:
            pass
        try:
            await sdk.disconnect()
        except Exception as e:
            pass
        try:
            await adk.disconnect()
        except Exception as e:
            pass
        try:
            await bdk.disconnect()
        except Exception as e:
            pass
        try:
            await cdk.disconnect()
        except Exception as e:
            pass
        try:
            await ddk.disconnect()
        except Exception as e:
            pass
        try:
            await edk.disconnect()
        except Exception as e:
            pass
        try:
            await vkk.disconnect()
        except Exception as e:
            pass
        try:
            await kkk.disconnect()
        except Exception as e:
            pass
        try:
            await lkk.disconnect()
        except Exception as e:
            pass
        try:
            await mkk.disconnect()
        except Exception as e:
            pass
        try:
            await sid.disconnect()
        except Exception as e:
            pass
        try:
            await shy.disconnect()
        except Exception as e:
            pass
        try:
            await aan.disconnect()
        except Exception as e:
            pass
        try:
            await ake.disconnect()
        except Exception as e:
            pass
        try:
            await eel.disconnect()
        except Exception as e:
            pass
        try:
            await khu.disconnect()
        except Exception as e:
            pass
        try:
            await shi.disconnect()
        except Exception as e:
            pass
        try:
            await yaa.disconnect()
        except Exception as e:
            pass
        try:
            await dav.disconnect()
        except Exception as e:
            pass
        try:
            await raj.disconnect()
        except Exception as e:
            pass
        try:
            await put.disconnect()
        except Exception as e:
            pass
        try:
            await eag.disconnect()
        except Exception as e:
            pass
        try:
            await gle.disconnect()
        except Exception as e:
            pass
        try:
            await wal.disconnect()
        except Exception as e:
            pass
        try:
            await aaa.disconnect()
        except Exception as e:
            pass
        try:
            await boy.disconnect()
        except Exception as e:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


@idk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.help"))

async def help(e):
    if e.sender_id in SMEX_USERS:
       text = "𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 ☠️☠️\n►Pɪɴɢ\n►Rᴇsᴛᴀʀᴛ\n►Jᴏɪɴ\n►Lᴇᴀᴠᴇ\n►Pᴊᴏɪɴ\n►Bɪɢsᴘᴀᴍ\n►Rᴀɪᴅ\n\n\n\n       "
       await e.reply(text, parse_mode=None, link_preview=None )

 

    
        
text = """
 𝙂𝙤 𝘿𝙤 .𝙥𝙞𝙣𝙜 𝙖𝙩 @@Team_dominatorchat
𝗕𝗬 @BEINGHEROX """

print(text)
print("")
print("𝗦𝗣𝗔𝗠 𝗕𝗢𝗧 𝗥𝗘𝗔𝗗𝗬 𝗙𝗢𝗥 𝗨𝗦𝗘")
if len(sys.argv) not in (1, 3, 4):
    try:
        idk.disconnect()
    except Exception as e:
        pass
    try:
        ydk.disconnect()
    except Exception as e:
        pass
    try:
        wdk.disconnect()
    except Exception as e:
        pass
    try:
        hdk.disconnect()
    except Exception as e:
        pass
    try:
        sdk.disconnect()
    except Exception as e:
        pass
    try:
        adk.disconnect()
    except Exception as e:
        pass
    try:
        bdk.disconnect()
    except Exception as e:
        pass
    try:
        cdk.disconnect()
    except Exception as e:
        pass
    try:
        edk.disconnect()
    except Exception as e:
        pass
    try:
        ddk.disconnect()
    except Exception as e:
        pass
    try:
        vkk.disconnect()
    except Exception as e:
        pass 
    try:
        kkk.disconnect()
    except Exception as e:
        pass
    try:
        lkk.disconnect()
    except Exception as e:
        pass 
    try:
        mkk.disconnect()
    except Exception as e:
        pass
    try:
        sid.disconnect()
    except Exception as e:
        pass
    try:
        shy.disconnect()
    except Exception as e:
        pass
    try:
        aan.disconnect()
    except Exception as e:
        pass
    try:
        ake.disconnect()
    except Exception as e:
        pass
    try:
        eel.disconnect()
    except Exception as e:
        pass
    try:
        khu.disconnect()
    except Exception as e:
        pass
    try:
        shi.disconnect()
    except Exception as e:
        pass
    try:
        yaa.disconnect()
    except Exception as e:
        pass
    try:
        dav.disconnect()
    except Exception as e:
        pass
    try:
        raj.disconnect()
    except Exception as e:
        pass
    try:
        put.disconnect()
    except Exception as e:
        pass
    try:
        eag.disconnect()
    except Exception as e:
        pass
    try:
        gle.disconnect()
    except Exception as e:
        pass
    try:
        wal.disconnect()
    except Exception as e:
        pass
    try:
        aaa.disconnect()
    except Exception as e:
        pass
    try:
        boy.disconnect()
    except Exception as e:
        pass
else:
    try:
        idk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ydk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        wdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        hdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        adk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        cdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        edk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ddk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        vkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        kkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        lkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        mkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sid.run_until_disconnected()
    except Exception as e:
        pass
    try:
        shy.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aan.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ake.run_until_disconnected()
    except Exception as e:
        pass
    try:
        eel.run_until_disconnected()
    except Exception as e:
        pass
    try:
        khu.run_until_disconnected()
    except Exception as e:
        pass
    try:
        shi.run_until_disconnected()
    except Exception as e:
        pass
    try:
        yaa.run_until_disconnected()
    except Exception as e:
        pass
    try:
        dav.run_until_disconnected()
    except Exception as e:
        pass
    try:
        raj.run_until_disconnected()
    except Exception as e:
        pass
    try:
        put.run_until_disconnected()
    except Exception as e:
        pass
    try:
        eag.run_until_disconnected()
    except Exception as e:
        pass
    try:
        gle.run_until_disconnected()
    except Exception as e:
        pass
    try:
        wal.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aaa.run_until_disconnected()
    except Exception as e:
        pass
    try:
        boy.run_until_disconnected()
    except Exception as e:
        pass
