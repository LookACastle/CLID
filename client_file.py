# -*- coding: utf-8 -*-
import discord
import asyncio, sys
import discord

class client(discord.Client):
	def __init__(self, token, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.token = token
	
	async def login(self):
		await super().login(self.token, bot=False)
	
	async def connect(self):
		await super().connect()
	
	async def logout(self):
		await super().logout()
	
	async def close(self):
		await super().close()
	
	async def start(self):
		await super().start()
		
	def run(self):
		super().run()
	
	
	async def send_message(self, channel_name, message):
		
		#Hopefully very temporary code
		for channel in self.get_all_channels():
			if channel.name == channel_name:
				channel_object = channel
	
		await super().send_message(channel_object, content=message)

	async def on_typing(self, channel, user, when):
		if channel.name == "testserv":
			await self.send_message("testserv", "testy testing from testland")
		
	async def on_ready(self):
		def get_servers():
			servers = []
			for text_channel in self.get_all_channels():
				if text_channel.server not in servers:
					#print(str(text_channel) + "\n" + str(text_channel.server) + "\n" + str(text_channel) + "\n" + str(servers))
					servers.append(text_channel.server)
			return servers
		
		servers = get_servers()
		for server in servers:
			print(server.name)
		
	
