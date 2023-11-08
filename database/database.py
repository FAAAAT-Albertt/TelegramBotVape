"""Database sqlite3 for Telegram Bot"""
import asyncio
import sqlite3
import json

con = sqlite3.connect("database/bot.db")
#con.row_factory = sqlite3.Row 
con.row_factory = lambda C, R: { c[0]: R[i] for i, c in enumerate(C.description) }
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS catalogs
            (id_catalog INTEGER, category TEXT, brand TEXT, image TEXT,
            name TEXT, price REAL, count INTEGER)""")
con.commit()

async def insert_catalogs(mas_goods: list) -> None:
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

async def get_unique_categories() -> dict:
    """Reterns unique categories"""
    select_query = "SELECT DISTINCT category FROM catalogs"
    return cur.execute(select_query).fetchall()


if __name__ == "__main__":
    asyncio.run(get_unique_categories())
