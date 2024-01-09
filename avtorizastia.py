import pygame
import sys
from batton import *
import sqlite3
import os


def vhodifadm(login, parol):
    connection = sqlite3.connect('plaeyrs.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS player(
    id INT PRIMARY KEY,
    name TEXT,
    parol TEXT,
    activ TEXT,
    icon TEXT,
    slova TEXT);
    ''')
    le = len(cursor.execute("""SELECT name FROM player""").fetchall())
    Flag1 = False
    cursor.execute("UPDATE player SET activ = '0'")
    if login != '':
        if parol != '':
            lew = len(cursor.execute("""SELECT name FROM player""").fetchall())
            # если пароля и логина нет в базе даных то добавить
            s = [i[0] for i in cursor.execute("""SELECT name, parol FROM player""").fetchall()]
            # print(s, login)
            if (login, parol) not in s:
                cursor.execute('INSERT INTO player(ID, name, parol, activ, icon, slova) VALUES (?, ?, ?, ?, ?, ?)',
                               (lew + 1, str(login), str(parol), '1', 'res/FlareMaleHero3.png', 'res/Муж голос добыча.mp3'))
                connection.commit()
            cursor.execute("UPDATE player SET  activ = '1'  WHERE name=? AND parol=?;",
                           (login, parol))
            connection.commit()
            connection.close()
            return True, login
        else:
            return False, 'Введите пароль длинной от 1 символа'
    else:
        return False, 'Введите логин длинной от 1 символа'

def scina():
    connection = sqlite3.connect('plaeyrs.db')
    cursor = connection.cursor()
    s = [i for i in cursor.execute("""SELECT icon, slova FROM player WHERE activ = '1'""").fetchall()]
    # print(s)
    connection.close()
    return s[0]

def update(icon, slova):
    connection = sqlite3.connect('plaeyrs.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE player SET  icon = ?  WHERE activ = '1';",
                   (icon,))
    cursor.execute("UPDATE player SET slova = ?  WHERE activ = '1';",
                   (slova,))
    connection.commit()
    connection.close()





