scrapy:
	scapy runspider ./webscraping/webscraping/spiders/JavaDoc.py -o ./webscraping/webscraping/spiders/output.json

action:
	./chatterbot_projeto/rasa run action

nlu:
	./chatterbot_projeto/

train:
	./chatterbot_projeto/rasa train

shell:
	./chatterbot_projeto/rasa shell
