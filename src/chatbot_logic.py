# Inport ListTrainer
from chatterbot.trainers import ListTrainer
from chatbot_model import chatbot


trainer = ListTrainer(chatbot)

trainer.train([
'Hi',
'Hallo',
'Ich brauche deine Unterstützung wegen meiner Bestellung.',
'Bitte gebe mir deine Bestellungsnummer an.',
'Ich habe eine Beschwerde.',
'Bitte erläutere dein Anliegen.',
'Wie lange wird es dauern, meine Bestellung zu erhalten?',
'Eine Bestellung dauert 3-5 Werktage, um abgeliefert zu werden.',
'Okay, danke!',
'Kein Problem! Ich wünsche dir einen guten Tag!'
])

