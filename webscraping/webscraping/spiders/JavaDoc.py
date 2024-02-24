import json
import scrapy
from bs4 import BeautifulSoup
from googletrans import Translator


class JavaDocSpider(scrapy.Spider):
    name = "JavaDoc"
    start_urls = [
        "https://www.w3schools.com/java/java_intro.asp",
        "https://www.w3schools.com/java/java_getstarted.asp",
        "https://www.w3schools.com/java/java_syntax.asp",
        "https://www.w3schools.com/java/java_output.asp",
        "https://www.w3schools.com/java/java_output_numbers.asp",
        "https://www.w3schools.com/java/java_comments.asp",
        "https://www.w3schools.com/java/java_variables.asp",
        "https://www.w3schools.com/java/java_variables_print.asp",
        "https://www.w3schools.com/java/java_variables_multiple.asp",
        "https://www.w3schools.com/java/java_variables_identifiers.asp",
        "https://www.w3schools.com/java/java_data_types.asp",
        "https://www.w3schools.com/java/java_data_types_boolean.asp",
        "https://www.w3schools.com/java/java_data_types_characters.asp",
        "https://www.w3schools.com/java/java_data_types_non-prim.asp",
        "https://www.w3schools.com/java/java_operators.asp",
        "https://www.w3schools.com/java/java_strings.asp",
        "https://www.w3schools.com/java/java_strings_concat.asp",
        "https://www.w3schools.com/java/java_strings_numbers.asp",
        "https://www.w3schools.com/java/java_strings_numbers.asp",
        "https://www.w3schools.com/java/java_math.asp",
        "https://www.w3schools.com/java/java_booleans.asp",
        "https://www.w3schools.com/java/java_conditions.asp",
        "https://www.w3schools.com/java/java_conditions_shorthand.asp",
        "https://www.w3schools.com/java/java_switch.asp",
        "https://www.w3schools.com/java/java_while_loop.asp",
        "https://www.w3schools.com/java/java_for_loop.asp",
        "https://www.w3schools.com/java/java_foreach_loop.asp",
        "https://www.w3schools.com/java/java_break.asp",
        "https://www.w3schools.com/java/java_arrays.asp",
        "https://www.w3schools.com/java/java_arrays_loop.asp",
        "https://www.w3schools.com/java/java_arrays_multi.asp",
        "https://www.w3schools.com/java/java_methods.asp",
        "https://www.w3schools.com/java/java_methods_param.asp",
        "https://www.w3schools.com/java/java_methods_overloading.asp",
        "https://www.w3schools.com/java/java_scope.asp",
        "https://www.w3schools.com/java/java_recursion.asp",
        "https://www.w3schools.com/java/java_oop.asp",
        "https://www.w3schools.com/java/java_classes.asp",
        "https://www.w3schools.com/java/java_class_attributes.asp",
        "https://www.w3schools.com/java/java_class_methods.asp",
        "https://www.w3schools.com/java/java_constructors.asp",
        "https://www.w3schools.com/java/java_modifiers.asp",
        "https://www.w3schools.com/java/java_encapsulation.asp",
        "https://www.w3schools.com/java/java_packages.asp",
        "https://www.w3schools.com/java/java_inheritance.asp",
        "https://www.w3schools.com/java/java_polymorphism.asp",
        "https://www.w3schools.com/java/java_inner_classes.asp",
        "https://www.w3schools.com/java/java_abstract.asp",
        "https://www.w3schools.com/java/java_interface.asp",
        "https://www.w3schools.com/java/java_enums.asp",
        "https://www.w3schools.com/java/java_user_input.asp",
        "https://www.w3schools.com/java/java_arraylist.asp",
        "https://www.w3schools.com/java/java_hashmap.asp",
        "https://www.w3schools.com/java/java_try_catch.asp"
        ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        sections = []

        translator = Translator()

        for tag in soup.select("#main h2"):
            # traduz o título para o português
            translated_title = translator.translate(
                tag.text.strip(), dest="pt"
            ).text

            if translated_title.startswith("Exercício:"):
                translated_title = translated_title.replace("Exercício:", "Exercício_")

            current_dict = {"title": translated_title, "content": ""}
            next_tag = tag.find_next_sibling()

            while next_tag and next_tag.name != "hr":
                current_dict["content"] += str(next_tag.get_text(separator=" ", strip=True))
                next_tag = next_tag.find_next_sibling()

            # traduz o conteúdo para o português
            translated_content = translator.translate(
                current_dict["content"], dest="pt"
            ).text
            current_dict["content"] = translated_content

            sections.append(current_dict)

        yield {"sections": sections}

    def closed(self, reason):
        # cria um dicionário com a chave "sections"
        sections_list = []
        for item in self.crawler.stats.get("item_scraped_count", []):
            sections_list.extend(item["sections"])
        result_dict = {"sections": sections_list}

        # converte o dicionário para JSON
        result_json = json.dumps(result_dict)
        self.logger.info(result_json)
        yield json.loads(result_json)
