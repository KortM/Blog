from http.client import NotConnected
from aiohttp import web
import aiohttp_jinja2 as ji

@ji.template('index.html')
async def index(request):
    return None