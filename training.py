from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import pickle

catbot = ChatBot(
    "catbot",
    trainer="chatterbot.trainers.ListTrainer",
    storage_adapter="chatterbot.storage.MongoDatabaseAdapter"
)
catbot.train("chatterbot.corpus.english")
catbot.set_trainer(ListTrainer)
with open('rom.pickle', 'rb') as rom:
	rom_dialogue = pickle.load(rom)[:15000]

catbot.train(rom_dialogue)
print(catbot.get_response("Are you a cat?"))





