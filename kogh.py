from os import system
import requests, threading, colorama, discord, time, re, http.client, random, json
from requests import get
import string
from colorama import Fore
import emoji as ej
import asyncio
from bs4 import BeautifulSoup
from PIL import Image
from pystyle import Colors, Colorate


from sys import stdout
from json import dumps, loads
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile, isdir
from py_compile import compile
from os import listdir, mkdir, remove, rmdir, rename, chdir, name
from shutil import move, copy, rmtree
from time import sleep
from binascii import hexlify
from colorama import Fore
from tqdm import tqdm, trange
from time import sleep
import os, websocket
from websocket import WebSocket
from concurrent.futures import ThreadPoolExecutor
from operator import truediv
from httpx import Client
from httpx_socks import SyncProxyTransport
from requests import get
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from subprocess import check_output
import httpx
import tkinter as tk
from tkinter import messagebox
import requests
import time

def LOGIN_MAIN():
    print("FLEXZY TOKEN TOOL")
    print("")
    
    while True:
        system = input("𝗞𝗘𝗬 : ")
        print("")
        response = requests.get("https://pastebin.com/raw/BDMdLpVr") # ใส่ link pastebin
        if response.status_code == 200:
            valid_keys = response.text.strip().split("\n")
            if system in valid_keys:
                print("Login Successful!!")
                time.sleep(1)
                # ใส่โค้ดฟังชั่นหลักของคุณ
                break  # ออกจากลูปเมื่อรหัสถูกต้อง
            else:
                print("Wrong Key")
        else:
            print("Wrong Key")

LOGIN_MAIN()


banner = r"""

                                     SHOP > https://discord.gg/2ZJwyxAE

         ,  . .,  °           , ·. ,.-·~·.,   ‘           , ·. ,.-·~·.,   ‘             ,.  '       
   ;'´    ,   ., _';\'        /  ·'´,.-·-.,   `,'‚          /  ·'´,.-·-.,   `,'‚           /   ';\       
   \:´¨¯:;'   `;::'\:'\      /  .'´\:::::::'\   '\ °       /  .'´\:::::::'\   '\ °       ,'   ,'::'\      
     \::::;   ,'::_'\;'   ,·'  ,'::::\:;:-·-:';  ';\‚    ,·'  ,'::::\:;:-·-:';  ';\‚      ,'    ;:::';'     
         ,'  ,'::;'  ‘    ;.   ';:::;´       ,'  ,':'\‚  ;.   ';:::;´       ,'  ,':'\‚     ';   ,':::;'      
         ;  ;:::;  °     ';   ;::;       ,'´ .'´\::';‚  ';   ;::;       ,'´ .'´\::';‚    ;  ,':::;' '      
         ;  ;::;'  ‘      ';   ':;:   ,.·´,.·´::::\;'°  ';   ':;:   ,.·´,.·´::::\;'°   ,'  ,'::;'         
         ;  ;::;'‚         \·,   `*´,.·'´::::::;·´      \·,   `*´,.·'´::::::;·´      ;  ';_:,.-·´';\‘  
         ',.'\::;'‚          \\:¯::\:::::::;:·´          \\:¯::\:::::::;:·´         ',   _,.-·'´:\:\‘ 
          \::\:;'‚           `\:::::\;::·'´  °            `\:::::\;::·'´  °           \¨:::::::::::\'; 
           \;:'      ‘           ¯                           ¯                       '\;::_;:-·'´‘   
             °                   ‘                            ‘                         '¨         

                                            PLS ENTER TO START
                                
"""[1:]



def rb(text):
        return (Colorate.Horizontal(Colors.rainbow,text))

System.Size(140, 45) 

Anime.Fade(Center.Center(banner), Colors.red_to_green, Colorate.Vertical, enter=True)





ur = 'https://discord.com/api/v10/channels/messages'
title = '                  TOKEN TOOL                  Running'
system(f'title {title}')
tokens = open('tokens.txt', 'r').read().splitlines()
  
