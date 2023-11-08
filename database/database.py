"""Database sqlite3 for Telegram Bot"""
import asyncio
import sqlite3

con = sqlite3.connect("database/bot.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS catalogs
            (id_catalog INTEGER, category TEXT, brand TEXT, image TEXT,
            name TEXT, price REAL, count INTEGER)""")
con.commit()

async def insert_catalogs(mas_goods: list):
    """Function inserts goods to table catalogs"""
    cur.execute("DELETE FROM catalogs")
    con.commit()

    index = 1
    for goods in mas_goods:
        insert_query = f"""INSERT INTO catalogs VALUES
                    ({index}, "{goods['Категория']}", "{goods['Подкатегория']}", "{goods['Картинка']}",
                    "{goods['Название']}", {goods['Цена']}, {goods['Кол-во']})"""
        cur.execute(insert_query)
        con.commit()
        index += 1
