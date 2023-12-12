from config import CMS, LST
from db import get_servs
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, web_app_info

subscribe_mrkp = InlineKeyboardMarkup()
mon1 = InlineKeyboardButton('1 месяц - 10$', callback_data='mon1')
mon3 = InlineKeyboardButton('3 месяца - 25$', callback_data='mon3')
mon6 = InlineKeyboardButton('6 месяцев - 40$', callback_data='mon6')
mon12 = InlineKeyboardButton('12 месяцев - 70$', callback_data='mon12')

subscribe_mrkp.add(mon1).add(mon3).add(mon6).add(mon12)

check_mrkp = InlineKeyboardMarkup()
chck = InlineKeyboardButton('Проверить', callback_data='chck')
check_mrkp.add(chck)

def gen_chs(uid):
    chs_mrkp = InlineKeyboardMarkup()
    lst = get_servs(uid)
    i = 0
    for serv in LST:
        i += 1
        f = 0
        for act in lst:
            if (act == serv):
                f = 1
        if (f == 1):
            if (i == 6 or i == 11 or i == 16 or i == 21):
                chs_mrkp.add(InlineKeyboardButton(serv + ' ✓', callback_data=f"serv_{serv}"))
            else:
                chs_mrkp.insert(InlineKeyboardButton(serv + ' ✓', callback_data=f"serv_{serv}"))
        else:
            if (i == 6 or i == 11 or i == 16 or i == 21):
                chs_mrkp.add(InlineKeyboardButton(serv, callback_data=f"serv_{serv}"))
            else:
                chs_mrkp.insert(InlineKeyboardButton(serv, callback_data=f"serv_{serv}"))
    return chs_mrkp