def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]

    return text


def mainHeader(token):
    return {
        "authorization": token,
        "accept": "*/*",
        'accept-encoding': 'gzip, deflate, br',
        "accept-language": "en-GB",
        "content-length": "90",
        "content-type": "application/json",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }

def secondHeader(token):
    return {
        ':authority': 'discord.com',
        ':method': 'PATCH',
        ':path': '/api/v9/users/@me',
        ':scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US',
        'authorization': token,
        'content-length': '124',
        'content-type': 'application/json',
        'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        'origin': 'https://canary.discord.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.616 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MTYiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjQ1OCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5ODgyMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='}



counttokens = len(open('tokens.txt').readlines())

def spammer():
    asc = asyncio.get_event_loop()
    tokens = open('tokens.txt', 'r').read().splitlines()
    counttokens = len(open('tokens.txt').readlines())
    clear = lambda: os.system('cls')
    clear()
    
    
    
    

    colorama.init()
    System.Size(100, 30) 
    print('')
    print('')
    print(f"""{Fore.LIGHTCYAN_EX}
    ________    _______  _________  __
   / ____/ /   / ____/ |/ /__  /\ \/ /
  / /_  / /   / __/  |   /  / /  \  / 
 / __/ / /___/ /___ /   |  / /__ / /  
/_/   /_____/_____//_/|_| /____//_/     
                                                             
║ 1  Joiner           | MAKE TOKEN JOIN SERVER.                
║ 2  Leaver           | MAKE TOKEN Leave SERVER.             
║ 3  Spammer          | MAKE TOKEN Spam message.        \n""")

    
   
            

    choice = input('\x1B[1m[-->]\x1B[1m ')


    
    if choice == '1':

        http.client._is_legal_header_name = re.compile(
            rb'[^\s][^:\r\n]*').fullmatch


        __tokens__ = (open('tokens.txt', 'r+').read().splitlines())
        __max_thread__ = 50
        def join(token, invite):
            r = httpx.post(f'https://discord.com/api/v9/invites/{invite}', headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
                    'Accept': '*/*',
                    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Content-Type': 'application/json',
                    'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
                    'Authorization': token,
                    'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
                    'X-Discord-Locale': 'en-US',
                    'X-Debug-Options': 'bugReporterEnabled',
                    'Origin': 'https://discord.com',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    'Referer': 'https://discord.com',
                    'Cookie': '__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'TE': 'trailers',
                }, json={})
            
            if r.status_code == 200:
                print(f'{Fore.GREEN}                                 [>] {token[:30]}******** | Done {Fore.RESET}')
            else:
                print(f'{Fore.RED}                                 [!] {token[:30]}******** | Error... {Fore.RESET}')

        __invite_code__ = input("                                 Invite code (ex. nz8jkMVH) : ")

        for token in __tokens__:
            while threading.active_count() >= __max_thread__:
                time.sleep(1)
            threading.Thread(target=join, args=[token, __invite_code__]).start()

        print(f'{Fore.LIGHTCYAN_EX}')
        time.sleep(3)
        b = input(f'{Fore.LIGHTCYAN_EX} [>] Do you want to bypass member screening y or n?: ')

        if b == 'y':
            def bpss(__invite_code__, serverId, token):
                headers = {
                    'Content-Type': 'application/json',
                    'Accept': '*/*',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'en-US',
                    'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                    'DNT': '1',
                    'origin': 'https://discord.com',
                    'TE': 'Trailers',
                    'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                    'authorization': token,
                    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
                bpsur = f"https://discord.com/api/v10/guilds/{serverId}/member-verification?with_guild=false&invite_code=" + __invite_code__
                r1 = requests.get(bpsur, headers=headers).json()
                data = {}
                data['version'] = r1['version']
                data['form_fields'] = r1['form_fields']
                data['form_fields'][0]['response'] = True
                req = f"https://discord.com/api/v10/guilds/{str(serverId)}/requests/@me"
                requests.put(req, headers=headers, json=data)

            serverId = input('Server ID: ')
            tokens = open('tokens.txt', 'r').read().splitlines()
            for token in tokens:
                threading.Thread(target=bpss, args=(__invite_code__, serverId, token)).start()
                print(f'{Fore.LIGHTCYAN_EX}[>] {token} {Fore.LIGHTCYAN_EX} Done')

        elif b == 'n':
            pass

        print(f'{Fore.LIGHTCYAN_EX}[>]{Fore.LIGHTCYAN_EX} Done')

        time.sleep(1)
        exit = input(f'[>] Press Enter: ')
        exit = clear()
        exit = spammer()


    if choice == '2':
        token = open("tokens.txt", "r").read().splitlines()

        ID = input(f'{Fore.LIGHTCYAN_EX} [!] Server ID : ')

        apilink = "https://discord.com/api/v10/users/@me/guilds/" + str(ID)

        with open('tokens.txt', 'r') as handle:
            tokens = handle.readlines()
            for i in tokens:
                token = i.rstrip()
                headers = {
                    'Authorization': token,
                    "content-length": "0",
                    "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                    "origin": "https://discord.com",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                    "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                    "x-debug-options": "bugReporterEnabled",
                    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="

                }
                requests.delete(apilink, headers=headers)
            print(f'{Fore.LIGHTCYAN_EX}[!]{Fore.LIGHTCYAN_EX} Done')

        time.sleep(1)
        exit = input(f'[>] Press Enter: ')
        exit = clear()
        exit = spammer()

    if choice == '3':
        print(f"""{Fore.LIGHTCYAN_EX}{Fore.LIGHTCYAN_EX}[!] Recommendation: Check the token before use And make sure you have token in tokens.txt!""")
        tokens = open("tokens.txt", "r").read().splitlines()
        server = input(f'[!] Server ID: ')
        channel = input(f'[!] Channel ID: ')
        mess = input(f'[!] Message: ')
        delay = float(input(f'[!] Delay : '))
        ch = input('[!] Bypass anti spam y/n? : ').lower()



        def spam(token, mess):
            pass

            if ch == 'y':
                mess += " | " + "".join(random.choices(string.ascii_lowercase + string.digits, k=5))

            elif ch == 'n':
                pass

            else:
                pass

            url = 'https://discord.com/api/v10/channels/' + channel + '/messages'
            payload = {"content": mess, "tts": False}
            header = mainHeader(token)

            while True:
                time.sleep(delay)
                src = requests.post(url, headers=header, json=payload)

                if src.status_code == 429:
                    ratelimit = json.loads(src.content)
                    print(f"{Fore.LIGHTRED_EX}[!]{Fore.LIGHTRED_EX} Ratelimit for",
                          str(float(ratelimit['retry_after'])) + " seconds")
                    time.sleep(float(ratelimit['retry_after']))

                elif src.status_code == 200:
                    time.sleep(delay)
                    print(f'{Fore.LIGHTCYAN_EX}[>] {token} {Fore.LIGHTCYAN_EX} Sent {mess} !')

                elif src.status_code == 401:
                    time.sleep(delay)
                    print(f'{Fore.LIGHTRED_EX}[!]{Fore.LIGHTRED_EX} Invalid Token')
                elif src.status_code == 404:
                    time.sleep(delay)
                    print(f'{Fore.LIGHTRED_EX}[!]{Fore.LIGHTRED_EX} Not Found...')
                elif src.status_code == 403:
                    time.sleep(delay)
                    print(f'{Fore.LIGHTRED_EX}[!]{Fore.LIGHTRED_EX} Token Doesnt Have Perms For This Channel...')

        def thread():
            text = mess
            for token in tokens:
                threading.Thread(target=spam, args=(token, text)).start()

        start = input(f'[!] Press Enter To Start: ')
        start = thread()

        time.sleep(5)
        exit = input(f'[!]  Press Enter To Start: ')
        clear()
        exit = spammer()


spammer()