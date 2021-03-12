import sqlite3

def CreateDB():
    name_db = "db_notes.db"
    try:
       conn = sqlite3.connect(name_db)
       return conn
    except sqlite3.Error:
        print("Ошибка подключения")

querryIn = '''INSERT INTO Notes (id_users, message)VALUES ( ?, ?)'''
querryOut = '''SELECT message FROM Notes WHERE id_users = ?'''
querryCheck = '''SELECT id_users FROM Notes WHERE id_users = ?'''
querryUpdate = '''UPDATE Notes SET message = ? WHERE id_users = ?'''

def AddText(id_user, text):
    conn = CreateDB()
    cursor = conn.cursor()
    cursor.execute(querryCheck, [id_user, ])
    check = cursor.fetchall()
    conn.commit()
    if len(check) > 0:
        cursor.execute(querryUpdate, (text, id_user))
        #print("Обновлено")
    else:
        cursor.execute(querryIn, (id_user, text))
        #print("Добавлено")
    conn.commit()
    conn.close()


def PrintText(id_user):
    conn = CreateDB()
    cursor = conn.cursor()
    cursor.execute(querryOut, [id_user,])
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return result
