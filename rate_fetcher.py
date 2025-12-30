import aiohttp
import asyncio
from database import CurrencyDatabase
from datetime import datetime

async def fetch_rate(session , currency):
    url = f"https://v6.exchangerate-api.com/v6/d12f49aa69b7d0b8c53ec0d9/latest/{currency}"
    try:
        async with session.get(url) as response:
            if response.status != 200:
                print(f"Status is not 200!")
                return None
            
            data = await response.json()
            return data
    except asyncio.TimeoutError:
        print("Timeout error.")
        return None
    except aiohttp.ClientError as e:
        print(f"Error : {e}")
        return None

async def fetch_all_rates():
    currencies = ['EUR', 'GBP', 'JPY', 'INR', 'CAD']
    timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        a = [fetch_rate(session , currency) for currency in currencies]
        result = await asyncio.gather(*a)
        
        with CurrencyDatabase("CurrencyCache.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS cache(
                               currency TEXT,
                               rate REAL,
                               timestamp TEXT
                               )
                           """)
            for i in result:
                if i is not None:
                    cursor.execute("""
                                   INSERT INTO cache(currency,rate,timestamp)
                                   VALUES (?,?,?)
                                   """,(i['base_code'], 1 / i['conversion_rates']['USD'] , datetime.now().strftime("%d/%m/%Y, %H:%M:%S")))
            conn.commit()
    return result




if __name__ == '__main__':
    asyncio.run(fetch_all_rates())

