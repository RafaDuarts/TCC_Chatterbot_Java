# 💻 Projeto de Trabalho de Conclusão de Curso
##### Nome: Rafael Duarte dos Santos
##### Universidade Federal de Pelotas - Engenharia de Computação

## 🚀 Desenvolvimento de um chatterbot que ensina conceitos de Orientação a Objetos na Linguagem de Programação Java

### 📋 Requisitos:
##### [Python](https://www.python.org/) versão: 3.10.7
##### [Scrapy](https://scrapy.org/)
##### [Rasa](https://rasa.com/)
##### Makefile (opcional)


⚙️ Comandos úteis com Makefile:
==========================

* [Comando que executa o web scraping:](#Comando-scraping-make)
    O Comando tem como saída o arquivo output.json, localizado na pasta spider, dentro da parte de webscraping. Quando executado, o arquivo é criado, mas não subescreve, caso haja um já existente. Recomendado deletar o arquivo antes de executar o comando.

    ```
    make scrapy
    ```

* [Comando que executa o arquivo action do Rasa:](#Comando-action-make)
    O arquivo output.json(extraído pelo webscraping) deve estar na pasta action para que seja executado corretamente.

    ```
    make action
    ```
    
* [Comando que executa o arquivo que cria a base do nlu.yml:](#Comando-nlu-make)
    O comando substitui o arquivo, sem adicionar as perguntas.
    ```
    make nlu
    ```

* [Comando que treina o bot:](#Comando-treino-bot-make)
    ```
    make train
    ```
    
* [Comando que executa o bot e inicia sua conversação pelo terminal:](#Comando-terminal-make)
    ```
    make shell
    ```

⚙️ Comandos úteis sem Makefile:
==========================

- [Comando que executa o web scraping:](#Comando-scraping)
    O Comando tem como saída o arquivo output.json, localizado na pasta spider, dentro da parte de webscraping. Quando executado, o arquivo é criado, mas não subescreve, caso haja um já existente. Recomendado deletar o arquivo antes de executar o comando.

    ```
    cd webscraping\webscraping\spiders && scapy runspider JavaDoc.py -o output.json
    ```

* [Comando que executa o arquivo action do Rasa:](#Comando-action)
    O arquivo output.json(extraído pelo webscraping) deve estar na pasta action para que seja executado corretamente.

    ```
    cd chatterbot_projeto && rasa run action
    ```
    
* [Comando que executa o arquivo que cria a base do nlu.yml:](#Comando-nlu)
    O comando substitui o arquivo, sem adicionar as perguntas.

    ```
    cd chatterbot_projeto\actions && python nlu_creator.py
    ```
* [Comando que treina o bot:](#Comando-treino-bot)
    ```
    cd chatterbot_projeto && rasa train
    ```
    
* [Comando que executa o bot e inicia sua conversação pelo terminal:](#Comando-terminal)
    ```
    cd chatterbot_projeto && rasa shell
    ```