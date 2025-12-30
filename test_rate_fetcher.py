'''
test_fetch_rate_success - Mock successful API response
test_fetch_rate_timeout - Mock timeout error
test_fetch_rate_bad_status - Mock 500 status code
test_fetch_rate_network_error - Mock ClientError
'''
from rate_fetcher import fetch_rate , fetch_all_rates
import aiohttp
import asyncio
from aioresponses import aioresponses
import pytest

@pytest.mark.asyncio
async def test_fetch_rate_success():
    with aioresponses() as mock:
        fake_response = ({'base_code' : 'API' , 'conversion_rates' : {'USD' : 12}})
        mock.get('https://v6.exchangerate-api.com/v6/d12f49aa69b7d0b8c53ec0d9/latest/API', payload = fake_response)
        async with aiohttp.ClientSession() as session:
            response = await fetch_rate(session , 'API')
            assert response == fake_response
            
            
@pytest.mark.asyncio
async def test_fetch_rate_timeout():
    with aioresponses() as mock:
        fake_response = ({'base_code' : 'API' , 'conversion_rates' : {'USD' : 12}})
        mock.get('https://v6.exchangerate-api.com/v6/d12f49aa69b7d0b8c53ec0d9/latest/API', exception = asyncio.TimeoutError)
        async with aiohttp.ClientSession() as session:
            response = await fetch_rate(session , 'API')
            assert response is None
@pytest.mark.asyncio
async def test_fetch_rate_network_error():
    with aioresponses() as mock:
        fake_response = ({'base_code' : 'API' , 'conversion_rates' : {'USD' : 12}})
        mock.get('https://v6.exchangerate-api.com/v6/d12f49aa69b7d0b8c53ec0d9/latest/API', exception = aiohttp.ClientError)
        async with aiohttp.ClientSession() as session:
            response = await fetch_rate(session , 'API')
            assert response is None
@pytest.mark.asyncio
async def test_fetch_rate_bad_status():
    with aioresponses() as mock:
        fake_response = ({'base_code' : 'API' , 'conversion_rates' : {'USD' : 12}})
        mock.get('https://v6.exchangerate-api.com/v6/d12f49aa69b7d0b8c53ec0d9/latest/API', payload = fake_response , status = 404)
        async with aiohttp.ClientSession() as session:
            response = await fetch_rate(session , 'API')
            assert response is None 
