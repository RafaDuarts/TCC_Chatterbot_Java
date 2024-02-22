scrapy:
	cd webscraping\webscraping\spiders && scrapy runspider JavaDoc.py -o output.json

action:
	cd chatterbot_projeto && rasa run action

nlu:
	cd chatterbot_projeto\actions && python nlu_creator.py

train:
	cd chatterbot_projeto && rasa train

shell:
	cd chatterbot_projeto && rasa shell
