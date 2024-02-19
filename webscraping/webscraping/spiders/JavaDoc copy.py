import json
import scrapy
from bs4 import BeautifulSoup
from googletrans import Translator


class JavaDocSpider(scrapy.Spider):
    name = "JavaDoc"
    start_urls = ["https://www.w3schools.com/java/java_intro.asp",
                  "https://www.w3schools.com/java/default.asp",
                  "https://www.w3schools.com/java/java_getstarted.asp",

                  ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        sections = []

        translator = Translator()

        for tag in soup.select('#main h2'):
            # traduz o título para o português
            translated_title = translator.translate(
                tag.text.strip(), dest='pt').text
            
            if translated_title.startswith("Exercício:"):
                translated_title = translated_title.replace("Exercício:", "Exercício_")

            current_dict = {'title': translated_title, 'content': ''}
            next_tag = tag.find_next_sibling()
           
            while next_tag and next_tag.name != 'hr':
                current_dict['content'] += str(next_tag.get_text(separator=' ', strip=True))
                next_tag = next_tag.find_next_sibling()
            
            
            # traduz o conteúdo para o português
            translated_content = translator.translate(
                current_dict['content'], dest='pt').text
            current_dict['content'] = translated_content

           

            sections.append(current_dict)

        yield {'sections': sections}

    def closed(self, reason):
        # cria um dicionário com a chave "sections"
        sections_list = []
        for item in self.crawler.stats.get('item_scraped_count', []):
            sections_list.extend(item['sections'])
        result_dict = {'sections': sections_list}

        # converte o dicionário para JSON
        result_json = json.dumps(result_dict)
        self.logger.info(result_json)
        yield json.loads(result_json)