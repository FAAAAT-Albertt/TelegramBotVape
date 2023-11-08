"""This file downloads any info from Google Table to the DataBase"""
import asyncio
import gspread
import database as base


async def get_goods():
    """Function insert goods to database"""
    gc = gspread.service_account(filename='database/credentials.json')
    wks = gc.open("TG_BOT")
    list_google = wks.worksheet("Товары").get_all_records()
    list_google = await prepare_price(list_google)
    await base.insert_catalogs(list_google) 

async def prepare_price(list_google: list):
    """Function prepare price"""
    index = 0
    for row in list_google:
        price = str(row['Цена']).replace('\xa0', '').replace(',', '')
        list_google[index]['Цена'] = float(price[:-2] + '.' + price[-2:])
        index += 1
    return list_google

if __name__ == "__main__":
    asyncio.run(get_goods())
