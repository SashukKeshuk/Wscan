import time
import pymysql
from config import HOST, DB_NAME, USR_PSWD, USR_NAME
def connect():
    conn = None
    try:
        conn = pymysql.connect(
            host=HOST,
            user=USR_NAME,
            passwd=USR_PSWD,
            database=DB_NAME
        )
        print("Connected")
    except Error as e:
        print(f"Conn error\t'{e}'")
    return conn

global conn
conn = connect()

def exec(conn, query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
        print("+\n")
    except Error as e:
        print(f"Execution error '{e}'")

def add_user(uid):
    create_users = f"INSERT INTO users (uid) VALUES ({str(uid)});"
    exec(conn, create_users)
    
def is_user(uid):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE uid={str(uid)};")
    iusr = cursor.fetchall()
    if (str(iusr) == '()'):
        return 0
    return 1

def topup(uid, m):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE uid={str(uid)};")
    usr = cursor.fetchall()
    if usr[0][1] < int(time.time()):
        date = m * 2592000 + int(time.time())
        buy_str = f"UPDATE users SET exp_date={str(date)} WHERE uid={str(uid)};"
    else:
        date = time_sub * 2592000 + usr[0][1]
        buy_str = f"UPDATE users SET exp_date={str(date)} WHERE uid={str(uid)};"
    exec(conn, buy_str)

def get_servs(uid):
    with conn.cursor() as cur:
        cur.execute(f"SELECT * FROM users WHERE uid={str(uid)}")
        usr = cur.fetchall()
        lst = usr[0][2].split(' ')
    return lst

def is_serv(uid, serv):
    with conn.cursor() as cur:
        cur.execute(f"SELECT * FROM users WHERE uid={str(uid)}")
        usr = cur.fetchall()
        lst = usr[0][2].split(' ')
    for ser in lst:
        if (ser == serv):
            return 1
    return 0

def toggle_serv(uid, serv):
    if (is_serv(uid, serv) == 1):
        Lst = ""
        lst = get_servs(uid)
        for ser in lst:
            if (ser != serv):
                Lst = Lst + ser + " "
        Lst = Lst[:-1]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE users SET servs='{Lst}' WHERE uid={str(uid)}")
            conn.commit()
    else:
        Lst = ""
        lst = get_servs(uid)
        for ser in lst:
            Lst = Lst + ser + " "
        Lst = Lst + serv
        with conn.cursor() as cur:
            cur.execute(f"UPDATE users SET servs='{Lst}' WHERE uid={str(uid)}")
            conn.commit()

def get_exp(uid):
    with conn.cursor() as cur:
        cur.execute(f"SELECT * FROM users WHERE uid={str(uid)}")
        data = cur.fetchall()
    return data[0][1]