# -*- coding: utf-8 -*-

import discord
import asyncio
import client_file
import logging

#Logging from official API start

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

#Logging end

token_file = open('token.txt', 'r')
token = token_file.read()
token_file.close()

schedule = asyncio.new_event_loop()
client = client_file.client(token, loop=schedule)



def main():
	client.run()

	
main()