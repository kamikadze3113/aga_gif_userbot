import asyncio
from .. import loader
import random
import time


@loader.tds
class АгаMod(loader.Module):
	strings = {"name": "Ага"}
	async def агаcmd(self, message):
		await message.edit("Ищу...")
		time.sleep(3)
		GIF = ["https://i.gifer.com/73H4.gif", "https://i.gifer.com/TfGF.gif", "https://i.gifer.com/Okak.gif", "https://i.gifer.com/7DSA.gif"]
		await message.send(random.choice(GIF))