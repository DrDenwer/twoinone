from telethon import *
import random
import logging
from .. import loader, utils
import asyncio

logger = logging.getLogger(__name__)



class YourMod(loader.Module):
    """Description for module"""  # Translateable due to @loader.tds
    strings = {"name": "l+s"}



   
    async def scwcmd(self,event):
        await event.delete()
        
        
        a=0
        while a<11:

            await event.respond("🕹 Действия")
            await asyncio.sleep(1)  
            await event.respond("👮 Патрулируем")

            await asyncio.sleep(621)  
            a+=1

    async def lcwcmd(self,event):
        await event.delete()
        
        
        a=0
        while a<19:

            await event.respond("🕹 Действия")
            await asyncio.sleep(1)  
            await event.respond("🚑 Лечим")

            await asyncio.sleep(361)  
            a+=1

            