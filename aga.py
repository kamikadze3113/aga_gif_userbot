#create kamikadze3113
#thanks @dashaushakova
#go to the https://t.me/friendlytgbot_ru / @friendlytgbot_ru
import asyncio
from .. import loader
import random
import time


@loader.tds
class АгаMod(loader.Module):
	strings = {"name": "Ага"}
	async def агаcmd(self, message):
		await message.edit("Ищу...")
		time.sleep(1)
		await message.delete()
		GIF = ["https://i.gifer.com/73H4.gif", "https://i.gifer.com/TfGF.gif", "https://i.gifer.com/Okak.gif", "https://i.gifer.com/7DSA.gif"]
		await message.client.send_file(message.to_id, random.choice(GIF))