# Projeto de Trabalho de Conclusão de Curso
## Nome: Rafael Duarte dos Santos
## Universidade Federal de Pelotas

## Chatterbot de Aprendizagem em Java

## Requisitos:
# [Python](https://www.python.org/) versão: 3.10.7
# [Scrapy](https://scrapy.org/)
# [Rasa](https://rasa.com/)
# Makefile (opcional)

Comandos úteis com Makefile:
==========================

* [Comando que executa o web crawler:] (#Comando que executa o web crawler)
make scrapy

* [Comando que executa o arquivo action do Rasa:] (#Comando que executa o arquivo action do Rasa)
make action

* [Comando que executa o arquivo que cria a base do nlu.yml:] (Comando que executa o arquivo que cria a base do nlu.yml)
make nlu

* [Comando que treina o bot:] (#Comando que treina o bot)
make train

* [Comando que executa o bot e inicia sua conversação pelo terminal:] (Comando que executa o bot e inicia sua conversação pelo terminal)
make shell

Comandos úteis sem Makefile:
==========================

Comando que executa o web crawler:


Comando que executa o arquivo action do Rasa:
rasa run action

Comando que executa o arquivo que cria a base do nlu.yml:
O comando substitui o arquivo, sem adicionar as perguntas.


Comando que treina o bot:
rasa train

Comando que executa o bot e inicia sua conversação pelo terminal:
rasa shell
