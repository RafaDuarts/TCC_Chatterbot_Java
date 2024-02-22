# 💻 Projeto de Trabalho de Conclusão de Curso
##### Nome: Rafael Duarte dos Santos
##### Universidade Federal de Pelotas - Engenharia de Computação

## 🚀 Chatterbot de Aprendizagem em Java

### 📋 Requisitos:
##### [Python](https://www.python.org/) versão: 3.10.7
##### [Scrapy](https://scrapy.org/)
##### [Rasa](https://rasa.com/)
##### Makefile (opcional)


⚙️ Comandos úteis com Makefile:
==========================

* [Comando que executa o web crawler:](#Comando-crawler-make)
    ```
    make scrapy
    ```

* [Comando que executa o arquivo action do Rasa:](#Comando-action-make)
    ```
    make action
    ```
    
* [Comando que executa o arquivo que cria a base do nlu.yml:](#Comando-nlu-make)
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

- [Comando que executa o web crawler:](#Comando-crawler)
    ```
    scapy runspider ./webscraping/webscraping/spiders/JavaDoc.py -o ./webscraping/webscraping/spiders/output.json
    ```

* [Comando que executa o arquivo action do Rasa:](#Comando-action)
    ```
    rasa run action
    ```
    
* [Comando que executa o arquivo que cria a base do nlu.yml:](#Comando-nlu)
        O comando substitui o arquivo, sem adicionar as perguntas.
    ```
    
    ```
* [Comando que treina o bot:](#Comando-treino-bot)
    ```
    rasa train
    ```
    
* [Comando que executa o bot e inicia sua conversação pelo terminal:](#Comando-terminal)
    ```
    rasa shell
    ```