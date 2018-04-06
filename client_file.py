# -*- coding: utf-8 -*-
import discord
import asyncio, sys
import aioconsole

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
		
		#Hopefully very temporary code, reason being that if multiple channels share a name this is positive for both.
		for channel in self.get_all_channels():
			if channel.name == channel_name:
				channel_object = channel
	
		await super().send_message(channel_object, content=message)

	async def async_input(self):
		input = await aioconsole.ainput(">>> ")
		return input
		
	async def on_message(self, message):
		if message.author != self.user:
			print(message.author.name + ": " + message.content)
		#TODO: make this not break the layout

	#async def on_typing(self, channel, user, when):
	#	if channel.name == "testserv":
	#		await self.send_message("testserv", "testy testing from testland")
		
	async def on_ready(self):
	#	def get_servers():
	#		servers = []
	#		for text_channel in self.get_all_channels():
	#			if text_channel.server not in servers:
	#				servers.append(text_channel.server)
	#		return servers
		
	#	servers = get_servers()
	#	for server in servers:
	#		print(server.name)
		
		while True:
			try:
				await self.send_message("testserv", await self.async_input())
			except: 
				pass

