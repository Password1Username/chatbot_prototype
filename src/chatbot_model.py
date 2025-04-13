# Importing chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


# Create a chatbot instance
service_bot = ChatBot('GermanBot')

# Set up the trainer
trainer = ChatterBotCorpusTrainer(service_bot)

# Train the chatbot on a specific language corpus (e.g., German)
trainer.train("chatterbot.corpus.german",
              "chatterbot.corpus.german.greetings",
              "chatterbot.corpus.german.conversations"
             )

print("Model trained on German language.")


