import pygame
import sys
from batton import *
import sqlite3
import os

connection = sqlite3.connect('plaeyrs.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS player(
    id INT PRIMARY KEY,
    name TEXT,
    parol TEXT,
    activ TEXT);
    ''')
le = len(cursor.execute("""SELECT name FROM player""").fetchall())

Flag1 = False

def vhodifadm(login, parol):
    if login != '':
        if parol != '':
            lew = len(cursor.execute("""SELECT name FROM player""").fetchall())
            # если пароля и логина нет в базе даных то добавить
            s = [i[0] for i in cursor.execute("""SELECT name, parol FROM player""").fetchall()]

            print(s, login)
            if login not in s:
                t = [cursor.execute("UPDATE player SET activ = '0'  WHERE name=?;", (i,)) for i in s]
                cursor.execute('INSERT INTO player(ID, name, parol, activ) VALUES (?, ?, ?, ?)',
                               (lew + 1, login, parol, '1'))
            cursor.execute("UPDATE player SET  activ = '1'  WHERE name=? AND parol=?;",
                           (login, parol))
            connection.commit()
            connection.close()
            return True, login
        else:
            return False, 'Введите пароль длинной от 1 символа'
    else:
        return False, 'Введите логин длинной от 1 символа'





