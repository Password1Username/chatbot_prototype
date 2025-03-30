# Importing chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


# Create a chatbot instance
chatbot = ChatBot('GermanBot')

# Set up the trainer
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on a specific language corpus (e.g., German)
trainer.train("chatterbot.corpus.german")


