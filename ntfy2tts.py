import asyncio
import json
import signal
import sys
import ntfpy
import pyttsx3

#fix keyboard interrupts.
signal.signal(signal.SIGINT, signal.SIG_DFL)

async def main():
	configFile=open("config.json")
	config=json.load(configFile)
	configFile.close()
	url=config["url"]
	topic=config["topic"]
	client=ntfpy.NTFYClient(ntfpy.NTFYServer(url), topic)
	await client.subscribe(speakMessage)

def speak(text):
	engin=pyttsx3.init()
	engin.say(text)
	engin.runAndWait()

def speakMessage(message: ntfpy.message.NTFYMessage):
	starter=message.title if message.title is not None else message.topic
	speak(f'{starter}: {message.message}')
if __name__ == "__main__":

	loop = asyncio.get_event_loop()
	try:
		loop.run_until_complete(main())
	except asyncio.CancelledError:
		pass