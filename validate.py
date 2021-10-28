# from rasa.core.agent import Agent
# from rasa.core.interpreter import RasaNLUInterpreter
# agent = Agent.load('models/20211013-231301.tar.gz')
# # # importing the "tarfile" module
# # import tarfile

# # # open file
# # file = tarfile.open('models/20211013-231301.tar.gz')

# # # extracting file
# # file.extractall('models/unpacked')

# # file.close()
# agent.handle_text('hello')

import asyncio
from rasa.core.agent import Agent


agent = Agent.load("models/20211013-231301.tar.gz")

async def process(msg):    
    output = await agent.handle_text(msg)
    print(output[0]['text'])
    return output

asyncio.run(process("my project is difficult"))

#(or)

# loop = asyncio.get_event_loop()
# reply = loop.run_until_complete(agent.handle_text("hi"))
# print(reply)